
```bash
pip install django && pip install pillow
```
- Criar projeto Django
```bash
django-admin startproject core .
```
- Setar as configs em settings.py
```bash
LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'
```
- Em core urls, setar a rota das views
  ```bash
  from django.urls import path, include

  path('perfil/', include('perfil.urls')),
```

- Executar servidor
```bash
python manage.py runserver
```
- Criar um novo app
  ```bash
  python3 manage.py startapp perfil
```
- Em core/settings setar o novo app
```bash
  INSTALLED_APPS = [
    'perfil'
]
```
- No novo app perfil criar as rotas, crie um novo arquivo urls.py:
  ```bash
  from django.urls import path
  from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('gerenciar/', views.gerenciar, name="gerenciar"),
]
```
- No perfil/views criar a função que chama a view:
```bash
  def home(request):
    return render(request, 'home.html')
```
- setar os diretórios dos templates no core em settings.py:
  ```bash
  import os
  // em setar o derecionamento dos templates
  TEMPLATES = [
    {
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
            ],
        },
    },
]
```
- Agora crie a estrutura de pastas do template do app na raíz

templates - bases -> base.html(arquivo base do cabeçalho padrão html)
          - static
            |_geral
              - css
              - img
              - js
            |_perfil(pasta do app)
              - css(css da home)
              - img(imagens da home)
              - js
          - home.html

- em bases.html crie o cabeçalho pasrão html que será carregado em todas as páginas html
agora extenda a base pra página home:
```bash

<h1>inicio da base</h1>
{% block 'body'%}

{% endblock %}
<h1>Fim da base</h1>
// extender o arquivo na home.html
{% extends "bases/base.html" %}
{% block 'body'%}
<h1> Eu sou a home</h1>
{% endblock %}

```

- Configurar os arquivos estáticos, em core/settings.py
```bash
import os 

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'templates/static'),)
STATIC_ROOT = os.path.join('static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

```

- utilizar os arquivos de css estáticos, no arquivo base.html
```bash
<link href="{% static 'geral/css/base.css' %}" rel="stylesheet">
// na linha 1 do arquivo carregar os arquivos
{% load static %}
```
- No arquivo da home carregar o css do head
```bash
{% load static %}
{% block 'head' %}
    <link href="{% static 'perfil/css/home.css' %}" rel="stylesheet">
{% endblock %}
```
