<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://user-images.githubusercontent.com/49699693/231891944-e7ae95dd-3512-4e70-a759-9cd9a10d0103.png" alt="Project logo"></a>
</p>
<h3 align="center">Basic Twitter API - FastAPI</h3>

---

 This project is part of the course [Curso de FastAPI: Modularización, Datos y Errores](https://platzi.com/cursos/fastapi-errores/) of [Platzi](https://platzi.com).



## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)
- [Next Steps](#next-steps)

## 🧐 About <a name = "about"></a>

The purpose of this project is to learn the following concepts about FastAPI.
  - Hosted & Interactive API Documentation with Swagger UI and ReDoc
  - Data modeling and validation with pydantic
  - Pydantic models
  - CRUD
  - GET, POST, UPDATE and DELETE methods.
  - FastAPI Routers
  - HTTP exceptions
  - JSON files as databases


## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

    Python >= 3.6

### Installing

1. Clone or download the repository

    ```bash
    $ git clone https://github.com/fernunex/fastapi-twitter-api-curso-project
    ```

2. Open the project directory and then create the virtual environment

    ```bash
    $ python3 -m venv venv
    $ source venv/bin/activate
    ```

3. Install all the dependencies

    ```bash
      (venv) $ pip3 install -r requirements.txt
    ```

4. Run the app

    ```bash
    (venv) $ uvicorn main:app --reload
    ```

Then you can go to http://127.0.0.1:8000/docs or http://127.0.0.1:8000/redoc and check out the interactive API documentation with Swagger UI or ReDoc.


## 🎈 Usage <a name="usage"></a>

To use all the paths of the API go to the interactive documentation at http://127.0.0.1:8000/docs or http://127.0.0.1:8000/redoc when the app is running.

## ⛏️ Built Using <a name = "built_using"></a>

- [FastAPI](https://fastapi.tiangolo.com/) - Web Framework

## ✍️ Authors <a name = "authors"></a>

- [@fernunex](https://github.com/fernunex)


## 💡 Next steps <a name = "next-steps"></a>

- Use MariaDB Database or MongoDB
- Use Docker
- Fix, update and delete some bad code
- Implement JWT Authentication
