# WAP to concatenate multiple dictionary in one
Fruit = {'Apple': 100, 'banana': 5}
 
Subject =  {'Math': 100, 'English': 98} 
 
animal =  {'name': 'Rabbit', 'age': 1}
 
conacte_Dict =  {}
 
for dict in (Fruit, Subject, animal): conacte_Dict.update(dict)
 
print(conacte_Dict)
