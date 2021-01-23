from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    # return HttpResponse("Hello")
    myname="Công Sơn"
    myage="21"
    thongtin=["0975676512","88 Bàu Cát","Đại học Bách Khoa"]
    return render(request,'pythonweb/index.html',{"name":myname,"age":myage,"thongtin":thongtin})
