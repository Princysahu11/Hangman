from random import  choice

def run_game():
    word:str = choice(['apple','kiwi','Mango','orange'])
    username:str= input('Hey!, What is your name? >> ')
    print(f'Hi! {username} welcome to hangman game')

    guessed: str =''
    tries: int = 4

    while tries>0:

        blanks:int = 0
        print('Word: ',end='')
        for char in word:
            if char in guessed:
                print(char,end ='')
            else:
                print('_',end='')
                blanks += 1

            #add a blank line
        print()
        if blanks == 0:
            print("Yeah! you get it correct")
            break

        guess:str = input('Enter a letter: ')
        if guess in guessed:
            print(f'you already chose this{guess} letter. Please try with anyother letter! ')
            continue
        guessed += guess
        if guess not in word:
            tries -= 1
            print(f' wrong choice you have only {tries} attempt remaining ')
        if tries == 0:
            print('No more tries... You lost it')
            break

if __name__ == '__main__':
    run_game()


