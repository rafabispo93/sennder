from django.shortcuts import render
import requests

API_URL = 'https://ghibliapi.herokuapp.com/'


def movies_list(request):
    try:
        is_cached = ('films' in request.session)
        if not is_cached:
            response = requests.get(API_URL + 'films')
            request.session['films'] = response.json()
        films = request.session['films']
        return render(request,
                      'movies/movies_list.html',
                      {'films': films})
    except Exception as error:
        print(error)
        return "Failed to retrieve data, please try again."
