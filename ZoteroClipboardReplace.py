import keyboard
import pyperclip
import time


# 新增一个全局变量来控制程序运行状态
is_paused = False
is_word = True
is_onlyOriginal = False
is_once = True


def format_zoteroword_markdown(original_text):
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
    global is_onlyOriginal
    if is_once:
        is_onlyOriginal = True
        print('Turn to OnlyOriginal')
    return formatted_text


def format_zoterosentence_markdown(original_text):
    # Splitting the text into components
    parts = original_text.split("” ")
    sentence = parts[0].strip("“")  # Extracting the word
    citations_links, pdf_citations_links, chinese_definition = parts[1].split(") ", 2)

    # Reformatting citations and links
    citations_links_formatted = citations_links + ")"
    pdf_citations_links_formatted = pdf_citations_links + ")"
    # Formatting the final string
    formatted_text = f">{sentence}\n{citations_links_formatted}{pdf_citations_links_formatted}\n{chinese_definition}"
    print(sentence+' Formatted!')
    global is_onlyOriginal
    if is_once:
        is_onlyOriginal = True
        print('Turn to OnlyOriginal')
    return formatted_text


def format_zoteroword_markdown_onlyoriginal(original_text):
    return original_text.split("” ")[0].strip("“")


def toggle_pause():
    global is_paused
    is_paused = not is_paused
    print('Paused' if is_paused else 'Resumed')


def toggle_word_sentence():
    global is_word
    is_word = not is_word
    print('Word' if is_word else 'Sentence')


def toggle_onlyOriginal():
    global is_onlyOriginal
    is_onlyOriginal = not is_onlyOriginal
    print('OnlyOriginal' if is_onlyOriginal else 'NotOnlyOriginal')


def toggle_once():
    global is_once
    is_once = not is_once
    print('Once' if is_once else 'NotOnce')

def main():
    last_txt = pyperclip.paste()
    transferred_text = pyperclip.paste()
    key_detect = "([pdf](zotero:"
    # 监听Ctrl+9按键
    keyboard.add_hotkey('ctrl+9', toggle_pause)
    keyboard.add_hotkey('ctrl+8', toggle_word_sentence)
    keyboard.add_hotkey('ctrl+7', toggle_onlyOriginal)
    keyboard.add_hotkey('ctrl+6', toggle_once)

    print('Start!')
    print('Press Ctrl+9 to pause/resume, and Ctrl+8 to switch word/sentence, and Ctrl+7 to switch onlyOriginal, and Ctrl+6 to switch once')
    print('Now ,is_word is '+str(is_word)+', is_onlyOriginal is '+str(is_onlyOriginal)+', is_paused is '+str(is_paused)+', is_once is '+str(is_once))

    while True:
        time.sleep(0.5)  # Add a short delay to reduce CPU usage
        if is_paused:  # 如果程序被暂停，则跳过当前循环
            continue
        try:
            txt = pyperclip.paste()  # Get current clipboard text
            if key_detect in txt and txt != last_txt and txt != transferred_text:
                last_txt = txt  # Update last_txt
                if is_onlyOriginal:
                    transferred_text = format_zoteroword_markdown_onlyoriginal(txt)
                elif is_word:
                    transferred_text = format_zoteroword_markdown(txt)
                else:
                    transferred_text = format_zoterosentence_markdown(txt)
                pyperclip.copy(transferred_text)  # Copy processed text to clipboard
        except Exception as e:
            print(f"An error occurred: {e}")  # Print exception details


if __name__ == "__main__":
    main()
