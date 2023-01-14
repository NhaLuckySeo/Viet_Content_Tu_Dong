import PySimpleGUI as sg

def make_window1():
    layout = [[sg.Text('Phần Mềm Viết Bài Tiếng Việt Tự Động')],
              [sg.Button('Gợi ý nội dung theo từ khóa'), sg.Button('Viết đoạn văn tự động theo gợi ý nội dung'), sg.Button('Exit')]]
    window = sg.Window('tulamseo 1.2.0: Phần Mềm Viết Bài Tiếng Việt Tự Động', layout, finalize=True, icon="Logo_Lycky (1).ico")
    return window


def make_window2():
    layout = [[sg.Text('Gợi ý các ý chính bài viết theo từ khóa')],
               [sg.Button('Về trang chủ'), sg.Button('Exit')]]
    window = sg.Window('tulamseo 1.2.0: Gợi ý các ý chính bài viết theo từ khóa = Tạo H2', layout, finalize=True, icon="Logo_Lycky (1).ico")
    return window

def make_window3():
    layout = [[sg.Text('Viết nội dung đoạn văn theo ý chính đã được gợi ý')],
               [sg.Button('Về trang chủ'), sg.Button('Exit')]]
    window = sg.Window('tulamseo 1.2.0: Viết nội dung đoạn văn theo ý chính đã được gợi ý', layout, finalize=True, icon="Logo_Lycky (1).ico")
    return window

window1, window2, window3 = make_window1(), make_window2(), make_window3()
# window1.maximize()
window2.hide()
window3.hide()

while True:

    window, event, values = sg.read_all_windows()

    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    elif event == 'Gợi ý nội dung theo từ khóa':
        window.hide()
        window = window1 if window == window2 else window2
        window.un_hide()
        # window.maximize()
    elif event == 'Viết đoạn văn tự động theo gợi ý nội dung':
        window.hide()
        window = window1 if window == window3 else window3
        window.un_hide()
        # window.maximize()
    elif event == 'Về trang chủ':
        window.hide()
        # window = window1 if window == window3 else window1
        window = window1
        window.un_hide()
        # window.maximize()


window1.close()
window2.close()
window3.close()