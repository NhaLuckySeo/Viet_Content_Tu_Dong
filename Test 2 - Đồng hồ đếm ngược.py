import PySimpleGUI as sg
import time

layout = [
    [sg.Text('Đồng hồ đếm ngược:')],
    [sg.Text('Phần mềm tự đóng sau 10 giây kể từ khi bạn bấm "Đếm Ngược"', font=('Helvetica', 20), justification='center', key='counter')],
    [sg.Button('Đếm Ngược', key='start'), sg.Button('Tạm Dừng Đồng Hồ Để Chạy Điểm', key='stop'), sg.Button('Đóng', key='close')]
]

window = sg.Window('Đồng hồ đếm ngược', layout, keep_on_top= True)

counter = 10
running = False

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'close':
        break

    if event == 'start':
        running = True
        window['counter'].update(counter)

    if event == 'stop':
        running = False

    while running:
        counter -= 1
        window['counter'].update(counter)
        print(counter)
        time.sleep(1)
        if counter == 0:
            running = False
            break
        if counter <= -1:
            break

window.close()
