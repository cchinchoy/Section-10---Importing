"""

"""

from turtle import Turtle, Screen
from tkinter import messagebox
import random
import json

wordList=[]
alphaBet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n",
"o","p","q","r","s","t","u","v","w","x","y","z"]
wordArray=[]
BODY = {1:"buildHead()",2:"buildNeck()",3:"BuildRS()",4:"buildLS()",5:"buildTorso()",
6:"buildRC()",7:"buildLC()",8:"buildRUA()",9:"buildRLA()",10:"buildRH()",11:"buildLUA()",
12:"buildLLA()",13:"buildLH()",14:"buildRUL()",15:"buildRLL()",16:"buildRF()",
17:"buildLUL()",18:"buildLLL()",19:"buildLF()"}
LETTER_COUNT = 0
TRIED_LETTERS = []
CORRECT_LETTERS = []
FIRST_LETTER_X = 0
FIRST_LETTER_Y = 0
PLAYER_CHOICE = ""
HEAD_START_X = 0
HEAD_START_Y = 0
RT_ARM_X = 0
RT_ARM_Y = 0
LT_ARM_X = 0
LT_ARM_Y = 0
HIP_X = 0
HIP_Y = 0
GAME_STATE = "Splash"
WIN = False
IS_PLAYING = False
START_COUNTER = 1
def resetValues():
    global LETTER_COUNT
    global TRIED_LETTERS
    global CORRECT_LETTERS
    global Win
    global IS_PLAYING
    global START_COUNTER
    global PLAYER_CHOICE
    global wordArray
    LETTER_COUNT = 0
    TRIED_LETTERS = []
    CORRECT_LETTERS = []
    WIN = False
    IS_PLAYING = True
    START_COUNTER = 1
    PLAYER_CHOICE = ""
    wordArray=[]
    return
def initWordList():
    global wordList
    tempList=[]
    with open('words.json') as f_in:
        data = json.load(f_in)
    for i in data:
        tempList.append(data[i])
    for i in range(len(tempList)):
        for si in range(len(tempList[i])):
            wordList.append(tempList[i][si])
    # print(tempList)
    # print(wordList)
    # print(wordList)
def buildRope():
    global HEAD_START_X
    global HEAD_START_Y
    k.penup()
    k.left(90)
    k.fd(112)
    k.left(90)
    k.pendown()
    k.color("Yellow","Brown")
    k.begin_fill()
    k.fd(55)
    k.right(90)
    k.fd(6)
    HEAD_START_X = k.xcor()+3
    HEAD_START_Y = k.ycor()-50
    k.right(90)
    k.fd(55)
    k.right(90)
    k.fd(6)
    k.penup()
    k.ht()
    k.end_fill()
def buildBrace():
    #---------------------------------------BRACE-----------------------------------
    k.penup()
    k.bk(65)
    k.begin_fill()
    k.pendown()
    k.left(45)
    k.fd(93)
    k.left(45)
    k.fd(10)
    k.left(135)
    k.fd(107)
    k.left(135)
    k.fd(11)
    k.penup()
    k.fd(65)
    k.pendown()
    k.end_fill()
def buildArm():
    #----------------------------------------ARM------------------------------------
    k.begin_fill()
    k.fd(200)
    k.left(90)
    k.fd(15)
    k.left(90)
    k.fd(200)
    k.left(90)
    k.fd(15)
    k.end_fill()
def buildPost():
    #---------------------------------------POST-----------------------------------
    k.begin_fill()
    k.fd(350)
    k.left(90)
    k.fd(15)
    k.left(90)
    k.fd(350)
    k.left(90)
    k.fd(15)
    k.penup()
    k.left(90)
    k.fd(300)
    k.left(90)
    k.fd(15)
    k.pendown()
    k.end_fill()
def buildBase():
    #--------------------------------------BASE------------------------------------
    k.begin_fill()
    k.fd(300)
    k.left(90)
    k.fd(20)
    k.left(90)
    k.fd(300)
    k.left(90)
    k.fd(20)
    k.penup()
    k.left(90)
    k.fd(270)
    k.left(90)
    k.fd(20)
    k.pendown()
    k.end_fill()
def buildGallo():
    k.penup()
    k.home()
    k.goto(0,-200)
    k.pendown()
    k.color("red","orange")
    buildBase()
    buildPost()
    buildArm()
    buildBrace()
    buildRope()
def buildHead():
    #--------------------------------------HEAD------------------------------------
    m.penup()
    m.goto(HEAD_START_X,HEAD_START_Y)
    m.seth(0)
    m.pendown()
    m.begin_fill()
    m.circle(25)
    m.end_fill()
def buildNeck():
    #-----------------------------------------NECK----------------------------------
    m.begin_fill()
    m.rt(90)
    m.fd(10)
def buildRS():
    global RT_ARM_X
    global RT_ARM_Y
    #---------------------------RIGHT SHOULDER--------------------------------------
    m.rt(90)
    m.fd(20)
    RT_ARM_X = m.xcor()
    RT_ARM_Y = m.ycor()
    m.bk(20)
def buildLS():
    global LT_ARM_X
    global LT_ARM_Y
    #---------------------------LEFT SHOULDER--------------------------------------
    m.rt(180)
    m.fd(20)
    LT_ARM_X = m.xcor()
    LT_ARM_Y = m.ycor()
    m.bk(20)
def buildTorso():
    global HIP_X
    global HIP_Y
    #------------------------------------TORSO--------------------------------------
    m.seth(0)
    m.rt(90)
    m.fd(60)
    HIP_X = m.xcor()
    HIP_Y = m.ycor()
    m.st()
def buildRC():
    #------------------------------RIGHT CHEST--------------------------------------
    m.goto(RT_ARM_X,RT_ARM_Y)
    m.seth(0)
    m.fd(40)
def buildLC():
    #------------------------------LEFT CHEST--------------------------------------
    m.goto(HIP_X,HIP_Y)
    m.end_fill()
def buildRUA():
    #------------------------------RIGHT UPPER ARM----------------------------------
    m.setpos(RT_ARM_X,RT_ARM_Y)
    m.seth(0)
    m.rt(135)
    m.fd(20)
def buildRLA():
    #------------------------------RIGHT LOWER ARM----------------------------------
    m.lt(45)
    m.fd(20)
def buildRH():
    #------------------------------RIGHT HAND---------------------------------------
    m.rt(45)
    m.fd(5)
    m.penup()
def buildLUA():
    #------------------------------LEFT UPPER ARM----------------------------------
    m.setpos(LT_ARM_X,LT_ARM_Y)
    m.seth(0)
    m.pendown()
    m.rt(45)
    m.fd(20)
def buildLLA():
    #------------------------------RIGHT LOWER ARM----------------------------------
    m.seth(0)
    m.rt(90)
    m.fd(20)
def buildLH():
    #------------------------------RIGHT HAND---------------------------------------
    m.lt(45)
    m.fd(5)
    m.penup()
def buildRUL():
    #------------------------------RIGHT UPPER LEG----------------------------------
    m.setpos(HIP_X,HIP_Y)
    m.seth(0)
    m.pendown()
    m.rt(135)
    m.fd(30)
def buildRLL():
    #------------------------------RIGHT LOWER LEG----------------------------------
    m.lt(45)
    m.fd(30)
def buildRF():
    #------------------------------RIGHT FOOT---------------------------------------
    m.rt(45)
    m.fd(10)
    m.penup()
def buildLUL():
    #------------------------------LEFT UPPER LEG----------------------------------
    m.setpos(HIP_X,HIP_Y)
    m.seth(0)
    m.pendown()
    m.rt(45)
    m.fd(30)
def buildLLL():
    #------------------------------LEFT LOWER LEG----------------------------------
    m.rt(45)
    m.fd(30)
def buildLF():
    #------------------------------LEFT FOOT---------------------------------------
    m.lt(45)
    m.fd(10)
    m.ht()
    m.penup()
def buildMAN():
    m.color("blue","pink")
    buildHead()
    buildNeck()
    buildRS()
    buildLS()
    buildTorso()
    buildRC()
    buildLC()
    buildRUA()
    buildRLA()
    buildRH()
    buildLUA()
    buildRLA()
    buildLH()
    buildRUL()
    buildRLL()
    buildRF()
    buildLUL()
    buildLLL()
    buildLF()
def buildSplash():
    l.penup()
    l.goto(0,200)
    l.pendown()
    l.write("PY - Hangman", False, "center", font=("Arial", 48, "normal"))
    l.penup()
    l.goto(-200,100)
    l.pendown()
    l.write("2 - Player", False, "center", font=("Arial", 28, "normal"))
    l.penup()
    l.goto(-200,0)
    l.pendown()
    l.write("1 - Player", False, "center", font=("Arial", 28, "normal"))
    l.penup()
    l.goto(-200,-100)
    l.pendown()
    l.write("d - DemoPlay", False, "center", font=("Arial", 28, "normal"))
    l.penup()
    l.goto(0,-250)
    l.pendown()
    l.write("Made by VertygoEclypse", False, "center", font=("Arial", 12, "normal"))
    buildGallo()
    buildMAN()
    return
def chooseWord():
    global wordArray
    global LETTER_COUNT
    word = random.choice(wordList)
    print(word)
    wordArray = list(word)
    print(wordArray)
    LETTER_COUNT = len(wordArray)
    print(LETTER_COUNT)
    for i in range(LETTER_COUNT):
        CORRECT_LETTERS.append(" ")
    print(CORRECT_LETTERS)
def printSpaces():
    global FIRST_LETTER_X
    global FIRST_LETTER_Y
    l.penup()
    l.goto(-300,-250)
    FIRST_LETTER_X = l.xcor()+5
    FIRST_LETTER_Y = l.ycor()+2
    l.pendown()
    l.pensize(3)
    for i in range(LETTER_COUNT):
        l.pendown()
        l.fd(20)
        l.penup()
        l.fd(15)
def printLetter():
    l.penup()
    l.goto(FIRST_LETTER_X+10,FIRST_LETTER_Y)
    for i in range(len(CORRECT_LETTERS)):
        l.pendown()
        l.write(CORRECT_LETTERS[i], False, "center", font=("Arial", 16, "normal"))
        l.penup()
        l.fd(35)
def compareLetters():
    global CORRECT_LETTERS
    global PLAYER_CHOICE
    global WIN
    global IS_PLAYING
    global START_COUNTER
    good = False
    if wordArray == CORRECT_LETTERS:
        WIN = True
        IS_PLAYING = False
        checkWin()
        return
    if GAME_STATE =="Demo":
        PLAYER_CHOICE = random.choice(alphaBet)
    else:
        PLAYER_CHOICE = s.textinput("Player's Choice","Choose a letter from a-z")
    for i in range(len(wordArray)):
        if wordArray[i] == PLAYER_CHOICE:
            CORRECT_LETTERS[i] = wordArray[i]
            # PLAYER_CHOICE = " "
            printLetter()
            good = True
    if good == True:
        TRIED_LETTERS.append(PLAYER_CHOICE)
        printTried()
        return
    else:
        if i == (len(wordArray)-1):
            checkLoss()
            return
    # TRIED_LETTERS.append(PLAYER_CHOICE)
    # printTried()
def checkLoss():
    global START_COUNTER
    global TRIED_LETTERS
    global PLAYER_CHOICE
    if START_COUNTER == 1:
        buildHead()
    elif START_COUNTER == 2:
        buildNeck()
    elif START_COUNTER == 3:
        buildRS()
    elif START_COUNTER == 4:
        buildLS()
    elif START_COUNTER == 5:
        buildTorso()
    elif START_COUNTER == 6:
        buildRC()
    elif START_COUNTER == 7:
        buildLC()
    elif START_COUNTER == 8:
        buildRUA()
    elif START_COUNTER == 9:
        buildRLA()
    elif START_COUNTER == 10:
        buildRH()
    elif START_COUNTER == 11:
        buildLUA()
    elif START_COUNTER == 12:
        buildLLA()
    elif START_COUNTER == 13:
        buildLH()
    elif START_COUNTER == 14:
        buildRUL()
    elif START_COUNTER == 15:
        buildRLL()
    elif START_COUNTER == 16:
        buildRF()
    elif START_COUNTER ==17:
        buildLUL()
    elif START_COUNTER ==18:
        buildLLL()
    elif START_COUNTER == 19:
        buildLF()
        answer = messagebox.askyesnocancel("Lose","player Loses!!!, Play again")
        if answer == True:
            IS_PLAYING = True
            WIN = False
            k.clear()
            m.clear()
            l.clear()
            resetValues()
            if GAME_STATE == "Singles":
                singlePlayer()
            elif GAME_STATE == "Doubles":
                doublePlayer()
            elif GAME_STATE == "Demo":
                demoPlay()
            return
        elif answer == False:
            exit()
        else:
            exit()
    START_COUNTER += 1
    TRIED_LETTERS.append(PLAYER_CHOICE)
    printTried()
    return
def printTried():
    l.penup()
    l.goto(FIRST_LETTER_X,FIRST_LETTER_Y+300)
    l.pendown()
    for i in range(len(TRIED_LETTERS)):
        l.write(TRIED_LETTERS[i],False,"center",font=("Arial", 16, "normal"))
        l.penup()
        l.fd(15)
def singlePlayer():
    global GAME_STATE
    global WIN
    GAME_STATE = "Singles"
    IS_PLAYING = True
    k.clear()
    m.clear()
    l.clear()
    initWordList()
    chooseWord()
    buildGallo()
    printSpaces()
    while WIN == False:
        compareLetters()
    return

def doublePlayer():
    global GAME_STATE
    global WIN
    global LETTER_COUNT
    global CORRECT_LETTERS
    global wordArray
    GAME_STATE = "Doubles"
    k.clear()
    m.clear()
    l.clear()
    word = s.textinput("Player's Choice","Player enter a word in common letters only")
    # print(word)
    wordArray = list(word)
    # print(wordArray)
    LETTER_COUNT = len(wordArray)
    # print(LETTER_COUNT)
    for i in range(LETTER_COUNT):
        CORRECT_LETTERS.append(" ")
    # print(CORRECT_LETTERS)
    buildGallo()
    printSpaces()
    while WIN == False:
        compareLetters()
    return
def demoPlay():
    global GAME_STATE
    global WIN
    GAME_STATE = "Demo"
    k.clear()
    m.clear()
    l.clear()
    initWordList()
    chooseWord()
    buildGallo()
    printSpaces()
    while WIN == False:
        compareLetters()
    return
def checkWin():
    global WIN
    global IS_PLAYING
    global GAME_STATE
    if WIN == True:
        answer = messagebox.askyesnocancel("win","player wins!!!, Play again")
        print(answer)
        if answer == True:
            IS_PLAYING = True
            WIN = False
            k.clear()
            m.clear()
            l.clear()
            resetValues()
            if GAME_STATE == "Singles":
                singlePlayer()
            elif GAME_STATE == "Doubles":
                doublePlayer()
            elif GAME_STATE == "Demo":
                demoPlay()
            return
        elif answer == False:
            exit()
        else:
            exit()
k = Turtle()
m = Turtle()
l = Turtle()
s = Screen()
k.setundobuffer(1)
m.setundobuffer(1)
l.setundobuffer(1)
k.ht()
m.ht()
l.ht()
s.bgcolor("green")

buildSplash()
#Keyboard bindings
s.onkey(singlePlayer,"1")
s.onkey(doublePlayer,"2")
s.onkey(demoPlay,"d")
s.listen()
# print(IS_PLAYING)
if IS_PLAYING==True:
    compareLetters()

s.mainloop()
delay = input("Press enter to exit")
