import random

simvoly = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
dlina = int(input("Введите длину пароля"))
sgparol = ""

for i in range (dlina):
    sgparol += random.choice(simvoly)
    
print(sgparol)    