from tkinter import *
import unwumbo

def print_summary():
  button.destroy()
  label.destroy()
  e.grid_forget()
  text = unwumbo.get_file_input(e.get())
  words = unwumbo.get_words(text)
  words_dict = unwumbo.get_word_dictionary(words)
  sentences = unwumbo.get_sentences(text)

  summary = unwumbo.most_relevant_sentences(words_dict, sentences, 5)

  Message(root, text = summary).grid(row = 4, column = 0)

root = Tk()
root.title('Unwumbo')
#root.geometry("400x400+0+0")

label = Label(root, text = "Enter file name ")
label.grid(row = 0)

e = Entry(root)
e.grid(row = 0, column = 1)

button = Button(root, text = "Unwumbo", command = print_summary)
button.grid(row = 3, column = 1)

mainloop()
