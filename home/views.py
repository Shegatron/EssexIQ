from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import smtplib
import os
import getpass
from datetime import datetime

# Create your views here.

def homeView(request):
	print("HomeView", datetime.now())
	try:
	 	x = request.GET['submit']
	 	return render(request, 'home.html', {"submitted": True})
	except KeyError:
	 	return render(request, 'home.html', {"submitted": False})

def load_winter(request):
	return render(request, 'winter.html', {"submitted": False})

def load_summer(request):
	return render(request, 'summer.html', {"submitted": False})


def sendEmail(request):
	data = request.POST
	email = str(data["username"])
	message = str(data["message"])
	fromaddr = "millburnvexrobotics@gmail.com"
	toaddrs = "millburnvexrobotics@gmail.com"
	username = "millburnvexrobotics@gmail.com"
	password = "millburn123"
	msg = "\nEmail: "+email+", Message: "+message
	print(msg)
	os.chdir("/root")
	file = open("messages.txt", 'a+')
	file.write(msg)
	file.close()
	return HttpResponseRedirect("/?submit=True")
