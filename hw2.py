"""
Aynur Nebioğlu
nabiyevaa20@gmail.com
Homework-2

"""

print("Aşağıda bulunan bilgileri doldurunuz")
first_name = input("Adınız: ")
last_name = input("Soyadınız: ")
age = int(input("Yaşınız: "))
date_of_birth = int(input("Doğum yılınız: "))

user = [first_name, last_name, age, date_of_birth]
for info in user:   
    print(info)

if age < 18:
    print("You can't go out because it's too dangerous!!!")
else:
    print("You can go out to the street")




