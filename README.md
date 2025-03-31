# 🐍 Pystack Week 13 - Monitorando

<div align="center">
<img src="https://github.com/MatheusGrilo/pystack-week-13/raw/main/.gitassets/1.png" alt="Pystack Week 13 gerado por inteligência artificial" width="350" />

<div data-badges>
    <img src="https://img.shields.io/badge/python-3776AB.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/Django-092E20.svg?style=for-the-badge&logo=django&logoColor=white" alt="Django" />
    <img src="https://img.shields.io/badge/Tailwind%20CSS-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind CSS" />
</div>
</div>

**Pystack Week 13 - Monitorando** é um projeto desenvolvido para gerenciar mentorados de forma eficiente e intuitiva. A aplicação oferece funcionalidades como login integrado, gráficos, agendamentos, acesso a vídeos gravados e muito mais.

O projeto é construído com Python e Django, utilizando TailwindCSS para estilização.

## 🖥️ Como rodar o aplicativo 🖥️

### Requisitos:

- Python 3.10+
- Ambiente virtual configurado
- Banco de dados configurado (SQLite ou outro de sua escolha)

### Execução:

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/pystack-week-13.git
    cd pystack-week-13
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    # Linux
    source venv/bin/activate 
    # Windows
    venv\Scripts\activate
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Execute as migrações:
    ```bash
    python manage.py migrate

5. Crie um usuário administrador:
    ```bash
    python manage.py createsuperuser
    ```

6. Inicie o servidor:
    ```bash
    python manage.py runserver
    ```

7. Acesse o aplicativo em [http://localhost:8000](http://localhost:8000).

## 🗒️ Features do projeto 🗒️

- Sistema de login integrado
- Gerenciamento de mentorados
- Agendamento de horários com notificações
- Acesso a vídeos gravados de calls e reuniões
- Gráficos interativos para análise de dados
- Interface estilizada com TailwindCSS

![](https://github.com/MatheusGrilo/pystack-week-13/raw/main/.gitassets/2.png)

## 💎 Links úteis 💎

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [TailwindCSS](https://tailwindcss.com/)