from flask import Flask, render_template
from math import sqrt
from werkzeug.utils import redirect
from data import db_session
from forms.user import Sides_and_angle, Two_kats, Geron

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/two_kat', methods=['GET', 'POST'])
def two_kat():
    form = Two_kats()
    if form.validate_on_submit():
        try:
            if float(form.kat1.data.replace(' ', '')) > 0 and \
                    float(form.kat2.data.replace(' ', '')) > 0:
                if 0.5 * float(form.kat2.data) * float(form.kat1.data) != int(0.5 * float(
                        form.kat2.data) * float(form.kat1.data)):

                    return render_template('register.html', title='Калькулятор',
                                           form=form,
                                           message=("Ваш результат: " +
                                                    str(
                                                        0.5 * float(
                                                            form.kat2.data) *
                                                        float(
                                                            form.kat1.data))))
                elif 0.5 * float(form.kat2.data) * float(form.kat1.data) == int(0.5 * float(
                        form.kat2.data) * float(form.kat1.data)):

                    return render_template('register.html', title='Калькулятор',
                                           form=form,
                                           message=("Ваш результат: " +
                                                    str(
                                                        int(0.5 * float(
                                                            form.kat2.data) *
                                                            float(
                                                                form.kat1.data)))))
            elif float(form.kat2.data.replace(' ', '')) <= 0 or \
                    float(form.kat1.data.replace(' ', '')) <= 0:
                return render_template('register.html', title='Калькулятор',
                                       form=form,
                                       message=
                                       "Один или несколько параметров равны 0 "
                                       "или отрицательны")
        except ValueError:
            return render_template('register.html', title='Калькулятор',
                                   form=form,
                                   message=
                                   "Один или несколько параметров не указаны или указаны неверно")

    return render_template('register.html', title='Через 2 катета', form=form)


@app.route('/sides_and_angle', methods=['GET', 'POST'])
def sides_and_angle():
    form = Sides_and_angle()
    if form.validate_on_submit():
        try:
            if float(form.param1.data) > 0 and \
                    float(form.param2.data) > 0 and -1 <= float(form.param3.data) <= 1 and \
                    float(form.param3.data) != 0:
                if 0.5 * float(form.param1.data) * float(form.param2.data) * float(form.param3.data) == int(
                        0.5 * float(form.param1.data) * float(form.param2.data) * float(form.param3.data)):

                    return render_template('sides.html', title='Калькулятор',
                                           form=form,
                                           message=("Ваш результат: " +
                                                    str(int(
                                                        0.5 * float(form.param1.data) *
                                                        float(form.param2.data) *
                                                        float(form.param3.data)))))
                elif 0.5 * float(form.param1.data) * float(form.param2.data) * float(form.param3.data) != int(
                        0.5 * float(form.param1.data) * float(form.param2.data) * float(form.param3.data)):

                    return render_template('sides.html', title='Калькулятор',
                                           form=form,
                                           message=("Ваш результат: " +
                                                    str(
                                                        0.5 * float(form.param1.data) *
                                                        float(form.param2.data) *
                                                        float(form.param3.data))))
            elif float(form.param1.data) <= 0 or \
                    float(form.param2.data) <= 0 or float(form.param3.data) == 0 or \
                    float(form.param3.data) > 1 or float(form.param3.data) < -1:
                return render_template('sides.html', title='Калькулятор',
                                       form=form,
                                       message=
                                       "Некоторые праметры указаны неверно:"
                                       " стороны должны быть положительными, синус угла не должен быть меньше -1,"
                                       " больше"
                                       " 1, равным 0")
        except ValueError:
            return render_template('sides.html', title='Калькулятор',
                                   form=form,
                                   message=
                                   "Один или несколько параметров не указаны или указаны неверно")

    return render_template('sides.html', title='Калькулятор', form=form)


@app.route('/geron', methods=['GET', 'POST'])
def geron():
    form = Geron()
    if form.validate_on_submit():
        try:
            if float(form.param1.data) > 0 and \
                    float(form.param2.data) > 0 and float(form.param3.data) > 0:
                p = 0.5 * (float(form.param1.data) + float(form.param2.data) + float(form.param3.data))
                if sqrt(p * (p - float(form.param1.data)) * (p - float(form.param2.data)) * (p - float(form.param3.data))) \
                        == int(
                        sqrt(p * (p - float(form.param1.data)) * (p - float(form.param2.data)) *
                             (p - float(form.param3.data)))):

                    return render_template('sides.html', title='Калькулятор',
                                           form=form,
                                           message=("Ваш результат: " +
                                                    str(int(sqrt(p * (p - float(form.param1.data)) *
                                                                 (p - float(form.param2.data)) *
                                                                 (p - float(form.param3.data)))))))
                elif sqrt(p * (p - float(form.param1.data)) * (p - float(form.param2.data)) *
                          (p - float(form.param3.data))) != int(
                        sqrt(p * (p - float(form.param1.data)) * (p - float(form.param2.data)) *
                             (p - float(form.param3.data)))):

                    return render_template('sides.html', title='Калькулятор',
                                           form=form,
                                           message=("Ваш результат: " +
                                                    str(
                                                        sqrt(p * (p - float(form.param1.data)) *
                                                             (p - float(form.param2.data)) *
                                                             (p - float(form.param3.data))))))
            elif float(form.param1.data) <= 0 or \
                    float(form.param2.data) <= 0 or float(form.param3.data) <= 0:
                return render_template('sides.html', title='Калькулятор',
                                       form=form,
                                       message=
                                       "Некоторые праметры указаны неверно:"
                                       " стороны должны быть положительными")
        except ValueError:
            return render_template('sides.html', title='Калькулятор',
                                   form=form,
                                   message=
                                   "Один или несколько параметров не указаны или указаны неверно")

    return render_template('sides.html', title='Калькулятор', form=form)


def main():
    app.run()


if __name__ == '__main__':
    main()
