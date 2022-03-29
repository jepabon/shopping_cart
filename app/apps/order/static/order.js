window.onload = function () {
    loadActiveOrder()
}

async function loadActiveOrder() {
    const fetchActiveOrder = await fetch('/api/v1/orders/get_active_order');
    const response = await fetchActiveOrder.json();
    printProductsOrder(response);
    loadConfirmedOrders()
}

async function loadConfirmedOrders() {
    const fetchConfirmedOrder = await fetch('/api/v1/orders/get_confirmed_orders');
    const response = await fetchConfirmedOrder.json();
    printConfirmedOrders(response);
}


function printConfirmedOrders(data) {
    if (data.status === 'Orders not found') return
    html = ``;
    let order_list = document.getElementById('confirmed_list_orders');
    order_list.innerHTML = '';
    let dollarUS = Intl.NumberFormat("en-US", {
        style: "currency",
        currency: "usd"
    })

    html += `
        <h2 class="text-center">Pedidos Pendientes</h2>
        <table class="table">
        <thead>
            <tr>
                <th>
                    Consecutivo
                </th>
                <th>
                    Total
                </th>
            </tr>
        </thead>
        <tbody>
    `;

    for(let i=0; i < data.length; i++) {
        html += `
        <tr>
            <td>
                Pedido #${data[i].order.id}
            </td>
            <td>
                ${dollarUS.format(data[i].order.total)}
            </td>
        </tr>
        `;
    }
    html += `
            </tbody>
        </table>
    `;
    order_list.innerHTML += html;
}

function printProductsOrder(data) {
    let number_order = document.getElementById('number_order');
    number_order.innerHTML = data.order.id;
    html = ``;
    let product_list = document.getElementById('product_list_order');
    product_list.innerHTML = '';
    let dollarUS = Intl.NumberFormat("en-US", {
        style: "currency",
        currency: "usd"
    })

    html += `<div class="row">`;

    for (let i=0; i < data.items.length; i++) {
        html += `
            <div class="col-12 card">
                <div class="card-body">
                    <div class="row">
                        <div class="col-4">
                            <img class="custom-img" src="${data.items[i].image_path ? data.items[i].image_path:'http://localhost:9001/media/default_product.png'}">
                        </div>
                        <div class="col-4">
                            <div class="align-top">
                                ${data.items[i].name}
                            </div>
                            <div class="align-bottom">
                                ${dollarUS.format(data.items[i].price)}
                            </div>
                        </div>
                        <div class="col-md-4">
                            ${data.items[i].amount}
                            <a class="btn" onclick="removeProduct(${data.items[i].id})"><i class="fa fa-trash"></i></a>
                        </div>
                    </div>
                </div>
            </div>
        `;
    }

    html += `</div>`;

    html += `
        <div class="col-12 mt-3">
            <div class="row">
                <div class="col-12">
                    Total: ${dollarUS.format(data.order.total)}
                </div>
                <div class="col-12">
                    <div class="row">
                        <div class="col-3">
                            <a href="/payment/process_payment" type="button" class="btn btn-primary">Realizar Pago</a>
                        </div>
                        <div class="col-3">
                            <a href="#" type="button" class="btn btn-primary" onclick="createOrder()">Crear nuevo pedido</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;

    product_list.innerHTML += html;
}

async function removeProduct(product) {
    let csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value;
    let data = {
        'id': product,
    }

    const fetchRemoveProduct = await fetch('/api/v1/orders/remove_product/', {
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf_token
        },
        method: 'POST',
        body: JSON.stringify(data)
    });

    const response = await fetchRemoveProduct.json();
    printProductsOrder(response);
    getItemsActiveOrder();
}


async function createOrder() {
    const fetchConfirmedOrder = await fetch('/api/v1/orders/confirmed_order/');

    const response = await fetchConfirmedOrder.json();
    if (response.status === 'Order confirmed') {
        loadActiveOrder()
    }
    getItemsActiveOrder();
}