import os
import openai
from dotenv import load_dotenv
import random
import PySimpleGUI as sg
import requests
import gspread
import webbrowser

# id-16-utu-and-dire-li@utu-and-dire-li.iam.gserviceaccount.com - Key gg sheet - nha.lucky.seo
# nguyenthanhha@utu-and-dire-li-11.iam.gserviceaccount.com - tuanhoangchatgtp@gmail.com tuan 123
# key 3-1 và 3-2 hoangtuanngocgpt tuan 123

# key vô gg sheet


gspread_key_list = ["116_Key_1.json",
                    "116_Nguyen_Thanh_Ha.json",
                    "116_Key_3_1.json",
                    "116_Key_3_2.json",
                    "116_Key_4_hoangtnchat.json",
                    "116_Key_4_2_hoangtnchat.json",
                    "116_Key_5_bui-lien-co.json",

                    "116_Key_6_gpthoangtuan.json"]

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
    'create_outline_Vietnamese': 'Create an outline for an essay in Vietnamese about:',
    'create_section_Vietnamese': 'Expand the blog section in to a detailed writing in Vietnamese about: ',
    'blog_ideas_Vietnamese': 'Give me blog topic ideas in Vietnamese on:',

    'create_outline_English': 'Create an outline for an essay about:',
    'create_section_English': 'Expand the blog section in to a detailed writing about:',
    'blog_ideas_English': 'Give me blog topic ideas on:',

    'create_outline_Mandarin': '用普通话写主题大纲关于:',
    'create_section_Mandarin': '用普通话细节地写这个主题的内容:',
    'blog_ideas_Mandarin': '用普通话写主题的heading 2目录:',

    'create_outline_Japanese': 'について日本語でエッセイのアウトラインを作成する:',
    'create_section_Japanese': 'ブログセクションを日本語で詳細に展開: ',
    'blog_ideas_Japanese': 'に関する日本語のブログ トピックのアイデアをください heading 2:',

    'create_outline_Korean': '대한 한국어 에세이의 개요를 작성:',
    'create_section_Korean': '한국어로 된 자세한 글로 블로그 섹션 확장: ',
    'blog_ideas_Korean': '한국어로 된 블로그 주제 아이디어 제공 heading 2:'
}

# chọn dòng AI đang hiện hành
OPEN_AI_ENGINE = 'text-davinci-003'

load_dotenv()
openai.api_key = key_api
print(openai.api_key)

# Bộ Tiếng Việt

def create_outline_Vietnamese(keyword, max_count=2500):

    full_cmd = '%s %s:'%(OPEN_AI_CMDS['create_outline_Vietnamese'], keyword)

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

def create_section_Vietnamese(topic, max_count=2500):

    full_cmd = '%s %s:'%(OPEN_AI_CMDS['create_section_Vietnamese'], topic)

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

def blog_ideas_Vietnamese(section, max_count=2500):

    full_cmd = '%s %s:'%(OPEN_AI_CMDS['blog_ideas_Vietnamese'], section)

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

# Bộ Tiếng Anh

def create_outline_English(keyword, max_count=2500):

    full_cmd = '%s %s:'%(OPEN_AI_CMDS['create_outline_English'], keyword)

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

def create_section_English(topic, max_count=3500):

    full_cmd = '%s %s:'%(OPEN_AI_CMDS['create_section_English'], topic)

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

def blog_ideas_English(section, max_count=2500):

    full_cmd = '%s %s:'%(OPEN_AI_CMDS['blog_ideas_English'], section)

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


# Bộ Tiếng Hoa

def create_outline_Mandarin(keyword, max_count=2500):

    full_cmd = '%s %s:'%(OPEN_AI_CMDS['create_outline_Mandarin'], keyword)

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

def create_section_Mandarin(topic, max_count=3500):

    full_cmd = '%s %s:'%(OPEN_AI_CMDS['create_section_Mandarin'], topic)

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

def blog_ideas_Mandarin(section, max_count=2500):

    full_cmd = '%s %s:'%(OPEN_AI_CMDS['blog_ideas_Mandarin'], section)

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


# Bộ Tiếng Nhật

def create_outline_Japanese(keyword, max_count=2500):

    full_cmd = '%s %s:'%(OPEN_AI_CMDS['create_outline_Japanese'], keyword)

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

def create_section_Japanese(topic, max_count=3500):

    full_cmd = '%s %s:'%(OPEN_AI_CMDS['create_section_Japanese'], topic)

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

def blog_ideas_Japanese(section, max_count=2500):

    full_cmd = '%s %s:'%(OPEN_AI_CMDS['blog_ideas_Japanese'], section)

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


# Bộ Tiếng Hàn

def create_outline_Korean(keyword, max_count=2500):

    full_cmd = '%s %s:'%(OPEN_AI_CMDS['create_outline_Korean'], keyword)

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

def create_section_Korean(topic, max_count=3500):

    full_cmd = '%s %s:'%(OPEN_AI_CMDS['create_section_Korean'], topic)

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

def blog_ideas_Korean(section, max_count=2500):

    full_cmd = '%s %s:'%(OPEN_AI_CMDS['blog_ideas_Korean'], section)

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


# Hàm chính

def openai_get_completion_result(openai_res):
    return openai_res['choices'][0]['text']


# Từ đây trở lên là code API nhập từ khóa và lấy dữ liệu của AI.
# Từ đây trở xuống là code giao diện và tính năng phần mềm



layout_main = [
    [sg.Text('Nhập từ khóa hoặc chủ đề muốn lập dàn bài (Heading 1) hoặc copy-edit-paste ý chính (Heading 2) muốn triển khai viết nội dung bằng ngôn ngữ muốn viết tại đây:')],
    [sg.Input(expand_x= True, key='KEYWORD')],

     [sg.Text('Bấm để xử lý các tác vụ Tiếng Việt:')],

    [sg.Button('Lập dàn bài học thuật Tiếng Việt', button_color=('white', 'green'), size=(30, 1)),
     sg.Button("Lập dàn bài (Heading 2) viết văn SEO Tiếng Việt", button_color=('white', 'blue'), size=(35, 1)),
     sg.Button("Triển khai viết tự động theo tiêu đề đã copy Tiếng Việt", button_color=('white', 'green'), size=(40, 1))],

    [sg.Text('Bấm để xử lý các tác vụ các ngôn ngữ khác:')],

    [sg.Button('Lập dàn bài học thuật Tiếng Anh', size=(30, 1)),
    sg.Button("Lập dàn bài (Heading 2) viết văn SEO Tiếng Anh", size=(35, 1)),
    sg.Button("Triển khai viết tự động theo tiêu đề đã copy Tiếng Anh", size=(40, 1))],

    [sg.Button('Lập dàn bài học thuật Tiếng Hoa', button_color=('white', 'grey'), size=(30, 1)),
    sg.Button("Lập dàn bài (Heading 2) viết văn SEO Tiếng Hoa", button_color=('white', 'grey'), size=(35, 1)),
    sg.Button("Triển khai viết tự động theo tiêu đề đã copy Tiếng Hoa", button_color=('white', 'grey'), size=(40, 1))],

    [sg.Button('Lập dàn bài học thuật Tiếng Hàn', size=(30, 1)),
    sg.Button("Lập dàn bài (Heading 2) viết văn SEO Tiếng Hàn", size=(35, 1)),
    sg.Button("Triển khai viết tự động theo tiêu đề đã copy Tiếng Hàn", size=(40, 1))],

    [sg.Button('Lập dàn bài học thuật Tiếng Nhật', button_color=('white', 'grey'), size=(30, 1)),
    sg.Button("Lập dàn bài (Heading 2) viết văn SEO Tiếng Nhật", button_color=('white', 'grey'), size=(35, 1)),
    sg.Button("Triển khai viết tự động theo tiêu đề đã copy Tiếng Nhật", button_color=('white', 'grey'), size=(40, 1)),

    sg.Button('Xóa nội dung cũ & nhập mới'),
    sg.Button("SEO & Tools' Tips", button_color=('white', 'blue')),
    sg.Button("Tips Hướng Nghiệp HS-SV", button_color=('white', 'green')),
    sg.Button("Tips Quản Trị DN & Marketing", button_color=('white', 'orange')),
    sg.Button("Hướng Dẫn Sử Dụng Phần Mềm", button_color=('white', 'purple'))],


    [sg.Text('Vui lòng chờ vài giây. Phần mềm đang xử lý và sẽ hiển thị kết quả dưới đây:')],

    [sg.Output(expand_x= True, expand_y= True, size=(80, 25), key= "OUTPUT-1"),
     sg.Output(expand_x= True, expand_y= True, size=(80, 25), key= "OUTPUT-2"),
     sg.Output(expand_x= True, expand_y= True, size=(80, 25), key= "OUTPUT-3"),],

    [ sg.Button("Bấm duyệt website tích điểm", button_color=('white', 'black')),
      sg.Button('Exit', button_color=('white','red')),
      sg.Text("Liên kết ngẫu nhiên:"),
      sg.Text("Hiện chưa kịp xây dựng thư viện. Sau này anh em tlseo xây dựng cùng.", text_color="#0000EE", enable_events=True, key="-LINK-NGAU-NHIEN-")]
    ]

window_main = sg.Window('tlseo 1.2.1: Phần mềm viết content SEO & viết luận văn tốt nghiệp & học ngoại ngữ tự động tiếng Việt - Anh - Hoa - Hàn - Nhật',
                   layout_main, finalize=True, icon="Logo_Lycky (1).ico", keep_on_top= True)

window_main.maximize()
window_main.finalize()
# window.read()

keyword = None

def clear_input():
    for key in values:
        window_main[key]("")
    return None

while True:
    event, values = window_main.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        sg.popup("Chân thành cám ơn bạn đã sử dụng tlseo 1.2.1 và duyệt website đồng hành cùng các đơn vị tài trợ đội ngũ phát triển hệ thống phần mềm tlseo!", icon="Logo_Lycky (1).ico", keep_on_top= True)
        break

    elif event == 'Xóa nội dung cũ & nhập mới':
           clear_input()

    elif event == "-LINK-NGAU-NHIEN-":
        webbrowser.open("https://google.com.vn")

    # Bộ Tiến Việt

    elif event == 'Lập dàn bài học thuật Tiếng Việt':
        keyword = values["KEYWORD"]
        # print(keyword)
        tieng_viet = create_outline_Vietnamese(keyword, max_count=2000)
        window_main["OUTPUT-1"].update(value=tieng_viet)

    elif event == 'Lập dàn bài (Heading 2) viết văn SEO Tiếng Việt':
        keyword = values["KEYWORD"]
        # print(keyword)
        tieng_viet = blog_ideas_Vietnamese(keyword, max_count=2000)
        window_main["OUTPUT-2"].update(value=tieng_viet)

    elif event == 'Triển khai viết tự động theo tiêu đề đã copy Tiếng Việt':
        keyword = values["KEYWORD"]
        # print(keyword)
        tieng_viet = create_section_Vietnamese(keyword, max_count=3500)
        window_main["OUTPUT-3"].update(value=tieng_viet)

    # Bộ Tiếng Anh


    elif event == 'Lập dàn bài học thuật Tiếng Anh':
        keyword = values["KEYWORD"]
        # print(keyword)
        tieng_anh = create_outline_English(keyword, max_count=2000)
        window_main["OUTPUT-1"].update(value=tieng_anh)

    elif event == 'Lập dàn bài (Heading 2) viết văn SEO Tiếng Anh':
        keyword = values["KEYWORD"]
        # print(keyword)
        tieng_anh = blog_ideas_English(keyword, max_count=2000)
        window_main["OUTPUT-2"].update(value=tieng_anh)

    elif event == 'Triển khai viết tự động theo tiêu đề đã copy Tiếng Anh':
        keyword = values["KEYWORD"]
        # print(keyword)
        tieng_anh = create_section_English(keyword, max_count=3500)
        window_main["OUTPUT-3"].update(value=tieng_anh)

    # Bộ Tiếng Hoa


    elif event == 'Lập dàn bài học thuật Tiếng Hoa':
        keyword = values["KEYWORD"]
        # print(keyword)
        tieng_hoa = create_outline_Mandarin(keyword, max_count=2000)
        window_main["OUTPUT-1"].update(value=tieng_hoa)

    elif event == 'Lập dàn bài (Heading 2) viết văn SEO Tiếng Hoa':
        keyword = values["KEYWORD"]
        # print(keyword)
        tieng_hoa = blog_ideas_Mandarin(keyword, max_count=2000)
        window_main["OUTPUT-2"].update(value=tieng_hoa)

    elif event == 'Triển khai viết tự động theo tiêu đề đã copy Tiếng Hoa':
        keyword = values["KEYWORD"]
        # print(keyword)
        tieng_hoa = create_section_Mandarin(keyword, max_count=3500)
        window_main["OUTPUT-3"].update(value=tieng_hoa)

    # Bộ Tiếng Nhật


    elif event == 'Lập dàn bài học thuật Tiếng Nhật':
        keyword = values["KEYWORD"]
        # print(keyword)
        tieng_nhat = create_outline_Japanese(keyword, max_count=2000)
        window_main["OUTPUT-1"].update(value=tieng_nhat)

    elif event == 'Lập dàn bài (Heading 2) viết văn SEO Tiếng Nhật':
        keyword = values["KEYWORD"]
        # print(keyword)
        tieng_nhat = blog_ideas_Japanese(keyword, max_count=2000)
        window_main["OUTPUT-2"].update(value=tieng_nhat)

    elif event == 'Triển khai viết tự động theo tiêu đề đã copy Tiếng Nhật':
        keyword = values["KEYWORD"]
        # print(keyword)
        tieng_nhat = create_section_Japanese(keyword, max_count=3500)
        window_main["OUTPUT-3"].update(value=tieng_nhat)


    # Bộ Tiếng Hàn


    elif event == 'Lập dàn bài học thuật Tiếng Hàn':
        keyword = values["KEYWORD"]
        # print(keyword)
        tieng_han = create_outline_Korean(keyword, max_count=2000)
        window_main["OUTPUT-1"].update(value=tieng_han)

    elif event == 'Lập dàn bài (Heading 2) viết văn SEO Tiếng Hàn':
        keyword = values["KEYWORD"]
        # print(keyword)
        tieng_han = blog_ideas_Korean(keyword, max_count=2000)
        window_main["OUTPUT-2"].update(value=tieng_han)

    elif event == 'Triển khai viết tự động theo tiêu đề đã copy Tiếng Hàn':
        keyword = values["KEYWORD"]
        # print(keyword)
        tieng_han = create_section_Korean(keyword, max_count=3500)
        window_main["OUTPUT-3"].update(value=tieng_han)
