import time

#Function for simple calculations
def calculatorSimpleCalculator():
    #Asks the user what operation they would like to use, saves it for future use
    #\n returns to the next line, adding space between each part of the text
    print("Welcome to the simple calculator!")
    chosenOperation = input("""Please enter which basic mathematical operation you would like you use on two integers (please enter in numeral form):
    \nType '+' to add
    \nType '-' to subtract
    \nType '*' to multiply
    \nType '/' to divide
    \nType '^' to take the power of
    \nType '%' to find the remainder\n""")

    #Asks the user what two numbers they would like to compute, saves it for future use
    firstNumber = int(input("Enter the first number: \n"))
    secondNumber = int(input("Enter the second number: \n"))

    #Conditional statement chain uses the operation the user chose in order to determine how to compute
    #Uses .format in order to place the numbers where they belong
    #Concatenates everything into a cohesive line
    if chosenOperation == "+":
        print(("{} + {} = ".format(firstNumber, secondNumber)) + str(firstNumber + secondNumber))
    elif chosenOperation == "-":
        print(("{} - {} = ".format(firstNumber, secondNumber)) + str(firstNumber - secondNumber))
    elif chosenOperation == "*":
        print(("{} * {} = ".format(firstNumber, secondNumber)) + str(firstNumber * secondNumber))
    elif chosenOperation == "/":
        print(("{} / {} = ".format(firstNumber, secondNumber)) + str(firstNumber / secondNumber))
    elif chosenOperation == "^":
        print(("{} ^ {} = ".format(firstNumber, secondNumber)) + str(firstNumber ** secondNumber))
    elif chosenOperation == "%":
        print(("{} % {} = ".format(firstNumber, secondNumber)) + str(firstNumber % secondNumber))
    else:
        print("Response unclear, please try again.")

#Function to find factors
def calculatorFactorFinder():
    print("Welcome to the factor finder!")
    #Asks the user what number they would like to find factors of, saves it for future use
    chosenNumber = int(input("Please enter which number you would like the find the factors of (please enter in numeral form): \n"))

    #Prints out the factors of the chosen number, using the 'end = " "'' segment in order to print all factors along the same line
    print("The factors of " + str(chosenNumber) + " are :", end = " ")
    #Uses a for loop to identify factors of the number
    for val in range(1, chosenNumber + 1):
        if chosenNumber % val == 0:
            print(str(val), end = " ")

#Function to find multiples
#continue work
def calculatorMultipleFinder():
    print("Welcome to the multiple finder!")
    chosenFactor = int(input("Please enter which number you would like to find the multiples of (please enter in numeral form): \n"))
    chosenMultipleNumber = int(input("Please enter the number of multiples you want to see (please enter in numeral form): \n"))
    multiples = 0
    print("The " + str(chosenMultipleNumber) + " multiples of " + str(chosenFactor) + ", starting from " + str(chosenFactor) + " are :", end = " ")
    for number in range(chosenMultipleNumber):
        print(str((number + 1) * chosenFactor), end = " ")

    #for val in range (0, ender < int(chosenMultipleNumber + 1), int(chosenFactor)):
    #    print(str(val), end = " ")
    #    ender += 1

perimeter = 0.0
def circleCircumference(circleRadius):
        piApprox = 3.14
        perimeter = 2 * float(circleRadius) * piApprox
        print("The approximate circumference of your circle of radius " + str(circleRadius) + " units is: " + str(perimeter) + " units.")
def squarePerimeter(squareSideLength):
        perimeter = 4.0 * float(squareSide)
        print("The perimeter of your square of side length " + str(squareSideLength) + " units is: " + str(perimeter) + " units.")
def rectanglePerimeter(rectangleLength, rectangleWidth):
        perimeter = 2.0 * float(rectangleLength + rectangleWidth)
        print("The perimeter of your rectangle of length " + str(rectangleLength) + " units and width "+ str(rectangleWidth) + " units is: " + str(perimeter) + "  units.")
def trianglePerimeter(triangleSideOne, triangleSideTwo, triangleSideThree):
        perimeter = int(triangleSideOne + triangleSideTwo + triangleSideThree)
        print("The perimeter of your triangle of side lengths " + str(triangleSideOne) + ", " + str(triangleSideTwo) + ", and " + str(triangleSideTree) + " units is: " + str(perimeter) + " units.")
def regularPolygonPerimeter(polygonSideNum, polygonSideLength):
        perimeter = int(polygonSideNum * polygonSideLength)
        print("The perimeter of your regular polygon with " + str(polygonSideNum) + " number of sides and side lengths of " + str(polygonSideLength) + " units is: " + str(perimeter) + " units.")

def calculatorPerimeter():
    chosenShape = str(input("Enter which shape you would like to find the perimeter of from the following: \n - Type 'circle' for circle.\n - Type 'square' for square.\n - Type 'rectangle' for rectangle.\n - Type 'triangle' for triangle.\n - Type 'polygon' for any normal polygon.\n"))
    if "circ" in chosenShape.lower():
        radius = float(input("Enter the radius of your circle. \n"))
        circleCircumference(radius)
    elif "squa" in chosenShape.lower():
        side = float(input("Enter the side length of your square. n"))
    elif "rect" in chosenShape.lower():
        length = float(input("Enter the length of your rectangle. \n"))
        width = float(input("Enter the width of your rectangle. \n"))
        rectanglePerimeter(length, width)
    elif "tria" in chosenShape.lower():
        side1 = float(input("Enter the first side of your triangle. \n"))
        side2 = float(input("Enter the second side of your triangle. \n"))
        side3 = float(input("Enter the third side of your triangle. \n"))
        trianglePerimeter(side1, side2, side3)
    elif "poly" in chosenShape.lower():
        sideNum = float(input("Enter the number of sides of your polygon. \n"))
        sideLength = float(input("Enter the side length of your polygon. \n"))
        regularPolygonPerimeter(sideNum, sideLength)
    else:
        calculatorPerimeter()

area = 0.0
def circleArea(circleRadius):
        piApprox = 3.14
        area = piApprox * float(circleRadius) * float(circleRadius)
        print("The approximate area of your circle of radius " + str(circleRadius) + " units is: " + str(area) + " square units.")
def rectangleArea(rectangleLength, rectangleWidth):
        area = float(rectangleLength) * float(rectangleWidth)
        print("The area of your rectangle of length " + str(rectangleLength) + " units and width " + str(rectangleWidth) + " units is: " + str(area) + " square units.")
def triangleArea(triangleBase, triangleHeight):
        area = 0.5 * float(triangleBase) * float(triangleHeight)
        print("The area of your triangle of base " + str(triangleBase) + " units and height " + str(triangleHeight) + " units is: " + str(area) + " square units.")
def trapezoidArea(trapezoidHeight, trapezoidBaseOne, trapezoidBaseTwo):
        area = (((trapezoidBaseOne + trapezoidBaseTwo)/2) * float(trapezoidHeight))
        print("The area of your trapezoid of height " + str(trapezoidHeight) + " units and bases of " + str(trapezoidBaseOne) + " and " + str(trapezoidBaseTwo) + " is: " + str(area) + " square units.")
        print("Welcome to the area finder!")
def calculatorArea():
    chosenShape = str(input("Enter which shape you would like to find the area of from the following: \n - Type 'circle' for circle.\n - Type 'rectangle' for rectangle.\n - Type 'triangle' for triangle.\n - Type 'trapezoid' for trapezoid.\n"))
    if "circ" in chosenShape.lower():
        radius = float(input("Enter the radius of your circle. \n"))
        circleArea(radius)
    elif "rect" in chosenShape.lower():
        length = float(input("Enter the length of your rectangle. \n"))
        width = float(input("Enter the width of your rectangle. \n"))
        rectangleArea(length, width)
    elif "tria" in chosenShape.lower():
        base = float(input("Enter the base of your triangle. \n"))
        height = float(input("Enter the height of your triangle. \n"))
        triangleArea(base, height)
    elif "trap" in chosenShape.lower():
        height = float(input("Enter the height of your trapezoid. \n"))
        base1 = float(input("Enter the first base of your trapezoid. \n"))
        base2 = float(input("Enter the second base of your trapezoid. \n"))
        trapezoidArea(height, base1, base2)
    else:
        calculatorArea()

def calculatorRunner():
    print("Welcome to the calculator functionality!")
    userCalculatorInput = str(input("Enter which feature of the calculator functionality you would like to try out: \n - Type 'simple' to use a simple calculator.\n - Type 'factor' to use a factor finder.\n - Type 'multiple' to use a multiple finder.\n - Type 'perimeter' to use a perimeter calculator.\n - Type 'area' to use an area calculator.\n"))

    userCalculatorActive = True
    while userCalculatorActive:
        if "exit" in userCalculatorInput.lower():
            userCalculatorActive = False
            break
        elif userCalculatorInput.lower() in "exit":
            userCalculatorActive = False
            break
        else:
            userCalculatorActive = True

        if "simple" in userCalculatorInput.lower():
            calculatorSimpleCalculator()
        elif "factor" in userCalculatorInput.lower():
            calculatorFactorFinder()
        elif "multiple" in userCalculatorInput.lower():
            calculatorMultipleFinder()
        elif "perimeter" in userCalculatorInput.lower():
            calculatorPerimeter()
        elif "area" in userCalculatorInput.lower():
            calculatorArea()
        else:
            userCalculatorInput = str(input("Sorry, I couldn't understand what you said. Try selecting one of the given options, or type 'exit' if you are trying to quit out of the calculator functionality. \n"))

        userCalculatorInput = str(input("Enter which feature of the calculator functionality you would like to try out: \n - Type 'simple' to use a simple calculator.\n - Type 'factor' to use a factor finder.\n - Type 'multiple' to use a multiple finder.\n - Type 'perimeter' to use a perimeter calculator.\n - Type 'area' to use an area calculator.\n - Type 'exit' if you are trying to quit out of the calculator functionality. \n"))
