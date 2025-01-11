from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *
from rest_framework.decorators import api_view

@csrf_exempt
@api_view(['POST'])
def additem(request):
    db = makeMongoConnection()
    body_unicode = request.body.decode('utf-8')  # Decode bytes to string
    body = json.loads(body_unicode)
    print(body)
    if "Product" in db.list_collection_names():
        collection = db["Product"]
    else:
        collection = makeMongoCollection(db, "Product")
    if collection is not None:
        collection.insert_one(body)
        msg = "Item added successfully."
        status = 200
    else:
        msg = "Item not added."
        status = 203
    db.close()
    return JsonResponse(data={"msg": msg}, status=status)


@csrf_exempt
@api_view(['GET'])
def getitem(request):
    db = makeMongoConnection()
    id = request.GET.get('id')
    if "Product" in db.list_collection_names():
        collection = db["Product"]
    else:
        collection = makeMongoCollection(db, "Product")
    if collection is not None:
        product = collection.find_one({"productId": int(id)})
        if product is not None:
            product["_id"] = str(product["_id"])
        if mongo_client:
            mongo_client.close()
        return JsonResponse(data={"product": product}, status=200)
    else:
        if mongo_client:
            mongo_client.close()
        return JsonResponse(data={"msg": "Item not found."}, status=203)


@csrf_exempt
@api_view(['DELETE'])
def deleteitem(request):
    db = makeMongoConnection()
    body_unicode = request.body.decode('utf-8')  # Decode bytes to string
    body = json.loads(body_unicode)
    print(body)
    if "Product" in db.list_collection_names():
        collection = db["Product"]
    else:
        collection = makeMongoCollection(db, "Product")
    if collection is not None:
        collection.delete_one({"productId": body.get("id")})
        if mongo_client:
            mongo_client.close()
        return JsonResponse(data={"msg": "Item deleted successfully."}, status=200)
    else:
        if mongo_client:
            mongo_client.close()
        return JsonResponse(data={"msg": "Item not deleted."}, status=203)


def home(request):
    return render(request, 'index.html', {'id': 12345})



