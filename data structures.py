# lists,
employees = ['Peter','John','Smith','Esther']
print(employees)
print(employees[2])
print(employees[1:4])
employees[3] = 'William'
print(employees)
employees.append('Jack')
print(employees)
employees.insert(0,'Juliana')
print(employees)
employees.extend(['Paul', 'Ann','Susan'])
print(employees)
# tuples,
languages = ('python', 'Java','Kotlin')
print(languages)
print(languages[1])
print(languages[1:3])
# languages(2)= 'Javascript' cannot reasign a value

# sets,
students= {'Andrew', 'Winnie', 'Alex', 'Paul'}
print(students)
if 'Andrew' in students:
    print('Andrew')
if 'Winnie' in students:
    print('Winnie')
if 'Alex' in students:
    print('Alex')
if 'Paul' in students:
    print('Paul')
if 'Susan' in students:
    print('Susan')
else:
    print('Not present')
students.add('Charles')
print(students)
students.update(['Reuben'])
print(students)
students.remove('Charles')
print(students)

# dictionary
pupil = {
    'first_name': 'Chris',
    'last_name': 'Njue',
    'email': 'njue@gmail.com',
    'gender': 'Female',
    'birthyear': '1999'
}
print(pupil)
print(pupil['first_name'])
pupil['skintone'] = 'brown'
print(pupil)
if 'skintone' in pupil:
    print('Yes it is present')
else:
    print('Not present')
if 'name' in pupil:
    print('Yes it is present')
else:
    print('Not present')

# create a random dictionary and
# illustrate how to check existence of a key
staff = {
    'staffname' : 'Mr Joshua',
    'staffNo' : '340',
    'DeptNo' : 'SD32',
    'Salary' : '34000',
    'Category' : 'Senior'
}
print(staff)
print(staff['staffname'])
if 'DeptNo' in staff:
    print('Yes it is present')
else:
    print('Not found')
if 'name' in staff:
    print('Yes it is present')
else:
    print('Not found')
age1=input('Enter age')
age2=input('Enter age')
age3=input('Enter age')
age4=input('Enter age')
print(age1,age2,age3,age4)
print(age1>age2 and age3>age4)
print(age1<age2 or age3<age4)
print(not(age1>=age2 and age3>=age4))
print(age1<=age2 or age3<=age4)


