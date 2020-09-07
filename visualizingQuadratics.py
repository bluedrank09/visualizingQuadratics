import matplotlib.pyplot as plt

def drawGraph(xList, yList):
    figure = plt.figure()

    graph = figure.add_subplot(111)
    
    graph.plot(xList, yList)

    graph.set_xlabel('X number from range')
    graph.set_ylabel('After equation done')

    plt.show() 


def getNumbersInRange(numberForRange):

    xList = []
    yList = []

    for number in range(-numberForRange, numberForRange+1):
        newNumber = number**2 + 2*number + 1
        xList.append(number)
        yList.append(newNumber)
    drawGraph(xList, yList)
        

if __name__ == "__main__":
    try:
        numberForRange = int(input(f"Give me a number to use as the maximum for the range of numbers : "))
        getNumbersInRange(numberForRange)

    except Exception as error:
        print(error)

    finally:
        print(f":)")
