from django.shortcuts import render
from Api.models import Customer, Product
from Api.serializers import CustomerSerializer, ProductSerializer, UpdateSerializer
from rest_framework import viewsets
from rest_framework.response import Response
import datetime


# Create your views here.

class customerApi(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class productApi(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class updateStatusApi(viewsets.ViewSet):
    def partial_update(self, request, pk):
        id = pk
        p = Product.objects.get(pk=id)
        date = datetime.date.today()
        print(date)
        d = request.data
        if d == {'status': 'inactive'}:
            print(d)
            diff = p.date - date
            da = diff.days
            if da > 60:
                serializer = UpdateSerializer(p, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'msg': 'Status updated'})
                return Response(serializer.errors)
            return Response({'msg': 'Status not updated'})
        else:
            if d == {'status': 'active'}:
                serializer = UpdateSerializer(p, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'msg': 'Status updated'})
                return Response(serializer.errors)
