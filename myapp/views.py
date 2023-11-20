from django.shortcuts import render
from faker import Faker
from faker.providers import address


# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')



def fake_data(request, data=False):
    fake = Faker()
    # fake.add_provider(address)
    # Create list of dictionary objects
    data = [{'name':fake.name(), 'email':fake.city(), 'phone':fake.phone_number(), 'dob':fake.date_of_birth()} for e in range(20)]    
    return render(request, 'myapp/index.html', {'data':data})