from django.shortcuts import render, render_to_response
from .models import Cliente, Rescatado,Adopcion 
from django.template import loader,RequestContext
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
