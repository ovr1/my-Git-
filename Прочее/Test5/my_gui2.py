from typing import List, Any
from appJar import gui
import json
file_name = 'registration.txt'
number = 'number_1.txt'

testn = []
# handle button events

def press(button):
    if button == 'Очистить':
        app.stop()
    else:
        fileN = app.getEntry("Имя файла")
        testn.append(fileN)
        usr = app.getEntry("Фамилия")
        testn.append(usr)
        pwd = app.getEntry('Паспорт')
        testn.append(pwd)

        with open(file_name, 'a', encoding="utf-8") as f:
            f.write(str(testn)+'\n')

# content = f.read()

        with open(file_name, 'r', encoding='utf-8') as f:
            contents = f.read()
            lines = contents.splitlines()
            num_lines = len(lines)
            print(contents)
            print(num_lines)

            with open(number, 'w', encoding="utf-8") as f:
                f.write(str(num_lines))



# create a GUI variable called app
app = gui("Login Window", "300x400")
app.setBg("yellow")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome to appJar")
app.setLabelBg("title", "blue")
app.setLabelFg("title", "yellow")

app.addLabelEntry("Имя файла")
app.addLabelEntry("Фамилия")
app.addLabelSecretEntry('Паспорт')
app.addScrolledTextArea(str(testn))


# link the buttons to the function called press


app.addButtons(["Ввод", 'Очистить',], press)

app.setFocus("Имя файла")


# start the GUI
app.go()