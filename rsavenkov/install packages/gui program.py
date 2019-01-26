from appJar import gui
from rsavenkov.console import checkIsWinCorrectPath

def press(button):
    file = app.getEntry("file")
    result = checkIsWinCorrectPath(file)
    if result != 0:
        app.setEntryInvalid("file")
    else:
        with open(file, "w+", encoding="utf-8") as f:
            f.writelines(app.getTextArea("text"))

app = gui("Моя оконная программа", "400x200")

app.addValidationEntry("file")
app.setEntryDefault("file", "Путь к файлу")
app.addTextArea("text")

app.addButtons(["Создать файл"], press)

app.go()