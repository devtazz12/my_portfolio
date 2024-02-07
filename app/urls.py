from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

handler404 = views.errorPage
urlpatterns = [
    path('', views.index, name='home'),
    path('contact/submit', views.contactSubmit, name='contact_submit'),
    path('404_error', views.errorPage, name="error_page")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
