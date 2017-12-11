from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def index(request):
    if request.method == 'GET':
        return render(request, 'photo/index.html')
    elif request.method == 'POST':
        uploaded = []
        fs = FileSystemStorage()
        myfiles = request.FILES.getlist('myfile')
        for myfile in myfiles:
            uploaded.append(fs.save(myfile.name, myfile))
    return render(request, 'photo/index.html', {'uploaded': uploaded})
