from flask import render_template, request, redirect, url_for
from hw_app import app

data = []
@app.route('/', methods=['GET','POST'])
def index():
    # использует метод POST, так как информация будет отправляться.
    # Request method сравнивает данные с HTTP-запросом.
    if request.method == 'POST':
        # функция request.form извлекает значение из соответствующих полей
        name = request.form.get('name')
        town = request.form.get('town')
        hobby = request.form.get('hobby')
        age = request.form.get('age')
        if name and town and hobby and age:
            data.append({
                'name' : name,
                'town' : town,
                'hobby' : hobby,
                'age' : age
            })
            #использует для обновления страницы и предотвращения повторной отправки формы
            return redirect(url_for('index'))
    # возвращает отрендеренный шаблон (находится в директории `templates` Flask приложения) с переданными данными.
    # Функция импортируется из модуля Flask и используется для рендеринга HTML-шаблонов.
    # Она принимает название файла шаблона и любые дополнительные аргументы, которые вы хотите передать в шаблон.
    # **`posts=data`**: Здесь `data` — это переменная, которая содержит данные, которые вы хотите передать в шаблон.
    # В контексте шаблона эти данные будут доступны под именем `posts`.
    # Это может быть список, словарь или любой другой объект Python, который вы хотите использовать в шаблоне
    return render_template('form_about.html', posts=data)