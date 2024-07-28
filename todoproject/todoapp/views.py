from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from todoapp.forms import UserregisterForm,TodoCreateForm,TodoEditForm
from todoapp.forms import UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from todoapp.models import todomodel
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy



# Create your views here.


class Home(TemplateView):
    # def get(self,request):
    #   return render(request,"home.html")    
    template_name="home.html" 





class Userregistrationview(View):
    def get(self,request):
        form= UserregisterForm()
        return render(request,'register.html',{'form':form})
    

    def post(self,request):
        data = UserregisterForm(request.POST)
        if data.is_valid():
            # data.save()
            formdata=data.cleaned_data
            User.objects.create_user(**formdata)
            return HttpResponse("Data Saved")    
        else:
            return HttpResponse("invalid credinals")    
         
        
class UserLoginview(View):
    def get(self,request):
        form= UserLoginForm()
        return render(request,'login.html',{'form':form})
    

    def post(self,request):
        # data = UserregisterForm(request.POST)
        uname=request.POST.get("username")
        psw=request.POST.get("password")
        user=authenticate(request,username=uname,password=psw)
        
        if user:
              login(request,user)
              messages.success(request,'login sucessful')
              return redirect('userhome_view')
        else:
              messages.error(request,'invalid credentials')
              return redirect('home_view')
        



class Logoutview(View):
    def get(self,request):
        logout(request)
        return redirect('home_view')
    


# class TodoCreateview(View):
#      def get(self,request):
#         form=TodoCreateForm()
#         return render(request,'todo_create.html',{'form':form})
#      def post(self,request):
#         data=TodoCreateForm(request.POST)
#         if data.is_valid():
    #             # title=data.cleaned_data.get('title')
#             # content=data.cleaned_data.get('content')
#             # user=request.user
#             # todomodel.objects.create(user=user,title=title,content=content)
#             data.instance.user=request.user
#             data.save()

#             return HttpResponse("created")



class TodoCreateview(CreateView):
    form_class=TodoCreateForm
    template_name='todo_create.html'
    model=todomodel
    success_url=reverse_lazy('create_view')  # another method used to redirect to another page 
    context_object_name="rv"

    def form_valid(self,form):
        form.instance.user=self.request.user   
        messages.success(self.request,"Task Created successfully") 
        return super().form_valid(form)
        


class TodoListView(ListView):
    # def get(self,request):
    #     data=todomodel.objects.filter(user=request.user)
    #     return render(request,'todo_list.html',{'data':data})
    model=todomodel
    template_name='todo_list.html'
    context_object_name='data'


    def  get_queryset(self):
         return todomodel.objects.filter(user=self.request.user)
       
    
      



# class TodoEditView(View):
#     def get(self,request,*args,**kwargs):  
#         id=kwargs.get('id')
#         task=todomodel.objects.get(id=id)
#         form=TodoEditForm(instance=task)
#         return render(request,'todo_edit.html',{'form':form})
    


       
#     def post(self,request,*args,**kwargs):
#         task_id = kwargs.get('id')
#         task = todomodel.objects.get(id=task_id)
#         data = TodoEditForm(request.POST,instance=task)
#         if data.is_valid():
#             data.save()
#             return redirect('list_view')  
        


class TodoEditView(UpdateView):
      model=todomodel
      form_class=TodoEditForm
      template_name='todo_edit.html'
      success_url=reverse_lazy('list_view')
      pk_url_kwarg='id'








# class TodoDeleteView(View):


    #    def get(self,request,*args,**kwargs):  
    #     id=kwargs.get('id')
    #     task=todomodel.objects.get(id=id)
    #     task.delete()
    #     return redirect('list_view')


class TodoDeleteView(DeleteView):
    model=todomodel
    pk_url_kwarg='id'
    success_url=reverse_lazy('list_view')
    template_name='delete.html'
    
    



class UserHomeView(View):
       def get(self,request):
        return render(request,'user_home.html')
       



# class UserProfileView(TemplateView):
#     # def get(self,request):
#     #     data = User.objects.filter(username=request.user)
#     #     return render(request,'profile.html',{'data':data})


#         template_name="todohome.html"



class UserProfileView(View):
    def get(self,request,*args,**kwargs):
        user=User.objects.filter(username=request.user)
        return render(request,'user_profile.html',{'data':user})   