from datetime import datetime

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)       #создаем объект на основе класса фласк
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pythonProject.db' #подключение к базе данных с названием бд ,которую мы создадим
db = SQLAlchemy(app)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<Article %r>" % self.id

    """стринг - немного текста, текст - много текста
            нулабл фолз - не пустая строка"""

    """выдается объект и его айди ,для получения записи из бд"""



@app.route('/')  #отслеживание главной странички
@app.route('/home')
def index():
    return render_template('index.html') # рендер выводит содержимое папки


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User page: " + name + " - " + str(id)


if __name__ == "__main__":  #запускает локальный сервер
    app.run(debug=True) #дебаг выведет все ошибки,как все будет готово,поменяем флаг на FALSE
