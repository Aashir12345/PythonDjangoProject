from django.contrib.auth import authenticate,login,logout
from Ecom.forms import CustomerUserform

def register(request):
    form = CustomerUserform()
    # if request.method == "POST":
    #     form = CustomerUserform(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request,"Successfully Registered")

    context = {'form':form}
    return render(request"Ecom/auth/register.html",context )