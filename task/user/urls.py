from .views import GetAppsView, UploadScreenshotView, ProfileView
from django.urls import path

# URLs
urlpatterns = [
    path('user/apps/', GetAppsView.as_view(), name='get_apps'),
    path('user/upload_screenshot/', UploadScreenshotView.as_view(), name='upload_screenshot'),
    path('user/profile/', ProfileView.as_view(), name='profile'),
]