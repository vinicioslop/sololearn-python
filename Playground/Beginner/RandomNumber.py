# Tier: 1-Beginner

# Generate a random number between a range of defined
# minimun and maximun.

# The generator allows the user to use the random property
# for purposes like games that contains some kind of lottary
# or for statistics.

# User Stories
# - User can define maximun and minimun values for the random number.
# - User can press the generate button to generate random number.

# Bonus features
# - User can add option for negative values
# - User can add option for decimal numbers

# IMPORT THE MODULE THAT HAS THE FUNCTION TO GENERATE A
# RANDOM NUMBER GIVEN THE INPUTED RANGE
import random

# PRINTS A MESSAGE OF WELCOME TO THE USER AND GIVES SOME
# INFORMATION ABOUT THE PROGRAM
print("Welcome to Random Number Generator.")
print("I'll ask you a number to start and finish :)")

# INFINTY LOOP THAT WILL STOP WHEN THE USER DECIDES TO
while True:
    # ERROR TREATMENT TO PREVENT THE PROGRAM TO STOP,
    # IN ANY SITUATION POSSIBLE
    try:
        # ASKS FOR THE USER TO INPUT A INTEGER NUMBER FOR
        # START POINT
        start = int(input("\nStart Number.: "))
        # ASKS FOR THE USER TO INPUT A INTEGER FOR FINISH
        # POINT
        finish = int(input("Finish Number: "))

        # GENERATE THE RANDOM NUMBER GIVEN THE RANGE INPUTED
        generatedNumber = random.randint(start, finish)

        # PRINTS FOR THE USER THE NUMBER THAT WAS GENERATE
        print("\nGenerated number: {}".format(str(generatedNumber)))

        # PRINTS A MESSAGE TO THE USER TO ASK IF HE/SHE WANT
        # TO STOP THE PROGRAM
        print("\nStop de generator? (Y)es or (N)o")
        # COLECT THE DECISION THAT THE USER INPUTED
        stop_point = input("Option: ")

        # CONVERT THE DECISION IN A UPPER CHARACTER
        stop_point = stop_point.upper()

        # VERIFY IF THE USER WANT TO STOP THE PROGRAM
        if stop_point == "Y":
            # IF THE CONDICION IS SATISFACTED PRINTS A MESSAGE
            # TO THE USER
            print("\nExit...")
            # INTERRUPT THE LOOP USING THE KEYWORD BREAK
            break
    # IF AN ERROR OCCURRED ENTERS THE EXCEPT
    except:
        # PRINTS A MESSAGE TO THE USER TO INFORM THAT AN
        # ERROR HAS OCCURRED
        print("\nA error has occurred. Try again...")
