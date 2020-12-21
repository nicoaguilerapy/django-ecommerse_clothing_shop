from django.shortcuts import render, redirect
from .models import Profile
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    template_name = 'accounts/profile_form.html'
    form_class = ProfileForm
    success_url = reverse_lazy('my_profile')
    
    def get_object(self):
        profile, status = Profile.objects.get_or_create(user = self.request.user)
        return profile
