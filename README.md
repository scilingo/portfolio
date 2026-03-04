# 🌿 Portfólio — Carolina Scilingo

Portfólio pessoal de Carolina Scilingo, estudante de Engenharia Biomédica na Faculdade Israelita Albert Einstein. Desenvolvido com Django e gerenciado via painel Admin.

🔗 **Acesse:** [portfolio-r8gu.onrender.com](https://portfolio-r8gu.onrender.com)

---

## 🛠️ Tecnologias Utilizadas

| Camada | Tecnologia |
|---|---|
| Backend | Django 6.0 |
| Banco de dados (local) | SQLite |
| Banco de dados (produção) | PostgreSQL — Neon |
| Storage de imagens | Cloudinary |
| Arquivos estáticos | Whitenoise |
| Servidor WSGI | Gunicorn |
| Deploy | Render |
| Frontend | HTML5, CSS3, JavaScript |
| Tipografia | Google Fonts (Playfair Display + DM Sans) |
| Versionamento | Git + GitHub |

---

## 📁 Estrutura do Projeto

```
portfolio/
├── apps/
│   ├── about/          # Perfil e fotos
│   ├── core/           # View principal (home)
│   ├── education/      # Formação e experiências
│   ├── projects/       # Projetos com slug e tags
│   ├── publications/   # Certificados e publicações
│   └── skills/         # Habilidades por categoria
├── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   └── wsgi.py
├── static/
│   └── images/profile/
├── templates/
│   ├── base.html
│   └── core/home.html
├── manage.py
├── requirements.txt
├── Procfile
└── build.sh
```

---

## 🗄️ Diagrama da Arquitetura de Dados

```
┌─────────────────────────────────────────────────────────┐
│                     REQUISIÇÃO HTTP                      │
└─────────────────────────┬───────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                    config/urls.py                        │
│         /  →  core     /projetos/  →  projects          │
└─────────────────────────┬───────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│                  apps/core/views.py                      │
│                      HomeView                            │
│                                                          │
│  Consulta simultaneamente:                               │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐               │
│  │ Profile  │  │ Project  │  │Certificate│              │
│  └──────────┘  └──────────┘  └──────────┘               │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐               │
│  │Education │  │Experience│  │SkillCat  │               │
│  └──────────┘  └──────────┘  └──────────┘               │
└─────────────────────────┬───────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│              PostgreSQL — Neon (produção)                │
│                  SQLite (desenvolvimento)                 │
└─────────────────────────┬───────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│             templates/core/home.html                     │
│         HTML renderizado → Resposta HTTP                 │
└─────────────────────────────────────────────────────────┘
```

### Modelos e Relacionamentos

```
Profile
  └── photo_hero (ImageField → Cloudinary)
  └── photo_about (ImageField → Cloudinary)

Project
  ├── slug (único)
  ├── image (ImageField → Cloudinary)
  └── tags ──── M2M ──── ProjectTag

Education
  └── logo (ImageField → Cloudinary)

Experience
  └── (sem imagem)

SkillCategory
  └── skills ──── FK ──── Skill

Certificate
  ├── image (ImageField → Cloudinary)
  └── file (FileField → Cloudinary)

Publication
  └── (sem arquivo)
```

---

## ⚙️ Guia de Execução Local

### Pré-requisitos
- Python 3.11+
- Git

### 1. Clonar o repositório
```bash
git clone https://github.com/scilingo/portfolio.git
cd portfolio
```

### 2. Criar e ativar o ambiente virtual
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:
```
SECRET_KEY=sua-chave-secreta-aqui
DATABASE_URL=sqlite:///db.sqlite3
```

### 5. Executar as migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Criar superusuário (Admin)
```bash
python manage.py createsuperuser
```

### 7. Iniciar o servidor
```bash
python manage.py runserver
```

Acesse:
- **Site:** http://127.0.0.1:8000
- **Admin:** http://127.0.0.1:8000/admin

---

## 🚀 Deploy (Render + Neon + Cloudinary)

### Variáveis de ambiente necessárias no Render

| Variável | Descrição |
|---|---|
| `DJANGO_SETTINGS_MODULE` | `config.settings.production` |
| `SECRET_KEY` | Chave secreta Django |
| `DATABASE_URL` | Connection string do Neon |
| `ALLOWED_HOSTS` | `portfolio-r8gu.onrender.com` |
| `CLOUDINARY_CLOUD_NAME` | Cloud name do Cloudinary |
| `CLOUDINARY_API_KEY` | API Key do Cloudinary |
| `CLOUDINARY_API_SECRET` | API Secret do Cloudinary |
| `DJANGO_SUPERUSER_USERNAME` | Usuário admin |
| `DJANGO_SUPERUSER_EMAIL` | Email admin |
| `DJANGO_SUPERUSER_PASSWORD` | Senha admin |

### Comandos de build (build.sh)
```bash
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

---

## 📋 Rotas da Aplicação

| Método | URL | Descrição |
|---|---|---|
| GET | `/` | Página principal |
| GET | `/projetos/` | Lista de projetos |
| GET | `/projetos/<slug>/` | Detalhe do projeto |
| GET/POST | `/admin/` | Painel de administração |

---

## 👩‍💻 Autora

**Carolina Scilingo**
Estudante de Engenharia Biomédica — Faculdade Israelita Albert Einstein

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/carolina-scilingo/)
