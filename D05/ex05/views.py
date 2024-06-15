from django.shortcuts import render
from .models import Movies
from django.http import HttpResponse
from .forms import Delmovie
# Create your views here.

def set_to_dict(p):
    dictionaries = []
    for elem in p :
        dictionary = {}
        spl = elem.split(' - ')
        for dic_elem in spl :
            dic_splited = dic_elem.split(':')
            dictionary[dic_splited[0].strip()] = dic_splited[1].strip()
        dictionaries.append(dictionary)
    return dictionaries
    
def Populate(request):
    raw_data = [
        'episode_nb: 1 - title: The Phantom Menace - director: George Lucas - producer: Rick McCallum - release_date: 1999-05-19',
        'episode_nb: 2 - title: Attack of the Clones - director: George Lucas - producer: Rick McCallum - release_date: 2002-05-16',
        'episode_nb: 3 - title: Revenge of the Sith - director: George Lucas - producer: Rick McCallum - release_date: 2005-05-19',
        'episode_nb: 4 - title: A New Hope - director: George Lucas - producer: Gary Kurtz, Rick McCallum - release_date: 1977-05-25',
        'episode_nb: 5 - title: The Empire Strikes Back - director: Irvin Kershner - producer: Gary Kurtz, Rick McCallum - release_date: 1980-05-17',
        'episode_nb: 6 - title: Return of the Jedi - director: Richard Marquand - producer: Howard G. Kazanjian, George Lucas, Rick McCallum - release_date: 1983-05-25',
        'episode_nb: 7 - title: The Force Awakens - director: J. J. Abrams - producer: Kathleen Kennedy, J. J. Abrams, Bryan Burk - release_date: 2015-12-11',
    ]
    dictionaries = set_to_dict(raw_data)
    results = ''
    for data in dictionaries:
        try:
            Movies.objects.create(**data)
            results += "OK\n"
        except Exception as e:
            results+= (f"{e}\n")
    return HttpResponse({'results': results})
    

def Display(request):
    movies = Movies.objects.all()
    if not movies :
        return HttpResponse('No data available')
    return render(request, 'ex05/display.html', {'movies': movies})
    pass

def Remove(request):
    if request.method == 'POST':
        form = Delmovie(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            m = Movies.objects.filter(title=title)
            if m :
                m.delete()
                return HttpResponse(f'Movie {title} deleted')
            return HttpResponse('Movies doesnt Exist')
    else:
        form = Delmovie()
        return render(request, 'ex05/remove.html', {'form': form})
        
        