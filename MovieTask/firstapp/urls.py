from . import views
from django.urls import path
app_name='firstapp'


urlpatterns = [
    path('',views.start,name='start'),
    path('register/',views.register,name='register'),
    # path('/',views.base,name='base'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('add/',views.add,name='add'),
    path('movie/<int:movie_id>/',views.details,name='details'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),

]