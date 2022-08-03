from telnetlib import LOGOUT
from app import responseBuilder
from app import userSession
from app.models import Message
from django.views.decorators.csrf import csrf_protect
from rest_framework.views import APIView
from rest_framework.response import Response
from app.userSession import user_login 
from .serializers import messageSerliazer
from copy import deepcopy
# Create your views here.

class MessageView(APIView):
    def get(self,request,*args,**kwargs):
        if userSession.get_user_from_session(request) is not None:
          receiver=userSession.get_user_from_session(request)
        else: 
         receiver=self.request.data.get('receiver',None)
         if receiver is None:
           return responseBuilder.missing_parameter("receiver")
        try:
           message = Message.objects.filter(receiver=receiver,is_read=False).latest('date')
           message.is_read=True
           message.save()
           return responseBuilder.get_message(sender=message.sender,receiver=message.receiver,message=message.message,subject=message.subject,creation_date=message.date)
        except message.DoesNotExist:
            return responseBuilder.no_unread_messages()

    def post(self,request,*args,**kwargs):
        serializer=messageSerliazer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return responseBuilder.add_message(serializer.data)
        return Response(serializer.errors)

    def delete(self,request,*args,**kwargs):
        id=self.request.data.get("id",None)
        user_name=self.request.data.get("user_name",None)
        if id is None:
          return responseBuilder.missing_parameter("id")
        if userSession.get_user_from_session(request) is not None:
          user_name=userSession.get_user_from_session(request)
        else:
          user_name=self.request.data.get("user_name",None)
          if user_name is None:
             return responseBuilder.missing_parameter("user_name")
        try:  
          message=Message.objects.get(id=id)
          if (message.receiver != user_name)&(message.sender != user_name):
            return responseBuilder.invalid_username(user_name,id)
          message.delete()
          return responseBuilder.delete_message()
        except message.DoesNotExist:
          return responseBuilder.message_doesnt_exists()

class AllMessagesView(APIView):
  def get(self,request,*args,**kwargs):
    if userSession.get_user_from_session(request) is not None:
      receiver=userSession.get_user_from_session(request)
    else:
      receiver=self.request.data.get('receiver',None)
      if receiver is None:
       return responseBuilder.missing_parameter("receiver")
    only_unread=self.request.data.get('only_unread',None)
    try:
      if only_unread == '1':
        message = Message.objects.filter(receiver=receiver,is_read=False)
      else:
        message = Message.objects.filter(receiver=receiver)     
      messages_list=list(message.values('sender','receiver','subject','message','date','id'))
      message.update(is_read=True)
      return responseBuilder.get_all_messages(messages_list)
    except message.DoesNotExist:
      if only_unread==True:
        return responseBuilder.no_unread_messages()
      else:
        return responseBuilder.no_messages()

class LoginView(APIView):
  def post(self,request,*args,**kwargs):
    user_name=self.request.data.get('user_name',None)
    if user_name is None:
          return responseBuilder.missing_parameter("user_name")     
    user_login(user_name,request)
    return responseBuilder.login(user_name)

    
           
          

        
    




        
    

    
        
