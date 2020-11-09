from sapt.models import *
from django.urls import path
from sapt.views import *
urlpatterns = [
        path('getall1/', getserial1.as_view()),
        path('getall2/', getview.as_view()),
        path('up1/', updateview.as_view()),
        path('postview/', postview.as_view()),
        path('postdata/', postser.as_view()),
        path('serch/', serchdata.as_view()),
        path('del/<int:pk>', deletedata.as_view()),
        path('vv/', vv),
]
