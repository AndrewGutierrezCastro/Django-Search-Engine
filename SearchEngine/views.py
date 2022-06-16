from django.shortcuts import render, redirect
from SearchEngine.search import google, oursearchengine


def homepage(request):
    return render(request,'home.html')


def results(request):
    if request.method == "POST":
        result = request.POST.get('search')
        google_link,google_text = google(result)
        google_data = zip(google_link,google_text)
        our_links, our_text = oursearchengine(result)
        our_data = zip(our_links, our_text)
        if result == '':
            return redirect('Home')
        else:
            return render(request,'results.html',{'google': google_data, 'oursearchengine': our_data})