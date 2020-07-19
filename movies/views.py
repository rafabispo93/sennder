from django.shortcuts import render
import requests

API_URL = 'https://ghibliapi.herokuapp.com/'


def movies_list(request):
    try:
        is_cached = ('films' in request.session)
        if not is_cached:
            request.session['films'] = _get_films_ordered_by_most_recent()
        films = request.session['films']
        return render(request,
                      'movies/movies_list.html',
                      {'films': films})
    except Exception as error:
        return error


def _get_films_ordered_by_most_recent() -> list:
    # Get the films and order by the most recent
    try:
        filter_data = {
            'limit': 250,
            'fields': 'id,title,description,director,producer,release_date,rt_score'
        }
        return sorted(_get_people_in_films(
            requests.get(API_URL + 'films', filter_data).json()), key=lambda k: k['release_date'], reverse=True) 
    except Exception as error:
        return error


def _get_people_in_films(films) -> list:
    # Returns all films with its respectively people
    try:
        filter_data = {
            'limit': 250,
            'fields': 'id,name,films'
        }
        people = requests.get(API_URL + 'people', filter_data).json()
        people_film = []
        for person in people:
            for f in person['films']:
                people_film.append({
                    'id': f.split('films/')[1],
                    'name': person['name']
                })
        for film in films:
            film['people'] = []
            for p in people_film:
                if p['id'] == film['id']:
                    if p['name'] not in film['people']:
                        film['people'].append(p['name'])
            film['people'] = ', '.join(film['people'])
        return films
    except Exception as error:
        return error
