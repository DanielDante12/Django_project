from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm
from .serializer import CustomerSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Customer
@api_view(['GET','POST'])
def home(request):
    if request.method=="GET":
          customers=Customer.objects.all()
          SerializedCustomer=CustomerSerializer(customers, many=True)
          return Response(SerializedCustomer.data)
    elif request.method=='POST':
        serialized=CustomerSerializer(data=request.data)  
        if serialized.is_valid(): 
            serialized.save()
            return Response(serialized.data,status=status.HTTP_200_OK)

def register(request):
    if request.method=='POST':
        form= UserRegisterForm(request.POST)
        if form.is_valid():
             form.save()
             username=form.cleaned_data.get('username')
             messages.success(request, f'Your Account has succesfully been created! You can now login')
             return redirect('login')
    else:
           form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form})
