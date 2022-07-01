import random

str = 'source-for-exercise/final-exercise-3/random_words.txt'
file = open(str, mode='r')
content = file.readlines()
arr_with_words = []

for x in content:
    arr_with_words.append(x.strip())

file.close()


def scramble_game():
    random_word = random.choice(arr_with_words)
    play_word = "".join(random.sample(random_word, len(random_word)))
    number_of_tries = 0

    print(play_word)

    guess_word = input('Digite a palavra na ordem correta: ')

    while guess_word != random_word and number_of_tries < 2:
        guess_word = input('Digite a palavra na ordem correta: ')
        number_of_tries += 1

    if guess_word != random_word:
        print(f"Que pena, a palavra correta era { random_word }, você perdeu!")
    else:
        print(f"Parabéns, você acertou a palavra correta { random_word }")


if __name__ == '__main__':
    scramble_game()
