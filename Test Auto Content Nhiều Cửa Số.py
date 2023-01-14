import os
import openai
from dotenv import load_dotenv
import random
import PySimpleGUI as sg
import requests
import gspread
import webbrowser

gspread_key_list = ["116_Key_1.json",
                    "116_Nguyen_Thanh_Ha.json",
                    "116_Key_3_1.json",
                    "116_Key_3_2.json",
                    "116_Key_4_hoangtnchat.json",
                    "116_Key_4_2_hoangtnchat.json",
                    "116_Key_5_bui-lien-co.json"]

gspread_key = random.choice(gspread_key_list)
print(gspread_key)
gs = gspread.service_account(gspread_key)

# lấy AI key
sheet_key_api = gs.open_by_url("https://docs.google.com/spreadsheets/d/1tdy2pLs_pU-rHFigWD5sxrG-TCHeIfAhog6YGe98Gdw/edit#gid=2129285762")
worksheet_key_api = sheet_key_api.get_worksheet(1)
key_api = random.choice(worksheet_key_api.col_values(2))
# print(key_api)

# lấy url marketing
worksheet_url_marketing = sheet_key_api.get_worksheet(0)
url_marketing = random.choice(worksheet_url_marketing.col_values(2))

OPEN_AI_CMDS = {
    'Viết gợi ý từ khóa': 'Hãy viết vài gợi ý đề mục H2 cho từ khóa sau:',
    'Viết đoạn văn': 'Hãy viết một đoạn văn về đề tài sau: ',
    'Viết tản văn': 'Viết một đoạn văn lãng mạn về đề tài:',
    'create_outline': 'Create an outline for an essay about',
    'create_section': 'Expand the blog section in to a detailed',
    'blog_ideas': 'Give me blog topic ideas on',
    '中文的大纲': '关于以下内容的论文创建中文的大纲'
}

# chọn dòng AI đang hiện hành
OPEN_AI_ENGINE = 'text-davinci-003'

load_dotenv()
openai.api_key = key_api
print(openai.api_key)

keyword = None
# print(keyword)
topic = None
# print()

# Mai test sửa keyword ở đây
def openai_goi_y_h2(keyword, max_count=2500):

    full_cmd = '%s %s:'%(OPEN_AI_CMDS['Viết gợi ý từ khóa'], keyword)

    res = openai.Completion.create(
        engine=OPEN_AI_ENGINE,
        prompt=full_cmd,
        temperature=0.7,
        max_tokens=max_count,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return openai_get_completion_result(res)

def openai_viet_doan_van(topic, max_count=2500):

    full_cmd = '%s %s:'%(OPEN_AI_CMDS['Viết đoạn văn'], topic)

    res = openai.Completion.create(
        engine=OPEN_AI_ENGINE,
        prompt=full_cmd,
        temperature=0,
        max_tokens=max_count,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return openai_get_completion_result(res)

def openai_viet_tan_van(section, max_count=2500):

    full_cmd = '%s %s:'%(OPEN_AI_CMDS['Viết tản văn'], section)

    res = openai.Completion.create(
        engine=OPEN_AI_ENGINE,
        prompt=full_cmd,
        temperature=0.7,
        max_tokens=max_count,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return openai_get_completion_result(res)

def openai_get_completion_result(openai_res):
    return openai_res['choices'][0]['text']

layout = [
    [sg.Text('Nhập từ khóa chính nội dung bài bạn muốn viết (tương đương H1):')],
    [sg.Input(expand_x= True, key='KEYWORD-GOI-Y-H2')],
    [sg.Button('Xuất ra dữ liệu các H2'), sg.Button("Nhập từ khóa khác"), sg.Button("Bấm duyệt website tích điểm"), sg.Button("SEO & Tools' tips")],
    [sg.Text('Gợi ý các ý chính (H2) của AI cho bài viết theo từ khóa bạn đã chọn như sau:')],
    [sg.Output(expand_x= True, size=(80, 25), key= "OUTPUT-GOI-Y-H2")],

    [sg.Button('Về trang chủ'), sg.Button('Exit')]]

window = sg.Window('tlseo 1.2.0: Phần Mềm Tự Động Viết Content Tiếng Việt, Tiếng Anh, Tiếng Hoa', layout, finalize=True, icon="Logo_Lycky (1).ico", keep_on_top= True)


#
# def window_main():
#     layout = [[sg.Text('Phần Mềm Viết Bài Tiếng Việt Tự Động')],
#               [sg.Button('Gợi ý đề mục H2 theo từ khóa'), sg.Button('Viết đoạn văn tự động theo một gợi ý nội dung H2')],
#               [sg.Button('Viết tản văn'),
#                sg.Button('Tám chuyện với Robot AI'), sg.Button("Bấm duyệt website tích điểm")],
#               [sg.Button('Exit')]]
#     window = sg.Window('tlseo 1.2.0: Phần Mềm SEO Viết Content Tiếng Việt Tự Động', layout, finalize=True, icon="Logo_Lycky (1).ico", keep_on_top= True)
#     return window
#
#
# def window_goi_y_h2():
#     layout = [
#         [sg.Text('Nhập từ khóa chính nội dung bài bạn muốn viết (tương đương H1):')],
#         [sg.Input(expand_x= True, key='KEYWORD-GOI-Y-H2')],
#         [sg.Button('Xuất ra dữ liệu các H2'), sg.Button("Nhập từ khóa khác"), sg.Button("Bấm duyệt website tích điểm"), sg.Button("SEO & Tools' tips")],
#         [sg.Text('Gợi ý các ý chính (H2) của AI cho bài viết theo từ khóa bạn đã chọn như sau:')],
#         [sg.Output(expand_x= True, size=(80, 25), key= "OUTPUT-GOI-Y-H2")],
#
#         [sg.Button('Về trang chủ'), sg.Button('Exit')]]
#
#     window = sg.Window('tlseo 1.2.0: Gợi ý các ý chính hoặc tiêu đề H2 chính của bài viết theo từ khóa', layout, finalize=True, icon="Logo_Lycky (1).ico", keep_on_top= True)
#     return window
#
# def window_viet_doan_van():
#     layout = [[sg.Text('Viết nội dung đoạn văn theo ý chính (H2) đã được gợi ý và được bạn chỉnh sửa:')],
#               [sg.Input(expand_x=True, key='TOPIC-VIET-DOAN-VAN')],
#               [sg.Button('Xuất ra dữ liệu viết đoạn văn'), sg.Button("Nhập ý chính H2 khác"), sg.Button("Bấm duyệt website tích điểm"),
#                sg.Button("SEO & Tools' tips")],
#               [sg.Text('Đoạn văn được phần mềm viết theo ý chính (H2) bạn đã được gợi ý và tự chỉnh sửa như sau:')],
#               [sg.Output(expand_x=True, size=(80, 25), key="OUTPUT-VIET-DOAN-VAN")],
#
#                [sg.Button('Về trang chủ'), sg.Button('Exit')]]
#     window = sg.Window('tlseo 1.2.0: Viết nội dung đoạn văn theo ý chính đã được gợi ý', layout, finalize=True, icon="Logo_Lycky (1).ico", keep_on_top= True)
#     return window
#
# def window_viet_tan_van():
#     layout = [[sg.Text('Viết nội dung tản văn: ')],
#                [sg.Button('Về trang chủ'), sg.Button('Exit')]]
#     window = sg.Window('tlseo 1.2.0: Viết nội dung đoạn văn theo ý chính đã được gợi ý', layout, finalize=True, icon="Logo_Lycky (1).ico", keep_on_top= True)
#     return window


# window_main, window_goi_y_h2, window_viet_doan_van, window_viet_tan_van = window_main(), window_goi_y_h2(), window_viet_doan_van(), window_viet_tan_van()
# # window1.maximize()
# window_goi_y_h2.hide()
# window_viet_doan_van.hide()
# window_viet_tan_van.hide()

def clear_input():
    for key in values:
        window[key]("")
    return None
#
# key_word = None
#
# while True:
#
#     window, event, values = sg.read_all_windows()
#
#     if event in (sg.WINDOW_CLOSED, 'Exit'):
#         # sg.popup("Text will be here", icon="Logo_Lycky (1).ico")
#         break
#
#     elif event == 'Gợi ý đề mục H2 theo từ khóa':
#         window.hide()
#         window = window_goi_y_h2
#         window.un_hide()
#         # window.maximize()
#
#     elif event == 'Viết đoạn văn tự động theo một gợi ý nội dung H2':
#         window.hide()
#         window = window_viet_doan_van
#         window.un_hide()
#         # window.maximize()
#
#     elif event == 'Về trang chủ':
#         window.hide()
#         # window = window1 if window == window3 else window1
#         window = window_main
#         window.un_hide()
#         # window.maximize()
#
#     elif event == 'Nhập từ khóa khác':
#         clear_input()
#
#     elif event == 'Nhập ý chính H2 khác':
#         clear_input()
#
#     elif event == 'Xuất ra dữ liệu các H2':
#         keyword = values["KEYWORD-GOI-Y-H2"]
#         # print(keyword)
#         goi_y_h2 = openai_goi_y_h2(keyword, max_count=2000)
#         window["OUTPUT-GOI-Y-H2"].update(value=goi_y_h2)
#         # clear_input()
#
#     elif event == 'Xuất ra dữ liệu viết đoạn văn':
#         topic = values["TOPIC-VIET-DOAN-VAN"]
#         print(topic)
#         viet_doan_van = openai_viet_doan_van(topic, max_count=3500)
#         print(viet_doan_van)
#         window["OUTPUT-VIET-DOAN-VAN"].update(value=viet_doan_van)
#         # clear_input()
#
#
#     elif event == 'Bấm duyệt website tích điểm':
#         webbrowser.open(url_marketing)
#         sg.popup("Trình duyệt mở liên kết đơn vị tài trợ.",
#                  "Vui lòng để trình duyệt chạy tối thiểu 10 giây.",
#                  "Bấm duyệt liên kết đơn vị tài trợ và coi tối thiểu 30 giây có tác vụ được cộng điểm tài trợ",
#                  "Trình duyệt chạy phía sau không ảnh hưởng hoạt động phần mềm hay các ứng dụng khác.",
#                  "Bấm OK để đóng cửa sổ này",
#                  "Chân thành cám ơn!", icon="Logo_Lycky (1).ico", keep_on_top= True)
#
#     elif event == "SEO & Tools' tips":
#         clear_input()
#
# print(keyword)
# print(topic)
#
# window_main.close()
# window_goi_y_h2.close()
# window_viet_doan_van.close()


# a = openai_viet_doan_van("băng tải việt phát", max_count= 2000)
# print(a)

# b = openai_goi_y_h2("băng tải việt phát", max_count= 2500)
# print(b)

# c = openai_viet_tan_van("Viết một bức xin thôi việc", max_count= 2500)
# print(c)