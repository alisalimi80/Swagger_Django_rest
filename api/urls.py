from django.urls import path , include 
from .views import Movies_view , Profile_view ,\
     Detailmovie , FileUploadView, UploadViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'file', UploadViewSet, basename="upload")

urlpatterns = [
    path('fileupload',FileUploadView.as_view(),name="fileupload"), 
    path('movies',Movies_view.as_view()),
    path('profile',Profile_view.as_view(),name="api-profile" ),   
    path('movies/<int:pk>',Detailmovie.as_view()),
    path("upload",include(router.urls),name="upload")
]