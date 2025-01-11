from .models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json


@csrf_exempt
def getuser(name):
    users = User.objects.filter(name=name)
    print(users)
    for user in users:
        return user
    return None


@csrf_exempt
@api_view(['GET'])
def getusers(request):
    users = User.objects.all()
    users_list = []
    if users is not None:
        for user in users:
            users_list.append({
                'id': user.id,
                'name': user.name,
                'email': user.email,
            })
    return JsonResponse({'users': users_list})


@csrf_exempt
@api_view(['POST'])
def adduser(request):
    body_unicode = request.body.decode('utf-8')  # Decode bytes to string
    body = json.loads(body_unicode)
    # print(request.body)
    name = body.get('name')
    email = body.get('email')
    User.objects.create(name=name, email=email)
    return JsonResponse(data={"status":"success"}, status=200)