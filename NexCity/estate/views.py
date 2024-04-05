from django.shortcuts import render, redirect
import smtplib
from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib import messages
from . models import Estate, Realtor, Branch, Purchase
from . forms import EstateForm, RealtorForm
PASSWORD = "opjfhgonjoyxgupn"

# Create your views here.


def home(request):
    estate = Estate.objects.order_by('-id')[:9]
    return render(request, "index.html", locals())

def all_listing(request):
    estate = Estate.objects.order_by('-id')
    return render(request, "all_listing.html", locals())

def branch_detail(request, id):
    branch = Branch.objects.filter(id = id)
    return render(request, "branch_detail.html", locals())


def land_details(request, id):
    PASSWORD = "opjfhgonjoyxgupn"
    estate = Estate.objects.filter(id = id)

    s = [i.title for i in estate]
    estates = get_object_or_404(Estate, pk=id)
    if request.method == 'POST':
        name = request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        address = request.POST['address']
        state = request.POST['state']
        if Purchase.objects.filter(email=email, name=name, estate=estates).exists():
            messages.info(request, "You have already contacted us, we will contact you shortly")
            return redirect('land_details', id)
        else:
            new_purchase = Purchase(
                name=name,
                contact=contact,
                email=email,
                address=address,
                state=state,
                estate=estates,
                estate_name = s[0]

            )
    
            new_purchase.save()

            # with smtplib.SMTP("smtp.gmail.com") as connection:
            #     connection.starttls()
            #     connection.login(user="happinessjoseph065@gmail.com", password=PASSWORD)
            #     connection.sendmail(from_addr="happinessjoseph065@gmail.com", to_addrs="happinessjoseph@gmail.com", msg=f"subject: NexCity\n\n Name = {name}, Contact = {contact}, Email = {email}, Address = {address}, {state} made a request to purchase {estate.title}")
            
            # with smtplib.SMTP("smtp.gmail.com") as connection:
            #     connection.starttls()
            #     connection.login(user="happinessjoseph065@gmail.com", password=PASSWORD)
            #     connection.sendmail(from_addr="happinessjoseph065@gmail.com", to_addrs=email, msg=f"subject: NexCity\n\n Thank you {name}, for making a request to purchase {estate.title}, below is the subscription form attached, fill it and send to our email or to nearest branch close to you as we process your request")
            

            return redirect('/thank_you/')
    else:    
        return render(request, "land_details.html", locals()) 


def checkout(request, id):
    estate = Estate.objects.filter(id = id)
    return render(request, "checkout.html", locals())

def dashboard(request):
    estate = Estate.objects.all()
    realtors = Realtor.objects.all()
    branch = Branch.objects.all()
    purchase = Purchase.objects.all()
    return render(request, "dashboard.html", locals())

def find_realtors(request):
    # realtors = Realtor.objects.all()
    if request.method == 'POST':
        address = request.POST['location']
        name = request.POST['name']
        if address is not None:


            results = Realtor.objects.all()
            if address and name:
                results = results.filter(address__icontains=address)
                results = results.filter(name__icontains=name)
                if results:
                    return render(request, 'find_realtors.html', {'results': results, 'address': address, 'name': name,})
                else:
                    no_results = "no_results"
                    return render(request, 'find_realtors.html', {'no_results': no_results , 'address':address, 'name':name})

            elif address:
                results = results.filter(address__icontains=address)
                if results:
                    return render(request, 'find_realtors.html', {'results': results, 'address': address, 'name': name,})
                else:
                    no_results = "no_results"
                    return render(request, 'find_realtors.html', {'no_results': no_results , 'address':address, 'name':name})


            elif name:
                results = results.filter(name__icontains=name)
                if results:
                    return render(request, 'find_realtors.html', {'results': results, 'address': address, 'name': name,})
                else:
                    no_results = "no_results"
                    return render(request, 'find_realtors.html', {'no_results': no_results , 'address':address, 'name':name})
            
                
            
            
        else:
            messages.info(request, "This Field is required to search Estates")
            return redirect('/find_realtors')

    return render(request, "find_realtors.html")

def find_branch(request):
    # realtors = Realtor.objects.all()
    branch = Branch.objects.all()
    if request.method == 'POST':
        address = request.POST['location']
        if address is not None:
            
            if address:
                results = Branch.objects.all()
                results = results.filter(address__icontains=address)
                if results:
                    return render(request, 'find_branch.html', {'results': results, 'address': address})
                    
                No_results ="No results"
                return render(request, 'find_branch.html', {'No_results': No_results, 'address':address})
            else:
                messages.info(request, "This Field is required to search Branches")
            return redirect('/find_branch')
        else:
            messages.info(request, "This Field is required to search Branches")
            return redirect('/find_branch', locals())

    return render(request, "find_branch.html", locals())

def searched_estate(request):
    if request.method == 'POST':
        
        address = request.POST['search_estate']
        if address is not None and address != " ":
            results = Estate.objects.all()
            if address:
                results = Estate.objects.filter(models.Q(title__icontains=address) | models.Q(location__icontains=address))
                
                if results:
                    return render(request, 'searched_estate.html', {'results': results, 'address': address})
                else:
                    no_results = "no_results"
                    return render(request, 'searched_estate.html', {'no_results': no_results , 'address':address,})
            
            
        else:
            messages.info(request, "This Field is required to search Estates")
            return redirect('/')
    

def about(request):
    return render(request, "about.html")


def thank_you(request):
    estate = Estate.objects.all()[:5:1]
    return render(request, "thank_you.html", locals())





def estate_registration(request):
    if request.method == 'POST':
        title = request.POST['title']
        location = request.POST['location']
        documents = request.POST['documents']
        landmarks = request.POST['landmarks']
        features = request.POST['features']
        
        google_map = request.POST['google_map']
        price = request.POST['price']
        size = request.POST['size']
        land_image = request.POST['land_image']
        subscription_form = request.POST['subscription_form']
        c_of_o = request.POST['c_of_o']
        
        if Estate.objects.filter(title=title).exists():
            messages.info(request, "Estate already exists")
            return redirect('estate_registration')
        else:
            new_estate = Estate(
                title = title,
                location=location,
                documents=documents,
                landmarks=landmarks,
                features=features,
                price=price,
                size=size,
                image='image/'+land_image,
                subscription_form='subscription/'+subscription_form,
                c_of_o=c_of_o,
                google_map=google_map

            )
            new_estate.save()
            return redirect('/all_listing/')
    else:    
        return render(request, "estate_registration.html", locals()) 


def success(request):
    return render(request, "success.html")

def register_realtor(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        profile_picture = request.POST['profile_picture']
        
        address = request.POST['address']
        state = request.POST['state']
        occupation = request.POST['occupation']
        gender = request.POST['gender']
        bank_name = request.POST['bank_name']
        account_name = request.POST['account_name']
        account_number = request.POST['account_number']
        invitee = request.POST['invitee']
        contact_invitee = request.POST['contact_invitee']
        receipt = request.POST['receipt']

        if Realtor.objects.filter(email=email).exists():
            messages.info(request, "Email already exists")
            return redirect('/register_realtor/')
        else:
            new_realtor = Realtor(
                name = f'{first_name} {last_name}',
                address=address,
                contact=phone,
                email=email,
                state=state,
                profile_picture=profile_picture,
                occupation=occupation,
                gender=gender,
                bank_name=bank_name,
                account_number=account_number,
                account_name=account_name,
                invite=invitee,
                invite_contact=contact_invitee,
                receipt=receipt,

            )
            new_realtor.save()
            return redirect('/success')
    else:    
        return render(request, "register_realtor.html", locals())

