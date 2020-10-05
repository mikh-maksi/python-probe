# Создаем игру на Python
**Python** - это язык программирования, который используется в различных сферах: от создания систем искусственного интеллекта до написания программ для веб-серверов.  
На **Python** также можно создавать игры.  
На этом уроке мы познакомимся с основами Python при создании небольшой игры: мы будем создавать игру "Змейка".  
Мы с вами за 1,5 часа создадим базовые элементы и научим змейку двигаться, а далее - добавим несколько элементов и вы сможете полноценно играть в созданную вами игру на своем компьютере.
## Запуск программы
Для запуска программы можно установить интерпретатор Python локально:
Либо же воспользоваться одним из он-лайн компиляторов:
<a href = "https://repl.it/">https://repl.it/</a>
Ниже приведены скриншоты того, как начать работать с <a href = "https://repl.it/">https://repl.it/</a>:  
<img src = "img/repl1.jpg">  
<img src = "img/repl2.jpg">  
<img src = "img/repl3.jpg">  
<img src = "img/start.jpg">  

## Холст
Мы будем использовать модуль `tkinter`, который позволяет создавать графический интерфейс.
```python
from tkinter import Tk, Canvas #Импортируем нужные модули

root = Tk() # Создаем переменную, в которой мы будем хранить класс модуля
root.title("GoITeens Python Snake") # Укажем заголовок

c = Canvas(root, width=400, height=400, bg="green") #Создадим холст (Canvas), на котором будет находиться наша игра
c.grid() #Размещение нашего созданного холста на экране

root.mainloop() # запуск модуля в работу
```  
При запуске данной программе получим поле:  
<img src = "img/Canvas.jpg">

# Элементы змейки
Добавим на холст один элемент змейки: это будет прямоугольник
```python
c.create_rectangle(20, 20, 40, 40, fill="#FF0000")
```
<img src = "img/Canvas2.jpg">

## Яблочко в случайной позиуии
```python
#Позиция яблочка
posx = 20 * random.randint(1, (400-20) / 20) 
posy = 20 * random.randint(1, (400-20) / 20)


#Отрисовка яблочка
BLOCK = c.create_oval(posx, posy,posx+20, posy+20,fill="yellow")
```
<img src = "img/Canvas3.jpg">

У нас получилось нарисовать кусочек змейки и яблоко. И мы их нарисовали отдельно. В программировании - для сложных конструкций используются классы. Такие блоки, которые можно 1 раз создать и далее вызывать во всех нужных ситуациях.
Определим общие параметры нашей игры:
```python
x = 20  #Начинается наша змейка с координаты x равной 20
y = 20 #Начинается наша змейка с координаты y равной 20
SEG_SIZE = 20 #Размер элемента змейки равен 20
WIDTH = 400 #Ширина поля
HEIGHT = 400 # Высота поля
```

Создадим класс сегмента змейки, который при вызове будет создавать прямоугольник.
```python
class Segment(object):
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y, x+SEG_SIZE, y+SEG_SIZE, fill="#FF0000")
```
И Создадим класс змейки, которая состоит из сегментов.
```python
#Класс змейки
class Snake(object):
    def __init__(self, segments):
        self.segments = segments #Сколько сегментов получили - такая и змейка по размеру
```
А также отдельно создадим функцию, которая вызовет новую змейку
```python
def create_snake():
    # Создаем сегменты и змейку
    segments = [Segment(SEG_SIZE, SEG_SIZE), Segment(SEG_SIZE*2, SEG_SIZE), Segment(SEG_SIZE*3, SEG_SIZE)] #Список из трех сегментов
    return Snake(segments)
```
И непосредственно вызовем функцию создания змейки:
```python
    create_snake()
```
Получим следующий код:
```python
from tkinter import Tk, Canvas #Импортируем нужные модули
import random


root = Tk() # Создаем переменную, в которой мы будем хранить класс модуля
root.title("GoITeens Python Snake") # Укажем заголовок

c = Canvas(root, width=400, height=400, bg="green") #Создадим холст (Canvas), на котором будет находиться наша игра
c.grid() #Размещение нашего созданного холста на экране


x = 20  #Начинается наша змейка с координаты x равной 20
y = 20 #Начинается наша змейка с координаты y равной 20
SEG_SIZE = 20 #Размер элемента змейки равен 20
WIDTH = 400
HEIGHT = 400
#Нарисуем змею из 1 элемента

c.create_rectangle(x, y, x+20, y + 20, fill="#FF0000")

#Позиция яблочка
posx = 20 * random.randint(1, (400-20) / 20)
posy = 20 * random.randint(1, (400-20) / 20)


#Отрисовка яблочка
BLOCK = c.create_oval(posx, posy,posx+20, posy+20,fill="yellow")


class Segment(object):
    # Один сегмент змейки
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y, x+SEG_SIZE, y+SEG_SIZE, fill="#FF0000")


#Класс змейки
class Snake(object):
    def __init__(self, segments):
        self.segments = segments #Сколько сегментов получили - такая и змейка по размеру



def create_snake():
    # Создаем сегменты и змейку
    segments = [Segment(SEG_SIZE, SEG_SIZE), Segment(SEG_SIZE*2, SEG_SIZE), Segment(SEG_SIZE*3, SEG_SIZE)] #Список из трех сегментов
    return Snake(segments)

create_snake()


root.mainloop() # запуск модуля в работу
```
<img src = "img/Canvas4.jpg">

Добавим змейке возможность двигаться:
Доработаем метод, который запускается при создании класса:
```python
def __init__(self, segments):
    self.segments = segments #Сколько сегментов получили - такая и змейка по размеру
    self.mapping = {"Down": (0, 1), "Right": (1, 0), "Up": (0, -1), "Left": (-1, 0), "a": (-1, 0)}         # Возможные направления движения
    self.vector = self.mapping["Down"]  # начальные направления движения
```
Добавляем метод, который "научит" змейку "Ходить".
```python
    def move(self): # Двигаем змейку по определенному вектору
        for index in range(len(self.segments)-1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index+1].instance)
            c.coords(segment, x1, y1, x2, y2)

        x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
        c.coords(self.segments[-1].instance,x1+self.vector[0]*SEG_SIZE, y1+self.vector[1]*SEG_SIZE,x2+self.vector[0]*SEG_SIZE, y2+self.vector[1]*SEG_SIZE)
```
Учим змейку изменять направление и останавливаться, при нажатии пробела:
```python
    def change_direction(self, event): # Изменяем направление змейки 
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]
        print(event.keysym)
        global game
        if event.keysym == "space":
            game = not(game)
            print(game)
```
А также функцию, которая запускает движение змейки:
```python
def move():
    c.bind("<KeyPress>", s.change_direction)
    if game:
        root.after(200, move)
    s.move()
```
И вызываем эту функцию:
```python
move()
```
А также добавим слушатель нажатия клавиш на клавиатуре:
```python
c.focus_set()
```
А также удалим элементы кода, которые мы использовали вначале для демонстрации возможностей:
```python
create_snake()
```
```python
c.create_rectangle(x, y, x+20, y + 20, fill="#FF0000")
```


Итоговый код:
```python
from tkinter import Tk, Canvas #Импортируем нужные модули
import random


root = Tk() # Создаем переменную, в которой мы будем хранить класс модуля
root.title("GoITeens Python Snake") # Укажем заголовок

c = Canvas(root, width=400, height=400, bg="green") #Создадим холст (Canvas), на котором будет находиться наша игра
c.grid() #Размещение нашего созданного холста на экране


x = 20  #Начинается наша змейка с координаты x равной 20
y = 20 #Начинается наша змейка с координаты y равной 20
SEG_SIZE = 20 #Размер элемента змейки равен 20
WIDTH = 400
HEIGHT = 400
#Нарисуем змею из 1 элемента

c.focus_set()
#Позиция яблочка
posx = 20 * random.randint(1, (400-20) / 20)
posy = 20 * random.randint(1, (400-20) / 20)

#Отрисовка яблочка
BLOCK = c.create_oval(posx, posy,posx+20, posy+20,fill="yellow")

class Segment(object):
    # Один сегмент змейки
    def __init__(self, x, y):
        self.instance = c.create_rectangle(x, y, x+SEG_SIZE, y+SEG_SIZE, fill="#FF0000")
        self.mapping = {"Down": (0, 1), "Right": (1, 0), "Up": (0, -1), "Left": (-1, 0), "a": (-1, 0)}         # Возможные направления движения
        self.vector = self.mapping["Down"]  # начальные направления движения

#Класс змейки
class Snake(object):
    def __init__(self, segments):
        self.segments = segments #Сколько сегментов получили - такая и змейка по размеру
        self.mapping = {"Down": (0, 1), "Right": (1, 0), "Up": (0, -1), "Left": (-1, 0), "a": (-1, 0)}         # Возможные направления движения
        self.vector = self.mapping["Down"]  # начальные направления движения

    def move(self): # Двигаем змейку по определенному вектору
        for index in range(len(self.segments)-1):
            segment = self.segments[index].instance
            x1, y1, x2, y2 = c.coords(self.segments[index+1].instance)
            c.coords(segment, x1, y1, x2, y2)
        x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
        c.coords(self.segments[-1].instance,x1+self.vector[0]*SEG_SIZE, y1+self.vector[1]*SEG_SIZE,x2+self.vector[0]*SEG_SIZE, y2+self.vector[1]*SEG_SIZE)


    def change_direction(self, event): # Изменяем направление змейки 
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]
        global game
        if event.keysym == "space":
            game = not(game)

def create_snake():
    # Создаем сегменты и змейку
    segments = [Segment(SEG_SIZE, SEG_SIZE), Segment(SEG_SIZE*2, SEG_SIZE), Segment(SEG_SIZE*3, SEG_SIZE)] #Список из трех сегментов
    return Snake(segments)

global game 
game = True

def move():
    c.bind("<KeyPress>", s.change_direction)
    if game:
        root.after(200, move)
    s.move()

s = create_snake()
move()

root.mainloop() # запуск модуля в работу
```

<img src = "img/Canvas5.jpg">