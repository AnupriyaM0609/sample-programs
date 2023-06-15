#TIC TAC TOE PYTHON GAME:
instruction='''
This will be our TIC TAC TOE board

  1  |  2  |  3
_ _ _|_ _ _|_ _ _
     |     |    
   4 |  5  |  6
_ _ _|_ _ _|_ _ _
     |     |     
   7 |  8  |  9    

istruction:
1.Insert the spot number(1-9) to put your sign
2.You must fill all 9 sports to get the result
3.Player 1 will go first  

'''
def tictactoe():
    sign_list=[]
    for i in range(9):
        sign_list.append(' ')
    def print_board():
        board=f''' 
    
  {sign_list[0]}  |  {sign_list[1]}  |  {sign_list[2]} 
_ _ _|_ _ _|_ _ _
     |     |    
   {sign_list[3]} |  {sign_list[4]}  |  {sign_list[5]} 
_ _ _|_ _ _|_ _ _
     |     |     
   {sign_list[6]} |  {sign_list[7]}  |  {sign_list[8]}            
             '''
        print(board)

    index_list=[]
    def get_input(player_name):
        while True:
            try:
               x=int(input(f'{player_name}:'))
               x-=1
               if 0<=x<10:
                  if x in index_list:
                    print('this spot is blocked.')
                    continue
                  index_list.append(x)
                  return x
               print('Please enter number between 1-9')
            except Exception as e :
                print('Please enter a number between 1-9')   
 
    def result(player_one,player_two):
        if sign_list[0]==sign_list[1]==sign_list[2]=='X' or sign_list[3]==sign_list[4]==sign_list[5] =='X'or sign_list[6]==sign_list[7]==sign_list[8]=='X'or sign_list[0]==sign_list[3]==sign_list[6] =='X' or sign_list[1]==sign_list[4]==sign_list[7]=='X' or sign_list[2]==sign_list[5]==sign_list[8]=='X' or sign_list[0]==sign_list[4]==sign_list[8]=='X' or sign_list[2]==sign_list[4]==sign_list[6]=='X':
            print(f'{player_one} You WON!!!')
            print ('Thank you for joining')
            return 1
        elif sign_list[0]==sign_list[1]==sign_list[2]=='O' or sign_list[3]==sign_list[4]==sign_list[5] =='O'or sign_list[6]==sign_list[7]==sign_list[8]=='O'or sign_list[0]==sign_list[3]==sign_list[6] =='O' or sign_list[1]==sign_list[4]==sign_list[7]=='O' or sign_list[2]==sign_list[5]==sign_list[8]=='O' or sign_list[0]==sign_list[4]==sign_list[8]=='O' or sign_list[2]==sign_list[4]==sign_list[6]=='O' :
            print(f'{player_two} You WON!!!')
            print ('Thank you for joining')  
            return 1 
 
    def main():
        print('Welcome to TIC TAC TIE Python Game')
        player_one=input('enter player_one name:').upper()
        player_two=input('enter player_two  name:').upper()
        print(f'Thank you for joining {player_one} and {player_two}')
        print(instruction)
        print(f'{player_one}\'s sign will be : X\n{player_two}\'s sign will be :O')
        input('enter any key to start the game:')
    
        print_board()
        count=0
        i=0
        while i<=8:
            if i%2==0:
                index=get_input(player_one)
                sign_list[index]='X'
            else:
                index=get_input(player_two)
                sign_list[index]='O'
            print_board()
            if result(player_one,player_two)==1:
                count+=1
            if count!=1 and i==8:
                print('This is a  TIE \n Thank you for joining.')
            if count==1:
                break
            i+=1   
    
    main()


tictactoe()    
print()
while True:
    print('Do you want to play again!\n     Press 1 for Yes\n     Press 2 for No')
    try:
        choice=int(input('Choice:'))
        if choice==1:
           tictactoe()
           print()
        else:
           quit('EXIT!!!\nThank you')   
    except ValueError:
        print('please enter 1 for continue or any other number to Exit')       
    
    
