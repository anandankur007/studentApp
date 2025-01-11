from .models import Order
from userApp.views import *
from product.models import *
import json
# Create your views here.


@csrf_exempt
@api_view(['GET'])
def getOrder(request):
    user = request.GET.get('user')
    data = []
    redis_client = makeRedisConnection()
    order = redis_client.get(user)
    redis_client.close()
    if order:
        odr = json.loads(order)
        data.append({
            'description': odr['description'],
            'orderid': odr['orderid'],
            'productId': odr['productId']
        })
        print("got data from redis db.")
        return JsonResponse(data=data, safe=False, status=200)
    orders = Order.objects.all()
    if orders:
        for order in orders:
            if order.user.name == user:
                data.append({
                    'description': order.description,
                    'orderid': order.id,
                    'productId': ord['productId']
                })
                break
    print(data)
    return JsonResponse(data=data, safe=False, status=200)


@csrf_exempt
@api_view(['POST'])
def createOrder(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print(body)
    user = getuser(body.get('user'))
    order = Order.objects.create(user=user, productId=body.get('productId'),
                                 description=body.get('description'), orderid=body.get('id'))
    redis_client = makeRedisConnection()
    redis_client.set(user.name, json.dumps(order.to_dict()))
    redis_client.close()
    return JsonResponse(data={"msg": "order placed successfully."}, status=200)