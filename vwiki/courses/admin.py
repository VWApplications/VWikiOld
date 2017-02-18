from django.contrib import admin
from .models import Category, Course, Topic, Subtopic, Lesson


class LessonAdmin(admin.ModelAdmin):
  list_display = ['title', 'subtopic', 'created_at', 'updated_at']
  search_fields = ['title', 'subtopic']
  prepopulated_fields = {'slug': ('title',)}


class SubtopicAdmin(admin.ModelAdmin):
  list_display = ['title', 'topic', 'created_at', 'updated_at']
  search_fields = ['title', 'topic']


class TopicAdmin(admin.ModelAdmin):
  list_display = ['title', 'course', 'created_at', 'updated_at']
  search_fields = ['title', 'course']
  list_filter = ['course', 'updated_at']


class CourseAdmin(admin.ModelAdmin):
  list_display = ['title', 'category', 'created_at', 'updated_at']
  search_fields = ['title', 'category']
  list_filter = ['category', 'updated_at']
  prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
  list_display = ['title', 'created_at', 'updated_at']
  search_fields = ['title']
  list_filter = ['created_at', 'updated_at']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Subtopic, SubtopicAdmin)
admin.site.register(Lesson, LessonAdmin)
