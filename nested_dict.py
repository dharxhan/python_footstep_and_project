student = {1: {'name': 'Jhon','age':'27','sex':'Male'},
           2: {'name': 'Marie','age':'22','sex':'Female'},
           3: {'name': 'Luna','age':'24','sex':'Female','married':'No'},
           4: {'name': 'Peter','age':'29','sex':'Male','married':'Yes'}
    }

print("Complete dictionary:",student)
print("Student 1:",student[1])
print("Student 2:",student[2])
print("Student 3:",student[3])
print("Student 4:",student[4])

for key in student.keys():
    print("Student",key,":",student[key]["name"])

del student[3]['married']
del student[4]['married']
