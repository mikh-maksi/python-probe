dicts = []

q = {'question':"Какой язык самый популярный:",'answer1':"JavaScript",'answer2':"Python",'answer3':"Java",'answer4':"C#",'right':'1'}
dicts.append(q)
q = {'question':"Какой язык самый популярный:",'answer1':"JavaScript",'answer2':"Python",'answer3':"Java",'answer4':"C#",'right':'3'}
dicts.append(q)
q = {'question':"Какой язык самый популярный:",'answer1':"JavaScript",'answer2':"Python",'answer3':"Java",'answer4':"C#",'right':'3'}
dicts.append(q)

result = 0
for dct in dicts:
    answ = f"{dct['question']}\n 1. {dct['answer1']} | 2. {dct['answer2']} | 3. {dct['answer3']} | 4. {dct['answer4']} \n"
    answer =input(answ)
    if answer == dct['right']:
        result += 1

print(f"Ваш результат: {result} из 3")