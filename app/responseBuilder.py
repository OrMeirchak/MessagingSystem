
from django.forms import DateField
from rest_framework.response import Response 

def no_unread_messages()->Response:
    data={
        'message':'No unread messages'
    }
    response=Response(data)
    response.status_code=404
    return response

def no_messages()->Response:
    data={
        'message':'No messages'
    }
    response=Response(data)
    response.status_code=404
    return response

def missing_parameter(paramter:str)->Response:
    data={
        'message':'Request is missing a required parameter : {}'.format(paramter)
    }
    response= Response(data)
    response.status_code=422
    return response

def add_message(message_details)->Response:
    data = {
       'message':'The message has been added to the database',
       'details':message_details
    }
    response=Response(data)
    response.status_code=201
    return response

def get_message(sender:str,receiver:str,message:str,subject:str,creation_date:DateField)->Response:
       data={
         'sender':sender,
         'receiver':receiver,
         'subject':subject,
         'message':message,
         'creation date':creation_date
    }
       return Response(data)

def get_all_messages(data)->Response:
    return Response(data)

def delete_message():
    data={
         'message':'The message has been deleted from the database'
    }
    return Response(data) 

def message_doesnt_exists()->Response:
      data={
         'message':'Message does not exist'
    }
      response=Response(data)
      response.status_code=404
      return response

def invalid_username(username:str,id:str)->Response:
      data={
         'message':'{} is neither the sender nor the receiver of message number {}'.format(username,id)
    }
      response=Response(data)
      response.status_code=401
      return response

def login(username:str)->Response:
    data={
         'message':'{} logged in'.format(username)
    }
    return Response(data)


