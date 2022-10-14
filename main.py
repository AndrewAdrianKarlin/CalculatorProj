import PySimpleGUI as sg

##Logic to run the calculation from the calculator and/or return an error.
def calclogic(num1, num2, opn):
    if opn == "/":
        out= num1 / num2
    if opn == "*":
        out= num1 * num2
    if opn == "-":
        out= num1 - num2
    if opn == "+":
        out= num1 + num2
    if len(out) > 8:
        return "ERR"
    return out

##Logic to concatenate button presses into a number and/or cutoff if 8 characters.
def displaylogic(instrnum, curstrnum):
    if len(curstrnum)>7:
        return curstrnum
    else:
        curstrnum = curstrnum + instrnum
        return curstrnum

##Logic to run "clear" function.
def clearmem(inputstr, buffer, numstore, opnstore):
    return  inputstr, buffer, numstore, opnstore

def opnlogic(inputstr, buffer, numstore, opnstore):
    if numstore == "":
        numstore = buffer
        buffer = ""
        opnstore = inputstr
    else:
        buffer = calclogic(buffer, numstore, opnstore)
        numstore = ""
        opnstore = inputstr
    return buffer, numstore, opnstore

##Logic to identify if an input is a number, operation or clear and to process appropriately.
def inputlogic(inputstr, buffer, numstore, opnstore):
    if inputstr == "C":
        inputstr, buffer, numstore, opnstore = clearmem(inputstr, buffer, numstore, opnstore)
        return buffer, numstore, opnstore
    if inputstr == "AC":
        buffer = "0"
        numstore = ""
        opnstore = ""
        return buffer, numstore, opnstore
    if inputstr == "/" or inputstr == "*" or inputstr == "-" or inputstr == "+":
        buffer, numstore, opnstore = opnlogic(inputstr, buffer, numstore, opnstore)
        return buffer, numstore, opnstore
    if inputstr == "=":
        if opnstore != "":
            buffer = calclogic(buffer, numstore, opnstore)
            opnstore = ""
            numstore = ""
        return buffer, numstore, opnstore
    else:
        buffer = displaylogic(inputstr, buffer)
        return buffer, numstore, opnstore

buffer = ""
numstore = ""
opnstore = ""
sg.theme('DarkAmber')


layout = [  [sg.Text("", size=(24, 1), key='-OUTPUT-')],
            [sg.Button("/", size=(3, 1)), sg.Button("7", size=(3, 1)), sg.Button("8", size=(3, 1)), sg.Button("9", size=(3, 1))],
            [sg.Button("*", size=(3, 1)), sg.Button("4", size=(3, 1)), sg.Button("5", size=(3, 1)), sg.Button("6", size=(3, 1))],
            [sg.Button("-", size=(3, 1)), sg.Button("1", size=(3, 1)), sg.Button("2", size=(3, 1)), sg.Button("3", size=(3, 1))],
            [sg.Button("+", size=(3, 1)), sg.Button("=", size=(3, 1)), sg.Button("0", size=(3, 1)), sg.Button("AC", size=(3, 1))]]

window = sg.Window("Andrew's Calculator", layout, element_justification='c')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    else:
        buffer, numstore, opnstore = inputlogic(event, buffer, numstore, opnstore)
        window['-OUTPUT-'].update(buffer)
        continue
window.close()