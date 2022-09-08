<h1 align="center"> How to run this code: </h1>


1 - **Inside a folder clone this repository with:**
<br>
    `git clone https://github.com/senseverthe1/fpf-back-end.git`

2 - **Access the directory with:**
<br>`cd fpf-back-end`

3 - **Create your virtual environment with:**
<br>`python3 -m venv venv or python -m venv venv or py -m venv venv`

4 - **Activate the virtual environment with:**
<br>`venv/Scripts/activate`

5 - **Install used libraries with:**
<br>`pip install -r requirements`

6 - **Create the models in the BD with:**
<br>`python manage.py migrate`

7 - **Run the project with:**
<br>`python manage.py runserver`


## :hammer: Project features

In this Project we have an EndPoint to request two tables
based on its parameters and its functionalities are:

- `1` It will be possible to create Products and Categories
- `2` It will be possible to edit Products and Categories
- `3` It will be possible to delete Products and Categories
- `4` Filter Products by Name and/or Category