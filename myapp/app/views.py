from django.shortcuts import render
from django.http import HttpResponse
from app import client
# Create your views here.
def index(request):
    return HttpResponse("Hello app!!")

def get(request):
    db = client["compnay"]
    collection = db["employees"]
    result = collection.find({})
    result_length = collection.count_documents({})
    string = ""
    result_list = list(result)
    print(len(result_list))

    return HttpResponse(f"{result_length}")