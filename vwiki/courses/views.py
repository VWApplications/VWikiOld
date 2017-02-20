from django.shortcuts import render, get_object_or_404
from .models import Course
from .forms import TopicForm


def course(request, course_slug):
  template = 'courses/course.html'
  course = get_object_or_404(Course, slug=course_slug)
  context = {'course': course}
  return render(request, template, context)


def create_topic(request, course_slug):
  template = 'courses/topic_create.html'
  course = get_object_or_404(Course, slug=course_slug)
  topic = Topic(course=course)
  form = TopicForm(request.POST or None, instance=topic)
  if form.is_valid():
    form.save()
    redirect('courses:course', kwargs=(course.id,))
  context = {'form': form}
  return render(request, template, context)
