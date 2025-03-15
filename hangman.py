from hangman_wordlist import words
import random

body_parts=['O','-','|','^']
# word=['a','l','a','s','k','a']
def display_game(body_parts):  
    print(' -------')
    print('|       |')
    print('|       |')
    for i in range(len(body_parts)):
        print(f'|       {body_parts[i]}')
    print('|       ')
    print('|       ')
    print('|       ')
    print('|       ')
    print('|       \n') 
display_game(body_parts)

def user_answer(body_parts):
    # country, capital = random.choice(list(d.items()))
    body_parts_copy=body_parts[:]
    word,description=random.choice(list(words.items()))
    word_list=list(word.lower())
    word_len=len(word)
    static_word_len=len(word)
    under_score='_'
    print('\nFind the word')
    # print(''.join(word))
    print(f'{description} The word length is {len(word)}')
    lives=4
    answer=''
    word_display=''
    while lives>=1:
        print(f'{lives} live/s remaining')
        answer=input('Letter: ').lower()
       
        if answer == word_list[0]:
            word_display+=answer
            word_len-=1
            word_list.remove(answer)
            if word_len!=0:
                print(f'Correct! {word_len} more letter/s to go!')
                print('\n')
                print(word_display.upper()+under_score*(word_len))
                print('\n')

               
                
            if word_list==[]:
                print('\n')
                print(word_display.upper()+under_score*(word_len))
                print('_'*static_word_len)
                return f'\nGreat, the word is {word.upper()}.All the letters are correct!'
            
                
        else:
            lives-=1
            body_parts_copy.pop()
            display_game(body_parts_copy) 
            if body_parts_copy!=[]:
                print('Sorry, the letter was wrong! TRY AGAIN!')
            elif body_parts_copy==[]:
                return f'OOps, you failed the game! The word is {word.upper()}\n'  
     

def main():
    game_on=True
    while game_on:
        print(user_answer(body_parts))
        user_input=''
        while True:
            user_input=input('\nDo you want to keep playing? (y/n) ').lower()
            if user_input=='y' or user_input=='n':
                break
            print('Please enter \'y\' or \'n\' ')
        if user_input=='n':
            game_on=False    
        
                
    print('\nThank you for playing...see ya!\n')        
    
       
if __name__=='__main__':
    main()    
          
