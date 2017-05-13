from sys import exit
import random


def evil_train():
    print "This train is full of unfortune."
    print "You get on this train, then you should help me search a new world."
    
    while True:
        next = raw_input("> first(set off for the adventure) or second(turn down)\n")
        
        if next == "first":
            print "You are a warrior."
            import ex35
        elif next == "second":
            print "You are the snakes' dinner now."
            dead("You are throwed out of the train and eated by the snakes.")
        else:
            print "You don't obey my rules, you have to go back."		
    

def lucky_train():
    print "Good choice! You have the chance to get home safely."
    print "But before you get on the train, you should pay."
    print "Here you get two choices."
    print "Pay 10000 yuan or pay a random number between 0 to 20000."
    print "What's funny is that you don't have the right to chose."
    
    next = random.choice(["first", "second", "\a"])
    
    if next == "first":
        print "Good trip!"
    elif next == "second":
        fee = random.randint(0,20000)
        print "Please pay %s" % fee
        your_account(fee)
    else:
        dead("You can't get something without paying and you are eated by the snakes.")
	
	
def ghost_train():
    print "Every logger died here."
    print "Will you be the next one?"
    print "Give your nose to me or I get my snakes to kill you."
      
    
    next = raw_input("> accept or refuse\n")
	
    if next == "accept":
        print "You follow my order, so I will let you leave here."
        print "What I mean is to send you to another train."
        evil_train()
    elif next == "refuse":
        dead("I don't trade with people I dislike and you are eated by the snakes.")
    else:
        dead("You can't get somthing without paying and you are eated by the snakes.")


def dead(why):
    print why,"\nWell done!\a"
    exit(0)

	
def your_account(balance):
    money = random.randint(0,20000)
    print "My machine has discovered that you only have %d yuan." % money
    if money >= balance:
	    print "Good trip!"
    else:
        dead("You a poor man.Go to see the snakes and they will treat you.")
	

def escape():
    print "Now, you are in the amazon forest."
    print "Here are three single-direction train built by the loggers."
    print "You must take one train to get out of the forest or you die here."
	
    next = raw_input("> blue train, red train or black train \n")
    
    if next == "blue train":
        evil_train()
    elif next == "red train":
        lucky_train()
    elif next == "black train":
	    ghost_train()
    else:
	    dead("You don't obey my rule and you are eated by the snakes.")
	
	
escape()