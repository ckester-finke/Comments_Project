# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Comment
from django.shortcuts import render, redirect
from django.contrib import messages
from operator import attrgetter
# Create your views here.
def index(request):
    #Comment.objects.all().delete()
    context = {
        "comments": sorted(Comment.objects.all(), key=attrgetter('created_at'), reverse= True)
    }
    return render(request, 'comments_app/index.html', context)
def add(request):
    results = Comment.objects.Validator(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')
    comment = Comment.objects.create(comment=request.POST['comment'])
    return redirect('/')
