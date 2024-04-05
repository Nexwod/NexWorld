from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('all_listing/', views.all_listing),
    path('about/', views.about),
    path('estate_registration/', views.estate_registration),
    path('success/', views.success),
    path('dashboard/', views.dashboard),
    path('find_realtors/', views.find_realtors),
    path('find_branch/', views.find_branch),
    path('thank_you/', views.thank_you),
    path('searched_estate', views.searched_estate),
    path('register_realtor/', views.register_realtor),
    path('land_details/<int:id>', views.land_details, name='land_details'),
    path('branch_detail/<int:id>', views.branch_detail, name='branch_details'),
    path('checkout/<int:id>', views.checkout),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)