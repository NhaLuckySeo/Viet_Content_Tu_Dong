import PySimpleGUI as sg
import webbrowser

layout = [
    [
        sg.Text("Cài link của mình vô đây. Đây là anchor text.", text_color="#0000EE", enable_events=True, key="-LINK-"),
        sg.Button("Pop Up")
    ]
]

window = sg.Window("Hyperlink", layout, finalize=True)

layout_2 = [
    [
        sg.Text("Hiển thị lại.", text_color="#0000EE", enable_events=True, key="-LINK-HTL"),
        # sg.Button("Pop Up")
    ]
]
window_2 = sg.Window("Hiển thị lại", layout_2)

# window["-LINK-"].set_cursor("hand2")
# window["-LINK-"].Widget.bind("<Enter>", lambda _: window["-LINK-"].update(font=(None, 20, "underline")))
# window["-LINK-"].Widget.bind("<Leave>", lambda _: window["-LINK-"].update(font=(None, 20)))

def display_again():
    layout_2 = [
    [
        sg.Text("Hiển thị lại.", text_color="#0000EE", enable_events=True, key="-LINK-HTL"),
    ]
    ]
    window_2 = sg.Window("Hiển thị lại", layout_2)
    while True:
        event, values = window_2.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "-LINK-HTL":
            webbrowser.open("https://tuoitre.vn/")
    window_2.close()


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        display_again()
        break

    elif event == "-LINK-":
        webbrowser.open("https://www.pysimplegui.org/")



window.close()