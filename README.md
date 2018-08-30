<p align="center"><img src="https://github.com/haseebT/Unwumbo/blob/master/logo.png" alt="Unwumbo" width="100" height="100"></p>

<h1 align="center">Unwumbo</h1>

Unwumbo is a Python program that summarizes text.

## How it works

The program works in the following way:

- All the words in the inputted text are put into a list.

- Common English words such as articles (the, a, an) and prepositions (of, at) are removed from the list.

- A dictionary is created from the list of words, with each key being a unique word from the list. The value of a key is the number of times that key (word) appears in the list.

- A second list is created from the inputted text, with each index holding a sentence from the text.

- The most relevant sentences are determined from the list of sentences by scoring each sentence.

  - A sentence is scored by summing the values of each word in the sentence. The values are obtained from the dictionary.

- The most relevant sentences (plus the very first sentence) are returned in chronological order.

## Demo

#### Command Line

To use Unwumbo from the command line, open up a terminal and type `python3 unwumbo.py -f` in the directory where unwumbo.py is located. You will then be prompted to enter the name of the text file you want summarized. Either enter the file's absolute path or its relative path. Finally, enter the number of sentences you would like to read.

![Gif 1](https://github.com/haseebT/Unwumbo/blob/master/gifs/cli-text.gif)

#### GUI

To use Unwumbo via a GUI, open up a terminal and type `python3 gui.py` in the directory where gui.py is located. A GUI window will pop up and give you the option to summarize a file, or summarize text inputted via the keyboard. Depending on which option you choose, either enter the file name (absolute or relative path), or enter your own text. The GUI option will always output 5 sentences.

![Gif 2](https://github.com/haseebT/Unwumbo/blob/master/gifs/gui.gif)


