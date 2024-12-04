from django.contrib import admin
from django.urls import path
from webhooks.views import WebhookView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/webhooks/oder/', WebhookView.as_view() , name='webhooks_order'),
]
