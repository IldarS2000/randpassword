import random
import string

SYMBOLS = []
SYMBOLS += list(string.ascii_letters)
SYMBOLS += list(string.digits)
SYMBOLS += list(string.punctuation)


def generate_password(length):
    return ''.join(random.choice(SYMBOLS) for _ in range(length))


def get_length():
    while True:
        try:
            length = int(input('enter length of random password: '))
            break
        except ValueError:
            print('length should be number type.')
    return length


def main():
    while True:
        length = get_length()
        if length >= 12:
            password = generate_password(length)
            print(f'password: {password}')
        else:
            print('length must be more than 12 symbols.')


if __name__ == '__main__':
    main()
