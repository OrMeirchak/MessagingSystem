from django.contrib.auth.models import User,auth

def user_login(user_name:str,request):
    user=User.objects.filter(username=user_name)
    if len(user)<=0:
      user=User.objects.create_user(username=user_name)
      user.save()
      auth.login(request,user)
    else:
      auth.login(request,user[0])

def get_user_from_session(request):
  if request.user.is_authenticated:
    return request.user.username