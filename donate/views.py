from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from pathlib import Path
# Create your views here.
from django.template.loader import render_to_string
from django.views.generic import UpdateView
import requests
from Project import settings
from donate.forms import DonatePostCreateForm, DonatePostEditForm, AddressForm
from django.forms import modelformset_factory
from twilio.rest import Client
account_sid = 'ACcb8386243a2056a3351ed9e7b6b68aaf' 
auth_token = '2064369a355edb52fc99f6d955760f1e' 
client = Client(account_sid, auth_token) 
from donate.models import Donate_Post
from home.models import Profile
from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives
your_doorNo = None
your_residence = None
your_street = None
your_country = None
your_pinCode = None
your_address = None
your_state = None
your_name = None

def donate_post_create(request):
    if request.method == 'POST':
        form = DonatePostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, f'Post for Donation created successfully!')
            print("=============================here ah==========================================")
            nos=[]
            phonenos=Profile.objects.filter(state=form.cleaned_data['state']).filter(
                city=form.cleaned_data['city']).filter(did_req=True).values_list('user', flat=True)
        
            for i in phonenos:
                #me=User.objects.filter(id=i)
                req=Profile.objects.filter(user=i).values_list('phoneno',flat=True)
                 
                    
                    

                message = client.messages \
                .create(
                     body='ITEMS AVAILABLE FOR DONATION - Team HELPERS',
                     from_='+12058986854',
                     to= (req)
                    )
                print(message.sid)
            mails = []
            emails = Profile.objects.filter(state=form.cleaned_data['state']).filter(
                city=form.cleaned_data['city']).filter(did_req=True).values_list('user', flat=True)
            print(emails)
            profiles = Profile.objects.filter(state=form.cleaned_data['state']).filter(
                city=form.cleaned_data['city']).filter(did_req=True)
            for prof in profiles:
                prof.did_req = False
            for i in emails:
                user_req = User.objects.filter(id=i).values_list('email', flat=True)
                mails.append(str(user_req[0]))
                print(user_req[0])
                # if(admins.count() == 1):
                #     admins = admins.email
                # else:
                #     admins = User.objects.filter(is_superuser = True).values_list('email')
            subject = 'ITEMS AVAILABLE FOR DONATION - Team HELPERS'
            message = render_to_string('donate/sendmails.html', {'data': form})
            send_mail(subject, message, settings.EMAIL_HOST_USER, mails, fail_silently=False)

            return redirect('profile')
    else:
        form = DonatePostCreateForm()
    context = {
        'form': form,
    }
    return render(request, 'donate/donate_post_create.html', context)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Donate_Post
    fields = ['body','doorNo','residence','street','city','pinCode','state','country']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return redirect('profile')
        return redirect('home')

def request_post(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        print("=================================here only===================================")
        if form.is_valid():
            print("=================================accepted===================================")
            global your_doorNo,your_address,your_country,your_pinCode,your_residence,your_state,your_street,your_name
            your_name = None
            your_name = request.user.username
            your_doorNo = None
            your_doorNo = form.cleaned_data['your_doorNo']
            your_residence = None
            your_residence = form.cleaned_data['your_residence']
            your_street = None
            your_street = form.cleaned_data['your_street']
            your_country = None
            your_country = form.cleaned_data['your_country']
            your_pinCode = None
            your_pinCode = form.cleaned_data['your_pinCode']
            your_address = None
            your_address = form.cleaned_data['your_address']
            your_state = None
            your_state = form.cleaned_data['your_state']
            urg = get_object_or_404(Profile, user=request.user)
            print(Profile, urg.did_req)
            posts = Donate_Post.objects.filter(city=form.cleaned_data['your_address'])
            posts_waste = Donate_Post.objects.filter(city=form.cleaned_data['your_address']).filter(is_requested=True)
            print(posts_waste.count())
            print(posts.count())
            Cposts = Donate_Post.objects.filter(city=form.cleaned_data['your_address']).filter(availableitems="Clothes")
            Fposts = Donate_Post.objects.filter(city=form.cleaned_data['your_address']).filter(availableitems="Food")
            Tposts = Donate_Post.objects.filter(city=form.cleaned_data['your_address']).filter(availableitems="Toys")
            Bposts = Donate_Post.objects.filter(city=form.cleaned_data['your_address']).filter(availableitems="Books")
            Oposts = Donate_Post.objects.filter(city=form.cleaned_data['your_address']).filter(availableitems="Others")

            if((posts.count() == 0) or (posts.count()==posts_waste.count())):
                messages.success(request, f'OOPS!!  Posts not available for booking in your city')
                posts = Donate_Post.objects.filter(state=form.cleaned_data['your_state'])
                posts_waste = Donate_Post.objects.filter(state=form.cleaned_data['your_state']).filter(is_requested=True)
                Cposts = Donate_Post.objects.filter(state=form.cleaned_data['your_state']).filter(availableitems="Clothes")
                Fposts = Donate_Post.objects.filter(state=form.cleaned_data['your_state']).filter(availableitems="Food")
                Tposts = Donate_Post.objects.filter(state=form.cleaned_data['your_state']).filter(availableitems="Toys")
                Bposts = Donate_Post.objects.filter(state=form.cleaned_data['your_state']).filter(availableitems="Books")
                Oposts = Donate_Post.objects.filter(state=form.cleaned_data['your_state']).filter(availableitems="Others")

            if((posts.count() == 0)  or (posts.count()==posts_waste.count())):
                messages.success(request, f'SORRY!!....No posts available for booking')
                urg.did_req = True
                urg.save()
                print(Profile, urg.did_req)
                nos=[]
                phonenos=Profile.objects.filter(city=form.cleaned_data['your_address']).values_list('user',flat=True)
            
                for i in phonenos:
                    #me=User.objects.filter(id=i)
                    req=Profile.objects.filter(user=i).values_list('phoneno',flat=True)
                 
                    
                    

                    message = client.messages \
                    .create(
                     body='Donars Required - Team HELPERS',
                     from_='+12058986854',
                     to= (req)
                    )
                    print(message.sid)
      
                mails = []
                #admin = User.objects.filter(is_superuser = True).values('email')
                emails = Profile.objects.filter(city=form.cleaned_data['your_address']).values_list('user',flat=True)
                print(emails)
                for i in emails:
                    user_req = User.objects.filter(id=i).values_list('email',flat=True)
                    mails.append(str(user_req[0]))
                    print(user_req[0])
                # if(admins.count() == 1):
                #     admins = admins.email
                # else:
                #     admins = User.objects.filter(is_superuser = True).values_list('email')
                subject = 'Donars Required - Team HELPERS'
                message = render_to_string('donate/mails.html', {'data': form})
                send_mail(subject, message, settings.EMAIL_HOST_USER, mails, fail_silently=False)
            context = {
                'posts': posts,
                'Cposts': Cposts,
                'Fposts': Fposts,
                'Tposts': Tposts,
                'Bposts': Bposts,
                'Oposts': Oposts

            }
            return render(request,  'donate/donate_post_list.html', context)
    else:
        form = AddressForm()
    context = {
        'form': form,
    }
    return render(request, 'donate/request_post.html', context)

def is_request_post(request):
    print(your_doorNo, your_residence, your_street, your_country, your_pinCode, your_address, your_state, your_name)
    post = get_object_or_404(Donate_Post, title=request.POST.get('post_title'))
    print("============================here vahhh==================================================")
    print(post, post.is_requested)
    if (post.is_requested == False and request.user!=post.author):
        mails = []
        post.is_requested = True
        post.to_doorNo = your_doorNo
        post.to_residence = your_residence
        post.to_street = your_street
        post.to_city = your_address
        post.to_state = your_state
        post.to_country = your_country
        post.to_pinCode = your_pinCode
        post.to_person = your_name
        post.mail_sent = False
        post.save()
        print(post,post.is_requested)
        # user_req = User.objects.filter(username=post.author).values_list('email', flat=True)
        # mails.append(str(user_req[0]))
        # image_path = 'C:/Users/user/Documents/sem5/Project/media/Gratitude.jpg'
        # image_name = Path(image_path).name
        # subject = "Token of Gratitude - from HELPERS"
        # text_message = f"Thanks alot of taking a step ahead to donate and spread LOVE & HUMANITY :) {image_name}."
        # html_message = f"""
        # <!doctype html>
        #     <html lang=en>
        #         <head>
        #             <meta charset=utf-8>
        #             <title>Some title.</title>
        #         </head>
        #         <body>
        #             <h1>{subject}</h1>
        #             <p>
        #             Thanks alot of taking a step ahead to donate and spread LOVE & HUMANITY :)<br>
        #             <img src='cid:{image_name}'/>
        #             </p>
        #         </body>
        #     </html>
        # """
        #
        # def send_email(subject, text_content, html_content=None, sender='pranitasaladi16101@gmail.com', recipient=mails, image_path=None, image_name=None):
        #     email = EmailMultiAlternatives(subject=subject, body=text_content, from_email=sender, to=recipient if isinstance(recipient, list) else [recipient])
        #     if all([html_content, image_path, image_name]):
        #         email.attach_alternative(html_content, "text/html")
        #         email.content_subtype = 'html'  # set the primary content to be text/html
        #         email.mixed_subtype = 'related'  # it is an important part that ensures embedding of an image
        #         with open(image_path, mode='rb') as f:
        #             image = MIMEImage(f.read())
        #             email.attach(image)
        #             image.add_header('Content-ID', f"<{image_name}>")
        #     email.send()
        # send_email(subject="Token of Gratitude", text_content=text_message, html_content=html_message, sender='pranitasaladi16101@gmail.com', recipient=mails, image_path=image_path, image_name=image_name)
        messages.success(request, f'Booking done successfully')
        #return render(request, 'donate/receive.html')
    elif post.is_requested == True:
        messages.success(request, f'Already booked!!...Sorry')
        return redirect('profile')
    return redirect('profile')

# def to_receive(request):
#     post = get_object_or_404(Donate_Post, title=request.POST.get('post_title'))
#     print(post, post.is_requested)
#     if (post.is_requested == False and request.user != post.author):
#         mails = []
#         post.is_requested = True
#         post.save()
#     return render(request, 'donate/receive.html')

def transport_mail(request):
    posts = Donate_Post.objects.filter(mail_sent=False)
    for i in posts:
        print(i.is_acc_for_transport, i.mail_sent)
        if i.is_acc_for_transport == True and i.mail_sent==False:
            profile = get_object_or_404(Profile, user=i.author)
            profile.total_donated = profile.total_donated + 1
            if (i.availableitems == "Clothes"):
                profile.clothes_donated = profile.clothes_donated + 1
                profile.save()
            if (i.availableitems == "Food"):
                profile.food_donated == profile.food_donated + 1
                profile.save()
            if (i.availableitems == "Toys"):
                profile.toys_donated = profile.toys_donated + 1
                profile.save()
            if (i.availableitems == "Books"):
                profile.books_donated = profile.books_donated + 1
                profile.save()
            if (i.availableitems == "Others"):
                profile.others_donated = profile.others_donated + 1
                profile.save()
            print("yes")
            mails = []
            user_req = User.objects.filter(username=i.author).values_list('email', flat=True)
            mails.append(str(user_req[0]))
            image_path = 'C:/Users/user/Documents/sem5/Project/media/Gratitude.jpg'
            image_name = Path(image_path).name
            subject = "Token of Gratitude - from HELPERS"
            text_message = f"Thanks alot of taking a step ahead to donate and spread LOVE & HUMANITY :) {image_name}."
            html_message = f"""
            <!doctype html>
                <html lang=en>
                    <head>
                        <meta charset=utf-8>
                        <title>Some title.</title>
                    </head>
                    <body>
                        <h1>{subject}</h1>
                        <p>
                        Thanks alot of taking a step ahead to donate and spread LOVE & HUMANITY :)<br>
                        <img src='cid:{image_name}'/>
                        </p>
                    </body>
                </html>
            """

            def send_email(subject, text_content, html_content=None, sender='pranitasaladi16101@gmail.com', recipient=mails, image_path=None, image_name=None):
                email = EmailMultiAlternatives(subject=subject, body=text_content, from_email=sender, to=recipient if isinstance(recipient, list) else [recipient])
                if all([html_content, image_path, image_name]):
                    email.attach_alternative(html_content, "text/html")
                    email.content_subtype = 'html'  # set the primary content to be text/html
                    email.mixed_subtype = 'related'  # it is an important part that ensures embedding of an image
                    with open(image_path, mode='rb') as f:
                        image = MIMEImage(f.read())
                        email.attach(image)
                        image.add_header('Content-ID', f"<{image_name}>")
                email.send()
            send_email(subject="Token of Gratitude", text_content=text_message, html_content=html_message, sender='pranitasaladi16101@gmail.com', recipient=mails, image_path=image_path, image_name=image_name)

            to_user = User.objects.filter(username=i.to_person).values_list('email', flat=True)
            print(to_user[0])
            subject = 'Successful Request - Team HELPERS'
            message = render_to_string('donate/success.html', {'data': i})
            send_mail(subject, message, settings.EMAIL_HOST_USER, [to_user[0]], fail_silently=False)
            i.mail_sent = True
            i.save()
            messages.success(request, f'Mails sent for accepted dontions')

        elif i.is_acc_for_transport == False and i.mail_sent==False:
            print("no")
            to_user = User.objects.filter(username=i.to_person).values_list('email',flat=True)
            print(to_user[0])
            subject = 'Request cancelled - Team HELPERS'
            message = render_to_string('donate/fail.html', {'data': i})
            send_mail(subject, message, settings.EMAIL_HOST_USER, [to_user[0]], fail_silently=False)
            i.to_doorNo = None
            i.to_residence = None
            i.to_street = None
            i.to_city = None
            i.to_state = None
            i.to_country = None
            i.to_pinCode = None
            i.is_requested = False
            i.to_person = None
            i.is_acc_for_transport = None
            i.mail_sent = True
            i.save()
            messages.success(request, f'Mails sent for rejected dontions')
        else:
            print("donno")
    return  redirect('index')