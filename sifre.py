import random


password_length = int(input("Lütfen parolanızın uzunluğunu girin: "))


password_characters = "+-!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


generated_password = ""


for _ in range(password_length):
    generated_password += random.choice(password_characters)


print("Oluşturulan Parola:", generated_password)
