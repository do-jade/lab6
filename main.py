def menu():
    print('Menu')
    print('------------- ')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')


def encode(password):
    password = int(password)
    password_list = [int(i) for i in str(password)]
    new_password = [i + 3 for i in password_list]
    new_password = [str(i) for i in new_password]
    new_password = ''.join(new_password)
    return new_password


def decode(password):
    pass


def main():
    calculating = True
    while calculating:
        menu()
        choice = int(input('Please enter an option: '))
        if choice == 1:
            old_password = input('Please enter your password to encode: ')
            new_password = encode(old_password)
            print('Your password has been encoded and stored!')
        elif choice == 2:
            print(f'The encoded password is {new_password}, and the original password is {decode(new_password)}')
        elif choice == 3:
            break


if __name__ == '__main__':
    main()

