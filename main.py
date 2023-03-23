def encoder(password):
    encoded_password = ""
    for digit in password:
        shifted_digit = str((int(digit) + 3) % 10)  # shift each digit up by 3 numbers
        encoded_password += shifted_digit
    return encoded_password


def decoder(encoded_password):
    password = ""
    for digit in encoded_password:
        shifted_digit = str((int(digit) - 3) % 10)  # shift each digit down by 3 numbers
        password += shifted_digit
    return password



if __name__ == "__main__":
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        choice = input("Please enter an option: ")
        if choice == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encoder(password)
            print("Your password has been encoded and stored!\n")
        elif choice == "2":
            if not encoded_password:
                print("Please encode a password first.")
            else:
                print(f"The encoded password is {encoded_password}, and the original password is {decoder(encoded_password)}.\n")
        elif choice == "3":
            break
            False
        else:
            print("Invalid option. Please try again.")

