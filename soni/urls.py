from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from portfolio.views import homepage, about, projects, contacts, task1, task2, task3, task4, task5, task6, form, task7, final

urlpatterns = [
    path('', homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path('about/', about, name = 'about'),
    path('projects/', projects, name = 'projects'),
    path('contacts/', contacts, name = 'contacts'),
    path('task1/', task1, name = 'task1'),
    path('task2/', task2, name = 'task2'),
    path('task3/', task3, name = 'task3'),
    path('task4/', task4, name = 'task4'),
    path('task5/', task5, name = 'task5'),
    path('task6/', task6, name = 'task6'),
    path('form', form, name = 'form'),
    path('task7', task7, name = 'task7'),
    path('final', final, name = 'final'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
