from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .forms import Appointment
from django.contrib import messages

# Create your views here.


def home(request):
	return render(request,"index.html",{})


def about(request):
	return render(request,"about.html",{})

def service(request):
	return render(request,"service.html",{})

def appointment(request):
	if request.method == 'POST':
		form = Appointment(request.POST)
		if form.is_valid():
			gen = ["Male","Female"]
			serv = ["General CheckUp","Laboratory Test","Children Care"]
			name = form.cleaned_data.get("Name")
			email = form.cleaned_data.get("Email")
			phonenumber = form.cleaned_data.get("Phone_Number")
			gender = form.cleaned_data.get("Gender")
			service = form.cleaned_data.get("Request_service")
			add = form.cleaned_data.get("Additional_message")
			
			message = "Hi Doctor, "+name+" has requested "+serv[int(service)-1]+" service. Please schedule an appointment for "+name+" immediately through the following details."+"\n\n"+"Gender: "+gen[int(gender)-1]+"\n"+"Phone number: "+phonenumber+"\n"+"Email address: "+email+"\n"+"Additional message: "+add+"\n\n"+"Thanks."
			
			send_mail('Appointment Request',message,'morladhospital@gmail.com',['morladhospital@gmail.com'],fail_silently=False)
			messages.success(request,'Appointment request delivered! Expect a mail from us.')
			return redirect('appointment')
	else:
		form = Appointment()

	return render(request,"appointment.html",{"form":form})
