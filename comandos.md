
- Criar ambiente virtual

```bash
python -m venv venv
```

- Ativar ambiente virtual do python

```bash
source venv/Scripts/Activate
```

- Executar servidor

```bash
python manage.py runserver
```

- Instalar blibliotecas

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


- Criar um novo app

```bash
  python manage.py startapp perfil
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
- Agora crie a estrutura de pastas do template do app na raíz:

```bash
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
```
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

- Crie a rota da view gerenciar em perfil/urls.py

```bash
path('gerenciar/', views.gerenciar, name="gerenciar"),
```

- Em tmplates crie o arquivo gerenciar.html, e cole o conteúdo do notion no arquivo gerenciar.html
- Agora crie o arquivo de modelo do banco de dados em perfil/models, cole o conteúdo do notion, para criar as tabelas no banco de dados já padrão do django, use o comando migrate:
 

- Para fazer a migração da model pro banco use o comando para criar o arquivo de migraçao:


```bash
python manage.py makemigrations

```
- Em sequida rode o comando para efetivar a migração da model.

```bash
python manage.py migrate

```
- Agora em perfil/admin importe a model, para podermos edita-la via painel do admin.
```bash
from .models import Conta, Categoria
# Register your models here.
admin.site.register(Conta)
admin.site.register(Categoria)
```

- Agora cria suas credenciais para login no painel admin.

```bash

python manage.py createsuperuser
```
user: projeto
password: projeto

- Se necessário alterar usuário do admin, execute o seguinte comando para acessar o shell interativo do Django:

```bash
python manage.py shell
```
- No shell interativo do Django, importe o modelo de usuário do Django:

```bash
from django.contrib.auth.models import User
```
- Use o método get() do modelo de usuário para obter o superusuário existente:

```bash
superuser = User.objects.get(username='admin')
```
Certifique-se de substituir 'admin' pelo nome de usuário correto do superusuário.

- Agora você pode alterar as informações do superusuário conforme necessário. Por exemplo, para alterar a senha, você pode usar o método set_password():
```bash
superuser.set_password('nova_senha')
```
SSubstitua 'nova_senha' pela nova senha desejada.

- Salve as alterações no superusuário:

```bash
superuser.save()
```
- Saia do shell interativo do Django:
```bash
exi()
```
- Caso queira alterar somente um novo usuário:
```bash
python manage.py createsuperuser
```
O comando irá solicitar algumas informações para configurar o superusuário. Você será solicitado a fornecer um nome de usuário, endereço de e-mail (opcional) e senha. Digite as informações solicitadas e pressione Enter.

-  Crie uma nova url em perfil/urls.py para poder fazer o input no banco:

```bash
path('cadastrar_banco/', views.cadastrar_banco, name="cadastrar_banco"),
```
- Crie a nova função em perfil/views.py view cadastrar_banco
- Pegar os inputs do frontend e gravar no banco, pra isso vá em templates/gerenciar.html, na linha 41 modifique o action:

```bash
                                                       //enctype="",Permite enviar arquivo via form
<form action="{% url 'cadastrar_banco' %}" method="POST" enctype='multipart/form-data'>{% csrf_token %}

```
- Importar a model em perfil/views.py, e importar o redirect:

```bash
// Adiciona o redirect junto com render
from django.shortcuts import render, redirect
from .models import Conta

```
- Em templates/gerenciar.html na linha 60 adicione o required no input para tornar o campo obrigatório

```bash
<input type="file" placeholder="Ícone" name="icone" required>

```

- Exibir mensagens de erros na perfil/views.py:
```bash
    # Mensagem de erro
    if len(apelido.strip()) == 0 or len(valor.strip()) == 0:
        return redirect('/perfil/gerenciar/')
```
- Exibir o alert de msg de erro usando o bootstrap, em core/settings.py

```bash
#Messages
from django.contrib.messages import constants

MESSAGE_TAGS = {
    constants.DEBUG: 'alert-primary',
    constants.ERROR: 'alert-danger',
    constants.WARNING: 'alert-warning',
    constants.SUCCESS: 'alert-success',
    constants.INFO: 'alert-info ',
}
```

- Em perfil/view.py fazer o import:
```bash
from django.contrib import messages
from django.contrib.messages import constants
```
- Na própria view atualiza a função cadastrar_banco para exibir as mensagens:

```bash
def cadastrar_banco(request):
    apelido = request.POST.get('apelido')
    banco = request.POST.get('banco')
    tipo = request.POST.get('tipo')
    valor = request.POST.get('valor')
    icone = request.FILES.get('icone')
    # Mensagem de erro
    if len(apelido.strip()) == 0 or len(valor.strip()) == 0:
        messages.add_messages(request, constants.ERROR, 'Preencha todos os campos !!!')//Adicione esta linha
        return redirect('/perfil/gerenciar/')
    
    conta = Conta(
        apelido = apelido,
        banco=banco,
        tipo=tipo,
        valor=valor,
        icone=icone
    )

    conta.save()
    messages.add_messages(request, constants.SUCCESS, 'Conta cadastrada com sucesso !!!')//Adicione esta linha
    return redirect('/perfil/gerenciar/')

```
- Em templates/gerenciar.htlm, exiba as mensagens no html na linha:

```bash
{% if messages %}
    {% for message in messages %}
        <div class="alert {{ message.tags }}">{{ message }}</div>
    {% endfor %}
{% endif %}

```
- Busque todas as contas cadastradas e envie para o HTML, em perfil/views.py na função gerenciar, modifiquea:
  
```bash
def gerenciar(request):
    contas = Conta.objects.all()
    return render(request, 'gerenciar.html', {'contas': contas,})

```
- Agora exiba as contas na linha 16 em templates/gerenciar.html


- Adicione uma URL para os arquivos de media atualis o core/urls.py atualize-o:

```bash
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('perfil/', include('perfil.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```
- Agora liste as contas a partir da linha 19 modifique o gerenciar.html:

```bash

{% for conta in contas %}
    <div class="lista-contas-main">
        <span><img width="10%" src="{{conta.icone.url}}">&nbsp&nbsp{{conta}}</span>

        <span class="total-conta positivo ">R$ {{conta.valor}}</span>
    </div>
    <br>
{% endfor %}
```
- Em perfil/vies.py, atualiza a função gerenciar.

```bash
def gerenciar(request):
    contas = Conta.objects.all()
    #total_contas = contas.aggregate(Sum('valor'))
    total_contas = 0

    for conta in contas:
        total_contas += conta.valor
    return render(request, 'gerenciar.html', {'contas': contas, 'total_contas': total_contas})

```
