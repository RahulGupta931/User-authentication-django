from django.urls import path
from .views import *

urlpatterns = [
    path('', view=dashboard_view),

    path('signup/', view=signup_view),
    path('login/', view=login_view),
    path('logout/', view=logout_view)
    

]
