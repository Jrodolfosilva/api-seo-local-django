# 🌎 API de Localidades do Brasil – SEO Local com Django

Este projeto é uma API RESTful desenvolvida com **Django** e **Django REST Framework**, que fornece dados estruturados sobre **estados**, **cidades** e **bairros** do Brasil. A proposta é acelerar e automatizar estratégias de **SEO local** em larga escala, facilitando desde a **geração de páginas dinâmicas** até a **criação de sitemaps geográficos**.

---

## 🧠 Sobre o projeto

A API foi criada com o propósito de auxiliar desenvolvedores e especialistas em SEO a:

- Gerar conteúdos geolocalizados automaticamente;
- Criar sitemaps dinâmicos baseados em hierarquia (estado → cidade → bairro);
- Reutilizar dados organizados para alimentar aplicações front-end;
- Escalar o SEO local de forma eficiente e técnica.

> 💡 Projeto desenvolvido enquanto aprendo Django na prática.

---

## ⚙️ Tecnologias utilizadas

- Python 3.11+
- Django 4.x
- Django REST Framework
- SQLite (em desenvolvimento)
- DRF Serializers e Class-based Views

---

## 🚀 Endpoints (em construção)

### 🔹 Estados

| Método | Rota              | Descrição                            |
|--------|-------------------|--------------------------------------|
| GET    | `/api/estados/`   | Lista todos os estados               |
| GET    | `/api/estado/`    | Detalha um estado via `slug`         |
| POST   | `/api/estado/`    | Cria um novo estado com dados SEO    |

# 1. Clone o projeto
git clone https://github.com/seu-usuario/api-seo-local.git
cd api-seo-local

# 2. Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Aplique as migrações
python manage.py migrate

# 5. Rode o servidor
python manage.py runserver


Rodolfo Silva
Desenvolvedor Front-end | Estudando Django & Back-end
🔗 https://www.linkedin.com/in/rodolfo-silva-14573b117
📧 contato: rodolfo.silva1602@gmail.com

📃 Licença
Este projeto está licenciado sob a licença MIT.
Sinta-se livre para usar, estudar e contribuir!



