
# Ridrex's custom (probably crappy) hash function, enjoy!

# Turn a string or int into a list of integers.
def makeIntList(input):
    return [int(d) for d in str(input)]


# Hash function. Input must be an integer. Output is a string.
# desiredOutputLength is how many characters you want the hash to be.
# difficulty can be any integer 1 or higher, more means better security but longer wait time.
def ridrexPseudoHashFunction(input, desiredOutputLength, difficulty):

    # Turn input int into list
    input = makeIntList(input)

    initialLen = len(input)

    # Modular addition, add five to first int in list
    firstInt = int(input[0])
    if firstInt // 5 >= 1:
        firstInt -= 5
    else:
        firstInt += 5
    input[0] = firstInt

    # Blow up the initial integer if it's too small
    tempStr = ''
    while len(input) < desiredOutputLength:
        for i in range(initialLen-1):
            eye1 = int(input[i+1])
            eye = int(input[i])
            workNum = eye1 ** 7 + eye
            workNum = str(workNum)
            tempStr = tempStr + workNum
            #print(tempStr)
        input = makeIntList(tempStr)

    # Shrink it down if it got too big
    tempStr = ''
    if len(input) > desiredOutputLength:
        for i in input:
            tempStr = tempStr + str(i)
        tempStr = tempStr[0:desiredOutputLength]
        input = makeIntList(tempStr)


    # Repeat modular addition back and forth steps 21 times
    for i in range(difficulty):

        # Use twenty-first power of previous number for modular addition to current
        for i in range(len(input)-1):
            eye1 = int(input[i+1])
            eye = int(input[i])
            workNum = eye1 ** 21 + eye
            workNum = str(workNum)
            workNum = workNum[-1]
            workNum = int(workNum)
            input[i+1] = workNum

        # Go back through the list with modular addition
        for i in range(len(input)):
            eye1 = int(input[-i-1])
            eye = int(input[-i])
            workNum = eye1 ** 21 + eye
            workNum = str(workNum)
            workNum = workNum[-1]
            workNum = int(workNum)
            input[-i-1] = workNum

    # Turn list back into integer
    tempInt = ''
    for i in input:
        tempInt = tempInt + str(i)
    tempInt = str(tempInt)
    input = tempInt

    return(input)
