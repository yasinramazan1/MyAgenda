# Projede ilk olarak url'ler ayarlanmalıdır.
from django.urls import path # Django ile alakalı Pylance(reportMissingModuleSource) hatası alındığında Pylance kütüphanesi, Extensions bölümünden disable yapılmalıdır.
from . import views 
urlpatterns = [
    path('',views.homepage,name="home"),
    path('developer/',views.developer,name="developer"),
    path('about/',views.about,name="about"),
    path('create/',views.create,name="create"),
    path('delete/<Todos_id>',views.delete,name="delete"),
    path('yes_finish/<Todos_id>',views.yes_finish,name="yes_finish"),
    path('no_finish/<Todos_id>',views.no_finish,name="no_finish"),
    path('update/<Todos_id>',views.update,name="update"),
    
    # """
    # # path('', views.home), 
    # Bu sayfa, template olmadan request yapıldığında karşılaşılan sayfadır.
    # """
    
    
]