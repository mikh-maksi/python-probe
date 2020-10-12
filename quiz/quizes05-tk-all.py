from tkinter import Tk, Canvas
import random



dicts = []

q = {'question':"Какой язык самый популярный:",'answer1':"JavaScript",'answer2':"Python",'answer3':"Java",'answer4':"C#",'right':1}
dicts.append(q)
q = {'question':"Какая доля Python:",'answer1':"12%",'answer2':"13,2%",'answer3':"15%",'answer4':"50%",'right':2}
dicts.append(q)
q = {'question':"Сколько в среденем зарабатывает Python-разработчик:",'answer1':"$1500",'answer2':"$2000",'answer3':"$2500",'answer4':"$2500",'right':3}
dicts.append(q)
nQuestion = 0
allQuestion = 3
result = 0


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
                             text=dicts[nQuestion].get('question'),
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

answer_text1 = c.create_text(200, 250,font='Arial 30', fill='black', text=dicts[nQuestion].get('answer1'), state='normal', activefill = 'bisque', justify = "center")
answer_text2 = c.create_text(600, 250,font='Arial 30', fill='black', text=dicts[nQuestion].get('answer2'), state='normal', activefill = 'bisque', justify = "left")
answer_text3 = c.create_text(200, 350,font='Arial 30', fill='black', text=dicts[nQuestion].get('answer3'), state='normal', activefill = 'bisque')
answer_text4 = c.create_text(600, 350,font='Arial 30', fill='black', text=dicts[nQuestion].get('answer4'), state='normal', activefill = 'bisque')

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
    global result
    if event.x>0 and event.x<400 and event.y>200 and event.y<300:
       userAnswer = 1
    
    if event.x>400 and event.x<800 and event.y>200 and event.y<300:
        userAnswer = 2

    if event.x>0 and event.x<400 and event.y>300 and event.y<400:
        userAnswer = 3

    if event.x>400 and event.x<800 and event.y>300 and event.y<400:
        userAnswer = 4

    if dicts[nQuestion].get('right') == userAnswer:
        c.itemconfigure(wrong_answer, state='hidden')
        c.itemconfigure(right_answer, state='normal')
        result+=1
    else:
        c.itemconfigure(right_answer, state='hidden')
        c.itemconfigure(wrong_answer, state='normal')

    c.itemconfigure(next_question, state='normal')
    


def nextQuestion(event):
    print("NextQuestion")
    global nQuestion 
    nQuestion +=1
    c.itemconfigure(right_answer, state='hidden')
    c.itemconfigure(wrong_answer, state='hidden')
    if nQuestion == allQuestion:
        result_answer = c.create_text(400, 150,
                             font='Arial 20',
                             fill='red',
                             text=f"Итоговый результат:{result} из {allQuestion}",
                             state='normal'
                            )
    else:
        c.itemconfigure(restart_text,  text=dicts[nQuestion].get('question'))
        c.itemconfigure(answer_text1,  text=dicts[nQuestion].get('answer1'))
        c.itemconfigure(answer_text2,  text=dicts[nQuestion].get('answer2'))
        c.itemconfigure(answer_text3,  text=dicts[nQuestion].get('answer3'))
        c.itemconfigure(answer_text4,  text=dicts[nQuestion].get('answer4'))


c.tag_bind(answer_text1, "<Button-1>", clicked)
c.tag_bind(answer_text2, "<Button-1>", clicked)
c.tag_bind(answer_text3, "<Button-1>", clicked)
c.tag_bind(answer_text4, "<Button-1>", clicked)


c.tag_bind(next_question, "<Button-1>", nextQuestion)



root.mainloop()
