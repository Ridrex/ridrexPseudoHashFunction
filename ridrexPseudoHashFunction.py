
# Hash function. Input must be a string of ASCII characters. Output is a string of ints.
# All other inputs are integers.
# Outputs the hash and number of blocks
def ridrexPseudoHashFunction(input, desiredOutputLength, blockSize, blockExponentLoop, wholeHashModLoop, exponentiator):

    # THIS SECTION PREPARES INPUT FOR HASH FUNCTION

    # Minimum number of blocks for blockwise mod addition
    # This is hardcoded to ensure blockwise addition functions
    minBlocks = 2

    # Minimum ratio of length required to ensure an output of sufficient length
    # Hardcoded to ensure functionality
    lengthToOutputRatio = 4

    # Blocks dictionary
    blocks = {}

    # Make sure the input is a string
    input = str(input)

    # Turn all ascii characters into an integer
    tempString = ''
    for i in input:
        tempString = tempString + str(ord(i))
    input = tempString

    # Calculate how many blocks there are
    blockCount = len(input) // blockSize

    # Make sure that minimum blocks requirement is met
    if len(input) - (minBlocks * blockSize) < 0:
        padding = (minBlocks * blockSize) - len(input)
        for i in range(padding):
            input = input + '0'
        # Recalculate how many blocks there are
        blockCount = len(input) // blockSize

    # Make sure there is enough data to satisfy the length to output ratio
    if len(input) - (desiredOutputLength * lengthToOutputRatio) < 0:
        padding = (desiredOutputLength * lengthToOutputRatio) - len(input)
        for i in range(padding):
            input = input + '0'
        # Recalculate how many blocks there are
        blockCount = len(input) // blockSize

    # Pad data to fill in the last block if applicable
    if len(input) % (blockCount * blockSize) > 0:
        padding = ((blockCount + 1) * blockSize) - len(input)
        for i in range(padding):
            input = input + '0'
        # Recalculate how many blocks there are
        blockCount = len(input) // blockSize

    # Add all of the data into the dictionary blockwise
    for i in range(blockCount):
        currentBlockData = str(input[i*blockSize:(i+1)*blockSize])
        currentBlockName = str(i)
        blocks[currentBlockName] = currentBlockData

    # ACTUAL HASH FUNCTION STARTS HERE

    # Perform exponentiation and truncation on individual blocks
    workNum = ''
    for i in range(blockCount):
        workNum = blocks[str(i)]
        for y in range(blockExponentLoop):
            workNum = int(workNum) ** exponentiator
            workNum = str(workNum)
            workNum = workNum[0:blockSize]
            blocks[str(i)] = workNum
        workNum = ''

    # Repeat modular addition back and forth steps
    for i in range(wholeHashModLoop):

        # Modular addition forward blockwise
        workNum = ''
        workNum2 = ''
        sum = 0
        for i in range(blockCount-1):
            workNum = blocks[str(i)]
            workNum2 = blocks[str(i+1)]
            workNum = int(workNum)
            workNum2 = int(workNum2)
            sum = workNum + workNum2
            sum = str(sum)
            sum = sum[0 - (blockSize):]
            # Pad if result is not long enough
            if len(sum) < blockSize:
                for i in range(blockSize - len(sum)):
                    sum = sum + '0'
            blocks[str(i+1)] = sum
            workNum = ''
            workNum2 = ''

        # Go back through the list with modular addition blockwise
        workNum = ''
        workNum2 = ''
        sum = 0
        for i in range(blockCount-1):
            workNum = blocks[str((blockCount-1)-i-1)]
            workNum2 = blocks[str((blockCount-1)-i)]
            workNum = int(workNum)
            workNum2 = int(workNum2)
            sum = workNum + workNum2
            sum = str(sum)
            sum = sum[0 - (blockSize):]
            # Pad if result is not long enough
            if len(sum) < blockSize:
                for i in range(blockSize - len(sum)):
                    sum = sum + '0'
            blocks[str((blockCount-1)-i-1)] = sum
            workNum = ''
            workNum2 = ''

    # Reconstruct the string from dictionary
    tempString = ''
    for i in blocks:
        tempString = tempString + blocks[i]
    input = tempString

    # Truncate it if it's too long
    if len(input) > desiredOutputLength:
        input = input[0:desiredOutputLength]

    return(input)
