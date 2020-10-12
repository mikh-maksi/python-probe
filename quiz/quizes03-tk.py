from tkinter import Tk, Canvas
import random

# Globals
WIDTH = 400
HEIGHT = 400

root = Tk()
root.title("PythonicWay Quiz")

c = Canvas(root, width=800, height=400, bg="white")
c.grid()
restart_text = c.create_text(400, 50,
                             font='Arial 20',
                             fill='black',
                             text="Текст вопроса ",
                             state='hidden'
                            )

right_answer = c.create_text(400, 150,
                             font='Arial 20',
                             fill='green',
                             text="Правильный ответ ",
                             state='hidden'
                            )

wrong_answer = c.create_text(400, 150,
                             font='Arial 20',
                             fill='red',
                             text="Не правильный ответ ",
                             state='hidden'
                            )




rect1 = c.create_rectangle(0,200,400,300,fill='orange')
rect2 = c.create_rectangle(400,200,800,300,fill='pink')
rect3 = c.create_rectangle(0,300,400,400,fill='blue')
rect4 = c.create_rectangle(400,300,800,400,fill='yellow')

answer_text1 = c.create_text(200, 250,font='Arial 30', fill='black', text="Ответ 1", state='normal', activefill = 'bisque', justify = "center")
answer_text2 = c.create_text(600, 250,font='Arial 30', fill='black', text="Ответ 2", state='normal', activefill = 'bisque', justify = "left")
answer_text3 = c.create_text(200, 350,font='Arial 30', fill='black', text="Ответ 3", state='normal', activefill = 'bisque')
answer_text4 = c.create_text(600, 350,font='Arial 30', fill='black', text="Ответ 4", state='normal', activefill = 'bisque')

next_question = c.create_text(680, 180,
                             font='Arial 15',
                             fill='green',
                             text="Следующий вопрос ->",
                             state='hidden'
                            )

c.itemconfigure(restart_text, state='normal')

right = 3
def clicked(event):
    print(event.x)
    print(event.y)
 
    if event.x>0 and event.x<400 and event.y>200 and event.y<300:
       userAnswer = 1
    
    if event.x>400 and event.x<800 and event.y>200 and event.y<300:
        userAnswer = 2

    if event.x>0 and event.x<400 and event.y>300 and event.y<400:
        userAnswer = 3

    if event.x>400 and event.x<800 and event.y>300 and event.y<400:
        userAnswer = 4

    if right == userAnswer:
        c.itemconfigure(wrong_answer, state='hidden')
        c.itemconfigure(right_answer, state='normal')
    else:
        c.itemconfigure(right_answer, state='hidden')
        c.itemconfigure(wrong_answer, state='normal')

    c.itemconfigure(next_question, state='normal')
    


def nextQuestion(event):
    print("NextQuestion")


c.tag_bind(answer_text1, "<Button-1>", clicked)
c.tag_bind(answer_text2, "<Button-1>", clicked)
c.tag_bind(answer_text3, "<Button-1>", clicked)
c.tag_bind(answer_text4, "<Button-1>", clicked)


c.tag_bind(next_question, "<Button-1>", nextQuestion)



root.mainloop()
