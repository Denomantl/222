from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class Two_kats(FlaskForm):
    kat1 = StringField('Первый катет')
    kat2 = StringField('Второй катет')
    submit = SubmitField('Посчитать')


class Sides_and_angle(FlaskForm):
    param1 = StringField('Первая сторона')
    param2 = StringField('Вторая сторона')
    param3 = StringField('Синус угла между ними')
    submit = SubmitField('Посчитать')


class Geron(FlaskForm):
    param1 = StringField('Первая сторона')
    param2 = StringField('Вторая сторона')
    param3 = StringField('Третья сторона')
    submit = SubmitField('Посчитать')
