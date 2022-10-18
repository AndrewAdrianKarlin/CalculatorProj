import PySimpleGUI as sg

##Logic to run the calculation from the calculator and/or return an error.
def calclogic(numa, numb, opn):
    if "." in numa or "." in numb:
        num1 = float(numa)
        num2 = float(numb)
    else:
        num1 = int(numa)
        num2 = int(numb)
    if opn == "/":
        out= num1 / num2
    if opn == "*":
        out= num1 * num2
    if opn == "-":
        out= num1 - num2
    if opn == "+":
        out= num1 + num2
    out = str(out)
    if len(out) > 8:
        return "ERR"
    return out

##Logic to concatenate button presses into a number and/or cutoff if 8 characters.
def displaylogic(instrnum, curstrnum, lastaction):
    if lastaction == "opn1":
        curstrnum ==""
        curstrnum = instrnum
        return curstrnum
    if curstrnum == "0":
        curstrnum = instrnum
        return curstrnum
    if len(curstrnum)>7:
        return curstrnum
    else:
        curstrnum = curstrnum + instrnum
        return curstrnum

##Logic to run "clear" function.
def clearmem(inputstr, buffer, numstore, opnstore, lastaction):
  if lastaction == "=" or lastaction == "C" or lastaction == "opn2":
    buffer = "0"
    numstore = ""
    opnstore = ""
    return buffer, numstore, opnstore
  if lastaction == "#":
    buffer = "0"
    return buffer, numstore, opnstore
  if lastaction == "opn1":
    opnstore = ""
    buffer = numstore
    numstore = ""
    return buffer, numstore, opnstore

def opnlogic(inputstr, buffer, numstore, opnstore, lastaction):
    if numstore == "":
        lastaction = "opn1"
        numstore = buffer
        opnstore = inputstr
    else:
        lastaction = "opn2"
        buffer = calclogic(buffer, numstore, opnstore)
        numstore = ""
        opnstore = inputstr
    return buffer, numstore, opnstore, lastaction

##Logic to identify if an input is a number, operation or clear and to process appropriately.
def inputlogic(inputstr, buffer, numstore, opnstore, lastaction):
    if inputstr == "C":
        buffer, numstore, opnstore = clearmem(inputstr, buffer, numstore, opnstore, lastaction)
        lastaction = "C"
        return buffer, numstore, opnstore, lastaction
    if inputstr == "AC":
        lastaction = "C"
        buffer = "0"
        numstore = ""
        opnstore = ""
        return buffer, numstore, opnstore, lastaction
    if inputstr == "/" or inputstr == "*" or inputstr == "-" or inputstr == "+":
        buffer, numstore, opnstore, lastaction = opnlogic(inputstr, buffer, numstore, opnstore, lastaction)
        return buffer, numstore, opnstore, lastaction
    if inputstr == "=":
        lastaction = "="
        if opnstore != "":
            buffer = calclogic(numstore, buffer, opnstore)
            opnstore = ""
            numstore = ""
        return buffer, numstore, opnstore, lastaction
    else:
        buffer = displaylogic(inputstr, buffer, lastaction)
        lastaction  = "#"
        return buffer, numstore, opnstore, lastaction

buffer = "0"
numstore = ""
opnstore = ""
lastaction = ""
sg.theme('DarkAmber')


layout = [  [sg.Text("", size=(24, 1), key='-OUTPUT-')],
            [sg.Button("/", size=(3, 1)), sg.Button("7", size=(3, 1)), sg.Button("8", size=(3, 1)), sg.Button("9", size=(3, 1))],
            [sg.Button("*", size=(3, 1)), sg.Button("4", size=(3, 1)), sg.Button("5", size=(3, 1)), sg.Button("6", size=(3, 1))],
            [sg.Button("-", size=(3, 1)), sg.Button("1", size=(3, 1)), sg.Button("2", size=(3, 1)), sg.Button("3", size=(3, 1))],
            [sg.Button("+", size=(3, 1)), sg.Button("C", size=(3, 1)), sg.Button("0", size=(3, 1)), sg.Button("AC", size=(3, 1))],
            [sg.Button("=", size=(23, 1))]]

window = sg.Window("Andrew's Calculator", layout, element_justification='c')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    else:
        buffer, numstore, opnstore, lastaction = inputlogic(event, buffer, numstore, opnstore, lastaction)
        window['-OUTPUT-'].update(buffer)
        continue
window.close()