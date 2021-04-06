#import fib.py as fib;
import telebot;
import parser;
bot = telebot.TeleBot('1730973536:AAFB8H1Ve71ojuWkh0zK4hyNQIcy1rzVjU8');
A=0
B=0
N=0
e=0
fx = ""
fibb = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]

def f(fx,x): 
  f = parser.expr(fx).compile()
  return eval(f)

def print_x(message,x1, x2, r, a, mtin):
  bot.send_message(message.from_user.id,"\n")
  bot.send_message(message.from_user.id,f"x1.{r} = a{r} + |ТИН{r}| * (iN{-1- r} / iN{1 - r}) = {a} + {mtin} * ({fibb[N - 1 - r]} / {fibb[N + 1 - r]}) = {x1[r]}")
  bot.send_message(message.from_user.id,f"x2.{r} = a{r} + |ТИН{r}| * (iN{-r} / iN{1 - r}) = {a} + {mtin} * ({fibb[N - r]} / {fibb[N + 1 - r]}) = {x2[r]}")
  bot.send_message(message.from_user.id,"\n")

def print_second(message,x1, xn):
  bot.send_message(message.from_user.id,"\nВторой этап")
  bot.send_message(message.from_user.id,f"x1.{N} = {xn}")
  bot.send_message(message.from_user.id,"\n")
  bot.send_message(message.from_user.id,f"Ф(x1.{N}) = Ф(x1.{N - 1}) = {f(fx,x1[N - 1])}")
  bot.send_message(message.from_user.id,f"Ф(x2.{N}) = {f(fx,xn)}")
  print("\n")
  if f(fx,xn) > f(fx,x1[N - 1]):
    bot.send_message(message.from_user.id,f"Ф(x2.{N}) > Ф(x1.{N})")
  else:
    bot.send_message(message.from_user.id,f"Ф(x2.{N}) < Ф(x1.{N})")
  
def print_f(message,r, fx1, fx2):
  if fx1 != fx2:
    
    bot.send_message(message.from_user.id,f"Ф(x1.{r}) = {fx1}")
    bot.send_message(message.from_user.id,f"Ф(x2.{r}) = {fx2}")
    if fx1 < fx2:
      bot.send_message(message.from_user.id,f"Ф(x1.{r}) < Ф(x2.{r})")
    else:
      bot.send_message(message.from_user.id,f"Ф(x1.{r}) > Ф(x2.{r})")
  else:
    bot.send_message(message.from_user.id, f"Ф(x1.{r}) = Ф(x2.{r}) = {fx1}")
  
def start(message):
  x1 = [0]
  x2 = [0]
  a = A
  b = B
  for r in range(1, N + 1):
    if (r < N):
      print("\n")
      bot.send_message(message.from_user.id,f"Итерация {r}")
      bot.send_message(message.from_user.id,"ТИН%s = [%s, %s]" % (r, a, b))
      
      mtin = b - a
      x1.append(a + mtin * (fibb[N - 1 - r] / fibb[N + 1 - r] ))
      x2.append(a + mtin * (fibb[N - r]) / fibb[N + 1 - r])
      
      fx1 = f(fx,x1[r])
      fx2 = f(fx,x2[r])
      
      print_x(message,x1, x2, r, a, mtin)

      if (r != N - 1):
        if fx1 < fx2:
          b = x2[r]
        else:
          a = x1[r]
      print_f(message,r, fx1, fx2)
        
    else:
      xn = x1[N - 1] + e
      if f(fx,xn) > f(fx,x1[N - 1]):
        b = x1[N - 1]
      else:
        a = x1[N - 1]
      print_second(message,x1, xn)

  bot.send_message(message.from_user.id,"ТИН = [%s, %s]" % (a, b))
#---------------------------------------
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Введите аргументы A B N E через запятую\nНапример 0,13,6,0.1")
'''
@bot.message_handler(['text'])
def first(message):
    bot.reply_to(message,message.text)
bot.polling(none_stop=True, interval=0) 
'''
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  input = message.text
  print(input)
  print(type(input))
  print(input.split(","))
  var=input.split(",")
  print(len(var))
  if(len(var) == 4):
    global A
    global B
    global N
    global E
    A=int(var[0])
    B=int(var[1])
    N=int(var[2])
    e=float(var[3])
    bot.send_message(message.from_user.id, "Введите функцию\nНапример 2 *(x-12) ** 2 + 3") 
  elif(len(var)==1):
    global fx
    fx=var[0]
    start(message)
'''    f = parser.expr(fx).compile()
    print(type(f))
    x = 10
    print(eval(f))
'''

  #print(f"you wrote A={A} B={B} N={N} E={E}")
bot.polling(none_stop=True, interval=0)
#-------------------------------------------