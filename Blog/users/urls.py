from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth.views import (
    
      PasswordResetView,
      PasswordResetDoneView,
      PasswordResetConfirmView,
      PasswordResetCompleteView,
      PasswordChangeView,
      PasswordChangeDoneView

)
from django.urls import reverse_lazy


urlpatterns = [

   path('',views.form),
   path('form/',views.form,name='form'),
   path('signup/',views.signup_view),
   path('login/',views.login_view),
   path('logout/',views.logout_view),
#    path('profile/<username>/',views.profile),
   path('profile/',views.profile),

   path('editProfile/',views.edit_profile),
   path('passwordReset/',PasswordResetView.as_view(
       template_name = 'users/passwordReset.html',
       email_template_name = 'users/passwordResetEmail.html',
       subject_template_name = 'users/passwordResetSubject.txt',
       success_url = reverse_lazy('users:passwordResetDone'),
       from_email = 'varshithkuravti@gmail.com'
   ),name='passwordReset'),

   path('passwordReset/done/',PasswordResetDoneView.as_view(
       template_name = 'users/passwordResetDone.html'),name='passwordResetDone'),

   
   path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(
       template_name = 'users/passwordResetConfirm.html',
       success_url = reverse_lazy('users:passwordResetComplete')
   ),name='passwordResetConfirm'),
   
   
   path('reset/done/',PasswordResetCompleteView.as_view(
       template_name = 'users/passwordResetComplete.html'
   ),name='passwordResetComplete'),

   path('passwordChange/',PasswordChangeView.as_view(
       template_name = 'users/passwordChange.html',
       success_url = reverse_lazy('users:passwordChangeDone')
   ),name='passwordChange'),

   path('passwordChange/done/',PasswordChangeDoneView.as_view(
       template_name = 'users/passwordChangeDone.html'
   ),name = 'passwordChangeDone')
   


   
   
   
   ]
