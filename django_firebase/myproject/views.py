
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
import pyrebase 
from django.shortcuts import render


config = {
    "apiKey": "AIzaSyAL6y7jvIY1win9H9XGy1BcQpqj7MyNSYg",
    "authDomain": "demo-df3a0.firebaseapp.com",
    "databaseURL": "https://demo-df3a0.firebaseio.com",
    "projectId": "demo-df3a0",
    "storageBucket": "demo-df3a0.appspot.com",
    "messagingSenderId": "538306671431",
    "appId": "1:538306671431:web:853596b85c3f3a6ff55262",
    "measurementId": "G-208ZMQNRMP"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()
storage = firebase.storage()

def homepage(request):
    return render(request, "accounts/superuser.html")

def signin(request):
    return render(request, "accounts/login.html")

def postsign(request):
    email=request.POST.get('email')
    passw = request.POST.get("password")
    try:
        user = auth.sign_in_with_email_and_password(email,passw)
    except:
        message="invalid credentials"
    session_id=user['idToken']
    idtoken= request.session['uid']=str(session_id)
    a = auth.get_account_info(idtoken)
    a = a['users']
    print (a)
    a = a[0]
    a = a['localId']
    
    name = database.child('users').child(a).child('username').get().val()
    return render(request, "accounts/dashboard.html",{"e":name})



def register(request):
    return render(request, "accounts/register.html")

def postregister(request):
    fname=request.POST.get('first_name')
    lname=request.POST.get('last_name')
    email=request.POST.get('email')
    passw=request.POST.get('psw')
    caddress=request.POST.get('address')
    pincode=request.POST.get('pin_code')
    contactno=request.POST.get('contact_no')
    url=request.POST.get('url')
    user=auth.create_user_with_email_and_password(email,passw)
    uid = user['localId']
    data={"First Name":fname,"Last Name":lname,"Email":email,"Password":passw,"Communication Address":caddress,"Pin Code":pincode,"Contact No":contactno,"Id Proof":url}
    database.child("users").child(uid).set(data)
    return render(request, "accounts/login.html")