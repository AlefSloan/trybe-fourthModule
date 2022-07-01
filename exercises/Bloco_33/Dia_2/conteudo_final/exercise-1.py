def vertical_words(word):
    name = word
    for index, n in enumerate(word):
        if int(index) == 0:
            print(word)
        else:
            name = name[:-1]
            print(name)


if __name__ == '__main__':
    user_name = input('Digite seu nome: ')
    vertical_words(user_name)
