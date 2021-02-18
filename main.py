word = []
word_two = []
word_two_clone = []
word_hide = []


def litter_hide():
    len_word_two = len(word_two)
    while 0 != len_word_two:
        len_word_two -= 1
        word_hide.append('_')


while True:
    try:
        word_one = input('Please enter your word: ')
        word.append(word_one.strip())
        break
    except ValueError:
        print('Enter only string value')


for words in word:
    for word_letter in words:
        word_two.append(word_letter.strip())
        word_two_clone.append(word_letter.strip())

attempts = 6
litter_hide()


while 0 != attempts:
    letter = input("Enter one letter: ").strip()
    if letter in word_two:
        index_letter = word_two.index(letter)
        word_hide[index_letter] = letter
        print(f"Good you guessed! Hide word - {' '.join(word_hide)}")
        word_two[index_letter] = '_'
        if word_two_clone == word_hide:
            print(f'Congratulation you win! \n Your word are {word}')
            break
    elif letter == 'quit':
        break
    else:
        attempts -= 1
        print(f'Hide word - {" ".join(word_hide)}')
        print(f'You have {attempts} trying')
        if attempts == 0:
            print('Gave over')




