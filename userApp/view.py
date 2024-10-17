from .models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def getusers(request):
    users = User.objects.all()
    users_list = []
    for user in users:
        users_list.append({
            'id': user.id,
            'name': user.name,
            'email': user.email,
        })
    return JsonResponse({'users': users_list})


@csrf_exempt
def adduser(request):
    body_unicode = request.body.decode('utf-8')  # Decode bytes to string
    body = json.loads(body_unicode)
    # print(request.body)
    name = body.get('name')
    email = body.get('email')
    User.objects.create(name=name, email=email)
    return JsonResponse(data={"status":"success"}, status=200)