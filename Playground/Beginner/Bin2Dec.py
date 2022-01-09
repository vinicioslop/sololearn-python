# Tier: 1-Beginner

# Binary is the number system all digital computers are based on.
# Therefore it's important for developers to understand binary,
# or base 2, mathematics. The purpose of Bin2Dec is to provide
# practice and understanding of how binary calculations.

# Bin2Dec allows the user to enter strings of up to 8 binary digits,
# 0's and 1's, in any sequence and then displays its decimal equivalent.
#
# This challenge requires that the developer implementing it follow
# these constraints:

#     Arrays may not be used to contain the binary digits entered by
#     the user
#     Determining the decimal equivalent of a particular binary digit
#     in the sequence must be calculated using a single mathematical function,
#     for example the natural logarithm. It's up to you to figure out which
#     function to use.

# FUNCTION THAT EVALUATES THE DECIMAL EQUIVALENT OF THE BINARY
# SEQUENCE, RECEIVING A VALID SEQUENCE AS PARAMETER
def bin2dec(binInput):
    # VARIABLE THAT STORES THE LENGHT OF THE SEQUENCE
    limit = len(binInput)
    # VARIABLE THAT WILL STORE THE DECIMAL CALCULATED, STARTING WITH 0
    decimal = 0

    # LOOP FOR THAT WALKS THROUGH THE ENTIRE SEQUENCE
    for i in range(limit):
        # COLECT THE DIGIT, STARTING WITH THE LAST DIGIT
        #   AND DECRESING DURING THIS EXECUTION
        # CONVERT IT TO INTEGER
        # AND MULTIPLIES IT BY 2^ACTUAL_POSITION
        # WITH THE VALUE CALCULATED SUMS IT TO THE VARIABLE
        decimal += int(binInput[limit - 1 - i]) * (2**i)

    # PRINTS THE MESSAGE THAT SHOWS ITS ENTRANCE VALUE AND YOUR
    # DECIMAL EQUIVALENT
    print("Binary {0} is equal than {1} in decimal!".format(
        binInput, str(decimal)))

print("Welcome to the Binary to Decimal Converter!")

# ASKS HOW MUCH DIGITS THE USER WANTS TO INPUT
limit = int(input("INPUT THE NUMBER OF DIGITS THAT WILL WANT TO EVALUATE: "))

# ASK TO USER INPUT A VALID BINARY DIGIT OF 8 DIGITS
binInput = input("Input a binary number of {} digits: ".format(limit))

# VERIFY IF THE BINARY DIGIT INPUTED CONTAINS 8 DIGITS
if len(binInput) == limit:
    # CREATE A VARIABLE THAT WILL BE USED TO VALIDATE THE DIGITS
    # INSIDE THE VARIABLE, STARTING WITH TRUE
    valid = True

    # LOOP FOR THAT WALKS THROUGH THE VARIABLE, TAKING THE DIGITS
    # AND STORING IN A VARIABLE
    for bin in binInput:
        # VERIFY IF THE DIGIT IS DIFFERENT TO THE ONLY
        # TWO VALID DIGITS (0, 1)
        # IF IS NOT CHANGES THE VALUE OF THE VARIABLE valid TO
        # FALSE
        if bin != "0" and bin != "1":
            valid = False

    # VERIFY IF THE VARIABLE INPUTED IS VALID, LOOKING FOR THE VALUE
    # OF THE VARIABLE valid
    # IF IS TRUE CALLS THE FUNCTION THAT CALCULATES THE EQUIVALENT
    # VALUE IN DECIMAL OF THE BINARY SEQUENCE
    if valid:
        bin2dec(binInput)
    
    # IF IS NOT, PRINTS THE MESSAGE AND STOP RUNNING THE CODE
    else:
        print("Binary inputed is invalid.")
# IF THE SEQUENCE IS LESS OR GREATER THAN 8, PRINTS THE MESSAGE
# AND STOP RUNNING THE CODE
else:
    print("Binary is greater than {}!".format(limit))
