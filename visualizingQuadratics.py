import matplotlib.pyplot as plt
import traceback

def drawGraph(listOfXLists, listOfYLists):
    figure = plt.figure()

    graph = figure.add_subplot(111)
    
    for graphListNumber in range(0,len(listOfXLists)):
        graph.plot(listOfXLists[graphListNumber], listOfYLists[graphListNumber])
        # print(listOfXLists[graphListNumber], listOfYLists[graphListNumber])

    graph.set_xlabel('X number from range')
    graph.set_ylabel('After equation done')

    plt.show() 

def checkEquation(equationList):
    # valueA = what you multiply x^2 by, like 8 times x^2. 8 is a.
    # valueX is the x, which comes from range.
    # the equation is ax^2+bx+c
    try:
        #currentValue = 0
        for equation in equationList:

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
                raise Exception('Please enter a number for value b')
                
            if equation[6] != 'x':
                raise Exception('Missing the character "x"')

            if not (equation[7] == '+' or equation[7] =='-'):
                raise Exception('Please enter a "+" or "-"')

            if  not equation[8].isdigit():
                raise Exception('Please enter a number for c')

        return(True)

        

    except Exception as error:
        raise error


def doCalculations(equationList ,numberForRange):
    listOfXLists = []
    listOfYLists = []

    for equation in equationList:
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

        listOfXLists.append(xList)
        listOfYLists.append(yList)

    return(listOfXLists, listOfYLists)

    
        
        

if __name__ == "__main__":
    try:

        equationList =[]

        loopNumber = int(input("How many eqautions do you want me to visualize? : "))

        for i in range(0,loopNumber):
            equation = input("Give me the equation that I will use (must fit format ax^2 +/- bx +/- c) : ")
            equationList.append(equation)
        numberForRange = int(input(f"Give me a number to use as the maximum for the range of numbers : "))
        checkEquation(equationList)
        listOfXLists, listOfYLists = doCalculations(equationList, numberForRange)
        drawGraph(listOfXLists, listOfYLists)

    except Exception as error:
        traceback.print_exc()

    finally:
        print(f":)")
