# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 18:42:15 2021
Last Updated March 30th 2023

Title: The Python Temple!

@author: Tick Magnet
"""

import os
import random
from sys import exit

"""Floor Diagram
0 = Wall
1 = Room 
2 = Stairs Up
3 = Monsters
4 = Fontain
5 = Treasure Room
6 = Stairs Down
7 = Boss Fight
"""

#initialize the first floor
v = 4
h = 3
floor_one = ([0,0,0,0,0,0,0,0],[0,0,1,1,3,6,5,0],[0,5,1,1,0,0,0,0],[0,3,0,1,0,1,4,0],[0,1,1,2,1,3,0,0],[0,0,5,1,0,1,0,0],[0,0,0,3,0,1,5,0],[0,0,0,0,0,0,0,0])
floor_one_monsters = ["Goblin","Kobold","Python"]
floor_one_weapon = ["Club","Steel Dagger","Quarterstaff"]
floor_one_armor = ["Padded","Studded Leather","Hide"]

#initialize the second floor
floor_two = ([0,0,0,0,0,0,0,0,0,0],[0,1,2,1,3,4,1,0,0,5,0],[0,1,1,0,1,5,0,1,5,0],[0,0,3,1,0,0,1,3,1,0],[0,0,1,1,0,0,1,3,1,0],[0,5,0,1,3,1,1,0,1,0],[0,5,0,1,3,1,0,1,3,0],[0,5,3,1,0,1,0,6,0,0],[0,0,1,1,0,5,0,0,1,0],[0,0,0,0,0,0,0,0,0,0])
floor_two_monsters = ["Skeleton","Ghoul","Zombie"]
floor_two_weapon = ["Spear","Handaxe","Mace"]
floor_two_armor = ["Chain Mail"," Bronze Plate","Chain Shirt"]

floor_three = ([0,0,0,0,0],[0,0,7,0,0],[0,1,5,0,0],[0,3,0,0,0],[0,5,5,5,0],[0,0,0,1,0],[0,0,1,3,0],[0,0,2,0,0],[0,0,0,0,0])
floor_three_monsters = ["Owlbear","Hobgoblin"]
floor_three_weapon = ["Longsword","Battle Axe","Warhammer"]
floor_three_armor = ["Scale Mail","Steel Plate","Ring Mail"]
python = False


def end_game():
    print(colors.GREEN + "Game End" + colors.ENDC)
    print("+" + "-"*98 + "+")
    print(player.name + " the " + player.job + " escaped the dungeon alive at level:" + str(player.lvl) + "!")
    print(player.name + " left wielding a " + player.weapon_name + " while wearing " + player.armor_name + " armor.")
    print("In total " + player.name + " found " + str(player.gold) + " pieces of gold!" )
    print("\n")
    if python != False:
        print(player.name + " slew the KING Python.")
    else:
        print("Unfortunatly " + player.name + " never entered the final chamber.")
    print("\n")
    print("Thank You for Playing!")
    print("\n")
    print("___       ___     __      ___       __          ___  ___        __        ___")
    print(" |  |__| |__     |__) \ /  |  |__| /  \ |\ |     |  |__   |\/| |__) |    |__ ")
    print(" |  |  | |___    |     |   |  |  | \__/ | \|     |  |___  |  | |    |___ |___")
    print("\n")
    print("+" + "-"*98 + "+")
    print("Enter anything to end " + player.name + "'s adventure.")
    print("+" + "-"*98 + "+")
    input(">")
    clear()
    exit()

def credit():
    print(colors.GREEN + "Credits" + colors.ENDC)
    print("+" + "-"*98 + "+")
    print(" ____ ____ ____ ____ ____ ____ ____")
    print("||C |||r |||e |||d |||i |||t |||s ||")
    print("||__|||__|||__|||__|||__|||__|||__||")
    print("|/__\|/__\|/__\|/__\|/__\|/__\|/__\|")
    print("\n")
    print("The Python Temple!")
    print("Designed and Developed by: " + colors.GREEN + "Tick Magnet" + colors.ENDC)
    print("With special thanks to, " + colors.GREEN +  "Banafsheh Rekabdar" + colors.ENDC + " for allowing me to indulge in this enjoyable project! ")
    print("\n" * 4)
    print("And to all others involved in this project, Thank You!")
    print("+" + "-"*98 + "+")
    print("When you are ready, enter anything to begin the adventure!")
    print("+" + "-"*98 + "+")
    input(">")
    clear()    
    startGame()

def tutorial():
    print(colors.GREEN + "Tutorial" + colors.ENDC)
    print("+" + "-"*98 + "+")
    print("The Python Temple is a text-based adventure game.")
    print("In order to perform an action type the corresponding letter or number and then press enter.")
    print("For instance, when moving from room to room the user could type in N for North.")
    print("This will result in the player moving into the Northern Room.")
    print("\n")
    print("Most commands will be shown in the text on the screen, but below is a comprehensive list of commands.")
    print("N,E,S,W: command directs character movement to North, East, South, and West respectively.")
    print("1,2,3,4: command selects options in a menu.")
    print("D: command activates stairs and fountains.")
    print("I: command can be used to see stats and inventory.")
    print("X: command exits the game.")
    print("\n")
    print("It is " + colors.GREEN + " HIGHLY " + colors.ENDC + " recommended to grab some scratch paper and write out a physical map as to not get lost." )
    print("And most importantly of all, have fun!")
    
    print("+" + "-"*98 + "+")
    print("When you are ready, enter in anything to begin the adventure!")
    print("+" + "-"*98 + "+")
    input(">")
    clear()    
    startGame()    
    
def lore():
    print(colors.GREEN + "Lore" + colors.ENDC)
    print("+" + "-"*98 + "+")
    print("Four hundred years ago the great Tezar Empire collapsed, leaving the swamps of Amphibula lawless and barren.")
    print("As time marched on the monuments of this long-gone era were slowly reclaimed by nature, and the Tezar's legacy fell into myth and legend.")
    print("Now the age of discovery races to connect every land and unearth every treasure.")    
    print("Young adventures seeking glory or wealth prepare to explore the heart of Amphibula and the depths of the Python Temple.")
    print("\n")
    print("Will you be the one to survive the ...")
    print("~~|~~|      _   ___      |  |             ")
    print("  |  |/~\  /_  |__/\  / ~|~ |/~\ /~\|/~\  ")
    print("  |  |  | /_   |    \/   |  |  | \_/|  |  ")
    print("                   _/                     ")
    print("      ~~|~~  _              |    _        ")
    print("        |  /_ |/~\ /~\ |~~\ |  /_         ")
    print("        | /_  |   |  | |__/ | /_          ")
    print("                       |                  ")
    print("+" + "-"*98 + "+")
    print("Enter anything to begin; if you dare!")
    print("+" + "-"*98 + "+")
    input(">")
    clear()    
    startGame()  
    
def clear(): 
    os.system('cls')
 
class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class player:
    
    name = "Gordon" 
    job = "na"
    
    lvl = 1
    lvl_bar = 0
    
    gold = 100
    
    hp = 0
    max_hp = 0
    
    stg = 0
    
    armor = 0
    armor_name = ""
    
    weapon = 0
    weapon_name = ""
       
def stats():
    
    print(colors.GREEN + "Name: " + player.name + "'s Stats" + colors.ENDC)
    print("+" + "-"*98 + "+")
    print("Class: " + str(player.job)) 
    print("Level: " + str(player.lvl))
    print("Exp: " + str(player.lvl_bar))
    print("Gold: " + str(player.gold))  
    print("Maxiumum Health: " + str(player.max_hp))  
    print("Current Health: " + str(player.hp))  
    print("Strength: " + str(player.stg))
    print("Armor Type: " + str(player.armor_name))
    print("Armor Strength: " + str(player.armor))
    print("Weapon Type: " + str(player.weapon_name))
    print("Weapon Strength: " + str(player.weapon))
    
    print("\n" * 3)
    
    print("+" + "-"*98 + "+")
    print("Enter anything to continue.")
    print("+" + "-"*98 + "+")
    input(">")
    clear()

def victory(enemy_name,reward,exp):
    print(colors.GREEN + "Victory Screen" + colors.ENDC)
    print("+" + "-"*98 + "+")
    print("V)    vv I)iiii   C)ccc  T)tttttt  O)oooo  R)rrrrr  Y)    yy !!!")
    print("V)    vv   I)    C)   cc    T)    O)    oo R)    rr  Y)  yy  !!!")
    print("V)    vv   I)   C)          T)    O)    oo R)  rrr    Y)yy   !!!")
    print(" V)  vv    I)   C)          T)    O)    oo R) rr       Y)    !!!")
    print("  V)vv     I)    C)   cc    T)    O)    oo R)   rr     Y)       ")
    print("   V)    I)iiii   C)ccc     T)     O)oooo  R)    rr    Y)    !!!")
    print("\n")
    print(player.name + " defeated the "+ enemy_name + ", and found " + str(reward) + " gold!")
    player.gold += reward
    print(player.name + " gained " + str(exp) + " exp!")
    player.lvl_bar += exp
    if (player.lvl_bar > 1000):
        player.lvl += 1
        player.lvl_bar -= 1000
        player.stg += 1
        player.max_hp += 10
        player.hp = player.max_hp
        print(player.name + " Leveled Up: " + str(player.lvl) )
        print("\n" * 5)
    else:
        print("\n" * 6)
    
    print("+" + "-"*98 + "+")
    print("Enter anything to continue.")
    print("+" + "-"*98 + "+")
    input(">")
    clear()
 
def defeat(enemy_name):
    print(colors.GREEN + "Defeat Screen" + colors.ENDC)
    print("+" + "-"*98 + "+")
    print(" ______  _______ _______ _______ _______ _______")
    print(" |     \ |______ |______ |______ |_____|    |   ")
    print(" |_____/ |______ |       |______ |     |    |   ")
    print("\n")
    print("Unfortunately," + player.name + " was slain by a "+ enemy_name + " while exploring the Python Temple.")
    print(player.name + " the " + player.job + " failed to leave the dungeon alive at level: " + str(player.lvl) + ".")
    print(player.name + "'s remains left wielding a " + player.weapon_name + " while wearing " + player.armor_name + " armor.")
    print("In total " + player.name + " had found " + str(player.gold) + " pieces of gold." )
    print("\n")
    print(" +-+-+-+-+ +-+-+ +-+-+-+-+-+")
    print(" |R|e|s|t| |i|n| |P|e|a|c|e|")
    print(" +-+-+-+-+ +-+-+ +-+-+-+-+-+")
    print("\n")
    print("+" + "-"*98 + "+")
    print("Say your last good by to abruptly end " + player.name + "'s adventure.")
    print("+" + "-"*98 + "+")
    input(">")
    clear()   
    exit()
    
def attack(enemy_hp,enemy_name,enemy_stg):
    
    #Combat Calculations
    damage = round((player.stg * player.weapon))
    enemy_hp = enemy_hp - damage
    
    bottom = enemy_stg * player.armor
    dmg = random.randint(int(bottom),int(enemy_stg))
    player.hp -= dmg
    
    print(colors.GREEN + "Combat" + colors.ENDC)
    print("+" + "-"*98 + "+")
    print(player.name + " quickly attacked the " + enemy_name + " doing a heafty " + str(damage) +" damage!" )
    print("\n")
    print("In retaliation the " + enemy_name + " strikes back doing " + str(dmg) + " damage!")
    
    print("\n" * 2)
    print("  0    \o ")
    print(" /0--- :\ ")
    print("/ >   / > ")
    print("\n" * 2)
    print("Who will be victorious?")
    print("Only time shall tell.")
    print("\n")
    
    print("+" + "-"*98 + "+")
    print("Enter anything to continue.")
    print("+" + "-"*98 + "+")
    input(">")
    clear()
    
    if player.hp <= 0:
        defeat(enemy_name)
    elif enemy_hp > 0:
        combat(enemy_hp,enemy_name,enemy_stg)     
    else:
        reward = enemy_stg * random.randint(10,30)
        exp = enemy_stg * random.randint(50,150)
        victory(enemy_name,reward,exp)

def combat(enemy_hp,enemy_name,enemy_stg):
    
    
    print(colors.GREEN + "Battle" + colors.ENDC)
    print("+" + "-"*98 + "+")
    print("\n")
    print("Not long after " + player.name + " entered the room a " + enemy_name + " sprung from the shadows.")
    print("The " + enemy_name + " immediately attacks " + player.name + "!")
    print("What shall " + player.name + " do?")
    print("\n")
    
    print("The " + enemy_name + " has " + str(enemy_hp) + " hp remaining!")
    print("While " +  player.name + " has " + str(player.hp) + " hp remaining!")
    print("\n" * 5)
    
    print("+" + "-"*98 + "+")
    print("What will " + player.name + " do?")
    print("+" + "-"*98 + "+")
    print("[" + colors.GREEN + "1" + colors.ENDC + "] Melee the " + enemy_name)
    print("[" + colors.GREEN + "2" + colors.ENDC + "] Check Stats" )
    print("[" + colors.RED + "3" + colors.ENDC + "] Run Away!" )
    action = input(">")

    if action == '1':
        clear()
        attack(enemy_hp,enemy_name,enemy_stg)
    elif action == '3':
        clear()
        end_game()
    elif action == '2':
        clear()
        stats()
        combat(enemy_hp,enemy_name,enemy_stg)
    else:
        print("Incorrect Input")
        clear()
        combat(enemy_hp,enemy_name,enemy_stg)
    
def game(v,h,current_floor):
    
    #Initialize The Mini-Map
    if current_floor == 1: 
        north = floor_one [v-1][h]
        east = floor_one [v][h+1]
        south = floor_one [v+1][h]
        west = floor_one [v][h-1]
        current = floor_one[v][h]
    elif current_floor == 2:
        north = floor_two [v-1][h]
        east = floor_two [v][h+1]
        south = floor_two [v+1][h]
        west = floor_two [v][h-1]
        current = floor_two[v][h]
    elif current_floor == 3:
        north = floor_three [v-1][h]
        east = floor_three [v][h+1]
        south = floor_three [v+1][h]
        west = floor_three [v][h-1]
        current = floor_three [v][h]
        
    #Begin Combat
    if (current == 3):
        if (current_floor == 1):
            enemy_name = random.choice(floor_one_monsters)
            enemy_hp = random.randint(10,30)
            enemy_stg = random.randint(2,5)
            floor_one[v][h] = 1
            combat(enemy_hp,enemy_name,enemy_stg)
        elif (current_floor == 2):
            enemy_name = random.choice(floor_two_monsters)
            enemy_hp = random.randint(25,50)
            enemy_stg = random.randint(6,10)
            floor_two[v][h] = 1
            combat(enemy_hp,enemy_name,enemy_stg)
        elif (current_floor == 3):
            enemy_name = random.choice(floor_three_monsters)
            enemy_hp = random.randint(50,100)
            enemy_stg = random.randint(12,18)
            floor_three[v][h] = 1
            combat(enemy_hp,enemy_name,enemy_stg)
    
    options = "("
    directions = 0
    if north != 0:
        options += "N,"
        directions = directions + 1
    if east != 0:
        options += "E,"
        directions = directions + 1
    if south != 0:
        options += "S,"
        directions = directions + 1
    if west != 0:
        options += "W,"
        directions = directions + 1
    options = options[:-1]
    options += ")"
        
    
    if (current_floor == 1):
        print(colors.GREEN +"Floor One: Scavenger Ruins"+ colors.ENDC )        
    elif (current_floor == 2):
        print(colors.GREEN +"Floor Two: Desolate Crypt"+ colors.ENDC ) 
    elif (current_floor == 3): 
        print(colors.GREEN +"Floor Three: The Python Shrine"+ colors.ENDC ) 
    print("+" + "-"*98 + "+")
    
    
    #ROOMS
    
    #Empty Room
    if (current == 1): 
        print("Illuminated only by the torch in " + player.name + "'s hand, the full chamber comes into view.")
        print("After careful observation " + player.name + " concludes that the room is,")
        print("dank, dark, and uneventful.")
        if (directions > 1):
            print("Looking around " + player.name + " sees hallways leading in " + str(directions) + " seperate directions." )
        else:
            print("After carefully searching the room " + player.name + " only sees one way back out.")
        print("\n" * 7)
     
    #Stairs Assending
    elif (current == 2):
        print("The stairwell " + player.name + " used to enter this floor protrudes from the ceiling. ")
        print("Besides said stairwell nothing else of note can be found in this chamber.")
        print("Does " + player.name + " wish to assend the stairs? (D) ")
        if (current_floor == 1):
            print(colors.RED + "Warning" + colors.ENDC + " (Doing so on this floor will end " + player.name + "'s campaign!)")
            print("\n" * 7)
        else:
            print("\n" * 8)
            
    #Stairs Desending    
    elif (current == 6):
        print("Entering into the chamber " + player.name + " quickly notices the central feature of the room.")
        print('A stairwell that desending deeper into the dungeon.')
        print("Does " + player.name + " dare to delve deeper? (D) ")
        print("\n" * 8)
        
    #Fountain Room
    elif (current == 4):   
        print("Before" + player.name + " even exits the hallway the sound of water could be heard.")
        print('A majestic fountain in the shape of a python dominates the room.')
        print("the water seems to emanate a faint light.")
        print("Will " + player.name + " donate 50 Gold to the fontain? (D) ")
        print("\n" * 7)
    
    #
    elif (current == 7):
        print(player.name + " enters into the final chamber.")
        print('A Massive King Python lies upon a pile of gold.')
        print("Does " + player.name + " have what it takes to defeat it? ")
        print("\n")
        print("   _________         _________              ")
        print("  /         \       /         \             ")
        print(" /  /~~~~~\  \     /  /~~~~~\  \            ")
        print(" |  |     |  |     |  |     |  |            ")
        print(" |  |     |  |     |  |     |  |         /  ")
        print(" |  |     |  |     |  |     |  |       //   ")
        print("(o  o)    \  \_____/  /     \  \_____/ /    ")
        print(" \__/      \         /       \        /     ")
        print("  |         ~~~~~~~~~         ~~~~~~~~      ")
        print("  ^                                         ")
        enemy_name = "The KING Python"
        enemy_hp = 150
        enemy_stg = 20
        
        
        
        print("+" + "-"*98 + "+")
        print("Enter anything to begin the final battle!")
        print("+" + "-"*98 + "+")
        input(">")
        clear()
        combat(enemy_hp,enemy_name,enemy_stg)
        global python
        python = True
        end_game()
    
    #Treasure Room
    elif (current == 5):
        
   
        a = random.randint(1,4)
        if a == 1:  
            print("Walking in " + player.name + " immediately notices the glint of gold resting apon a decaying table.")
            new_gold = random.randint(50,100)
            
            print("The loot to a staggering " + str(new_gold) + " gold!")
            
            player.gold += new_gold
            print("That brings " + player.name + "'s total gold too: " + str(player.gold))
            
            if current_floor == 1:
                floor_one[v][h] = 1
            elif current_floor == 2:
                floor_two[v][h] = 1
            elif current_floor == 3:
                floor_three[v][h] = 1
                
            print("\n" * 8)
        elif a == 2:
            print(player.name + " explores the cluttered chamber finding a potion of exp on the shelf.")
            player.lvl_bar += random.randint(100,400)
            print(player.name + " the preseds to gulp it down bring exp to: " + str(player.lvl_bar))
            
            if current_floor == 1:
                floor_one[v][h] = 1
            elif current_floor == 2:
                floor_two[v][h] = 1
            elif current_floor == 3:
                floor_three[v][h] = 1
        
            print("\n" * 9)
        elif a == 3:
            if current_floor == 1:
                new = random.choice(floor_one_weapon)
            elif current_floor == 2:
                new = random.choice(floor_two_weapon)
            elif current_floor == 3:
                new = random.choice(floor_three_weapon)
                
            print("Walking in " + player.name + " notices the corpse of a former adventurer.")
            print("Looting the body " + player.name + " equips a " + new)
            player.weapon_name = new
            player.weapon += 0.2
            
            if current_floor == 1:
                floor_one[v][h] = 1
            elif current_floor == 2:
                floor_two[v][h] = 1
            elif current_floor == 3:
                floor_three[v][h] = 1
            print("\n" * 9)
            
        elif a == 4:
            if current_floor == 1:
                new = random.choice(floor_one_armor)
            elif current_floor == 2:
                new = random.choice(floor_two_armor)
            elif current_floor == 3:
                new = random.choice(floor_three_armor)
            print("Walking in " + player.name + " notices the corpse of a former adventurer.")
            print("Looting the body " + player.name + " equips a " + new)
            player.armor_name = new
            player.armor -= 0.2
            
            if current_floor == 1:
                floor_one[v][h] = 1
            elif current_floor == 2:
                floor_two[v][h] = 1
            elif current_floor == 3:
                floor_three[v][h] = 1
            print("\n" * 9)
    
    
    
    #Defeated Enemy
    else:
        print(player.name + " now stands alone hulking over the now slain enemy.")
        if (directions > 1):
            print("Looking around " + player.name + " sees hallways leading in " + str(directions) + " seperate directions." )
        else:
            print("After carefully searching the room " + player.name + " only sees one way back out.")
        print("\n" * 9)
        
    print("  " + str(north))
    print(str(west) + " " + colors.GREEN + str(current) + colors.ENDC + " " + str(east))
    print("  " + str(south))
    
    print("+" + "-"*98 + "+")
    print("What path shall " + player.name + " take? " + options)
    print("+" + "-"*98 + "+")
    path = input(">")
    
    if 'N' in options and (path == 'N' or path == 'n'):
        v = v-1
        clear()
        game(v,h,current_floor)
    elif 'E' in options and (path == 'E' or path == 'e'):
        h = h+1
        clear()
        game(v,h,current_floor)
    elif 'S' in options and (path == 'S' or path == 's'):
        v = v+1
        clear()
        game(v,h,current_floor)    
    elif 'W' in options and (path == 'W' or path == 'w'):
        h = h-1
        clear()
        game(v,h,current_floor)
    elif path == 'I' or path == 'i':
        clear()
        stats()
        game(v,h,current_floor)
    elif path == 'X' or path == 'x':
        clear()
        exit()
        
    #Delve Deeper    
    elif current == 6 and (path == 'D' or path == 'd'):
        clear()
        if (current_floor == 1):
            v = 1
            h = 2
            current_floor += 1
            
            print("Delving Deeper: " + player.name)
            print("+" + "-"*98 + "+")
            print(player.name + " takes one tentative step at a time down the stairwell.")
            
            print("\n" * 3)
        
            print("▄▄▀█▄───▄───────▄")
            print("▀▀▀██──███─────███")
            print("░▄██▀░█████░░░█████░░")
            print("███▀▄███░███░███░███░▄")
            print("▀█████▀░░░▀███▀░░░▀██▀")
            
            print("\n" * 2)
            
            print("+" + "-"*98 + "+")
            print("Enter anything to continue.")
            print("+" + "-"*98 + "+")
            input(">")
            clear()
            game(v,h,current_floor)
            
        elif(current_floor == 2):
            v = 7
            h = 2
            current_floor += 1
            
            print("Delving Deeper: ")
            print("+" + "-"*98 + "+")
            print(player.name + " takes one tentative step at a time down the stairwell.")
            
            print("\n" * 3)
        
            print("▄▄▀█▄───▄───────▄")
            print("▀▀▀██──███─────███")
            print("░▄██▀░█████░░░█████░░")
            print("███▀▄███░███░███░███░▄")
            print("▀█████▀░░░▀███▀░░░▀██▀")
            
            print("\n" * 2)
            
            print("+" + "-"*98 + "+")
            print("Enter anything to continue.")
            print("+" + "-"*98 + "+")
            input(">")
            clear()
            game(v,h,current_floor)
            
        else:
            game(v,h,current_floor)
    
    #Donating to the Fontain
    elif current == 4 and player.gold >= 50 and (path == 'D' or path == 'd'):
        clear()
        player.gold -= 50
        player.hp += 5
        print("Healing: ")
        print("+" + "-"*98 + "+")
        print(player.name + " donates 50 gold pieces and walks away feeling lighter.")
        
        print("\n")
        print("       ('     ")
        print("      `),     ")
        print("  ____/\____  ")
        print(" !_________!  ")
        print("   \_____/    ")
        print("    !___!     ")
        print("     | |      ")
        print("    _!_!_     ")
        print("  /_______\   ")
        print("\n" * 2)
            
        print("+" + "-"*98 + "+")
        print("Enter anything to continue.")
        print("+" + "-"*98 + "+")
        input(">")
        clear()
        game(v,h,current_floor)
        
    #Assending Higher
    elif current == 2 and (path == 'D' or path == 'd'):
        clear()
        if (current_floor == 1):
            end_game()
            
        elif (current_floor == 2):
            v = 1
            h = 5
            current_floor -= 1
            
            print("Assending Higher: ")
            print("+" + "-"*98 + "+")
            print(player.name + " returns to the first floor.")
            print("\n" * 3)
        
            print(" ▄▄▀█▄───▄───────▄")
            print(" ▀▀▀██──███─────███")
            print(" ░▄██▀░█████░░░█████░░")
            print(" ███▀▄███░███░███░███░▄")
            print(" ▀█████▀░░░▀███▀░░░▀██▀")
            
            print("\n" * 2)
            
            print("+" + "-"*98 + "+")
            print("Enter anything to continue.")
            print("+" + "-"*98 + "+")
            input(">")
            clear()
            game(v,h,current_floor)
        elif(current_floor == 3):
            v = 7
            h = 7
            current_floor -= 1
            
            print("Assending Higher: ")
            print("+" + "-"*98 + "+")
            print(player.name + " returns to the second floor.")
            print("\n" * 3)
        
            print("▄▄▀█▄───▄───────▄")
            print("▀▀▀██──███─────███")
            print("░▄██▀░█████░░░█████░░")
            print("███▀▄███░███░███░███░▄")
            print("▀█████▀░░░▀███▀░░░▀██▀")
            
            print("\n" * 2)
            
            print("+" + "-"*98 + "+")
            print("Enter anything to continue.")
            print("+" + "-"*98 + "+")
            input(">")
            clear()
            game(v,h,current_floor)
        else:
            game(v,h,current_floor)
            
    else:
        print("Invalid Input:")
        input(">")
        clear()
        game(v,h,current_floor)
     
def newGame():

    print(colors.GREEN + "Character Creation Step: 1/2" + colors.ENDC)
    print("+" + "-"*98 + "+")
    print("\n")
    print("Old Man: Ahh, you're finally awake. ")
    print("Old Man: I was out on my morning stroll and found you passed out along the swamp bank. ")
    print("Old Man: So I decided to drag you back to my humble abode.")
    print("Old Man: You know I've been waiting for someone like you to come along.")
    print(colors.YELLOW + "The Old Man brandishes a crusty-looking piece of parchment." + colors.ENDC)
    print("Old Man: This is a map to the mythical "+ colors.GREEN + "Python Temple." + colors.ENDC)
    print("Old Man: Legend has it that the dungeon is brimming with" + colors.GREEN + "treasure" + colors.ENDC + "and crawling with" + colors.RED +  " monsters." + colors.ENDC)
    print(colors.YELLOW + "Puffing his chest out the Old Man continues." + colors.ENDC)
    print("Old Man: I'd go and find out myself, but alas, my glory days are far behind me.")
    print("Old Man: So I say the chance of a lifetime is yours.")
    print("Old Man: If your willing to fall asleep in a swamp you have nothing better to do then chase down fairy tales.")
    print(colors.YELLOW + "The Old Man thrusts the map into your hands." + colors.ENDC)
    print("Old Man: All I want in return is to know your name.")
    print("\n" * 2)
    print("+" + "-"*98 + "+")
    print("Please print your character's name.")
    print("+" + "-"*98 + "+")
    name = input(">")
    
    if (name != ""):
        player.name = name
    else:
        clear()
        newGame()
        
    print(player.name + " accepts the man and begins to leave.")
    print("Old Man: Wonderful!")
    print("Old Man: Now don't forget to come back and tell me all about your adventure.")
    print("Press any button to continue.")
    input(">")
    clear()
    
    print(colors.GREEN + "Character Creation Step: 2/2" + colors.ENDC)
    print("+" + "-"*98 + "+")
    print("The map is crude, to say the least, resulting in " + player.name + " to get turrned around on multiple occasions.")
    print("Eventually, after fording a handful of rivers, surviving the elements, ")
    print("and fighting off the natural fauna " + player.name + " makes it to the " + colors.RED + "X." + colors.ENDC)
    print("Standing before " + player.name + " at the very heart of Amphibula's swamp stands the very real Python Temple." )
    print("\n")
    print("Even after hundreds of years of neglect and decay, the temple is still awe-inspiring.")
    print("\n")
    print(player.name + " stands before the mouth of the dungeon, and in a quick moment of self-reflection thinks about the past.")
    print("Before delving straight into the depths.")
    print(" _   /\  _  ")
    print("[_]--'--[_] ")
    print("|'|""`""\ \ ")
    print("| | /^\ | | ")
    print("|_|_|I|_|_| ")
    print("\n")
    print("+" + "-"*98 + "+")
    print("Please select " + player.name + "'s Class.")
    print("+" + "-"*98 + "+")
    print("[" + colors.GREEN + "1" + colors.ENDC + "] Fighter")
    print("[" + colors.GREEN + "2" + colors.ENDC + "] Barbarian")
    print("[" + colors.GREEN + "3" + colors.ENDC + "] Rogue")
    print("[" + colors.GREEN + "4" + colors.ENDC + "] Paladin")
    print("[" + colors.GREEN + "5" + colors.ENDC + "] Janitor")
 
    enter = input(">")
    
    if enter == '1':
        player.job = "Fighter"
        player.weapon = 1.2
        player.weapon_name = "Bronze Short-Sword"
        player.armor = 0.8
        player.armor_name = "Bronze"
        player.stg = 6
        player.max_hp = 40
        player.hp = 40
        player.gold = 100
        print(player.job)
    elif enter == '2':
        player.job = "Barbarian"
        player.weapon = 1.5
        player.weapon_name = "Bronze Long-Sword"
        player.armor = 1
        player.armor_name = "Leather"
        player.stg = 10
        player.max_hp = 20
        player.hp = 20 
        player.gold = 50
        print(player.job)
    elif enter == '3':
        player.job = "Rogue"
        player.weapon = 1.3
        player.weapon_name = "Bronze Short-Sword"
        player.armor = 0.9
        player.armor_name = "Leather"
        player.stg = 5
        player.max_hp = 30
        player.hp = 30
        player.gold = 500
        print(player.job)    
    elif enter == '4':
        player.job = "Paladin"
        player.weapon = 1
        player.weapon_name = "Morning-Star"
        player.armor = 0.8
        player.armor_name = "Bronze Plate"
        player.stg = 6
        player.max_hp = 50
        player.hp = 50
        player.gold = 400
        print(player.job)
    elif enter == '5':
        player.job = "Janitor"
        player.weapon = 0.2
        player.weapon_name = "Mop"
        player.armor = 1
        player.armor_name = "Overalls"
        player.stg = 1
        player.max_hp = 1
        player.hp = 1
        player.gold = -1000
    else:
        clear()
        newGame()
        
    if player.job == "Janitor" and player.name == "qwerty":
        player.job = "Janitor"
        player.weapon = 10
        player.weapon_name = "Mop"
        player.armor = 0
        player.armor_name = "Overalls"
        player.stg = 100
        player.max_hp = 1000
        player.hp = 1000
        player.gold = 0
    clear()
    
    current_floor = 1
    game(v,h,current_floor)
  
def startGame():
    
    clear()
    print(colors.GREEN + "Tick Magnet Proudly Presents:" + colors.ENDC )
    print("+" + "-"*98 + "+")
    print("\n")
    print(" ████████╗██╗  ██╗███████╗    ██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗    ")
    print(" ╚══██╔══╝██║  ██║██╔════╝    ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║    ")
    print("    ██║   ███████║█████╗      ██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║    ")
    print("    ██║   ██╔══██║██╔══╝      ██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║    ")
    print("    ██║   ██║  ██║███████╗    ██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║    ")
    print("    ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ") 
    print("\n")
    print("              ████████╗███████╗███╗   ███╗██████╗ ██╗     ███████╗                     ")
    print("              ╚══██╔══╝██╔════╝████╗ ████║██╔══██╗██║     ██╔════╝                     ")
    print("                 ██║   █████╗  ██╔████╔██║██████╔╝██║     █████╗                       ")
    print("                 ██║   ██╔══╝  ██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝                       ")
    print("                 ██║   ███████╗██║ ╚═╝ ██║██║     ███████╗███████╗                     ")
    print("                 ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝                     ")
    print("Release Build: 0.0.2")
    print("+" + "-"*98 + "+")
    print("[" + colors.GREEN + "1" + colors.ENDC + "] New Game")
    print("[" + colors.GREEN + "2" + colors.ENDC + "] Credits")
    print("[" + colors.GREEN + "3" + colors.ENDC + "] How to Play")
    print("[" + colors.GREEN + "4" + colors.ENDC + "] Lore Summary")
    print("\n")
    print("[" + colors.RED + "X" + colors.ENDC + "] Exit")
    print("+" + "-"*98 + "+")
    enter = input(">")
    
    clear() 
    if enter == '1':
        newGame()
    elif enter == '2':
        credit()
    elif enter == '3':
        tutorial()
    elif enter == '4':
        lore()
    elif enter == 'X' or enter == 'x':
        clear()
        exit()
    else:
        startGame()

startGame()