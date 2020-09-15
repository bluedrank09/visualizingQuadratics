import matplotlib.pyplot as plt

def drawGraph(xList, yList):
    figure = plt.figure()

    graph = figure.add_subplot(111)
    
    graph.plot(xList, yList)

    graph.set_xlabel('X number from range')
    graph.set_ylabel('After equation done')

    plt.show() 

def checkEquation(equation):
    # valueA = what you multiply x^2 by, like 8 times x^2. 8 is a.
    # valueX is the x, which comes from range.
    # the equation is ax^2+bx+c
    try:
        #currentValue = 0

        if not equation[0].isdigit():
            raise Exception("Missing a number here to use for a")
        
        if equation[1] != 'x':
            raise Exception('Missing the character "x"')
        
        if equation[2] != '^':
            raise Exception('Missing a carot sign ("^")')

        if equation[3] != '2':
            raise Exception('Please enter a 2')

        if not (equation[4] == '+' or equation[4] =='-'):
            raise Exception('Please enter a "+" or "-"')

        if  not equation[5].isdigit():
            raise Exception('Please enter a number for b')
            
        if equation[6] != 'x':
            raise Exception('Missing the character "x"')

        if not (equation[7] == '+' or equation[7] =='-'):
            raise Exception('Please enter a "+" or "-"')

        if  not equation[8].isdigit():
            raise Exception('Please enter a number for c')

        return(True)

        

    except Exception as error:
        raise error


def doCalculations(equation ,numberForRange):
    xList = []
    yList = []

    for number in range(-numberForRange, numberForRange+1):
        valueA = int(equation[0])
        valueB = int(equation[5])
        valueC = int(equation[8])

        firstIteration = int(valueA*number**2)

        if equation[4] == '+':
            secondIteration = int(firstIteration + valueB*number)
        elif equation[4] == '-':
            secondIteration = int(firstIteration - valueB*number)
        
        if equation[7] == '+':
            thirdIteration = int(secondIteration + valueC*number)
        elif equation[7] == '-':
            thirdIteration = int(secondIteration - valueC*number)

        xList.append(number)
        yList.append(thirdIteration)
    print(xList)
    print(yList)

    drawGraph(xList, yList)
        
        

if __name__ == "__main__":
    try:
        equation = input("Give me the equation that I will use (must fit format ax^2 +/- bx +/- c) : ")
        numberForRange = int(input(f"Give me a number to use as the maximum for the range of numbers : "))
        checkEquation(equation)
        doCalculations(equation, numberForRange)

    except Exception as error:
        print(error)

    finally:
        print(f":)")
