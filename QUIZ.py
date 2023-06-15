import time

instructions=''' 
1.There will be five questions(MCQ).
2.Enter correct answer in given spot.
3.There will be no negative marking.
4.Total time will be 60 seconds
5.You will be shown your result at the end

'''

quiz=[{'question':'Which of the following is the correct extension of the python file?',
       'options':['A).python','B).pl','C).py','D).p'],
       'answer':'C'
       },
       {'question':'Which word is used for function in python language?',
       'options':['A)Function','B)def','C)Fun','D)define'],
       'answer':'B'
       },
       {'question':'Which of the following character is used to give single-line comments in python?',
       'options':['A)//','B)#','C)/*','D)!'],
       'answer':'B'
       },
       {'question':'Is python case sensitive when dealing with identifiers?',
       'options':['A)No','B)Yes','C)Machine dependent','D)none of the mentioned'],
       'answer':'B'
       },
       {'question':'Which type of programming does python support?',
       'options':['A)Object-oriented programming','B)Structural-oriented programming','C)Functional-oriented programming','D)all of the mentioned'],
       'answer':'D'
       }]

timer_duration=60
def display_timer(seconds):
    minutes=seconds//60
    seconds=seconds % 60
    print(f'Time remaining:{minutes:02d}:{seconds:02d}')

def start_quiz():
    score=0
    index=0
    guesses=[]
    start_time=time.time()
    end_time=int(start_time +timer_duration)
    while time.time()< end_time:
        print()
        display_timer(int(end_time-time.time()))
       
        question=quiz[index]['question']
        options=quiz[index]['options']
        print(f'\nquestion{index+1}:{question}')
        for i in options:
            print(i)
        while True:    
            answer=input('\nChoose the correct option(a,b,c,d):').upper()
            if answer=='A' or answer=='B' or answer=='C' or answer=='D':
                guesses.append(answer)  
                break
        if answer==quiz[index]['answer']:
            print('Correct')
            score+=1
        else:
            print('Incorrect')
        index+=1
        time.sleep(1)
        if index==5:
            break    
    print()
    print('Quiz finished!!!')
    print()
    print('RESULT')   
    print('___________') 
    print('Answers:C B B B D')
    print('your answers:',end=' ')
    for i in guesses:
        print(i,end=' ')
    print()
    print('___________')
    total_score=int((score/len(quiz))*100)
    print(f'Your score:{total_score}/100')
    print('Thank you for joining PYTHON QUIZ')

def main():
    print('Welcome to PYTHON QUIZ!!!')
    print()
    player=input('enter your name:').upper()
    print(f'Thank you for joining {player}')
    print(instructions)
    input('enter any key to start:')
    print()
    start_quiz()

main()
