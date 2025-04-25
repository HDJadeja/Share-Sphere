from django.shortcuts import render,redirect
from SSMAIN.models import *
from CCClub.models import *
from PearlM.models import *
from RSClub.models import *
from SSSS.models import *
import os 
from SSMAIN.data_structure import linked_list


# Create your views here.

def generate_id(mode=""):
    import random
    valid_stuff = "abcdefghijklmnopqrstuvwxyz1234567890,';:&^%$#"
    if mode == "num":
        valid_stuff = "1234567890"
    memid = "".join(random.choice(valid_stuff) for i in range(10))
    return memid

def Home(request):
    error=""

    if request.POST and request.session.get('MEMBER_id') is None:
        invitation_id = request.POST['invite_id']
        inviter_username = request.POST['invite_username']
        CODE = request.POST['CODE']
        username = request.POST['member_username']
        email = request.POST['email']
        phone = request.POST['phonenumber']
        add = request.POST["address"]
        print("======================",len(request.POST["phonenumber"]))
        if members_invited.objects.filter(invitation_id=invitation_id,CODE=CODE).exists() and (member.objects.filter(member_username=inviter_username).exists() or inviter_username=="SS&CO.") and len(request.POST["phonenumber"]) in range(5,16):
            generated_id = generate_id()
            member(member_email=email,member_username=username,member_Memberid = generated_id,member_address=add,member_phone=phone).save()
            request.session["MEMBER_id"] = generated_id
            request.session["CART"] = linked_list().serialize()
            
        else:
            error = "PLEASE ENTER VALID INVITATION DATA"

    elif request.POST:
        invi_id = generate_id()
        CODE = generate_id("num")
        member_id = request.session['MEMBER_id']
        invited_email = request.POST['email']
        invited_add = request.POST['ADD']
        members_invited(invitation_id=invi_id,CODE=CODE,inviter_memberid=member_id,INVITED_EMAIL=invited_email,INVITED_ADDRESS=invited_add).save()
        print("elif ma ayu")
        

    return render(request,'HOME.html',context={'error':error})

def logout(request):
    if "adminid" in request.session:
        del request.session['adminid']
    elif "MEMBER_id" in request.session:
        del request.session['MEMBER_id']
    return redirect("SSH")

def adminlog_in(request):
    goterror = ""
    print(" bare ubhu che if na ",request.POST)

    if request.POST and not request.session.get("adminid"):
        username = request.POST['uname']
        password = request.POST['SSkey']
        if admins.objects.filter(admin_id=username,admin_pass=password).exists():
            request.session['adminid'] = username
        else:
            goterror = "PLEASE ENTER VALID ADMIN CREDENTIALS"
            
    elif request.POST.get("submit_mode"):
        mode = request.POST.get("submit_mode")

        print(mode)
        if mode.startswith("Add_"):

            mtype = mode[-2::1]
            print(" add ma ayu aa toh ")

            if mtype=="PM":
                id = request.POST.get("product_id")
                name = request.POST.get("product_name")
                price = request.POST.get("product_price")
                monarch = request.POST.get("product_monarch")
                image = request.FILES.get("product_image")
                country = request.POST.get("product_country")
                product_PMclub(product_id=id,product_name=name,product_price=price,product_monarch=monarch,product_image=image,product_country=country).save()
         
            elif mtype == "CC":
                id = request.POST.get("product_id")
                name = request.POST.get("artist_name")
                price = request.POST.get("art_price")
                title = request.POST.get("art_title")
                image = request.FILES.get("art_img")
                description = request.POST.get("art_description")
                product_CCClub(product_id=id,art_name=name,art_price=price,art_description=description,art_img=image,art_title=title).save()
        
            elif mtype == "SS":
                id = request.POST.get("product_id")
                name = request.POST.get("product_name")
                price = request.POST.get("product_price")
                image = request.FILES.get("product_image")
                artist = request.POST.get("product_artist")
                SSSS_products(product_id=id,product_name=name,product_price=price,product_artist=artist,product_image=image).save()
            
            elif mtype == "RS":
                id = request.POST.get("product_id")
                name = request.POST.get("product_name")
                price = request.POST.get("product_price")
                image = request.FILES.get("product_image")
                product_RSclub(product_id=id,product_name=name,product_price=price,product_image=image).save()
                print(" ander ayu rs ma ")

        elif mode.startswith("R_"):
            print(" ander remove mate ayu ")
            id = request.POST.get("product_id")
            mtype = mode[-2::1]
            print(mtype)
        
            deleted_count = 0

            if mtype == "CC" and product_CCClub.objects.filter(product_id=id).exists():
                product = product_CCClub.objects.get(product_id=id)
                image_to_be_removed = product.art_img.path
                os.remove(image_to_be_removed)
                print(" ayu ayu ho")
                deleted_count = product.delete()[0]

            elif mtype == "SS" and SSSS_products.objects.filter(product_id=id).exists():
                product = SSSS_products.objects.get(product_id=id)
                image_to_be_removed = product.product_image.path
                os.remove(image_to_be_removed)
                print(" ayu ayu ho")
                deleted_count = product.delete()[0]

            elif mtype=="PM" and product_PMclub.objects.filter(product_id=id).exists():
                product = product_PMclub.objects.get(product_id=id)
                image_to_be_removed = product.product_image.path
                os.remove(image_to_be_removed)
                print(" ayu ayu ho")
                deleted_count = product.delete()[0]

            elif mtype=="RS" and product_RSclub.objects.filter(product_id=id).exists():
                product = product_RSclub.objects.get(product_id=id)
                image_to_be_removed = product.product_image.path
                os.remove(image_to_be_removed)
                deleted_count = product.delete()[0]

                
            if deleted_count>0:
                print("removed")
            else:
                print("not removed")

        
    return render(request,"adminlog.html",context={'Got_error':goterror})



def add_in_cart(request,product_id,club):

    cart = linked_list().deserialize(list(request.session["CART"]))
    if club == "PM" and product_PMclub.objects.filter(product_id=product_id).exists():
        product = product_PMclub.objects.get(product_id=product_id)
        cart.add_product(str(product.product_image.url),product.product_name,900,float(product.product_price))

    elif club == "CC" and product_CCClub.objects.filter(product_id=product_id).exists():
        product = product_CCClub.objects.get(product_id=product_id)
        print(str(product.art_img.url))
        cart.add_product(str(product.art_img.url),product.art_title,900,float(product.art_price))

    elif club == "SS" and SSSS_products.objects.filter(product_id=product_id).exists():
        product = SSSS_products.objects.get(product_id=product_id)
        cart.add_product(str(product.product_image.url),product.product_name,2200,float(product.product_price))

    elif club == "RS" and product_RSclub.objects.filter(product_id=product_id).exists():
        product = product_RSclub.objects.get(product_id=product_id)
        cart.add_product(str(product.product_image.url),product.product_name,2200,float(product.product_price))

    request.session["CART"] = cart.serialize()
    return show_cart(request)
    
def show_cart(request):
    cart = list(request.session["CART"])
    totals = sum([item['product_price']+item['club_charge'] for item in cart])
    return render(request,"cart.html",context={'cart':cart,'total_amount':totals,'Item_total':len(cart)})

def remove_from_cart(request):

    if request.POST:
        product_name = request.POST["p_name"]
        cart = list(request.session["CART"])

        for items in cart:
            print(" looping ",product_name)
            if items['product_name'] == product_name:
                cart.remove(items)
                print(" malyu remove amte ")
                break

        request.session["CART"] = cart
        
    return show_cart(request)
