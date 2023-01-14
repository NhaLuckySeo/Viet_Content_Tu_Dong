#!/usr/bin/env python

import PySimpleGUI as sg
import time

def time_as_int():
    return int(round(time.time() * 100))

sg.theme('Black')

layout = [ [sg.Text('')],
             [sg.Text('Bấm thoát tool hoặc đóng browser vừa mở trước 10s: trừ 1 điểm tích lũy.')],
            [sg.Text('Điểm tích lũy -10: Phần mềm bị hủy, và máy tính này sẽ vĩnh viễn không kích hoạt lại được phần mềm này.')],
           [sg.Text('')],
            [sg.Text('Bấm thoát tool hoặc đóng browser vừa mở sau 10s: không bị trừ điểm.')],
            [sg.Text('Đồng hồ chạy tới 60s và browser vẫn mở: cộng 1 điểm tích lũy.')],
            [sg.Text('')],

            [sg.Text('Bấm dừng đồng hồ. Bấm đè chuột phải có thể di chuyển đồng hồ sang vị trí khác.')],
           [sg.Text('Vẫn sử dụng màn hình máy tính bình thường, không liên quan tới đồng hồ.')],
            [sg.Text('')],
            [sg.Text('Bấm vô các liên kết liên quan của các đơn vị tài trợ: cộng 1 điểm tích lũy.')],
            [sg.Text('Tiếp tục bấm và xem website các nhà tài trợ: cộng điểm thưởng theo hoạt động tự nhiên.')],
            [sg.Text('Duyệt website đơn vị tài trợ cần để đồng hồ chạy mới tính và cộng điểm thưởng được.')],
            [sg.Text('')],

          [sg.Text('', size=(8, 2), font=('Helvetica', 30),
                justification='center', key='text')],
          [sg.Button('Dừng', key='-RUN-PAUSE-', button_color=('white', '#001480')),
           sg.Button('Làm Mói', button_color=('white', '#007339'), key='-RESET-'),
           sg.Button('Thoát', button_color=('white', 'firebrick4'), key='Exit')],
            [sg.Text('')],
           ]

window = sg.Window('Running Timer', layout,
                   no_titlebar=True,
                   auto_size_buttons=False,
                   keep_on_top=True,
                   grab_anywhere=True,
                   element_padding=(0, 0),
                   finalize=True,
                   element_justification='c',
                   right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_EXIT)

current_time, paused_time, paused = 0, 0, False
start_time = time_as_int()

while True:
    # --------- Read and update window --------
    if not paused:
        event, values = window.read(timeout=10)
        current_time = time_as_int() - start_time
    else:
        event, values = window.read()
    # --------- Do Button Operations --------
    if event in (sg.WIN_CLOSED, 'Exit'):        # ALWAYS give a way out of program
        break
    if event == '-RESET-':
        paused_time = start_time = time_as_int()
        current_time = 0
    elif event == '-RUN-PAUSE-':
        paused = not paused
        if paused:
            paused_time = time_as_int()
        else:
            start_time = start_time + time_as_int() - paused_time
        # Change button's text
        window['-RUN-PAUSE-'].update('Bấm Chạy' if paused else 'Dừng')

    # --------- Display timer in window --------
    window['text'].update('{:02d}:{:02d}.{:02d}'.format((current_time // 100) // 60,
                                                        (current_time // 100) % 60,
                                                        current_time % 100))
window.close()