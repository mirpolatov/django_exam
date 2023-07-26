from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from apps.forms import RegisterForm, CustomLoginForm, UpdateForm
from apps.models import Register


# Create your views here.


#
def main(request):
    regis = Register.objects.all()
    return render(request, 'new_customer_list.html', {'regis': regis})


#
#
def register(request):
    if request.POST:
        data = RegisterForm(request.POST)
        if data.is_valid():
            data.save()
        return redirect(reverse('login'))
    return render(request, 'register.html')


def userfunc(request, pk):
    user = Register.objects.filter(pk=pk).first()
    if request.user.id != user.id:
        return redirect('main')
    else:
        if request.POST:
            form = UpdateForm(request.POST, files=request.FILES, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('main')
    return render(request, 'update.html', {'user': user})


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'index.html'
    next_page = reverse_lazy('main')

    def form_invalid(self, form):
        return HttpResponse('Xato')



def deletefunc(request, pk):
    user = Register.objects.filter(pk=pk).first()
    if request.user.id != user.id:
        return redirect('main')
    else:
        Register.objects.filter(id=pk).delete()
        return redirect('main')


def users_list(request):
    if request.GET:
        key = request.GET.get('q')
        regis = Register.objects.filter(Q(first_name__contains=key)| Q(last_name__contains=key))
    else:
        regis = Register.objects.all()
    return render(request, 'new_customer_list.html', {'regis': regis})