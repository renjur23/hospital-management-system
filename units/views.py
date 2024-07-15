from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Department,Doctors,Contact,Pharmacy
from .forms import BookingForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy
from django.urls import reverse
# Create your views here.

def about(request):
    return render(request,'Abouts.html')
def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'Bookings.html',dict_form)

def doctor(request):
    doc_dict={
        'doctor':Doctors.objects.all()
    }
    return render(request,'Doctors.html',doc_dict)
def pharmacy(request):
    pharma_dict={
        'med':Pharmacy.objects.all()
    }
    return render(request,'Pharmacy.html',pharma_dict)

   
class Tasklistview(ListView):
    model=Department
    template_name='Departments.html'
    context_object_name='dept'

class TaskDetailview(DetailView):
    model=Department
    template_name='clsdetail.html'
    context_object_name='dept'

class TaskUpdateview(UpdateView):
    model=Department
    template_name='update.html'
    fields=('department_name','department_description')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
    

class TaskDeleteview(DeleteView):
    model=Department
    template_name='delete.html'
    success_url=reverse_lazy('Home')



def contact(request):
     if request.method == 'GET':
        return render(request,'Contact us.html')
     elif request.method =='POST':
        name1=request.POST['name']
        mail_id=request.POST.get('mail_id',None)
        msg1=request.POST.get('msg',None)
        cont =Contact(name=name1,mail_id=mail_id,msg=msg1)
        cont.save()
        return HttpResponse('<h1>We Will Contact you soon</h1>')

def login(request):
    if request.method == 'GET':
        if 'logged_in' in request.COOKIES and 'username' in request.COOKIES:
            context = {
                'username': request.COOKIES['username'],
                'login_status': request.COOKIES.get('logged_in'),
            }
            return render(request, 'Home.html', context)
        else:
            return render(request, 'login.html')
    
    if request.method == "POST":
        username = request.POST.get('email')
        context = {
            'username': username,
            'login_status': 'TRUE',
        }
        response = render(request, 'Home.html', context)

        response.set_cookie('username', username)
        response.set_cookie('logged_in', True)
        return response

def home(request):
    if 'logged_in' in request.COOKIES and 'username' in request.COOKIES:
        context = {
            'username': request.COOKIES['username'],
            'login_status': request.COOKIES.get('logged_in'),
        }
        return render(request, 'Home.html', context)
    else:
        return render(request,'login.html')

def logout(request):
    response = HttpResponseRedirect(reverse('login'))
    response.delete_cookie('username')
    response.delete_cookie('logged_in')
    return response

