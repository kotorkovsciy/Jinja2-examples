from jinja2 import Template

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

person2 = { 'name': 'Фёдор', 'age': 34 }

tm2 = Template("Мне {{ p['age'] }} лет и зовут {{ p['name'] }}.")
msg2 = tm2.render(p = person2)

per = Person('Фёдор', 33)

tm = Template('Мне {{ p.getAge() }} лет и зовут {{ p.getName() }}.')
msg = tm.render(p = per)

print(msg)
print(msg2)