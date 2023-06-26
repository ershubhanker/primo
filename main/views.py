from django.shortcuts import render,HttpResponse,redirect
from django.core.mail import EmailMessage
from . models import Contact,Image,Headings,navItems,buttonText,paragraph,spareParts
from django.core.mail import send_mail,BadHeaderError
from django.template.loader import render_to_string
from django.conf import settings
from .forms import ContactForm
# Create your views here.
def home(request):
    nav = navItems.objects.all()
    nav0 = nav[0]
    nav1 = nav[1]
    nav2 = nav[2]
    nav3 = nav[3]
    nav4 = nav[4]
    nav5 = nav[5]
    nav6 = nav[6]


    para = paragraph.objects.all()
    para0 =  para[0]
    para1 =  para[1]
    para2 =  para[2]
    para3 =  para[3]
    para4 =  para[4]
    para5 =  para[5]
    para6 =  para[6]
    para7 =  para[7]
    para8 =  para[8]
    para9 =  para[9]
    para10 =  para[10]
    para11 =  para[11]
    para12 =  para[12]
    para13 =  para[13]
    para14 =  para[14]
    para15 =  para[15]
    para16 =  para[16]
    # footer
    para17 =  para[17]
    para18 =  para[18]
    para19 =  para[19]
    para20 =  para[20]
    para21 =  para[21]
    para22 =  para[22]
    para23 =  para[23]
    para24 =  para[24]
    para25 =  para[25]

    btnText = buttonText.objects.all()
    btnText0 =  btnText[0]
    btnText1 =  btnText[1] #Learn More
    btnText2 =  btnText[2]
    btnText3 =  btnText[3] #Call Us today
    btnText4 =  btnText[4]
    # btnText5 =  btnText[5]

    headings = Headings.objects.all()
    heading0 = headings[0]
    heading1 = headings[1]
    heading2 = headings[2]
    heading3 = headings[3]
    heading4 = headings[4]
    heading5 = headings[5]
    heading6 = headings[6]
    heading7 = headings[7]
    heading8 = headings[8]
    heading9 = headings[9]
    heading10 = headings[10]
    heading11 = headings[11]
    heading12 = headings[12]
    heading13 = headings[13]

    

    images = Image.objects.all()
    image0 =  images[0]
    image1 = images[1]
    image2 = images[2]
    image3 = images[3] #logo image
    image4 = images[4]
    image5 = images[5]
    image6 = images[6]
    image7 = images[7]
    image8 = images[8]
    image9 = images[9]
    return render(request, 'index.html',{'images': images,'image1':image1,'image0':image0,'image2':image2,'image3':image3,'image4':image4,'image5':image5,'image6':image6,'image7':image7,'image8':image8,'image9':image9,
                                         'nav':nav,'nav0':nav0,'nav1':nav1,'nav2':nav2,'nav3':nav3,'nav4':nav4,'nav5':nav5,'nav6':nav6,
                                         'headings':headings,'heading0':heading0,'heading1':heading1,'heading2':heading2,'heading3':heading3,'heading4':heading4,'heading5':heading5,'heading6':heading6,'heading7':heading7,'heading8':heading8,'heading9':heading9,'heading10':heading10,'heading11':heading11,'heading12':heading12,'heading13':heading13,
                                         'btnText':btnText,'btnText0':btnText0,'btnText1':btnText1,'btnText2':btnText2,'btnText3':btnText3,'btnText4':btnText4,
                                         'para':para,'para0':para0,'para1':para1,'para2':para2,'para3':para3,'para4':para4,'para5':para5,'para6':para6,'para7':para7,'para8':para8,'para9':para9,'para10':para10,'para11':para11,'para12':para12,'para13':para13,'para14':para14,'para15':para15,'para16':para16,'para17':para17,'para18':para18,'para19':para19,'para20':para20,'para21':para21,'para22':para22,'para23':para23,'para24':para24,'para25':para25})


def about(request):
    nav = navItems.objects.all()
    nav0 = nav[0]
    nav1 = nav[1]
    nav2 = nav[2]
    nav3 = nav[3]
    nav4 = nav[4]
    nav5 = nav[5]
    nav6 = nav[6]

    

    images = Image.objects.all()
    image0 =  images[0]
    image1 = images[1]
    image2 = images[2]
    image3 = images[3] #logo image
    image10 =  images[10]
    # team member images
    image11 =  images[11]
    image12 =  images[12]
    image13 =  images[13]


    para = paragraph.objects.all()
    para7 = para[7]
    para8 = para[8]
    para9 = para[9]
    para10 = para[10]
    para17 =  para[17]
    para18 =  para[18]
    para19 =  para[19]
    para20 =  para[20]
    para21 =  para[21]
    para22 =  para[22]
    para23 =  para[23]
    para24 =  para[24]
    para25 =  para[25]
    # our existence
    para39 =  para[39]
    para40 =  para[40]
    para41 =  para[41]
    para42 =  para[42]
    para43 =  para[43]
    # paras under 4 headers
    para49 = para[49]
    para50 = para[50]
    para51 = para[51]
    para52 = para[52]
    # para under our team heading
    para53 = para[53]
    # quotes of team members
    para54 = para[54]
    para55 = para[55]
    para56 = para[56]

    


    btnText = buttonText.objects.all()
    btnText6 =  btnText[6]

    headings = Headings.objects.all()
    heading6 = headings[6]
    heading7 = headings[7]
    heading23 = headings[23]
    heading24 = headings[24]
    heading25 = headings[25]
    heading26 = headings[26]
    heading27 = headings[27]
    heading32 = headings[32]
    heading33 = headings[33]
    heading34 = headings[34]
    heading35 = headings[35]
    heading36 = headings[36]
    heading37 = headings[37]
    heading38 = headings[38]
    heading39 = headings[39]
    heading40 = headings[40]
    # names of team members
    heading41 = headings[41]
    heading42 = headings[42]
    heading43 = headings[43]

    return render(request,'about.html',{'nav':nav,'nav0':nav0,'nav1':nav1,'nav2':nav2,'nav3':nav3,'nav4':nav4,'nav5':nav5,'nav6':nav6,
                                        'btnText':btnText,'btnText6':btnText6,
                                        'headings':headings,'heading6':heading6,'heading7':heading7,'heading32':heading32,'heading23':heading23,'heading24':heading24,'heading25':heading25,'heading26':heading26,'heading27':heading27,'heading33':heading33,'heading34':heading34,'heading35':heading35,'heading36':heading36,'heading37':heading37,'heading38':heading38,'heading39':heading39,'heading40':heading40,'heading41':heading41,'heading42':heading42,'heading43':heading43,
                                        'para7':para7,'para8':para8,'para9':para9,'para10':para10,'para17':para17,'para18':para18,'para19':para19,'para20':para20,'para21':para21,'para22':para22,'para23':para23,'para24':para24,'para25':para25,'para39':para39,'para40':para40,'para41':para41,'para42':para42,'para43':para43,'para49':para49,'para50':para50,'para51':para51,'para52':para52,'para53':para53,'para54':para54,'para55':para55,'para56':para56,
                                        'images':images,'image1':image1,'image0':image0,'image2':image2,'image3':image3,'image10':image10,'image11':image11,'image12':image12,'image13':image13,})


def coffee(request):
    nav = navItems.objects.all()
    nav0 = nav[0]
    nav1 = nav[1]
    nav2 = nav[2]
    nav3 = nav[3]
    nav4 = nav[4]
    nav5 = nav[5]
    nav6 = nav[6]

    headings = Headings.objects.all()
    heading23 = headings[23]
    heading24 = headings[24]
    heading25 = headings[25]
    heading26 = headings[26]
    heading27 = headings[27]
    heading28 = headings[28]
    heading29 = headings[29]
    heading30 = headings[30]
    heading31 = headings[31]
    heading32 = headings[32]
    
    btnText = buttonText.objects.all()
    btnText6 =  btnText[6]

    para = paragraph.objects.all()
    # our existence
    para39 =  para[39]
    para40 =  para[40]
    para41 =  para[41]
    para42 =  para[42]
    para43 =  para[43]
    # other paras
    para44 =  para[44]
    para45 =  para[45]
    para46 =  para[46]
    para47 =  para[47]
    para48 =  para[48]
    # footer
    para17 =  para[17]
    para18 =  para[18]
    para19 =  para[19]
    para20 =  para[20]
    para21 =  para[21]
    para22 =  para[22]
    para23 =  para[23]
    para24 =  para[24]
    para25 =  para[25]    

    nav = navItems.objects.all()
    nav0 = nav[0]
    nav1 = nav[1]
    nav2 = nav[2]
    nav3 = nav[3]
    nav4 = nav[4]
    nav5 = nav[5]
    nav6 = nav[6]

    images = Image.objects.all()
    image3 =  images[3] #logo image
    image10 =  images[10]

    return render(request,'coffee.html',{'nav':nav,'nav0':nav0,'nav1':nav1,'nav2':nav2,'nav3':nav3,'nav4':nav4,'nav5':nav5,'nav6':nav6,
                                         'btnText':btnText,'btnText6':btnText6,
                                         'heading23':heading23,'heading24':heading24,'heading25':heading25,'heading26':heading26,'heading27':heading27,
                                         'para17':para17,'para18':para18,'para19':para19,'para20':para20,'para21':para21,'para22':para22,'para23':para23,'para24':para24,'para25':para25,'para39':para39,'para40':para40,'para41':para41,'para42':para42,'para43':para43,'para44':para44,'para45':para45,'para46':para46,'para47':para47,'para48':para48,
                                         'images':images,'image10':image10,'image3':image3,
                                         'headings':headings,'heading28':heading28,'heading29':heading29,'heading30':heading30,'heading31':heading31,'heading32':heading32,})


def shoproaster(request):
    nav = navItems.objects.all()
    nav0 = nav[0]
    nav1 = nav[1]
    nav2 = nav[2]
    nav3 = nav[3]
    nav4 = nav[4]
    nav5 = nav[5]
    nav6 = nav[6]

    images = Image.objects.all()
    image3 =  images[3] #logo image
    image14 =  images[14]
    image15 =  images[15]
    image16 =  images[16]
    image17 =  images[17]
    image18 =  images[18]
    image19 =  images[19]



    nav = navItems.objects.all()
    nav0 = nav[0]
    nav1 = nav[1]
    nav2 = nav[2]
    nav3 = nav[3]
    nav4 = nav[4]
    nav5 = nav[5]

    btnText = buttonText.objects.all()
    btnText5 =  btnText[5] #order now
    btnText1 =  btnText[1] #learn more

    para = paragraph.objects.all()
    para26 =  para[26]
    para27 =  para[27]
    para28 =  para[28]
    para29 =  para[29]
    para30 =  para[30]
    para31 =  para[31]
    para32 =  para[32]
    para33 =  para[33]
    para34 =  para[34]
    para35 =  para[35]
    para36 =  para[36]
    para37 =  para[37]
    para38 =  para[38]
    para39 =  para[39]
    para40 =  para[40]
    para41 =  para[41]
    para42 =  para[42]
    para43 =  para[43]

    # para = paragraph.objects.all()
    para17 =  para[17]
    para18 =  para[18]
    para19 =  para[19]
    para20 =  para[20]
    para21 =  para[21]
    para22 =  para[22]
    para23 =  para[23]
    para24 =  para[24]
    para25 =  para[25]
    

    headings = Headings.objects.all()
    heading14 = headings[14]
    heading15 = headings[15]
    heading16 = headings[16]
    heading17 = headings[17] #Technical Information
    heading18 = headings[18]
    heading19 = headings[19]
    heading20 = headings[20]
    heading21 = headings[21]
    heading22 = headings[22]
    heading23 = headings[23]
    heading24 = headings[24]
    heading25 = headings[25]
    heading26 = headings[26]
    heading27 = headings[27]
    

    return render(request,'shop.html',{'nav':nav,'nav0':nav0,'nav1':nav1,'nav2':nav2,'nav3':nav3,'nav4':nav4,'nav5':nav5,'nav6':nav6,
                                       'images':images,'image3':image3,'image14':image14,'image15':image15,'image16':image16,'image17':image17,'image18':image18,'image19':image19,
                                       'btnText':btnText,'btnText5':btnText5,'btnText1':btnText1,
                                       'headings':headings,'heading14':heading14,'heading15':heading15,'heading16':heading16,'heading17':heading17,'heading18':heading18,'heading19':heading19,'heading20':heading20,'heading21':heading21,'heading22':heading22,'heading23':heading23,'heading24':heading24,'heading25':heading25,'heading26':heading26,'heading27':heading27,
                                         'para':para,'para17':para17,'para18':para18,'para19':para19,'para20':para20,'para21':para21,'para22':para22,'para23':para23,'para24':para24,'para25':para25,'para26':para26,'para27':para27,'para28':para28,'para29':para29,'para30':para30,'para31':para31,'para32':para32,'para33':para33,'para34':para34,'para35':para35,'para36':para36,'para37':para37,'para38':para38,'para39':para39,'para40':para40,'para41':para41,'para42':para42,'para43':para43,})

# def gallery(request):
#     return render(request, 'gallery.html')


def blog(request):
    nav = navItems.objects.all()
    nav0 = nav[0]
    nav1 = nav[1]
    nav2 = nav[2]
    nav3 = nav[3]
    nav4 = nav[4]
    nav5 = nav[5]
    nav6 = nav[6]



    images = Image.objects.all()
    image3 =  images[3]

    para = paragraph.objects.all()
    para17 =  para[17]
    para18 =  para[18]
    para19 =  para[19]
    para20 =  para[20]
    para21 =  para[21]
    para22 =  para[22]
    para23 =  para[23]
    para24 =  para[24]
    para25 =  para[25]

    nav = navItems.objects.all()
    nav0 = nav[0]
    nav1 = nav[1]
    nav2 = nav[2]
    nav3 = nav[3]
    nav4 = nav[4]
    nav5 = nav[5]
    return render(request,'news.html',{'nav':nav,'nav0':nav0,'nav1':nav1,'nav2':nav2,'nav3':nav3,'nav4':nav4,'nav5':nav5,'nav6':nav6,
                                       'para17':para17,'para18':para18,'para19':para19,'para20':para20,'para21':para21,'para22':para22,'para23':para23,'para24':para24,'para25':para25,
                                       'images':images,'image3':image3,})






def contact(request):
    nav = navItems.objects.all()
    nav0 = nav[0]
    nav1 = nav[1]
    nav2 = nav[2]
    nav3 = nav[3]
    nav4 = nav[4]
    nav5 = nav[5]
    nav6 = nav[6]

    images = Image.objects.all()
    image3 =  images[3] #logo image

    para = paragraph.objects.all()
    para17 =  para[17]
    para18 =  para[18]
    para19 =  para[19]
    para20 =  para[20]
    para21 =  para[21]
    para22 =  para[22]
    para23 =  para[23]
    para24 =  para[24]
    para25 =  para[25]

    para26 = para[26]


    headings = Headings.objects.all()
    heading45 = headings[45] #Contact

    para = paragraph.objects.all()
    para57 = para[57] #GET 24/7 SUPPORT


    # contact form
    if request.method == 'POST':
        print(request.method)
        form = ContactForm(request.POST)
        if form.is_valid():
            print("entered the if block")
            # Get the form data
            # name = form.cleaned_data['name']
            # print(name)
            email = form.cleaned_data['email']
            print(email)
            subject = form.cleaned_data['subject']
            print(subject)
            message = form.cleaned_data['message']
            print(message)

            # Send the email
            send_mail(
                subject,
                message,
                'django.core.mail.backends.smtp.EmailBackend',
                [email],
            )
            print("sent successfully----------------")
            return redirect('contact')
    else:
        print('---------done')
        form = ContactForm()

    return render(request, 'contact.html',{'form':form,'nav':nav,'nav0':nav0,'nav1':nav1,'nav2':nav2,'nav3':nav3,'nav4':nav4,'nav5':nav5,'nav6':nav6,
                                           'heading45':heading45,
                                           'images':images,'image3':image3,
                                           'para':para,'para17':para17,'para18':para18,'para19':para19,'para20':para20,'para21':para21,'para22':para22,'para23':para23,'para24':para24,'para25':para25,'para26':para26,'para57':para57})



def spareparts(request):
    images = Image.objects.all()
    image3 =  images[3] #logo image

    nav = navItems.objects.all()
    nav0 = nav[0]
    nav1 = nav[1]
    nav2 = nav[2]
    nav3 = nav[3]
    nav4 = nav[4]
    nav5 = nav[5]
    nav6 = nav[6]

    headings = Headings.objects.all()
    heading44 = headings[44] #Spare parts
    
    
    para = paragraph.objects.all()
    para17 =  para[17]
    para18 =  para[18]
    para19 =  para[19]
    para20 =  para[20]
    para21 =  para[21]
    para22 =  para[22]
    para23 =  para[23]
    para24 =  para[24]
    para25 =  para[25]

    spare = spareParts.objects.all()


    return render(request,'spareparts.html',{'spare':spare,
        'nav':nav,'nav0':nav0,'nav1':nav1,'nav2':nav2,'nav3':nav3,'nav4':nav4,'nav5':nav5,'nav6':nav6,
                                             'image3':image3,
                                             'para':para,'para17':para17,'para18':para18,'para19':para19,'para20':para20,'para21':para21,'para22':para22,'para23':para23,'para24':para24,'para25':para25,
                                             'heading44':heading44,})
    # send_mail(
    #         'This is test mail',
    #         'this is message',
    #         'boredstuff2021@gmail.com',
    #         ['spacelover2003@gmail.com'],
    #         fail_silently=False,
    # )

    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     # print("form")

    #     if form.is_valid():
    #         # name = form.cleaned_data['name']
    #         # print("name sent")
    #         email = form.cleaned_data['email']
    #         print("email sent")
    #         subject = form.cleaned_data['subject']
    #         print("subject sent")
    #         message = form.cleaned_data['message']
    #         print("message sent")

    #         send_mail(
    #                   subject,
    #                   message,
    #                   'boredstuff2021@gmail.com',
    #                   [email],
    #                   fail_silently=False,
    #                   )
    #         print("------------------sent")
    #         return redirect('contact')
          
    # form = ContactForm()
    # return render(request, 'contact.html')


# def service(request):
#     return render(request,'service.html')


# def reservation(request):
#     return render(request, 'reservation.html')
 

# def testimonial(request):
#     return render(request, 'testimonial.html')

# def test(request):
#     return render(request, 'cart.html')