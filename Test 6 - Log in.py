import winreg

def get_installed_browsers():
    browsers = []
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Clients\StartMenuInternet")
    for i in range(winreg.QueryInfoKey(key)[0]):
        name = winreg.EnumKey(key, i)
        subkey = winreg.OpenKey(key, name)
        try:
            path, _ = winreg.QueryValueEx(subkey, "")
            browsers.append(path)
        except WindowsError:
            pass
    return browsers

print(get_installed_browsers())

import random
import webbrowser

browsers = get_installed_browsers()

browser_aliases = {
    "Mozilla Firefox": "firefox",
    "Google Chrome": "chrome",
    "Internet Explorer": "iexplore",
    "Microsoft Edge": "edge",
    "Safari": "safari",
}

selected_browser = random.choice(browsers)

# chuyển đổi tên đầy đủ của trình duyệt thành tên tắt
alias = browser_aliases.get(selected_browser, selected_browser)

if webbrowser.get(alias):
    webbrowser.get(alias).open("http://www.google.com")
else:
    print(f"{selected_browser} is not supported")

# import threading
#
# def task():
#     print("Thread is running")
#
# # Tạo thread
# thread = threading.Thread(target=task)
#
# # Chạy thread
# thread.start()
#
# # Chờ cho thread kết thúc
# thread.join()
#
# print("Thread has ended")
#
#
#
#
#
#
# import random
#
# # Tạo số thực ngẫu nhiên trong đoạn từ 0.5 đến 2.5
# x = random.uniform(0.5, 2.5)
# print(x)
#
#
#
#
#
#
#





#
#
# import PySimpleGUI as sg
# import pandas as pd
#
# # load data from excel
# data = pd.read_excel('user_data.xlsx')
#
# layout = [
#     [sg.Text('Username')],
#     [sg.Input(key='username')],
#     [sg.Text('Password')],
#     [sg.Input(key='password', password_char='*')],
#     [sg.Button('Sign In'), sg.Button('Sign Up')],
# ]
#
# window = sg.Window('User Authentication', layout)
#
# while True:
#     event, values = window.read()
#
#     if event == sg.WIN_CLOSED:
#         break
#
#     if event in (None, 'Sign In'):
#         # check username and password
#         if (data['username'] == values['username']).any():
#             user_data = data[data['username'] == values['username']]
#             if user_data['password'].values[0] == values['password']:
#                 sg.popup("Welcome!")
#                 break
#             else:
#                 sg.popup("Incorrect Password!")
#         else:
#             sg.popup("Username not found!")
#     elif event == 'Sign Up':
#         # add new user to the data
#         new_user = {'username': [values['username']], 'password': [values['password']]}
#         new_user = pd.DataFrame(data=new_user)
#         data = data.append(new_user)
#         data.to_excel('user_data.xlsx', index=False)
#         sg.popup("New user created!")
#
# window.close()
