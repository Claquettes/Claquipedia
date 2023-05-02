import wikipediaapi
import tkinter as tk
from PIL import Image


def search_wikipedia():
    # Get the input text from the entry field
    input_text = entry.get()
    
    # Use the Wikipedia API to search for the input text
    wiki = wikipediaapi.Wikipedia(lang.get())
    page = wiki.page(input_text)
    
    # If the page exists, display its content in the text box
    if page.exists():
        output_text.delete('1.0', tk.END)
        output_text.insert('1.0', page.text)
    # If the page does not exist, display an error message
    else:
        output_text.delete('1.0', tk.END)
        output_text.insert('1.0', 'Page not found.')
    

def copy_text():
    text = output_text.get('1.0', tk.END)
    truncated_text = text[:3999] # We truncate the text to 3999 characters, because discord has a limit of 4000 characters
    window.clipboard_clear()
    window.clipboard_append(text)
    # We change the text of the copy button to indicate that the text has been copied
    copy_button.config(text='Copied!')

# Create the GUI window
window = tk.Tk()
window.title('Wikipedia Search')

# We change the color of the window,and of the text
window.configure(bg='#24273a')
window.option_add('*Font', 'Helvetica 12')
# we change the color of the buttons and input
window.option_add('*Button.Background', '#24273a')
window.option_add('*Button.Foreground', 'white')
window.option_add('*Entry.Background', '#24273a')
window.option_add('*Entry.Foreground', 'white')
window.option_add('*Label.Background', '#24273a')
window.option_add('*Label.Foreground', 'white')
window.option_add('*Text.Background', '#24273a')
window.option_add('*Text.Foreground', 'white')
# We change the color of the output text
window.option_add('*Text.Background', '#24273a')
window.option_add('*Text.Foreground', 'white')
# We change the color of the scrollbar, and of the options menu
window.option_add('*Scrollbar.Background', '#24273a')
window.option_add('*Scrollbar.Foreground', 'white')
window.option_add('*TCombobox.Background', '#24273a')
window.option_add('*TCombobox.Foreground', 'white')
# We change the color of the menu
window.option_add('*Menu.Background', '#24273a')
window.option_add('*Menu.Foreground', 'white')




lang = tk.StringVar()
# We add a label to indicate the purpose of the menu
lang_label = tk.Label(window, text='Choose a language:')
lang_label.grid(row=0, column=0, columnspan=2)
# We create an option menu to choose the language
lang_menu = tk.OptionMenu(window, lang, 'en', 'fr', 'es', 'de', 'it', 'pt', 'ru', 'ja', 'zh', 'ar', 'hi', 'ko', 'tr', 'pl', 'zh-tw')
lang_menu.grid(row=0, column=2, columnspan=2)

# Create the input label and entry field
input_label = tk.Label(window, text='Input a word:')
input_label.grid(row=3, column=0)
entry = tk.Entry(window)
entry.grid(row=3, column=1)

# Create the search button
search_button = tk.Button(window, text='Search', command=search_wikipedia)
search_button.grid(row=4, column=0, columnspan=2)

# Create the copy button
copy_button = tk.Button(window, text='Copy', command=copy_text)
copy_button.grid(row=4, column=2)

# Create the output label and text box
output_label = tk.Label(window, text='Wikipedia page content:')
output_label.grid(row=5, column=0)
#we delete every character that is after the 3999th character
output_text = tk.Text(window, height=10, width=50)

output_text.grid(row=5, column=0, columnspan=2)
# we add padding to the text box
output_text.config(padx=10, pady=10)


# Start the GUI loop
window.mainloop()
