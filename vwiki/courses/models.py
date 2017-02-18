from django.db import models


class Category(models.Model):
  title = models.CharField('Título', max_length=100)
  icon = models.CharField('Icone', max_length=100, help_text='Icones do Font Awesome', default='fa fa-folder-open')
  created_at = models.DateTimeField('Criado em', auto_now_add=True)
  updated_at = models.DateTimeField('Modificado em', auto_now=True)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = 'Categoria'
    verbose_name_plural = 'Categorias'
    ordering = ['title']


class Course(models.Model):
  title = models.CharField('Título', max_length=100)
  slug = models.SlugField('Identificador', max_length=100)
  category = models.ForeignKey(Category, verbose_name="Categoria", related_name="courses")
  created_at = models.DateTimeField('Criado em', auto_now_add=True)
  updated_at = models.DateTimeField('Modificado em', auto_now=True)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = 'Curso'
    verbose_name_plural = 'Cursos'
    ordering = ['title']


class Topic(models.Model):
  title = models.CharField('Título', max_length=100)
  course = models.ForeignKey(Course, verbose_name="Curso", related_name="topics")
  created_at = models.DateTimeField('Criado em', auto_now_add=True)
  updated_at = models.DateTimeField('Modificado em', auto_now=True)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = 'Tópico'
    verbose_name_plural = 'Tópicos'
    ordering = ['title']


class Subtopic(models.Model):
  title = models.CharField('Título', max_length=100)
  topic = models.ForeignKey(Topic, verbose_name="Tópico", related_name="subtopics")
  created_at = models.DateTimeField('Criado em', auto_now_add=True)
  updated_at = models.DateTimeField('Modificado em', auto_now=True)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = 'Subtopico'
    verbose_name_plural = 'Subtopicos'
    ordering = ['title']


class Lesson(models.Model):
  title = models.CharField('Título', max_length=100)
  slug = models.SlugField('Identificador', max_length=100)
  content = models.TextField('Conteúdo', max_length=100)
  subtopic = models.ForeignKey(Subtopic, verbose_name="Subtopico", related_name="lessons")
  created_at = models.DateTimeField('Criado em', auto_now_add=True)
  updated_at = models.DateTimeField('Modificado em', auto_now=True)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = 'Aula'
    verbose_name_plural = 'Aulas'
    ordering = ['title']
