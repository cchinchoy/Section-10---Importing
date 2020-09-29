# -*- coding: utf-8 -*-
"""
    Project name : Import Assignment
    File name : main.py
    Programmer : Colin B. Chin Choy
    Description: My attempt at a horse racing game - Turtle Racing
"""

import turtle
import random
from tkinter import messagebox

k = turtle.Turtle()
sc = turtle.Screen()
TRACKS = 0
DISTANCE = 600
ANGLE = 90
HEIGHT = 50
BACKGROUND = "green"
LINE_COLOR = "white"
ri = []
r = "racer "
X_DIM = 640
Y_DIM = 640
BORDER = 20
X_OFFSET = 10
Y_OFFSET = 25
X_ORIGIN_POS = 0
Y_ORIGIN_POS = 0
X_FIRST_POS = 0
Y_FIRST_POS = 0
X_FINISH_POS = 0
FIN_POS_OFFSET = 15
IS_RACING = False
R_ATTRIBS = 8
PLAYER_COLORS  = ["red","black","blue","orange","purple","pink","yellow","brown","teal"]
STILL_PLAYING = True

def startLine():
    global TRACKS
    global STILL_PLAYING
    global X_FIRST_POS
    global Y_FIRST_POS
    global X_FINISH_POS
    track_stop = (HEIGHT*TRACKS)/2
    k.ht()
    k.screen.bgcolor(BACKGROUND)
    k.penup()
    k.back((X_DIM/2)-BORDER)
    k.right(ANGLE)
    k.fd(track_stop)
    k.left(ANGLE)
    k.pendown()
    X_ORIGIN_POS = k.xcor()
    Y_ORIGIN_POS = k.ycor()
    turtle.title("Crazy Snapping Turtle Day at the Races!!! - Ver. 1.0")
    X_FIRST_POS = X_ORIGIN_POS+X_OFFSET
    Y_FIRST_POS = Y_ORIGIN_POS+Y_OFFSET
    X_FINISH_POS = X_ORIGIN_POS+DISTANCE
    STILL_PLAYING = True

def racerCount():
    global ri
    global TRACKS
    try:
        num = int(turtle.numinput("Racers","Quantity of Racers",5,minval=2,maxval=9))
        TRACKS = num
    except:
        num = 0
        TRACKS = num
        exit()
    qty_racers = TRACKS
    for i in range(qty_racers):
        ri.append([])
        for n in range(R_ATTRIBS):
            ri[i].append("")

def deployRacers(tracks):
    global X_FIRST_POS
    global Y_FIRST_POS
    global ri
    racers = TRACKS
    for i in range(racers):
        color = random.choice(PLAYER_COLORS)
        name = r+str(i)
        r_name = str(name)
        name = turtle.Turtle()
        name.shape("turtle")
        name.turtlesize(1)
        name.penup()
        name.color(color)
        name.goto(X_FIRST_POS,Y_FIRST_POS)
        n = 0
        r_shape = (str(name.shape()))
        r_size = (str(name.turtlesize()))
        r_color = (str(name.color()))
        r_pos = (str(name.pos()))
        ri[i][n] = name
        ri[i][n+1] = r_name
        ri[i][n+2] = r_shape
        ri[i][n+3] = r_size
        ri[i][n+4] = r_color
        ri[i][n+5] = r_pos
        ri[i][n+6] = str(X_FIRST_POS)
        ri[i][n+7] = str(Y_FIRST_POS)
        Y_FIRST_POS = Y_FIRST_POS+50

def buildTrack(trackcount):
    TRACKS = trackcount
    for i in range(TRACKS):
        k.forward(DISTANCE)
        k.left(ANGLE)
        k.forward(HEIGHT)
        k.left(ANGLE)
        k.forward(DISTANCE)
        k.left(ANGLE)
        k.forward(HEIGHT)
        k.penup()
        k.back(HEIGHT)
        k.left(ANGLE)
        k.pendown()
    k.ht()

def startRace(tracks):
    IS_RACING = True
    racers = tracks
    while(IS_RACING == True):
        number = random.randrange(racers)
        rname = ri[number][0]
        name = str(ri[number][1])
        rname.setx(rname.xcor()+1)
        if(rname.xcor() == X_FINISH_POS-FIN_POS_OFFSET):
            messagebox.showinfo("Winner",name+" is the Winner")
            IS_RACING = False

while STILL_PLAYING == True:
    k.screen.bgcolor(BACKGROUND)
    k.ht()
    racerCount()
    startLine()
    buildTrack(TRACKS)
    deployRacers(TRACKS)
    startRace(TRACKS)
    answer = messagebox.askyesno("Crazy Turtle","Do you want to play again")
    if answer == True:
        STILL_PLAYING = True
        k.clear()
        k.reset()
        k.ht()
        for i in range(TRACKS):
            rname = ri[i][0]
            rname.clear()
            rname.reset()
            rname.ht()
    else:
        STILL_PLAYING = False
        exit()

turtle.done()
