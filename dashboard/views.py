from django.shortcuts import render

# Create your views here.
def account_list(request):
    return render(request, 'dashboard/account_list.html', {})