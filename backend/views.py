import os
from collections import Counter
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from sklearn.cluster import KMeans
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from backend.forms import ImageForm
import cv2
import numpy as np

def get_dominant_color(image, k=4):
    image = image.reshape((image.shape[0] * image.shape[1], 3))
    clt = KMeans(n_clusters=k)
    labels = clt.fit_predict(image)
    label_counts = Counter(labels)
    dominant_color = clt.cluster_centers_[label_counts.most_common(1)[0][0]]
    return list(dominant_color)
    
@csrf_exempt
def view(request):
    if request.method == 'PUTH':
        file_name = request.body.decode().split('/', 3)[3].split('----')[0][:-2]
        img = cv2.imread(file_name)
        hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        dom_color = get_dominant_color(hsv_image)
        result = []
        for i in dom_color:
            result.append(round(i))
        print("Преобладающий цвет:", f'Красный: {result[0]}, Зеленый: {result[1]}, Синий: {result[2]}')
        return HttpResponse(f'Красный: {result[0]}, Зеленый: {result[1]}, Синий: {result[2]}')
    if request.method == 'DELETE':
        file_name = request.body.decode().split('/', 3)[3].split('----')[0][:-2]
        os.remove(file_name)
        return HttpResponse(f'{file_name} deleted')
    if request.method == 'POST':
        try:
            f: InMemoryUploadedFile = request.FILES['file']
            with open(f'media/images/{f.name}', 'wb') as file:
                file.write(f.read())
            os.remove(request.POST['old_file'].split('/', 3)[3])
        except:
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
            img_obj = []
            files = os.listdir('media/images')
            for i in files:
                img_obj.append('media/images/' + i)
            return render(request, 'view.html', {'form': form, 'img_obj': img_obj})
        img_obj = []
        files = os.listdir('media/images')
        for i in files:
            img_obj.append('media/images/' + i)
        return render(request, 'view.html', {'form': None, 'img_obj': img_obj})
    else:
        form = ImageForm()
    files = os.listdir('media/images')
    img_obj = []
    for i in files:
        img_obj.append('media/images/' + i)
    return render(request, 'view.html', {'form': form, 'img_obj': img_obj})

def index(request):
    return render(request, 'index.html')


def addNew(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/')
    form = ImageForm()
    return render(request, 'addNew.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'user/profile.html')
