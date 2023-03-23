# This was an interesting project.
def arr_to_string(data):
    answer = ""
    for x in data:
        answer += str(x)
    return answer

def encoder(x):
    answer = []
    for i in x:
        i = int(i)
        if i == 7:
            i = 0
        elif i == 8:
            i = 1
        elif i == 9:
            i = 2
        else:
            i += 3
        answer.append(i)
    return answer

def decoder(y):
    answer = []
    for i in y:
        i = (i + 7) % 10
        answer.append(i)
    return answer

is_running = True
menuselection = ''
encoded_answer = []
while is_running:
    print("Menu\n------------\n1. Encode\n2. Decode\n3. Quit\n")
    menuselection = input("Please enter an option:")

    if menuselection == "1":
        x = input("Please enter your password to encode:")
        encoded_answer = encoder(x)
        print("Your passcode has been encoded and stored!")

    if menuselection == "2":
        decoded_answer = decoder(encoded_answer)
        print("The encoded password is", arr_to_string(encoded_answer), "and the original password is", arr_to_string(decoded_answer))

    if menuselection == "3":
        is_running = False




