# -*- coding: utf-8 -*-
"""
Program allows user to move around a pokemon while specifying certain properties, 
such as how often it runs into another pokemon, essentially allowing it to 
play a simpler version of pokemon

Created on Wed Oct  9 13:44:08 2019

@author: Sayak Bagchi
"""

#to specify the coordinates a pokemon will be at next depending on several variables such as the previous position, direction, and steps it will take
#inputs: previous dimensions the pokemon was at, the direction the pokemon will move, the steps the pokemon will take
#expected return values: new dimnsions the pokemon is at
def move_pokemon(dimension, direction, steps):
    if(direction == 'n' or direction == 'N'):
        x = dimension[0] - steps
        y = dimension[1]
    elif(direction == 's' or direction == 'S'):
        x = dimension[0] + steps
        y = dimension[1]
    elif(direction == 'e' or direction == 'E'):
        x = dimension[0]
        y = dimension[1] + steps
    elif(direction == 'w' or direction == 'W'):
        x = dimension[0]
        y = dimension[1] - steps
    else:
        x = dimension[0]
        y = dimension[1]
    if(x<0):
        x = 0
    if(y<0):
        y = 0
    if(x>150):
        x = 150
    if(y>150):
        y = 150
    return (x, y)

loc = (75, 75)
turns = input("How many turns? => ")
print(turns)
name = input("What is the name of your pikachu? => ")
print(name)
freq = input("How often do we see a Pokemon (turns)? => ")
print(freq)
print("\nStarting simulation, turn 0", name, "at", loc)
record = []
no_pokemon = 0
turns = int(turns)
freq = int(freq)
battle = 0
turn = 0
while(battle < turns/freq):
    turn_before_poke = 0
    special_turn = 0
    if((0 < (turns/freq - battle) < 1) and turns>freq):
        while(special_turn < round((turns/freq - battle) * freq)):
            direc = input("What direction does " + str(name) + " walk? => ")
            print(direc)
            loc = move_pokemon(loc, direc, 5)
            special_turn += 1
        battle+=1
    else:
        while(turn_before_poke < min(turns,freq)):
            direc = input("What direction does " + str(name) + " walk? => ")
            print(direc)
            loc = move_pokemon(loc, direc, 5)
            turn+=1
            turn_before_poke += 1
        if(turn%freq==0):    
            print("Turn " + str(turn) + ", " + str(name) + " at", loc)
            poke_type = input("What type of pokemon do you meet (W)ater, (G)round? => ")
            print(poke_type)
            if(poke_type == 'W' or poke_type == 'w'):
                loc = move_pokemon(loc, direc, 1) 
                print(name + " wins and moves to", loc)
                record.append("Win")
            elif(poke_type == 'G' or poke_type == 'g'):
                if(direc == 'n' or direc == 'N'):
                    loc = move_pokemon(loc, 's', 10)
                elif(direc == 's' or direc == 'S'):
                    loc = move_pokemon(loc, 'n', 10)
                elif(direc == 'e' or direc == 'E'):
                    loc = move_pokemon(loc, 'W', 10)
                elif(direc == 'w' or direc == 'W'):
                    loc = move_pokemon(loc, 'e', 10)
                print(name + " runs away to", loc)
                record.append("Lose")
            else:
                no_pokemon+=1
                record.append("No Pokemon")
        battle+=1
print(name + " ends up at " + str(loc) + ", Record: ", record)
    
