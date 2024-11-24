from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from sacco.models import Customer, Deposit


# Create your views here.
def test(request):
    # save a customer
    # c1= Customer(first_name='Sasha' ,last_name='Mukami',email='sasmu@x.com',dob='2004-06-21',gender='Female',weight='54')
    # c1.save()
    #
    # c2 = Customer(first_name='Mark', last_name='Sloan', email='sloan@x.com', dob='2002-08-12', gender='Male',
    #               weight='64')
    # c2.save()
    customer_count = Customer.objects.count()

    c1=Customer.objects.get(id=1)  #SELECT * FROM customers WHERE id=1
    print(c1)

    d1 = Deposit(amount=2500,status=True,customer=c1)
    d1.save()
    deposit_count = Deposit.objects.count()


    return HttpResponse(f"Ok,done,We have {customer_count} customers and {deposit_count}deposits.")


def customers(request):
    data = Customer.objects.all().order_by('id').values() # ORM SELECT * FROM customers
    paginator = Paginator(data,15)
    page_number = request.GET.get('page',1)
    try:
        paginated_data= paginator.page(page_number)
    except EmptyPage:
        paginated_data= paginator.page(1)
    return render(request, "customers.html",{"data":paginated_data})


def delete_customer(request, customer_id):
    customer=Customer.objects.get(id=customer_id)#select *from customers where id =7
    customer.delete() #delete from customers where id=7
    return redirect("customers")


def customers_details(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    deposits= customer.deposits.all()
    return render(request, "details.html", {"customer": customer,"deposits": deposits})


def delete_customer(request, customer_id):
    customer=Customer.objects.get(id=customer_id)#select *from customers where id =7
    customer.delete() #delete from customers where id=7
    return redirect("customers")


def delete_customers(request):
    return None