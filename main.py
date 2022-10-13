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

##Logic to identify if an input is a number, operation or clear and to process appropriately.
def inputlogic(instr, num1, num2, opn):
##need to separate C vs. AC
    if instr == "C" or instr == "AC":
        instr = ""
        num1 = ""
        num2 = ""
        opn = ""
        return num1, num2, opn
    if instr == "/" or instr == "*" or instr == "-" or instr == "+":
        opn = instr
        instr = ""
        return num1, num2, opn
    if instr == "=":
        num2 = calclogic(num1, num2, opn)
        instr = ""
        return num1, num2, opn
 ##Need logic for numbers
    else:



curstrnum = ""
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
        curstrnum = displaylogic(event, curstrnum)
        window['-OUTPUT-'].update(curstrnum)
        continue
window.close()