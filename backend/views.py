import os
from django.shortcuts import render

from backend.forms import ImageForm


def index(request):
    if request.method == 'POST':

        form = ImageForm(request.POST['inp_name'], request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'index.html', {'form': form})
    else:
        form = ImageForm()
    files = os.listdir('media/images')
    img_obj = []
    for i in files:
        img_obj.append('media/images/' + i)
    return render(request, 'index.html', {'form': form, 'img_obj': img_obj})