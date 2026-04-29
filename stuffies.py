import time
import sys

def slow_print(text):
    print(text)
    time.sleep(0.5)

def start_game_paths(hours, hours_prev):
    hours = 0
    hours_prev = hours
    slow_print("OH NO!")
    slow_print("\nYou find yourself stranded in the middle of the forest due to random reasons that you don't know.")
    slow_print("\nSo then you walk because why not?")
    slow_print("\nYou stumble across like 3 totaly naturally generated paths because I need an excuse to expand this slop.")
    slow_print("\nWHICH PATH DO YOU CHOOSE?")
    slow_print("\nIs it path 'a', which leads you so deep in the forrest?")
    slow_print("Is it path 'b' which leads you to a random cave that is totaly random and naturally generated? ")
    slow_print("Is it path 'c' that is totaly naturally generated because I need more options to make my game more interactive?")
    choice_starter_path = input("So where do you choose to go(a, b, or c)? Disclaimer: all paths are useless and lead to doom...")
    if choice_starter_path.lower() == "a":
        path_a(water = False, food = False, shelter = False, alive = True, hours = 0, hours_prev = 0)
    elif choice_starter_path.lower() == "b":
        path_b(water = False, food = False, shelter = False, alive = True, hours = 0, hours_prev = 0)
    elif choice_starter_path.lower() == "c":
        path_c(water = False, food = False, shelter = False, alive = True, hours = 0, hours_prev = 0)
    else:
        print("BRO REPLY PROPERLY")
        return start_game_paths(hours = 0, hours_prev = 0)

def path_a(water, food, shelter, alive, hours, hours_prev):
    hours = hours_prev + 3
    hours_prev = hours
    slow_print("\nYou walk a long time ")
    slow_print("After walking for that long time you find a bear that can speak")
    slow_print("The bear that can speak is angry at you for no reason because that is what bears just do")
    slow_print("\nBEAR: Greetings mere human what brings you here to this humble cave and HOW DARE YOU STEP INTO THIS FORREST?")
    slow_print("\nBEAR: Oh, how rude of me.")
    slow_print("\nBEAR: ...")
    slow_print("\nBEAR: The name is bear")
    slow_print("\nYOU: Well... that is pretty obvious.")
    slow_print("\nBEAR: Well... I suppose I dont mind company...")
    slow_print("\nBEAR: Prove that you are worthy and I will let you have a place in the BearCave!")
    slow_print("\nWhat do you do?")
    slow_print("1:Do you fight the bear (higher rewards but you will probably die)?")
    slow_print("2: Do you outsmart the bear in a riddle?")
    slow_print("3: Do you politely decline and go somewhere else?")
    slow_print("4: Or do you crashout really hard for no reason in front of the bear?")
    bear_cave_starter = input("What do you do? (1, 2, 3, or 4)") #i will continue on this later once i am done with the other parts (return functions)
    if bear_cave_starter == "1":
        slow_print("\nYOU: *gets in a fighting stance*")
        slow_print("\nBEAR: Well you choose to fight...")
        slow_print("\nRIP You get KOed")
    elif bear_cave_starter == "2":
        slow_print("\nYOU: I challenge you to a RIDDLE!")
        slow_print("\nBEAR: Ooh, I love a good riddle!")
        slow_print("\nRIP The bear is smart.")
        slow_print("\nRIP You get Koed")
    elif bear_cave_starter == "3":
        slow_print("\nYOU: Thank you for the invitation but I would rather not trouble you, so I shall take my leave. Bye!")
        slow_print("\nBEAR: Goodbye! See you soon! Come visit me whenever you want!")
        slow_print("\nWhen you are leaving and waving goodbye in you end up randomly falling in this pit of totaly naturally generated lava.")
    elif bear_cave_starter == "4":
        slow_print("\nYOU: AAAAAAAAAAAAAA WHAT DO I DO WHAT SHOULD I DO TO PROVE MYSELF WORTHY AAAAAAAAAAAAAA")
        slow_print("\nBEAR: Calm down please.")
        slow_print("\nYOU: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        slow_print("\nBEAR: *sigh*")
        slow_print("\nBEAR:...")
        slow_print("\nBEAR: Fine, you can stay")
        slow_print("\nYou get killed by a random bit of naturally generated dripstone. KO you are dead.")
    else:
        start_game_paths(hours, hours_prev)

def path_b(water, food, shelter, alive, hours, hours_prev):
    hours=hours_prev + 5
    hours_prev=hours
    slow_print("So you decide to stumble across a naturally generated cave.")
    slow_print("Your minecraft instincts tell you to punch some trees and make some torches and a picaxe.")
    slow_print("Once you are done you expand the cave and gather stone.")
    slow_print("Plot twist you fall into lava because why not")
    slow_print("So You die, RIP. It sucks to be you.")
    slow_print("GAME OVER. Death is inevitable.")
    sys.exit()
def path_c(water, food, shelter, alive, hours, hours_prev):
    hours=hours_prev
    hours_prev=hours
    slow_print("You got nuked by a naturally spawning nuke. :D")
    sys.exit()

start_game_paths(hours = 0, hours_prev = 0)

