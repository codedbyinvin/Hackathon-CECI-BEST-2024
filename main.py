message = "code = 2313"
shift = 23454

new_message = ""
for car in message:
    new_message += chr(ord(car)+shift)

print("encrypted message: ", new_message)

solved_message = ""
for car in new_message:
    solved_message += chr(ord(car)-shift)

print("decrypted message: ", solved_message)
