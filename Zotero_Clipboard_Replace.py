import pyperclip
import time


def format_text_v3(original_text):
    # Splitting the text into components
    parts = original_text.split("” ")
    word = parts[0].strip("“")  # Extracting the word
    citations_links, pdf_citations_links, chinese_definition = parts[1].split(") ", 2)

    # Reformatting citations and links
    citations_links_formatted = citations_links + ")"
    pdf_citations_links_formatted = pdf_citations_links + ")"
    # Formatting the final string
    formatted_text = f"{word}|{chinese_definition}|{citations_links_formatted}{pdf_citations_links_formatted}"

    return formatted_text


last_txt = pyperclip.paste()
transferred_tet = pyperclip.paste()
while True:
    # txt 存放当前剪切板文本
    txt = pyperclip.paste()
    # 剪切板内容和上一次对比如有变动，再进行内容判断，判断后如果发现有指定字符在其中的话，再执行替换
    try:
        if txt != last_txt or txt != transferred_tet:
            last_txt = txt  # 没查到要替换的子串，返回None
            transferred_tet = format_text_v3(txt)
            pyperclip.copy(transferred_tet)
        time.sleep(0.2)
        # 检测间隔（延迟0.2秒）
    except:
        pass
