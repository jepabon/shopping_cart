window.onload = function() {
    loadConfirmedOrders()
    loadPayments()
}

var confirmed_orders_list = [];
var payment_list = [];

async function loadConfirmedOrders() {
    const fetchConfirmedOrder = await fetch('/api/v1/orders/get_confirmed_orders');
    const response = await fetchConfirmedOrder.json();
    confirmed_orders_list = response;
    printConfirmedOrders(response);
}


async function loadPayments() {
    const fetchPayments = await fetch('/api/v1/payments/');
    const response = await fetchPayments.json();
    payment_list = response;
    printPayments(response);
}

function printPayments(data) {
    let payments = document.getElementById('payments');
    payments.innerHTML = '';
    let html = ``;
    for (let i=0; i < data.results.length; i++) {
        html += `
            <div class="col-12">
                <div class="row">
                    <div class="card col-12">
                        <div class="card-body">
                            <div class="row">
                                <div class="col-2">
                                    <label for="id_valor_pago_${data.results[i].id}">Valor</label>
                                </div>
                                <div class="col-3">
                                    <input onchange="updateValue(this, ${i})" id="id_valor_pago_${data.results[i].id}" type="number">
                                </div>
                                <div class="col-2">
                                    <label for="id_method_payment_${data.results[i].id}">Método de Pago</label>
                                </div>
                                <div class="col-3">
                                    <select onchange="updateMethodPayment(this, ${i})" class="col-12">`;
        for (let j=0; j < data.method_payments.length; j++) {
            html += `
                                        <option ${data.results[i].method_payment === data.method_payments[j][0] ? 'selected':''} value="${data.method_payments[j][0]}">${data.method_payments[j][1]}</option>
            `;
                                }
        html += `
                                    </select>
                                </div>
                                <div class="col-2 text-right">
                                    <span><i class="fa fa-trash"></i></span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
    }

    html += `
        <div class="col-12 text-center">
            <a href="#" onclick="addPayment()"><i class="fa fa-plus"></i> Agregar pago</a>
        </div>
    `;

    payments.innerHTML = html;
}

function updateValue(input_value, index) {
    let value = parseFloat(input_value.value);
    payment_list.results[index].value = value;
    updateDataPayment();
}

function updateMethodPayment(input_method_payment, index) {
    let method_payment = input_method_payment.value;
    payment_list.results[index].method_payment = method_payment;
    updateDataPayment();
}

async function addPayment() {
    const fetchAddPayments = await fetch('/api/v1/payments/create_payment/');
    const response = await fetchAddPayments.json();
    loadPayments();
}

function printConfirmedOrders(data) {
    if (data.status === 'Orders not found') return
    html = ``;
    let order_list = document.getElementById('confirmed_orders');
    order_list.innerHTML = '';
    let dollarUS = Intl.NumberFormat("en-US", {
        style: "currency",
        currency: "usd"
    })

    for(let i=0; i < data.length; i++) {
        data[i].selected = false;
        html += `
            <div class="col-4 card ml-2">
                <div class="card-body">
                    <div class="row">
                        <div class="col-12">
                            <div class="row">
                                <div class="col-6">
                                    <input onchange="updateOrderSelected(this, ${i})" type="checkbox" name="checkbox_${data[i].order.id}" id="id_checkbox_${data[i].order.id}">
                                </div>
                                <div class="col-6 text-right">
                                    <a href="#" class="text-right" onclick="removeOrder(${data[i].order.id})"><i class="fa fa-trash"></i></a>
                                </div>
                            </div>
                        </div>
                        <div class="col-12 text-center">
                            Pedido #${data[i].order.id}
                        </div>
                        <div class="col-12 text-center">
                            Total: ${dollarUS.format(data[i].order.total)}
                        </div>
                        <div class="col-12 text-center mt-2">
                            <button type="button" class="btn btn-primary" onclick="openDetailOrder(${i})">Ver detalle</button>
                        </div>
                    </div>
                </div>
            </div>
        `;
    }

    order_list.innerHTML += html;
}

async function removeOrder(order_id) {
    let csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    const fetchAddPayments = await fetch('/api/v1/orders/'+order_id+'/', {
        method: "DELETE",
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token
        },
    });
    loadConfirmedOrders();
}

function updateOrderSelected(checkbox_order, index) {
    let selected = checkbox_order.checked;
    confirmed_orders_list[index].selected = selected;
    updateDataPayment();
}

function openDetailOrder(index) {
    let order = confirmed_orders_list[index];
    let detail_order = document.getElementById('bodyDetailOrder');
    detail_order.innerHTML = '';
    let dollarUS = Intl.NumberFormat("en-US", {
        style: "currency",
        currency: "usd"
    })
    let html = '';

    for (let i=0; i < order.items.length; i++) {
        html += `
        <div class="row mb-3">
            <div class="col-4">
                <img class="custom-img" src="${order.items[i].image_path ? order.items[i].image_path:'/media/default_product.png'}">
            </div>
            <div class="col-6 text-center">
                <div class="align-top">
                    ${order.items[i].name}
                </div>
                <div class="align-bottom">
                    ${dollarUS.format(order.items[i].price)}
                </div>
            </div>
        </div>
        `;
    }
    detail_order.innerHTML = html;
    $('#detailOrder').modal('show');
}


function updateDataPayment() {
    let input_payments = document.getElementById('id_payments');
    let input_orders = document.getElementById('id_orders');

    input_payments.value = JSON.stringify(payment_list);
    input_orders.value = JSON.stringify(confirmed_orders_list);
}