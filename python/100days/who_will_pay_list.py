#fruits = ["apple", "orange", "guava", "banana"]
# print(fruits[0])
# fruits.append("mango")
# print(fruits)

import random
names = input("who all are present\n")
nameslist = names.split(", ")
print(nameslist)

no_of_names = len(nameslist)
print(no_of_names)

random_person = random.randint(0, no_of_names-1)

person_wo_will_pay = nameslist[random_person]
print(person_wo_will_pay + " will for todays meal")

print(random.choice(nameslist))
# the above function does everyting that is writtrn in te above code
