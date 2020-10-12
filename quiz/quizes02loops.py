dicts = []

q = {'question':"Какой язык самый популярный:",'answer1':"JavaScript",'answer2':"Python",'answer3':"Java",'answer4':"C#",'right':'1'}
dicts.append(q)
q = {'question':"Какая средняя зарплата Python-Разработчика:",'answer1':"1500",'answer2':"2000",'answer3':"2500",'answer4':"3000",'right':'3'}
dicts.append(q)
q = {'question':"Какая доля Python-разработки в Украине на 2020 год:",'answer1':"25%",'answer2':"12,4%",'answer3':"13,2%",'answer4':"17,1%",'right':'3'}
dicts.append(q)


result = 0
for dct in dicts:
    answ = f"{dct['question']}\n 1. {dct['answer1']} | 2. {dct['answer2']} | 3. {dct['answer3']} | 4. {dct['answer4']} \n"
    answer =input(answ)
    if answer == dct['right']:
        result += 1

print(f"Ваш результат: {result} из 3")