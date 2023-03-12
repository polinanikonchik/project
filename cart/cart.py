from .models import Cart


def get_cart(request,params):
    try:
        cart = Cart.objects.get(user=request.user)
        params['cart'] = cart
    except:
        pass
    finally:
        return params
