from tkinter import *
import unwumbo

def text_summary():
  text_button.destroy()
  file_button.destroy()
  welcome_label.destroy()

  text_label = Label(root, text = "Enter the text you would like summarized:\n")
  text_label.grid(row = 0)

  e = Entry(root, textvariable = user_input)
  e.grid(row = 1)

  unwumbo_button = Button(root, text = "Unwumbo", command = print_text)
  unwumbo_button.grid(row = 3, column = 1)

def print_text():

  for widget in root.winfo_children():
    widget.destroy()
  text = user_input.get()
  words = unwumbo.get_words(text)
  words = unwumbo.remove_common_words(words)
  words_dict = unwumbo.get_word_dictionary(words)
  sentences = unwumbo.get_sentences(text)

  summary = unwumbo.most_relevant_sentences(words_dict, sentences, 5)

  Message(root, text = summary).grid(row = 4, column = 0)

def file_summary():
  text_button.destroy()
  file_button.destroy()
  welcome_label.destroy()

  file_label = Label(root, text = "Enter the file name you would like summarized:\n")
  file_label.grid(row = 0)

  e = Entry(root, textvariable = user_input)
  e.grid(row = 1)

  unwumbo_button = Button(root, text = "Unwumbo", command = print_file)
  unwumbo_button.grid(row = 3, column = 1)

def print_file():

  for widget in root.winfo_children():
    widget.destroy()
  text = unwumbo.get_file_input(user_input.get())
  words = unwumbo.get_words(text)
  words = unwumbo.remove_common_words(words)
  words_dict = unwumbo.get_word_dictionary(words)
  sentences = unwumbo.get_sentences(text)

  summary = unwumbo.most_relevant_sentences(words_dict, sentences, 5)

  Message(root, text = summary).grid(row = 4, column = 0)

root = Tk()
root.title('Unwumbo')

user_input = StringVar()

welcome_label = Label(root, text = '''Welcome to Unwumbo! Would you like to
    summarize a file or summarize your own typed in text?''')
welcome_label.grid(row = 0)

text_button = Button(root, text = "Summarize inputted text", command = text_summary)
text_button.grid(row = 2, column = 1)

file_button = Button(root, text = "Summarize a file", command = file_summary)
file_button.grid(row = 3, column = 1)

mainloop()
