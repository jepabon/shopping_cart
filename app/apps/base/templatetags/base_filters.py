from django import template

register = template.Library()

@register.filter(name='currency')
def currency(value, symbol="$"):
    return "{symbol}{value}".format(symbol=symbol, value="{:,.0f}".format(value))
