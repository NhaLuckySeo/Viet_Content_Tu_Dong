
import PySimpleGUI as sg

layout = [
    [sg.Text('Nhập mã hàng muốn lấy dữ liệu:')],
    [sg.Input(key='get-data')],
    [sg.Button('Xuất ra dữ liệu')],
    [sg.Output(size=(80, 20))],
]

window = sg.Window('Quản lý dữ liệu sản phẩm theo mã hàng', layout)

while True:
    event, values = window.read()
    if event == 'Xuất ra dữ liệu':
        prompt = values['get-data']
        # generated_text = generate_text(prompt)
        # print(generated_text, end='\n\n')
    elif event in (None, 'Exit'):

        sg.PopupTimed('Đồng hồ đếm ngược:', title='Pop-up', timeout=5)
        break

window.close()