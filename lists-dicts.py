jan = {"name": "Jan", "email": "jan@mail.com", "fav_color": "red", "salary": "1000"}
michael = {"name": "Michael", "email": "micheal@mail.com", "fav_color": "green", "salary": "20000"}
karol = {"name": "Karol", "email": "karol@mail.com", "fav_color": "blue", "salary": "12121212"}

emloyees = [jan, michael, karol]
print(emloyees)

for i in emloyees:
    print(i["email"])

contact_dict = {}
for i in emloyees:
    contact_dict[i["name"]] = i

print(contact_dict["Michael"]["fav_color"])

print(10 * "-", "LAB", 10 * "-")

a1 = {
    "time": "9:00",
    "teacher": "profesor Wirus",
    "subject": "mikrobiology",
    "type": "lecture"
}

a2 = {
    "time": "12:00",
    "teacher": "doctor Colb",
    "subject": "chemistry",
    "type": "lab"
}

a3 = {
    "time": "14:00",
    "teacher": "profesor Wirus",
    "subject": "ethic",
    "type": "doctor oil"
}

plan = [a1, a2, a3]
print(plan)

new_plan = {}
for j in plan:
    new_plan[j["subject"]] = j
print(new_plan)

# for position in plan:
# print(position["subject"], position["time"])

for k, v in new_plan.items():
    print(k, v["time"])

print(10 * "-", "SAME EXERCISES WITH CLASSES", 10 * "-")


# jan = {"name": "Jan", "email": "jan@mail.com", "fav_color": "red", "salary": "1000"}
# michael = {"name": "Michael", "email": "micheal@mail.com", "fav_color": "green", "salary": "20000"}
# karol = {"name": "Karol", "email": "karol@mail.com", "fav_color": "blue", "salary": "12121212"}


class Person:
    def __init__(self, name, email, fav_color, salary):
        self.name = name
        self.email = email
        self.fav_color = fav_color
        self.salary = salary


jan2 = Person("Jan", "jan@mail.com", "red", "1000")
michael2 = Person("Michael", "michael@mail.com", "green", "20000")
karol2 = Person("Karol", "karol@mail.com", "blue", "12121212")

emploees2 = [jan2, michael2, karol2]

for i in emploees2:
    print(i.name, i.salary)

print(michael2.fav_color)

print(10 * "-", "LAB", 10 * "-")


# a1 = {
#     "time": "9:00",
#     "teacher": "profesor Wirus",
#     "subject": "mikrobiology",
#     "type": "lecture"
# }
#
# a2 = {
#     "time": "12:00",
#     "teacher": "doctor Colb",
#     "subject": "chemistry",
#     "type": "lab"
# }
#
# a3 = {
#     "time": "14:00",
#     "teacher": "profesor Wirus",
#     "subject": "ethic",
#     "type": "doctor oil"
# }


class StudyPlan:
    def __init__(self, time, teacher, subject, type):
        self.time = time
        self.teacher = teacher
        self.subject = subject
        self.type = type


a1 = StudyPlan("9:00", "profesor Wirus", "mikrobiology", "lecture")
a2 = StudyPlan("12:00", "doctor Colb", "chemistry", "lab")
a3 = StudyPlan("14:00", "profesor Wirus", "ethic", "doctor oil")


plan = [a1, a2, a3]

for i in plan:
    print(i.__dict__)


dict_plan = {}
for i in plan:
    dict_plan[i.subject] = i

print(dict_plan)

