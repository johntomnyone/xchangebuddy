from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def index(request):
	if request.method == 'POST':
		fname = request.POST['fname']
		lname = request.POST['lname']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message'] 

		#send a mail
		#send_mail(
		#	'Xchangebuddy: message from ' + fname + lname, # Subject
		#	message, # Message
		#	email, # From Email
		#	['tomnyone@outlook.com'], # Recipient Email
		#	)

		return render(request, 'index.html', {'fname': fname})

	else:
		return render(request, 'index.html', {})



def btc(request):
	return render(request, 'btc.html', {})


def contact(request):
	if request.method == 'POST':
		fname = request.POST['fname']
		lname = request.POST['lname']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message'] 

		#send a mail
		contact = "Message from: " + fname + "\n Last Name: " + lname + "\n Email: " + email + "\n Subject: " + subject + "\n Message: " + message
		send_mail(
			'Xchangebuddy: message from ' + fname + lname + 'n/', # Subject
			contact, # Message
			email, # From Email
			['tomnyone@outlook.com'], # Recipient Email
			)

		return render(request, 'contact.html', {'fname': fname, 'lname': lname, 'subject': subject})

	else:
		return render(request, 'index.html', {})



def paypal(request):
	return render(request, 'paypal.html', {})