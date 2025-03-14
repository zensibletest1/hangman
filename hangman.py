body_parts=['O','-','|','^']
word=['a','l','a','s','k','a']
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
    print('|       ') 
display_game(body_parts)

def user_answer(body_parts):
    print('\nFind the word')
    # print(''.join(word))
    print('A state in United States')
    lives=4
    answer=''
    while lives>=1:
        print(f'{lives} live/s remaining')
        answer=input('Letter: ')
       
        if answer in word:
            word.remove(answer)
            if word==[]:
                return 'Great, all the letters are correct!'
            
                
        else:
            lives-=1
            body_parts.pop()
            display_game(body_parts) 
            if body_parts==[]:
                return 'OOps, you failed the game!'  
     

def main():
    print(user_answer(body_parts))
       
if __name__=='__main__':
    main()    
          
 
     


 
        