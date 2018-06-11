# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.http import JsonResponse
import json

from django.shortcuts import render

from django.shortcuts import render
from backEnd.models import User

def add_friend(id1,id2):
    player1 = User.objects.get(user_id=id1)
    player2 = User.objects.get(user_id=id2)
    player1.friends.add(player2)
    player2.friends.add(player1)
    player1.save()
    player2.save()

def del_friend(id1,id2):
    player1 = User.objects.get(user_id=id1)
    player2 = User.objects.get(user_id=id2)
    player1.friends.remove(player2)
    player2.friends.remove(player1)
    player1.save()
    player2.save()

def empty_data():
    for player in User.objects.all():
        player.history_high = 0
        player.save()

def game_view(request,user_id):
    # add_friend(1,3)
    player = User.objects.get(user_id = user_id)
    high = player.history_high
    friends = player.friends.all()
    # friends = User.objects.all()
    data = {
        'history_high': json.dumps(high),
        'friends': friends,
        'user_id':json.dumps(user_id),
    }
    return render(request, 'tinyHeart.html', data)

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))

def update_data(request):
    new_score = int(request.GET['new_score'])
    id = int(request.GET['id'])
    player = User.objects.get(user_id=id)
    player.history_high = new_score
    player.save()
    return HttpResponse()
