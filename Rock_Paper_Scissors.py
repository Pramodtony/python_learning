# Rock Paper Scissors
import random
name=input("please enter your name : ")
robo=""
h_cnt=0
r_cnt=0
print("lets start the game")
trials=int(input("enter the number of rounds :"))
print("1: Rock    2: Paper    3: Scissors")
while trials>0:
    
    chosen=int(input("please enter your option: "))
    if chosen==1 :
        human="Rock"
    elif chosen==2:
        human="Paper"
    elif chosen==3:
        human="Scissors"
    else:
        print("you have entered wrong option")
    generator=random.randint(1,3)
    if generator==1:
        robo="Rock"
    elif generator==2:
        robo="Paper"
    elif generator==3:
        robo="Scissors"
    print("{} has chosen {} and robo has chosen {}".format(name,human,robo))    
    
    if human =="Rock" and robo=="Scissors":
        print("1 point for {}".format(name))
        h_cnt+=1
    elif human=="Rock" and robo=="Paper":
        print("1 point for robo")
        r_cnt+=1
    elif human =="Paper" and robo=="Rock":
        printf("1 point for {}".format(name))
        h_cnt+=1
    elif human=="Paper" and robo=="Scissors":
        print("1 point for robo")
        r_cnt+=1
    elif human =="Scissors" and robo=="Paper":
        print("1 point for {}".format(name))
        h_cnt+=1
    elif human=="Scissors" and robo=="Rock":
        print("1 point for robo")
        r_cnt+=1
    else :
        print("OOPS! Both chosen the same. Try Again")
        
    trials-=1

if h_cnt>r_cnt:
    print("winner is {} with total score {} and loser is robo with total score {}".format(name,h_cnt,r_cnt))
elif r_cnt>h_cnt:
    print("winner is robo with total score {} and loser is {} with total score {}".format(r_cnt,name,h_cnt))
else :
    print("Its a tie match")