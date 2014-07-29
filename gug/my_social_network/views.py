from django.template import Context, loader 
from django.http import HttpResponse 
from models import UserLink
from django.contrib.auth.models import User

def users_list(request): 
  user_list = User.objects.all() 
  t = loader.get_template('my_social_network/list.html') 
  c = Context({ 'user_list': user_list, }) 
  return HttpResponse(t.render(c)) 

def users_followers(request,user_id): 
  user_list1 = UserLink.objects.all() 
  user_list = []
  for ulink in user_list1:
    if(ulink.to_user.username==user_id):
      user_list.append(ulink.from_user)
  user_list2 = User.objects.all()
  for user in user_list2:
    if(user.username==user_id):
      t = loader.get_template('my_social_network/followers.html') 
      c = Context({ 'user_list': user_list, }) 
      return HttpResponse(t.render(c)) 
  t = loader.get_template('my_social_network/nulluser.html') 
  c = Context({ 'user_list': user_list, }) 
  return HttpResponse(t.render(c))   

def users_following(request,user_id): 
  user_list1 = UserLink.objects.all() 
  user_list = []
  for ulink in user_list1:
    if(ulink.from_user.username==user_id):
      user_list.append(ulink.to_user)
  user_list2 = User.objects.all()
  for user in user_list2:
    if(user.username==user_id):
      t = loader.get_template('my_social_network/following.html') 
      c = Context({ 'user_list': user_list, }) 
      return HttpResponse(t.render(c)) 
  t = loader.get_template('my_social_network/nulluser.html') 
  c = Context({ 'user_list': user_list, }) 
  return HttpResponse(t.render(c))   