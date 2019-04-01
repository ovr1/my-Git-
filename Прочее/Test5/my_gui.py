from typing import List, Any
from appJar import gui

import json
registration = []

# handle button events

def press(button):
    if button == 'Очистить':
        app.stop()
    else:
        fileN = app.getEntry("Имя файла")
        registration.append(fileN)
        usr = app.getEntry("Фамилия")
        registration.append(usr)
        pwd = app.getEntry('Паспорт')
        registration.append(pwd)
        print("Фамилия:", usr, "Паспорт:", pwd)
        print("Registration: ",registration)
        with open(str(registration), 'a') as f_obj:
            json.dump(registration,f_obj)


# create a GUI variable called app
app = gui("Login Window", "378x265")
app.setBg("yellow")
app.setButtonFont(14)
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Welcome to appJar")
app.setLabelBg("title", "lightblue")



app.addLabelEntry("Имя файла")
app.addLabelEntry("Фамилия")
app.addLabelSecretEntry('Паспорт')

# link the buttons to the function called press

app.addButtons(["Ввод", 'Очистить',], press)

app.setFocus("Имя файла")


# start the GUI
app.go()