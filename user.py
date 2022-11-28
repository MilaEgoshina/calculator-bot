import tkinter as tk
from tkinter import messagebox
import rational_test as rt
import complex as c
import logirovanie as l
import telebot
# import log                                       #  logger.add('debug.log', format='{time} {level} {message}', level='DEBUG', serialize=True) 
                                                      # то что можно в это log положить красиво ошибки подсвечивает

API_TOKEN ='5478998023:AAEnIUT5-1BRTMlmvb9-YIoyF2pE9c1_jok'
bot = telebot.TeleBot(API_TOKEN)
calc = False

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Готов к работе!")

@bot.message_handler(commands=['calc'])
def calc_message(message):
    global calc
    calc=True
    bot.send_message(message.chat.id, "А теперь введите выражение для вычисления" )

@bot.message_handler(content_types='text')
def message_reply(message):
    global calc
    if calc:
        value = message.text      # функция принимает значение value (это строка, состоящяя из введенных 'число опнрация число')
        if value.count('j') > 0:
            value = c.list_complex(value)
            bot.send_message(message.chat.id,c.calculator(value))
            l.info_log(c.calculator(value))
            calc=False
        else:
            value = rt.get_expression(value)
            bot.send_message(message.chat.id,rt.calculate(value))
            l.info_log(rt.calculate(value))
            calc=False

bot.polling()

def add_digit(digit):
    value = calc.get()    
    if  value[0]=='0' and len(value)==1:     
        value = value[1:]    
    calc.delete(0,tk.END)
    calc.insert(0,value+digit)
    l.info_log(digit)

def add_complex_char(compl):
    value = calc.get()
    calc.delete(0,tk.END)
    calc.insert(0,value+compl) 

def add_point_char(point):
    value = calc.get()
    calc.delete(0,tk.END)
    calc.insert(0,value+point) 

def add_bracket_char(bracket):
    value = calc.get()
    calc.delete(0,tk.END)
    calc.insert(0,value+bracket) 

    

def add_operation(operation):
    value = calc.get()                                                   # конкатенация, чтобы числа добавлялись справа
    if value[-1] in '-+/*':
        value = value[:-1]
    # elif '+' in value or  '-' in value or '*' in value or '/' in value:   # если последним в поле ввода стоит операция, то мы вычисляем значение и продолжаем ввод, напр
    #     calculate()                                                      # 7+8-, а так получим 15- и дальше можно продолжать ввод чисел
    #     value = calc.get() 
    calc.delete(0,tk.END)
    calc.insert(0,value+operation)
    l.info_log(operation)

#@logger.catch 
def calculate():
    value = calc.get()       # функция принимает значение value (это строка, состоящяя из введенных 'число опнрация число')
    if value[-1] in '+-/*':   # если строка заканчивается на операцию, тогда мы к числу прибавим это же число (так в калькуляторах)
        value = value + value[:-1]
    if value.count('j') > 0:
        value = c.list_complex(value)
        calc.delete(0,tk.END)       # очищаем поле ввода
        calc.insert(0, c.calculator(value))    # вставляем значение, которое вычисляем при помощи функции eval
        l.info_log(c.calculator(value))
    else:
        value = rt.get_expression(value)
        calc.delete(0,tk.END)       
        calc.insert(0, rt.calculate(value))
        l.info_log(rt.calculate(value))

  

def clear():
    calc.delete(0,tk.END)  
    calc.insert(0,0)
    l.info_log(clear())

def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=('Arial',13), command=lambda : add_digit(digit))    


def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial',13), fg='red',
                    command=lambda : add_operation(operation))    

def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial',13), fg='red',
                    command=calculate) 

def make_clear_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial',13), fg='red',
                    command=clear) 

def press_key(event):
    print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/':
        add_operation(event.char)
    elif event.char =='\r':          # этот символ эквивалентен кнопке Enter на клавиатуре
        calculate()
    elif event.char =='j':          
        add_complex_char(event.char) 
    elif event.char =='.':          
        add_point_char(event.char) 
    elif event.char =='(':          
        add_bracket_char(event.char)
    elif event.char ==')':          
        add_bracket_char(event.char)                 

win = tk.Tk()
win.geometry(f"240x335+100+200")
win['bg'] = '#33ffe6'
win.title('Калькулятор')

win.bind('<Key>', press_key)         # функция обрабатывает"событие""= нажатие на клавишу

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial',15),width=15)   # поле ввода в самом верху, цифры по правому краю
calc.insert(0,'0')
calc.grid(row=0, column=0, columnspan=4, stick='we', padx=5)

# создадим несколько кнопок 
make_digit_button('1').grid(row=1, column=0, stick='wens',padx=5, pady=5)
make_digit_button('2').grid(row=1, column=1, stick='wens',padx=5, pady=5)
make_digit_button('3').grid(row=1, column=2, stick='wens',padx=5, pady=5)
make_digit_button('4').grid(row=2, column=0, stick='wens',padx=5, pady=5)
make_digit_button('5').grid(row=2, column=1, stick='wens',padx=5, pady=5)
make_digit_button('6').grid(row=2, column=2, stick='wens',padx=5, pady=5)
make_digit_button('7').grid(row=3, column=0, stick='wens',padx=5, pady=5)
make_digit_button('8').grid(row=3, column=1, stick='wens',padx=5, pady=5)
make_digit_button('9').grid(row=3, column=2, stick='wens',padx=5, pady=5)
make_digit_button('0').grid(row=4, column=0, stick='wens',padx=5, pady=5)
make_digit_button('j').grid(row=5, column=1, stick='wens',padx=5, pady=5)
make_digit_button('.').grid(row=4, column=1, stick='wens',padx=5, pady=5)
make_digit_button('(').grid(row=5, column=2, stick='wens',padx=5, pady=5)
make_digit_button(')').grid(row=5, column=3, stick='wens',padx=5, pady=5)

make_operation_button('+').grid(row=1, column=3, stick='wens',padx=5, pady=5)
make_operation_button('-').grid(row=2, column=3, stick='wens',padx=5, pady=5)
make_operation_button('/').grid(row=3, column=3, stick='wens',padx=5, pady=5)
make_operation_button('*').grid(row=4, column=3, stick='wens',padx=5, pady=5)

make_calc_button('=').grid(row=4, column=2, stick='wens',padx=5, pady=5)
make_clear_button('c').grid(row=5, column=0, stick='wens',padx=5, pady=5)

win.grid_columnconfigure(0,minsize=60)
win.grid_columnconfigure(1,minsize=60)
win.grid_columnconfigure(2,minsize=60)
win.grid_columnconfigure(3,minsize=60)
win.grid_columnconfigure(4,minsize=60)

win.grid_rowconfigure(1,minsize=60)
win.grid_rowconfigure(2,minsize=60)
win.grid_rowconfigure(3,minsize=60)
win.grid_rowconfigure(4,minsize=60)
win.grid_rowconfigure(5,minsize=60)

win.mainloop()