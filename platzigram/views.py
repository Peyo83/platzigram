from django.http import HttpResponse
from datetime import datetime
import json

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M')
    return HttpResponse(f'Hello World! Now is {now}')

def hi(request):
    import pdb
    # pdb.set_trace()  Sirve para tracear
    return HttpResponse('Hi')

def numbers(request):
    # http://127.0.0.1:8000/numbers/?numbers=3,2,5,3
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sort_numbers = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sort_numbers,
        'message': 'Process successful'
    }
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type='application.json')
    
def say_hi(request, name, age):
    # http://127.0.0.1:8000/hi/Peyo/37
    if age < 12:
        message = f"Sorry {name}, you are not allowed here."
    else:
        message = f'Hello {name}!, welcome to Platzigram.'
    return HttpResponse(message)
