import PySimpleGUI as sg
import threading
import time
import webbrowser

def thread_reminder(seconds, window):
    count = 0
    while count < seconds :
        count += 1
        time.sleep(1)
        print(count)
    window.write_event_value('Alarm', "1 minute passed")

layout = [
    [sg.Text('', size=(40, 1))],
    [sg.Text('', size=(30, 2)), sg.Text('Press "Start" button', size=(55, 12), key='-MAIN-')],
    [sg.Button('Start', size=(10,2))],
]
window = sg.Window('APP', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        webbrowser.open("https://www.google.com/search?q=nhôm+định+hình+việt+phát")
        sg.popup_timed("Text: Bạn cần chờ 10s trước khi đóng phần mềm", auto_close_duration= 10, keep_on_top= True)
        time.sleep(10)
        break
    elif event == 'Start':
        threading.Thread(target=thread_reminder, args=(10, window), daemon=True).start()
    elif event == 'Alarm':
        message = values[event]
        sg.popup_auto_close(message)

window.close()