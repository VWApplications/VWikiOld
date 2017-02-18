from django.shortcuts import render
from django.views.generic import View


class HomeView(View):
  template = 'core/home.html'

  def get(self, request):
    return render(request, self.template)

