"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""

from flask import Flask, request, render_template
from markupsafe import escape
from views.about import about_view
from views.index import index_view

app = Flask(__name__)

app.register_blueprint(
    about_view,
)

app.register_blueprint(
    index_view,
)


#using bootstrap templates
@app.get("/", endpoint="index")
def index():
    return render_template("index.html")

@app.get("/about", endpoint="about")
def about():
    return render_template("about.html")

@app.get("/about/", endpoint="about/")
def about():
    return render_template("about.html")

@app.get('/hello')
def hello_view():
    name = request.args.get("name", "") #name or empty
    name = name.strip() #del spaces
    if not name:
        name = "Anonimous"
    return f'Hello, {escape(name)}' #ret simply string with url parameter "name"

if __name__ == "__main__":
    app.run(debug=True)
