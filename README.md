<p align="center"><img src="https://github.com/haseebT/Unwumbo/blob/master/logo.png" alt="Unwumbo" width="100" height="100"></p>

<h1 align="center">Unwumbo</h1>

Unwumbo is a Python program that summarizes text.

## How it works

The program works in the following way:

- All the words in the inputted text are put into a list.

- Common English words (the, of, an, etc.) are removed from the list.

- A dictionary is created from the list of words, with each key being a unique word from the list. The value of a key is the number of times that key (word) appears in the list.

- A second list is created from the inputted text, with each index holding a sentence from the text.

- The most relevant sentences are determined from the list of sentences by scoring each sentence.

  - A sentence is scored by summing the values of each word in the sentence. The values are obtained from the dictionary.

- The most relevant sentences (plus the very first sentence) are returned in chronological order.
