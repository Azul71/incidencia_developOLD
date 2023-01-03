from django.shortcuts import render
from .models import Enquiry,Follow_ups,Concello,Received,Roles,Status,TypeFollowUp
from django.contrib import messages
from django.shortcuts import redirect
from user.models import CustomUser
from datetime import datetime
from django.db.models import Count,Sum
from random import randint
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

# Insert an Enquiry
def enquiry(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		nif = request.POST['nif']
		razonsocial = request.POST['razonsocial']
		relation = request.POST['relation']
		address = request.POST['address']
		contact = request.POST['contact']
		email = request.POST['email']
		concello = request.POST['concello']
		status = request.POST.get('status')
		#status = request.POST['status']
		received = request.POST['received']
		enquire = request.POST['enquire']
		typefollowup = request.POST['typefollowup']
		#rol = request.POST['rol']
		register = request.POST['register']
		created_on = request.POST['created_on']
		asigned = request.POST['asigned']


		#createdby = CustomUser.objects.get(id=request.user.id)
		createdby = request.user.id
	#	course_instance = Course.objects.get(id=course)

		insert = Enquiry(first_name=first_name,last_name=last_name,nif=nif,
			razonsocial=razonsocial,relation=relation,address=address,
			contact=contact,email=email,concello_id=concello,status_id=status,
			received_id=received,enquire=enquire,typefollowup_id=typefollowup,
			asigned_id=asigned,register=register,created_on=created_on,createdby_id=createdby)
		insert.save()
		messages.success(request,'Guardado!!')
		return redirect('enquiry')

	enquires = Enquiry.objects.all()
	concellos = Concello.objects.all()
	roles = Roles.objects.all()
	statuss = Status.objects.all()
	typefollowups = TypeFollowUp.objects.all()
	receiveds = Received.objects.all()
	asigneds = CustomUser.objects.all()
	
	

	context = {
	'courses':enquires,
	'concellos':concellos,
	'roles':roles,
	'statuss':statuss,
	'typefollowups':typefollowups,
	'receiveds':receiveds,
	'asigneds':asigneds,

	'active_link':'new_enquiry'
	}
	return render(request,'profile/enquiry.html',context)


# View all enquirey 
def all_enquires(request):
	asigned = CustomUser.objects.get(id=request.user.id)

	#all_enquires = Enquiry.objects.filter(asigned_id=asigned,status=1).order_by('-id')
	all_enquires = Enquiry.objects.filter(asigned_id=asigned).order_by('-id')
	context = {
		'enquiries':all_enquires,
		'active_link':'all_enquiry'
	}
	return render(request,'profile/all_enquiries.html',context)


def view_enquiry(request,id):
	fetch = Enquiry.objects.get(id=id)
	fetch_followup = Follow_ups.objects.filter(enquiry=id).order_by('date')
	
	typefollowups_param = TypeFollowUp.objects.all()
	context = {
		'data':fetch,
		'follow_ups':fetch_followup,
		'typefollowups_param':typefollowups_param,
		#'start_date':date
	}
	return render(request,'profile/view_enquiry.html',context)


def follow_up(request,e_id):
	fetch = Enquiry.objects.get(id=e_id)
	if request.method == 'POST':
		typefollowup = request.POST['typefollowup']
		description = request.POST['description']
		date = request.POST['date']
		created_on = request.POST['date']
		#fetch.save()
		insert = Follow_ups(enquiry=fetch,description=description,date=date,typefollowup_id= typefollowup,created_on=created_on)
		insert.save()
		messages.success(request,'Successfully Submitted!!')

	fetch_followup = Follow_ups.objects.filter(enquiry=e_id).order_by('date')
	typefollowups_param = TypeFollowUp.objects.all()
	context = {
		'data':fetch,
		'follow_ups': fetch_followup,
		'typefollowups_param':typefollowups_param,
	}
	return render(request,'profile/view_enquiry.html',context)




def accounts(request,e_id):
	fetch = Enquiry.objects.get(id=e_id)
	details = request.POST['details']
	date = request.POST['date_time']
	amount = request.POST['amount']
	
	insert = account(enquiry_id=fetch,detail=details,date=date,amount=amount)
	insert.save();

	messages.success(request,'Successfully Submitted!!')

	fetch_followup = Follow_ups.objects.filter(enquiry=e_id).order_by('date')
	fetch_account = account.objects.filter(enquiry_id=e_id).order_by('date')
	course_fee=int(fetch.course_fee)
	paid=0;

	for i in fetch_account:
		paid += int(i.amount)

	balance = course_fee-paid

	batch = Batch.objects.filter(center=request.user.select_center.id,status=0)

	date=''
	if fetch.batch:
		batch_start = Batch.objects.get(id=fetch.batch.id)
		date = batch_start.start_date

	context = {
		'data':fetch,
		'follow_ups':fetch_followup,
		'accounts':fetch_account,
		'balance':balance,
		'course_fee':course_fee,
		'batchs':batch,
		'start_date':date
	}
	return render(request,'profile/view_enquiry.html',context)




def status_filter(request,s_id):
	asigned = CustomUser.objects.get(id=request.user.id)

	fetch_data = Enquiry.objects.filter(asigned_id=asigned,status=s_id).order_by('-id')

	context = {
		'enquiries':fetch_data,
		'status':s_id,
		
	}
	return render(request,'profile/status_filter.html',context)


def create_user(request,u_id):
	student = Enquiry.objects.get(id=u_id)
	random_num = str(randint(100000, 999999))
	generate_id = student.first_name.lower() + random_num
	username = generate_id.replace(" ", "")
	password = CustomUser.objects.make_random_password(length=14)

	create_user = CustomUser.objects.create_user(username=username,email=student.email,password=password,role=3,phone=student.contact,first_name=student.first_name,last_name=student.last_name)
	create_user.is_staff = False
	create_user.save

	student.lms_id=1
	student.lms_username=username
	student.save()

	subject = 'Congratulation ! ID has been created for your Course'
	message = 'Your Credentials to login to Golearn \n Username: '+username+'\nPassword: '+password+'\n\n You can Change the password later in the account section after logging in'
	email_from = settings.EMAIL_HOST_USER
	recipient_list = [student.email,]
	send_mail( subject, message, email_from, recipient_list )

	messages.success(request,'LMS ID Successfully Created !!')
	return redirect('dashboard')

	

	