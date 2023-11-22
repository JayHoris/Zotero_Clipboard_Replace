import keyboard
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
    print(word+' Formatted!')
    return formatted_text


# 新增一个全局变量来控制程序运行状态
is_paused = False


def toggle_pause():
    global is_paused
    is_paused = not is_paused
    print('Paused' if is_paused else 'Resumed')


def main():
    last_txt = pyperclip.paste()
    transferred_text = pyperclip.paste()
    key_detect = "([pdf](zotero:"
    # 监听Ctrl+9按键
    keyboard.add_hotkey('ctrl+9', toggle_pause)

    while True:
        time.sleep(0.5)  # Add a short delay to reduce CPU usage
        if is_paused:  # 如果程序被暂停，则跳过当前循环
            continue
        try:
            txt = pyperclip.paste()  # Get current clipboard text
            if key_detect in txt and txt != last_txt and txt != transferred_text:
                last_txt = txt  # Update last_txt
                transferred_text = format_text_v3(txt)  # Process text
                pyperclip.copy(transferred_text)  # Copy processed text to clipboard
        except Exception as e:
            print(f"An error occurred: {e}")  # Print exception details


if __name__ == "__main__":
    main()
