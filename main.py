import wikipediaapi
import tkinter as tk
from PIL import Image


def search_wikipedia():
    # Get the input text from the entry field
    input_text = entry.get()
    
    # Use the Wikipedia API to search for the input text
    wiki = wikipediaapi.Wikipedia('en')
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
    # Get the text from the text box
    text = output_text.get('1.0', tk.END)
    
    # Copy the text to the clipboard
    window.clipboard_clear()
    window.clipboard_append(text)

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






# Create the input label and entry field
input_label = tk.Label(window, text='Input a word:')
input_label.grid(row=0, column=0)
entry = tk.Entry(window)
entry.grid(row=0, column=1)

# Create the search button
search_button = tk.Button(window, text='Search', command=search_wikipedia)
search_button.grid(row=1, column=0, columnspan=2)

# Create the copy button
copy_button = tk.Button(window, text='Copy', command=copy_text)
copy_button.grid(row=1, column=2)


# Create the output label and text box
output_label = tk.Label(window, text='Wikipedia page content:')
output_label.grid(row=2, column=0)
output_text = tk.Text(window)
output_text.grid(row=3, column=0, columnspan=2)
# we add padding to the text box
output_text.config(padx=10, pady=10)



# Start the GUI loop
window.mainloop()
