# InFlowAI 🧠

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.0+-green.svg)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)](https://getbootstrap.com/)

## Description 📝

InFlowAI is an AI-powered todo list application built with Django. It helps users break down large projects into smaller, manageable tasks with the help of AI. Users can create projects, define prompts, and leverage the AI to generate task breakdowns. It provides user authentication, project management and leverages the Groq AI service.

## Table of Contents 📑

1.  [Features](#features-%EF%B8%8F)
2.  [Tech Stack](#tech-stack-computer)
3.  [Installation](#installation-gear)
4.  [Usage](#usage-rocket)
5.  [Project Structure](#project-structure-file_folder)
6.  [Contributing](#contributing-handshake)
7.  [License](#license-⚖️)
8.  [Important Links](#important-links-link)
9.  [Footer](#footer-page_facing_up)

## Features ✨

*   **AI-Powered Task Breakdown:** Utilizes Groq AI to break down projects into smaller tasks.
*   **User Authentication:** Secure signup, login, and logout functionality. 🔑
*   **Project Management:** Create, view, and delete projects. 🗂️
*   **Interactive Project Dashboard:** Display project details and AI-generated prompts. 📊
*   **Email OTP Verification:** Secure user registration using OTP verification. 📧
*   **Responsive Design:** Uses Bootstrap for a consistent user experience across devices.📱

## Tech Stack 💻

*   **Backend:** Python, Django 🐍
*   **Frontend:** HTML, Bootstrap, JavaScript 🌐
*   **AI:** Groq AI 🤖
*   **Database:** SQLite (default) 💽

## Installation ⚙️

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Aarav-Jain123/InFlowAI.git
    cd InFlowAI
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    The `requirements.txt` file includes the following dependencies:

    ```text
    langchain_core
    python-dotenv
    langchain_community
    groq
    langchain-groq
    langserve
    sentence_transformers
    django
    django-cors-headers
    djangorestframework
    crispy-bootstrap5
    django-autoslug
    ```

4.  **Set up environment variables:**

    *   Create a `.env` file in the project root.

    *   Add your Groq API key and email host password to the `.env` file:

        ```
        GROQ_API_KEY=YOUR_GROQ_API_KEY
        EMAIL_HOST_PASSWORD=YOUR_EMAIL_HOST_PASSWORD
        ```

        Replace `YOUR_GROQ_API_KEY` and `YOUR_EMAIL_HOST_PASSWORD` with your actual API key and email password. Get groq api key from https://console.groq.com/ and create an account if you don't have one. 

        Configure the email settings in `todoAiProject/settings.py`.

        ```python
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAIL_HOST = 'smtp.gmail.com'
        EMAIL_USE_TLS = True
        EMAIL_PORT = 587
        EMAIL_HOST_USER = 'jainaarav552@gmail.com'
        EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
        ```

5.  **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage 🚀

1.  **Sign up:**

    *   Navigate to the signup page (`/sign-up/`) and create a new account.
    *   Enter your username, first name, last name, email, and password.
    *   You will receive an OTP (One-Time Password) via email to verify your account.

2.  **Login:**

    *   Navigate to the login page (`/login/`) and enter your credentials.
    *   You can reset your password if you have forgotten it by navigating to the password reset page.

3.  **Create a new project:**

    *   After logging in, you will be redirected to the home page (`/`).
    *   Click on "Create new company" under the Actions dropdown to navigate to the project creation form (`/project-create-form/`).
    *   Enter the project name and a prompt describing the project.
    *   Click "Send to AI" to generate a task breakdown using the Groq AI.
    *   Click 'Create Todo' to save the project and prompt in database.

4.  **View Project Dashboard**

    *   On the home page, click the "View Dashboard" button to see project name and prompt that you saved.

## Project Structure 📂

```text
InFlowAI/
├── mainapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── middleware.py
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_userprofile_username_alter_userprofile_name.py
│   │   ├── 0003_alter_userprofile_email_inflowaiproject.py
│   │   ├── 0004_rename_company_link_inflowaiproject_project_link.py
│   │   └── __init__.py
│   ├── models.py
│   ├── planner.py
│   ├── templates/
│   │   └── main/
│   │       ├── base.html
│   │       ├── index.html
│   │       ├── projectDashboard.html
│   │       ├── todo_ai_form.html
│   │       └── registration/
│   │           ├── login.html
│   │           ├── otp.html
│   │           └── signup.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── todoAiProject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md
```

*   `mainapp/`: Contains the core application logic.
    *   `models.py`: Defines the database models (UserProfile, InFlowAIProject).
    *   `views.py`: Contains the view functions for handling user requests.
    *   `forms.py`: Defines the forms for user registration.
    *   `planner.py`: Implements the AI-powered task breakdown functionality using Groq.
    *   `templates/`: Stores the HTML templates.
    *   `urls.py`: Defines the URL patterns for the app.
*   `todoAiProject/`: Contains the project-level settings and configurations.
    *   `settings.py`: Defines the Django project settings.
    *   `urls.py`: Defines the root URL patterns for the project.
*   `requirements.txt`: Lists the Python dependencies.
*   `manage.py`: A command-line utility for Django administrative tasks.

## Contributing 🤝

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive messages.
4.  Submit a pull request.

## License ⚖️

This project has no license.

## Important Links 🔗

*   **Repository:** [https://github.com/Aarav-Jain123/InFlowAI](https://github.com/Aarav-Jain123/InFlowAI)

## Footer 📃

**InFlowAI** - [https://github.com/Aarav-Jain123/InFlowAI](https://github.com/Aarav-Jain123/InFlowAI) by [Aarav-Jain123](https://github.com/Aarav-Jain123). Feel free to fork, star, and open issues!


---
**<p align="center">Generated by [ReadmeCodeGen](https://www.readmecodegen.com/)</p>**
