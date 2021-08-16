from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import ClassdetailSerializer
from .models import Classdetail
import datetime


class ClassdetailViewSet(viewsets.ModelViewSet):
    queryset = Classdetail.objects.all()
    serializer_class = ClassdetailSerializer

    #  queryset = Book.objects.all()
    # serializer_class = BookSerializer
    # search_fields = ('name','author')

    def create(self, request, *args, **kwargs):
        """
        #checks if post request data is an array initializes serializer with many=True
        else executes default CreateModelMixin.create function
        """
        # currentDate = datetime.date.today()
        data = request.data
        is_many = isinstance(request.data, list)
        if not is_many:

            # newObj, created = Classdetail.objects.update_or_create(
            #     date=data.get('date'), question=data.get('question'),
            #     defaults={'value': data.get('value')},
            # )
            # return newObj

            return super(ClassdetailViewSet, self).create(request, *args, **kwargs)
        else:
            # firstDate = request.data[0]['date']
            # newDate = datetime.datetime.strptime(firstDate,'%Y-%m-%d').date()
            # # dateToCheck = data[0].get('date')
            # Classdetail.objects.filter(date=firstDate).delete()
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    # def get_queryset(self):
    #     question = self.request.query_params.get('question')
    #     date= self.request.query_params.get('date')

    #     if (date != None and question != None):
    #         queryset = Answer.objects.filter(question=question, date=date)
    #     elif (date != None and question == None):
    #         queryset = Answer.objects.filter(date=date)
    #     elif (date == None and question != None):
    #         queryset = Answer.objects.filter(question=question)
    #     else:
    #         queryset = Answer.objects.all()


        

    #     return queryset
