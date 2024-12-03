from django.urls import path
from . import views

# URL patterns
urlpatterns = [
    path('health-check/', views.health_check, name='health_check'),
    path('sign/', views.sign_documents, name='sign_documents'),
    path('signature-status/', views.get_signature_status, name='get_signature_status'),
    path('download-signed-document/', views.download_signed_document, name='download_signed_document'),
]