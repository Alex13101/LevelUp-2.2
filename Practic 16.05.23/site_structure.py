

from flask import Flask, render_template

app = Flask(__name__)

context = {'title': 'Заголовок',
           'text': 'Текст'}


@app.route('/')
def index():
    class New:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    new = New('Vasya', 20)
    lst = [1, 2, 3, 4, 5, 6]
    for i in lst:
        print(i)
    else:
        print('else')

    return render_template(
        'index1.html',
        number=4,
        hello='hello',
        world='hello',
        context=context,
        new=new,
        lst=[1, 2, 3, 4, 5, 6]
    )




if __name__ == '__main__':
    app.run(debug=True)