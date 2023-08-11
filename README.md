# Projeto django Agenda de Contatos

## Descrição do Projeto

Projeto de uma agenda de contatos desenvolvido em Django.

## Comandos

### Criar ambiente virtual

```bash
poetry init
```

### Instalar Django

```bash
poetry add django
```

### Criar projeto Django

```bash
poetry run django-admin startproject core
```

### Criar app

```bash
poetry run python manage.py startapp contacts
```

### Criar migrações

```bash
poetry run python manage.py makemigrations
```

### Executar migrações

```bash
poetry run python manage.py migrate
```

### Criar super usuário

```bash
poetry run python manage.py createsuperuser
```

### Executar servidor

```bash
poetry run python manage.py runserver
```

### Criar arquivo requirements.txt

```bash
poetry export -f requirements.txt -o requirements.txt
```

### Instalar dependências

```bash
poetry install
```

### Criar arquivo .env

```bash
python contrib/env_gen.py
```

## Referências

- [Django](https://www.djangoproject.com/)

## Autor

- [Walber Vaz]("https://linkedin.com/in/walber-vaz")

## Licença

[MIT](LICENSE)
