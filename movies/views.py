from django.shortcuts import render
import requests
import json

API_URL = 'https://ghibliapi.herokuapp.com/'


def movies_list(request):
    try:
        response = requests.get(API_URL + 'films')
        # print(response.json())
        films = response.json()
        return render(request,
                      'movies/movies_list.html',
                      {'films': films})
    except Exception as error:
        print(error)
        return "Failed to retrieve data, please try again."
