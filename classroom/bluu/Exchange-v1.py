def main():
    colour = getColour()
    print(isColourPresent(colour))
    
    print(isColourPresent('pink'))
    print(isColourPresent('purple'))

    print (isColourPresent(getColour()))

def isColourPresent(color):
    colours = ['red', 'green', 'brown','purple','cyan','grey']
    for c in colours:
        if c == color:
            return True   
    return False
    
def getColour():
    colour = input("enter colour? ")
    return colour

        
if __name__ == '__main__':
    main()

