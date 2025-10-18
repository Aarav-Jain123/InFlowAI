from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='Index'),
    path('sign-up/', signup, name='sign_up'),
    path('otp/', otp, name='otp'),
    path('log-out/', logout_page, name='log-out'),
    path('project-create-form/', todo_ai_form, name='Project creation form'),
    # path('save-project/', save_project, name='Save project'),
    path('project_link/<slug:slug>/', project_page, name='Project page'),
]
