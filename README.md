# Cho-han
from tkinter import *
from PIL import *

root=Tk()
root.title("CHO - HAN GAME")
root.geometry("1900x980")
img=PhotoImage(file="background.png")
label= Label(root,image=img)
label.place(relx=0, rely=0,relwidth=1,relheight=1)
head=Label(text="Chō-Han (丁半)",pady=100,font=('courier',40,"bold","underline"),bg="#141413",fg="#FFFDD0")
head.place(relx=.36,rely=0.05,relwidth=.3,relheight=.1)


#main code
import random

CHO = "cho"
HAN = "han"

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1+die2


def get_computer_choice():

    return CHO if random.randint(0, 1) == 0 else HAN

def determine_winner(player_choice, computer_choice, dice_total):
 
    is_even = dice_total % 2 == 0
    if (is_even and player_choice == CHO and computer_choice == CHO) or (not is_even and player_choice == HAN and computer_choice == HAN):
         return "Tie"
    elif (is_even and player_choice == CHO) or (not is_even and player_choice == HAN):
        return "Player"
    elif (is_even and computer_choice == CHO) or (not is_even and computer_choice == HAN):
        return "Computer"
    else:
        return ""
     
global value
value=StringVar()
value.set("cho")
Round=StringVar()
Round.set("1")

def play():
    global label9
    global border1
    
    label9=Label(text='Enter Number of rounds to play',font=("courier", 25),bg="#141413",fg="#FFFDD0")
    label9.place(relx=.32,rely=.3)
    border1 =Frame(highlightbackground = "black",highlightthickness = 4, bd=0)
    border1.place(relx=.4575,rely=.595,relwidth=.1049,relheight=.058)
    b1=Button(text="Begin",bg="purple",fg="white",font=('courier'),command=valid)
    b1.place(relx=.46,rely=.6,relwidth=.1,relheight=.05)
    global choice1
    
    
    choice1 =Entry(root,textvariable=Round,font=('courier',20),bg="#141413",fg="#FFFDD0",cursor="crosshair",bd=8,justify="center")
    choice1.place(relx=.46,rely=.4,relwidth=.1,relheight=.048)
    
    
    
def valid():
        n=Round.get()
        if(n.isnumeric()):
            global r
            r=int(n)
            play_game()
        else:
            border1 =Frame(highlightbackground = "black",highlightthickness = 4, bd=0)
            border1.place(relx=.4575,rely=.595,relwidth=.1049,relheight=.058)
            b1=Button(text="Begin",bg="purple",fg="white",font=('courier'),command=valid)
            b1.place(relx=.46,rely=.6,relwidth=.1,relheight=.05)
    
    
def play_again():
    
    label100.place_forget()
    global label9
    global choice1
    global border1
    label9=Label(text='Enter Number of rounds to play',font=("courier", 25),bg="#141413",fg="#FFFDD0")
    label9.place(relx=.32,rely=.3)
    
    border1 =Frame(highlightbackground = "black",highlightthickness = 4, bd=0)
    border1.place(relx=.4575,rely=.595,relwidth=.1049,relheight=.058)
    b1=Button(text="Begin",bg="purple",fg="white",font=('courier'),command=valid)
    b1.place(relx=.46,rely=.6,relwidth=.1,relheight=.05)
    choice1 =Entry(root,textvariable=Round,font=('courier',20),bg="#141413",fg="#FFFDD0",cursor="crosshair",bd=8,justify="center")
    choice1.place(relx=.46,rely=.42,relwidth=.1,relheight=.06)
    

def play_again1():
    
    label200.place_forget() 
    global label9
    global choice1
    global border1
    label9=Label(text='Enter Number of rounds to play',font=("courier", 25),bg="#141413",fg="#FFFDD0")
    label9.place(relx=.32,rely=.3)
    border1 =Frame(highlightbackground = "black",highlightthickness = 4, bd=0)
    border1.place(relx=.4575,rely=.595,relwidth=.1049,relheight=.058)
    b1=Button(text="Begin",bg="purple",fg="white",font=('courier'),command=valid)
    b1.place(relx=.46,rely=.6,relwidth=.1,relheight=.05) 
    choice1 =Entry(root,textvariable=Round,font=('courier',20),bg="#141413",fg="#FFFDD0",cursor="crosshair",bd=8,justify="center")
    choice1.place(relx=.46,rely=.42,relwidth=.1,relheight=.06)
    
    
def play_again2():
    
    label100.place_forget()
    label200.place_forget()
    global label9
    global choice1
    global border1
    label9=Label(text='Enter Number of rounds to play',font=("courier", 25),bg="#141413",fg="#FFFDD0")
    label9.place(relx=.32,rely=.3)
    border1 =Frame(highlightbackground = "black",highlightthickness = 4, bd=0)
    border1.place(relx=.4575,rely=.595,relwidth=.1049,relheight=.058)
    b1=Button(text="Begin",bg="purple",fg="white",font=('courier'),command=valid)
    b1.place(relx=.46,rely=.6,relwidth=.1,relheight=.05)
    choice1 =Entry(root,textvariable=Round,font=('courier',20),bg="#141413",fg="#FFFDD0",cursor="crosshair",bd=8,justify="center")
    choice1.place(relx=.46,rely=.42,relwidth=.1,relheight=.06)
    
        
player_score = 0
computer_score = 0
i=0

def play_game():
    global i
    global player_score
    global computer_score
    i=0
    player_score = 0
    computer_score = 0
    
    label9.place_forget()
    choice1.place_forget()

    
    b1.place_forget()
    border1.place_forget()
    global p
    global b
    
    p=Label(text="Player Score",font=('courier',25),bg="#141413",fg="#FFFDD0")
    p.place(relx=0.05,rely=.1)
    b=Label(text="Bot Score",font=('courier',25),bg="#141413",fg="#FFFDD0")
    b.place(relx=.82,rely=.1)
    
    global img1
    global img2
    global choice2
    global border2
    global label20
    global label21
    global label70
    
    img1=PhotoImage(file="player.png")
    label20 = Label(root,image=img1)
    label20.place(relx=.25, rely=.78,relwidth=.12,relheight=.235)
    
    img2=PhotoImage(file="bot.png")
    label21 = Label(root,image=img2)
    label21.place(relx=.668, rely=.78,relwidth=.12,relheight=.235)
  
    label3=Label(text='ROUND '+str(i+1)+' BEGINS',font=("courier", 25),bg="#141413",fg="#FFFDD0")
    label3.place(relx=.416,rely=.3)
    
    
    label70=Label(text='Pick your choice',font=("courier", 20),bg="#141413",fg="#FFFDD0")
    label70.place(relx=.425,rely=.36)
    
    choice2=OptionMenu(root,value,"cho","han")
    choice2.place(relx=.46,rely=.42,relwidth=.1,relheight=.06)
    choice2.config(font=('courier',20),bg="#141413",fg="#FFFDD0",cursor="crosshair",bd=8,justify="center")
    

    player_choice=value.get()

    def rounds():
        global i
        i=i+1
        
        global label6
        global label7
        global label4
        global label5
        global player_score
        global computer_score
        global label1
        global label2
        global label8
        
        
        
        
        if (i<=r):
            
            if(i!=1):
                label6.place_forget()
                label7.place_forget()
                label8.place_forget()
                label4.place_forget()
                label5.place_forget()
            if(i<r): 
             
             label3=Label(text='ROUND '+str(i+1)+' BEGINS',font=("courier", 25),bg="#141413",fg="#FFFDD0")
             label3.place(relx=.416,rely=.3)
             choice3=OptionMenu(root,value,"cho","han")
             choice3.place(relx=.46,rely=.42,relwidth=.1,relheight=.06)
             choice3.config(font=('courier',20),bg="#141413",fg="#FFFDD0",cursor="crosshair",bd=8,justify="center")
            if(i==r):
             label70.place_forget()
             label30=Label(text='GAME OVER',font=("courier", 25),bg="#141413",fg="#FFFDD0")
             label30.place(relx=.416,rely=.3,relwidth=.19,relheight=.05)  
             border9 =Frame(highlightbackground = "black",highlightthickness = 4, bd=0)
             border9.place(relx=.4575,rely=.595,relwidth=.1049,relheight=.058)
             b9=Button(root,text="Winner",bg="purple",fg="white",font=('courier'),command=winners)
             b9.place(relx=.46,rely=.6,relwidth=.1,relheight=.05)
        
            player_choice=value.get()
            
            label4=Label(text=player_choice,font=('courier',20),bg="#141413",fg="#FFFDD0")
            label4.place(relx=0.39,rely=.78)
            computer_choice=get_computer_choice()
            label5=Label(text=computer_choice,font=('courier',20),bg="#141413",fg="#FFFDD0")
            label5.place(relx=0.616,rely=.78)
            dice_total = roll_dice()
            winner =determine_winner(player_choice, computer_choice, dice_total)
            if winner == "Player":
                player_score += 1
                label6=Label(text=player_score,font=('courier',25),bg="#141413",fg="#FFFDD0")
                label6.place(relx=.117,rely=.17)
                label7=Label(text=computer_score,font=('courier',25),bg="#141413",fg="#FFFDD0")
                label7.place(relx=.87,rely=.17)
            elif winner == "Computer":
                computer_score += 1
                label6=Label(text=player_score,font=('courier',25),bg="#141413",fg="#FFFDD0")
                label6.place(relx=.117,rely=.17)
                label7=Label(text=computer_score,font=('courier',25),bg="#141413",fg="#FFFDD0")
                label7.place(relx=.87,rely=.17)
            elif winner=="Tie":
                computer_score += 1
                player_score +=1
                label6=Label(text=player_score,font=('courier',25),bg="#141413",fg="#FFFDD0")
                label6.place(relx=.117,rely=.17)
                label7=Label(text=computer_score,font=('courier',25),bg="#141413",fg="#FFFDD0")
                label7.place(relx=.87,rely=.17)
            else:
                label6=Label(text=player_score,font=('courier',25),bg="#141413",fg="#FFFDD0")
                label6.place(relx=.117,rely=.17)
                label7=Label(text=computer_score,font=('courier',25),bg="#141413",fg="#FFFDD0")
                label7.place(relx=.87,rely=.17)
               
            japanese_numbers = {1: 'ICHI', 2: 'NI', 3: 'SAN',4: 'SHI', 5: 'GO', 6: 'ROKU',7:'SHICHI',8:'HACHI',9:'KYU',10:'JUU',11:'JU ICHI',12:'JU NI'}
            label8=Label(text="Sum was "+japanese_numbers[dice_total]+"("+str(dice_total)+")",font=('courier',25),bg="#141413",fg="#FFFDD0")
            label8.place(relx=.385,rely=.5,relwidth=.25)
    
        
    global border4    
    border4 =Frame(highlightbackground = "black",highlightthickness = 4, bd=0)
    border4.place(relx=.4575,rely=.595,relwidth=.1049,relheight=.058)
    b4=Button(root,text="Next",bg="purple",fg="white",font=('courier'),command=rounds)
    b4.place(relx=.46,rely=.6,relwidth=.1,relheight=.05)
    
    
    
def winners():
    label6.place_forget()
    label7.place_forget()
    label20.place_forget()
    label21.place_forget()
    label4.place_forget()
    label5.place_forget()
    global img3
    global img4
    label5.place_forget()
    label8.place_forget()
    p.place_forget()
    b.place_forget()
    choice1.place_forget()
    choice2.place_forget()
    border1.place_forget()
    border4.place_forget()
    label70.place_forget()
    global label100
    global label200
    
    if player_score > computer_score:
        label9=Label(text="Winner!",font=('courier',20),bg="#141413",fg="#FFFDD0")
        label9.place(relx=.416,rely=.3,relwidth=.19,relheight=.05)
        img3=PhotoImage(file="player.png")
        label100 = Label(root,image=img3)
        label100.place(relx=.45, rely=.35,relwidth=.12,relheight=.235)
        border9 =Frame(highlightbackground = "black",highlightthickness = 4, bd=0)
        border9.place(relx=.4575,rely=.595,relwidth=.1049,relheight=.058)
        b9=Button(root,text="Play again",bg="purple",fg="white",font=('courier'),command=play_again)
        b9.place(relx=.46,rely=.6,relwidth=.1,relheight=.05)
    elif computer_score > player_score:
        label10=Label(text="Winner!",font=('courier',20),bg="#141413",fg="#FFFDD0")
        label10.place(relx=.416,rely=.3,relwidth=.19,relheight=.05)
        img4=PhotoImage(file="bot.png")
        label200 = Label(root,image=img4)
        label200.place(relx=.45, rely=.35,relwidth=.12,relheight=.235)
        border9 =Frame(highlightbackground = "black",highlightthickness = 4, bd=0)
        border9.place(relx=.4575,rely=.595,relwidth=.1049,relheight=.058)
        b9=Button(root,text="Play again",bg="purple",fg="white",font=('courier'),command=play_again1)
        b9.place(relx=.46,rely=.6,relwidth=.1,relheight=.05)
        
    else:
        label11=Label(text="Both are winners!",font=('courier',20),bg="#141413",fg="#FFFDD0")
        label11.place(relx=.416,rely=.3,relwidth=.19,relheight=.05)
        border9 =Frame(highlightbackground = "black",highlightthickness = 4, bd=0)
        border9.place(relx=.4575,rely=.595,relwidth=.1049,relheight=.058)
        b9=Button(root,text="Play again",bg="purple",fg="white",font=('courier'),command=play_again2)
        b9.place(relx=.46,rely=.6,relwidth=.1,relheight=.05)
        img3=PhotoImage(file="player.png")
        label100 = Label(root,image=img3)
        label100.place(relx=.39, rely=.35,relwidth=.12,relheight=.235)
        img4=PhotoImage(file="bot.png")
        label200 = Label(root,image=img4)
        label200.place(relx=.51, rely=.35,relwidth=.12,relheight=.235)


#start button
border1 =Frame(highlightbackground = "black",highlightthickness = 4, bd=0)
border1.place(relx=.4575,rely=.595,relwidth=.1049,relheight=.058)
b1=Button(text="Start",bg="purple",fg="white",font=('courier'),command=play)
b1.place(relx=.46,rely=.6,relwidth=.1,relheight=.05)

root.mainloop()
