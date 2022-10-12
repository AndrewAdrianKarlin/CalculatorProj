import PySimpleGUI as sg

def calculation(num1, num2, opn):
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

def displaylogic(instrnum, currstrnum):
    if len(currstrnum)>7:
        return currstrnum
    else:
        currstrnum = currstrnum + instrnum
        return currstrnum


sg.theme('DarkAmber')    # Keep things interesting for your users

layout = [  [sg.InputText("replace with an output display", size=(24, 1))],
            [sg.Button("/", size=(3, 1)), sg.Button("7", size=(3, 1)), sg.Button("8", size=(3, 1)), sg.Button("9", size=(3, 1))],
            [sg.Button("*", size=(3, 1)), sg.Button("4", size=(3, 1)), sg.Button("5", size=(3, 1)), sg.Button("6", size=(3, 1))],
            [sg.Button("-", size=(3, 1)), sg.Button("1", size=(3, 1)), sg.Button("2", size=(3, 1)), sg.Button("3", size=(3, 1))],
            [sg.Button("+", size=(3, 1)), sg.Button("=", size=(3, 1)), sg.Button("0", size=(3, 1)), sg.Button("AC", size=(3, 1))]]

window = sg.Window("Andrew's Calculator", layout, element_justification='c')

while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break
window.close()