from django.shortcuts import render, redirect, HttpResponse
from .models import BookOrder, Post
from django.views import generic


def book(request):
    return render(request, 'book.html')

def infectioncontrolcleaning(request):
    if request.method=='POST':
        print(request)
        postcode = request.POST['q']
        name = request.POST['Name']
        email = request.POST['Email']
        Ph = request.POST['Phone']
        flat_bulding_name = request.POST['flat']
        street_name = request.POST['street']
        service_details = request.POST['service_details']
        infection = request.POST['cleaning']
        appointment_timing_date = request.POST['appointment']
        total_price = request.POST['totalpricesssss']
        user_description = request.POST['note_first']
        note_final = request.POST['note_final']

        
        
        print(postcode)
        datafrom = BookOrder(postcode=postcode,name=name, email=email, user_description=user_description, note_final=note_final, Ph=Ph,service_details=service_details,infection=infection, flat_bulding_name=flat_bulding_name, street_name=street_name,appointment_timing_date=appointment_timing_date, total_price=total_price)
        datafrom.save()
        return redirect('book')
    else:
        product=Post.objects.all()
        context={
            "post_list":product,
        }
        

    

       
            # HttpResponse("hello world")
    return render(request, 'infectioncontrolcleaning.html',context)

# class infectioncontrolcleaning(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'infectioncontrolcleaning.html'
        
    


def Builderscleaning(request):
    if request.method=='POST':
        print(request)
        postcode = request.POST['q']
        name = request.POST['Name']
        email = request.POST['Email']
        Ph = request.POST['Phone']
        flat_bulding_name = request.POST['flat']
        street_name = request.POST['street']
        service_details = request.POST['service_details']
        # infection = request.POST['cleaning']
        appointment_timing_date = request.POST['appointment']
        total_price = request.POST['totalpricesssss']
        user_description = request.POST['note_first']
        note_final = request.POST['note_final']

        please_tell_us_about_your_place1 = request.POST['please_tell_us_about_your_place']
        please_tell_us_about_your_place2 = request.POST['bed7']
        please_tell_us_about_your_place3 = request.POST['bath7']
        please_tell_us_about_your_place4 = request.POST['level7']
        is_the_property_furnished_or_empty = request.POST['property7']
        how_would_you_like_your_carpet_to_be_cleaned = request.POST['Hoovered7']
        most_of_our_customers_who_book_after_builders_cleaning_also_include = request.POST['selectedtext5']
        most_of_our_customers_who_book_after_builders_cleaning_also_include2 = request.POST['matress5']
        we_recommend_a_total_of_time_served = request.POST['manhour4']
       
        
        
        
        print(postcode)
        datafrom = BookOrder(postcode=postcode,we_recommend_a_total_of_time_served=we_recommend_a_total_of_time_served,most_of_our_customers_who_book_after_builders_cleaning_also_include2=most_of_our_customers_who_book_after_builders_cleaning_also_include2,most_of_our_customers_who_book_after_builders_cleaning_also_include=most_of_our_customers_who_book_after_builders_cleaning_also_include,how_would_you_like_your_carpet_to_be_cleaned=how_would_you_like_your_carpet_to_be_cleaned,is_the_property_furnished_or_empty=is_the_property_furnished_or_empty,please_tell_us_about_your_place4=please_tell_us_about_your_place4,please_tell_us_about_your_place3=please_tell_us_about_your_place3,please_tell_us_about_your_place2=please_tell_us_about_your_place2,name=name,please_tell_us_about_your_place1=please_tell_us_about_your_place1, email=email, user_description=user_description, note_final=note_final, Ph=Ph,service_details=service_details, flat_bulding_name=flat_bulding_name, street_name=street_name,appointment_timing_date=appointment_timing_date, total_price=total_price)
        datafrom.save()
        return redirect('book')
    else:
        product=Post.objects.all()
        context={
            "post_list":product,
        }

    return render(request, 'Builderscleaning.html',context)

def constructioncleaning(request):
    return render(request, 'constructioncleaning.html')


def rubbishremoval(request):
    return render(request, 'rubbishremoval.html')


def carpetcleaning(request):
    return render(request, 'carpetcleaning.html')

def upholsterycleaning(request):
    return render(request, 'upholsterycleaning.html')


def mattresscleaning(request):
    return render(request, 'mattresscleaning.html')

def commercialkitchencleaning(request):
    return render(request, 'commercialkitchencleaning.html')

def commercialkitchencanopycleaning(request):
    return render(request, 'commercialkitchencanopycleaning.html')

def ovencleaning(request):
    return render(request, 'ovencleaning.html')

def endleasecleaning(request):
    return render(request, 'endleasecleaning.html')


def guttercleaning(request):
    return render(request, 'guttercleaning.html')

def highpressurecleaning(request):
    return render(request, 'highpressurecleaning.html')

def strippingsealingfloor(request):
    return render(request, 'strippingsealingfloor.html')

def tilegroutcleaning(request):
    return render(request, 'tilegroutcleaning.html')

def wallcleaning(request):
    return render(request, 'wallcleaning.html')


def windowcleaning(request):
    return render(request, 'windowcleaning.html')    

def highrisewindowscleaning(request):
    return render(request, 'highrisewindowscleaning.html')    

def highhustingcleaning(request):
    return render(request, 'highhustingcleaning.html')    

def ventscleaning(request):
    return render(request, 'ventscleaning.html')    

def factorycleaning(request):
    return render(request, 'factorycleaning.html')    

def warehousecleaning(request):
    return render(request, 'warehousecleaning.html')    

def poolcleaning(request):
    return render(request, 'poolcleaning.html')        

def gardenmowing(request):
    return render(request, 'gardenmowing.html')        

def oneOffcleaning(request):
    return render(request, 'oneOffcleaning.html')        

def regularofficecleaning(request):
    return render(request, 'regularofficecleaning.html')        


