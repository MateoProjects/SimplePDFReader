import PySimpleGUI as sg
from readerFile import *

sg.theme("BlueMono")
sg.set_options(font=('Helvetica', 10))
layout = [[sg.T("")],
          [sg.Text("Choose a file: "), sg.Input(key="-IN2-", change_submits=True), sg.FileBrowse(key="-IN-")],
          [sg.Text("Choose a folder"), sg.Input(key="-IN3-", change_submits=True), sg.FolderBrowse(key="-IN4-")],
          [sg.Button("Submit")]]

###Building Window
window = sg.Window('PDFReader', layout, size=(600, 150))

if __name__ == "__main__":

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == "Submit":
            rd = ReaderFile(values['-IN2-'])
            text = rd.readFile()
            """
            Put your functions here for extract all information that you required
            """

