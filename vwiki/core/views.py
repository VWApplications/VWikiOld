from django.shortcuts import render
from django.views.generic import View
from vwiki.courses.models import Category


class HomeView(View):
  template = 'core/home.html'

  def get(self, request):
    categories = Category.objects.all()
    context = {
      'categories': categories,
    }
    return render(request, self.template, context)


