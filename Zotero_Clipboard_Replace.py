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
    print('Formatted!')
    return formatted_text

last_txt = pyperclip.paste()
transferred_text = pyperclip.paste()
key_detect = "([pdf](zotero:"
while True:
    time.sleep(0.5)  # Add a short delay to reduce CPU usage
    try:
        txt = pyperclip.paste()  # Get current clipboard text
        if key_detect in txt and txt != last_txt:
            last_txt = txt  # Update last_txt
            transferred_text = format_text_v3(txt)  # Process text
            pyperclip.copy(transferred_text)  # Copy processed text to clipboard
    except Exception as e:
        print(f"An error occurred: {e}")  # Print exception details
