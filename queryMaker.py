#Query maker - copy docs to ODC QA servers

#Input Fields:
'''
Source Table Name:
Max ID from Destination table:
Min ID from Source table among target Doc IDs:
List of Doc IDs:
'''

import PySimpleGUI as sg
import appmethods
import pyperclip

# color theme, use sg.theme_previewer() to see all theme options
sg.theme('Topanga')

layout = [  [sg.Text("Source Table:")],
            [sg.InputText(key='_SOURCE_')],
            [sg.Text("MIN ID among Source DocIDs: ")],
            [sg.InputText(key='_MINSOURCE_')],
            [sg.Text("MAX ID of Destination Table: ")],
            [sg.InputText(key='_MAXDEST_')],
            [sg.Text("List of DocIDs: ")],
            [sg.Multiline(key='_DOCIDS_',size=(45,5))],
            [sg.Button('Run'), sg.Text(' '*48), sg.Button('Clear')] ,
            [sg.Text('_'*30)],
            [sg.Text("Query: ")],
            [sg.InputText(key="_RESULT_")],
            [sg.Button('Copy Query'), sg.Text(' '*38), sg.Button('Exit')] ]

# Create actual window to display
window = sg.Window('QueryMaker', layout, location=(500,275)) #note: location of window specific to this computer.

# Event loop
while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event == 'Run':
        window['_RESULT_'].update(appmethods.makequery(values['_SOURCE_'], values['_MINSOURCE_'], values['_MAXDEST_'], values['_DOCIDS_']))
    if event == 'Copy Query':
        pyperclip.copy(values['_RESULT_'])
    if event == 'Clear':
        window['_SOURCE_']("")
        window['_MINSOURCE_']("")
        window['_MAXDEST_']("")
        window['_DOCIDS_']("")
        window['_RESULT_']("")

window.close()