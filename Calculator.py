import math
import re
import os

def Factorial(n):
    factorial = 1
    if n == 0:
        factorial = 1
    else:
        for i in range(1, n+1):
            factorial *= i
    return factorial


mathSign = ["+", "-", "*", "/", "!", "^", "%", "(", ")"]


mathSignOperation = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y

}

while True:

    numberList = []
    mathSignList = []
    number = ""
    mathSignAdd = []
    numberAdd = []
    maxBrackets = 0
    bracketsCount = 0
    bracketsListPoint = {}  

    while True:
        check = ""
        mathFunction = input("\nЧтобы завершить программу введите End.\nВведите пример: ").replace(" ","")
        if mathFunction.lower() == "end":
            os.abort()
        check = re.search(r'[a-zA-Zа-яА-ЯёЁ@"#$&?><|]', mathFunction)
        if check != None:
            print("Пример введен не корректно\n")
        else:
            break


    for i in range(len(mathFunction)):
        if mathFunction[i] in mathSign:
            if mathFunction[i] != "(":
                if number != "":
                    numberList.append(str(number))
                number = ""
                mathSignList.append(mathFunction[i])
            if mathFunction[i] == "-" and (mathFunction[i-1] in mathSign or i == 0):
                numberList.append("minus")
                mathSignList.pop()
                mathSignList.append("minus")
            if mathFunction[i] == "%":
                numberList.append("%")
            if mathFunction[i] == "!":
                numberList.append("!")
            if mathFunction[i] == "(":
                numberList.append("brackets"+str(bracketsCount))
                mathSignList.append(mathFunction[i])
                bracketsListPoint["brackets"+str(bracketsCount)] = [len(mathSignList)-1, None]
                bracketsCount += 1
                maxBrackets = bracketsCount
            if mathFunction[i] == ")":
                while bracketsCount >= 0:
                    bracketsCount -= 1
                    if bracketsCount < 0:
                        print("Присутствуют лишнии знаки закрытой скобки")
                        os.abort()
                    if bracketsListPoint["brackets"+str(bracketsCount)][1] == None:
                        numberList.append("brackets-"+str(bracketsCount))
                        bracketsListPoint["brackets"+str(bracketsCount)][1] = len(mathSignList)-1
                        break
                bracketsCount = maxBrackets   
        else:

            number += mathFunction[i]
    if number != "":
        numberList.append(number)

   

    for i in range(maxBrackets-1, -2, -1):
        
        numberAdd.clear()
        mathSignAdd.clear()
        if i == -1:
            numberAdd = numberList
            mathSignAdd = mathSignList
            j = 1
        else:
            j = bracketsListPoint["brackets"+str(i)][0]
            while mathSignList[j] != ")":
                mathSignAdd.append(mathSignList.pop(j))
            mathSignList.pop(j)
            j = numberList.index("brackets"+str(i)) + 1
            while "brackets-"+str(i) in numberList:
                numberAdd.append(numberList.pop(j))
            numberAdd.pop()
            mathSignAdd.pop(0)

        
        
        while "minus" in mathSignAdd:
            Point = mathSignAdd.index("minus")
            numberAdd[Point+1] = -float(numberAdd[Point+1])
            numberAdd.pop(Point)
            mathSignAdd.pop(Point)
        while "%" in mathSignAdd:
            Point = mathSignAdd.index("%")
            numberAdd[Point] = float(numberAdd[Point]) / 100
            numberAdd.pop(Point+1)
            mathSignAdd.pop(Point)
        while "!" in mathSignAdd:
            Point = mathSignAdd.index("!")
            numberAdd[Point] = Factorial(int(numberAdd[Point]))
            numberAdd.pop(Point+1)
            mathSignAdd.pop(Point)
        while "^" in mathSignAdd :
            Point = mathSignAdd.index("^")
            x = float(numberAdd[Point])
            y = float(numberAdd.pop(Point+1))
            numberAdd[Point] = x ** y
            mathSignAdd.pop(Point)
        while "*" in mathSignAdd or "/" in mathSignAdd:
            if "*" in mathSignAdd:
                Point = mathSignAdd.index("*")
            else: 
                Point = mathSignAdd.index("/")
            x = float(numberAdd[Point])
            y = float(numberAdd.pop(Point+1))
            numberAdd[Point] = mathSignOperation[mathSignAdd[Point]](x, y)
            mathSignAdd.pop(Point)
        while mathSignAdd != []:
            if "+" in mathSignAdd:
                Point = mathSignAdd.index("+" or "-")
            else: 
                Point = mathSignAdd.index("-")
            x = float(numberAdd[Point])
            y = float(numberAdd.pop(Point+1))
            numberAdd[Point] = mathSignOperation[mathSignAdd[Point]](x, y)
            mathSignAdd.pop(Point)
        numberList[j-1] = numberAdd[0]
    
    print("Ответ: " + str(numberList[0]))