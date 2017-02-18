from django.shortcuts import render, get_object_or_404
from .models import Course


def course(request, course_slug):
  template = 'courses/course.html'
  course = get_object_or_404(Course, slug=course_slug)
  context = {'course': course}
  return render(request, template, context)


