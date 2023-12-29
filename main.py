import tkinter
from tkinter import ttk
import math
from numpy import pi as pi3
from matplotlib import rcParams, style


rcParams['font.sans-serif'] = ['Arial']
style.use('classic')


def renov1(event):
    stext.set(stext.get() + '1')

def renov2(event):
    stext.set(stext.get() + '2')


def renov3(event):
    stext.set(stext.get() + '3')


def renov4(event):
    stext.set(stext.get() + '4')


def renov5(event):
    stext.set(stext.get() + '5')


def renov6(event):
    stext.set(stext.get() + '6')


def renov7(event):
    stext.set(stext.get() + '7')


def renov8(event):
    stext.set(stext.get() + '8')


def renov9(event):
    stext.set(stext.get() + '9')


def renov0(event):
    stext.set(stext.get() + '0')


def renov_dot(event):
    stext.set(stext.get() + '.')


def renovB(event):
    stext.set(stext.get()[:-1])


def renov_pm(event):
    s = stext.get()
    if s.startswith('-'):
        s = s[1:]
    else:
        s = '-' + s
    stext.set(s)


def renov_plus(event):
    global hidden, preoper
    if not hidden:
        hidden = float(stext.get())
    else:
        if preoper == '+':
            hidden += float(stext.get())
        elif preoper == '-':
            hidden -= float(stext.get())
    stext.set('')
    preoper = '+'


def renov_minus(event):
    global hidden, preoper
    if not hidden:
        hidden = float(stext.get())
    else:
        if preoper == '+':
            hidden += float(stext.get())
        elif preoper == '-':
            hidden -= float(stext.get())
    stext.set('')
    preoper = '-'


def proizvedenie(event):
    global hidden, preoper
    if not hidden:
        hidden = float(stext.get())
    else:
        if preoper == '*':
            hidden *= float(stext.get())
    stext.set('')
    preoper = '*'


def delenie(event):
    global hidden, preoper
    if not hidden:
        hidden = float(stext.get())
    else:
        if preoper == '/':
            hidden /= float(stext.get())
    stext.set('')
    preoper = '/'


def renov_equal(event):
    global hidden, preoper
    if not hidden:
        hidden = float(stext.get())
    else:
        if preoper == '+':
            hidden += float(stext.get())
        elif preoper == '-':
            hidden -= float(stext.get())
        elif preoper == '*':
            hidden *= float(stext.get())
        elif preoper == '/':
            try:
                hidden /= float(stext.get())
            except:
                hidden = 'Деление на 0 невозможно'
    stext.set(str(hidden))
    preoper = ''


def cancel(event):
    global hidden, preoper
    hidden = 0
    preoper = ''
    stext.set('')


def pi(event):
    stext.set(str(pi3))


def sinus(event):
    global hidden, preoper
    hidden = math.sin(float(stext.get()))
    stext.set(str(hidden))


def cosinus(event):
    global hidden, preoper
    hidden = math.cos(float(stext.get()))
    stext.set(str(hidden))


def tangens(event):
    global hidden, preoper
    hidden = math.tan(float(stext.get()))
    stext.set(str(hidden))


def obratnoe(event):
    global hidden, preoper
    hidden = 1 / (float(stext.get()))
    stext.set(str(hidden))


def sqroot(event):
    global hidden, preoper
    hidden = math.sqrt(float(stext.get()))
    stext.set(str(hidden))


def xin2(event):
    global hidden, preoper
    hidden = (float(stext.get())) ** 2
    stext.set(str(hidden))


def log(event):
    stext.set('Функция не готова')


def xiny(event):
    stext.set('Функция не готова')


def expon(event):
    stext.set('Функция не готова')


# память
hidden = 0

# предыдущая операция
preoper = ''

prog = tkinter.Tk()

stext = tkinter.StringVar(value='')
widtext = ttk.Entry(textvariable=stext, width=24)
widtext.grid(column=0, row=0, columnspan=3)

# кнопка 1
btn1 = ttk.Button(text='1', width=6)
btn1.bind('<Button-1>', renov1)
btn1.grid(column=0, row=1)

# кнопка 2
btn2 = ttk.Button(text='2', width=6)
btn2.bind('<Button-1>', renov2)
btn2.grid(column=1, row=1)

# кнопка 3
btn3 = ttk.Button(text='3', width=6)
btn3.bind('<Button-1>', renov3)
btn3.grid(column=2, row=1)

# кнопка4
btn4 = ttk.Button(text='4', width=6)
btn4.bind('<Button-1>', renov4)
btn4.grid(column=0, row=2)

# кнопка 5
btn5 = ttk.Button(text='5', width=6)
btn5.bind('<Button-1>', renov5)
btn5.grid(column=1, row=2)

# кнопка 6
btn6 = ttk.Button(text='6', width=6)
btn6.bind('<Button-1>', renov6)
btn6.grid(column=2, row=2)

# кнопка 7
btn7 = ttk.Button(text='7', width=6)
btn7.bind('<Button-1>', renov7)
btn7.grid(column=0, row=3)

# кнопка 8
btn8 = ttk.Button(text='8', width=6)
btn8.bind('<Button-1>', renov8)
btn8.grid(column=1, row=3)

# кнопка 9
btn9 = ttk.Button(text='9', width=6)
btn9.bind('<Button-1>', renov9)
btn9.grid(column=2, row=3)

# кнопка 0
btn0 = ttk.Button(text='0', width=6)
btn0.bind('<Button-1>', renov0)
btn0.grid(column=1, row=4)

# кнопка "точка"
btn_dot = ttk.Button(text='.', width=6)
btn_dot.bind('<Button-1>', renov_dot)
btn_dot.grid(column=2, row=4)

# кнопка DEL
btnB = ttk.Button(text='<-', width=6)
btnB.bind('<Button-1>', renovB)
btnB.grid(column=3, row=1)

# кнопка смены знака
btn_pm = ttk.Button(text='+/-', width=6)
btn_pm.bind('<Button-1>', renov_pm)
btn_pm.grid(column=0, row=4)

# кнопка ПЛЮС
btn_plus = ttk.Button(text='+', width=6)
btn_plus.bind('<Button-1>', renov_plus)
btn_plus.grid(column=3, row=2)

# кнопка МИНУС
btn_minus = ttk.Button(text='-', width=6)
btn_minus.bind('<Button-1>', renov_minus)
btn_minus.grid(column=3, row=3)

# кнопка РАВНО
btn_equal = ttk.Button(text='=', width=6)
btn_equal.bind('<Button-1>', renov_equal)
btn_equal.grid(column=3, row=4)

# кнопка CANCEL
btn_canc = ttk.Button(text='C', width=6)
btn_canc.bind('<Button-1>', cancel)
btn_canc.grid(column=3, row=0)

# кнопка УМНОЖИТЬ
btn_proizv = ttk.Button(text='*', width=6)
btn_proizv.bind('<Button-1>', proizvedenie)
btn_proizv.grid(column=0, row=5)

# кнопка РАЗДЕЛИТЬ
btn_delenie = ttk.Button(text='/', width=6)
btn_delenie.bind('<Button-1>', delenie)
btn_delenie.grid(column=1, row=5)

# кнопка 1/X
btn_1nax = ttk.Button(text='1/x', width=6)
btn_1nax.bind('<Button-1>', obratnoe)
btn_1nax.grid(column=2, row=5)

# кнопка ЛОГАРИФМ
btn_log = ttk.Button(text='ln', width=6)
btn_log.bind('<Button-1>', log)
btn_log.grid(column=3, row=5)

# кнопка SQRT
btn_sqrt = ttk.Button(text='sqrt(x)', width=6)
btn_sqrt.bind('<Button-1>', sqroot)
btn_sqrt.grid(column=0, row=6)

# кнопка КВАДРАТ
btn_x2 = ttk.Button(text='x^2', width=6)
btn_x2.bind('<Button-1>', xin2)
btn_x2.grid(column=1, row=6)

# кнопка СТЕПЕНЬ
btn_xy = ttk.Button(text='x^y', width=6)
btn_xy.bind('<Button-1>', xiny)
btn_xy.grid(column=2, row=6)

# кнопка ЭКСПОНЕНТА
btn_exp = ttk.Button(text='e^x', width=6)
btn_exp.bind('<Button-1>', expon)
btn_exp.grid(column=3, row=6)

# кнопка SIN
btn_sinus = ttk.Button(text='sin(x)', width=6)
btn_sinus.bind('<Button-1>', sinus)
btn_sinus.grid(column=0, row=7)

# кнопка COS
btn_cosinus = ttk.Button(text='cos(x)', width=6)
btn_cosinus.bind('<Button-1>', cosinus)
btn_cosinus.grid(column=1, row=7)

# кнопка TAN
btn_tan = ttk.Button(text='tg(x)', width=6)
btn_tan.bind('<Button-1>', tangens)
btn_tan.grid(column=2, row=7)

# кнопка PI
btn_pi = ttk.Button(text='pi', width=6)
btn_pi.bind('<Button-1>', pi)
btn_pi.grid(column=3, row=7)

prog.mainloop()