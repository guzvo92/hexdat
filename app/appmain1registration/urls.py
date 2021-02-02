
#urls.py [appmain1registration]
#path ('accounts/', include ('app.appmain1registration.urls')),

from django.urls import path
from . import views
from .views import SignUpView, ProfileUpdate

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('profile/', ProfileUpdate.as_view(), name="profile"),

]

