from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', {'message': ''})

import pickle
def generating_prediction(value):
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    prediction = model.predict([[value]])
    message = f'Prediction made is: {prediction[-1][-1]}'
    return message

#model = loading_pickle_model()
def generate_model_val(requests):
    if requests.method == "POST":
        data = requests.POST
        print(data)
        val = float(data.get('YearsExperience'))
        #val = int(val)
        message = generating_prediction(val)
    return render(requests, 'index.html', {'message': message})