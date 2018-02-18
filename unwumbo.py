from string import punctuation
import re

def main():
  text = get_input()
  words = get_words(text)
  words = remove_common_words(words)
  words_dict = get_word_dictionary(words)
  sentences = get_sentences(text)

def get_input():
  file_name = input("Enter the name of the file you want summarized:\n")
  f = open(file_name, 'r')
  text = f.read()
  return text

def get_words(text):
  text_no_punc = ''.join(c for c in text if c not in punctuation)
  text_no_punc = text_no_punc.lower()
  words = text_no_punc.split()
  return words

def get_word_dictionary(words):
  words_dict = {}
  seen_words = []

  for word in words:
    if word in seen_words:
      continue
    key = word
    value = words.count(word)
    words_dict[key] = value
    seen_words.append(word)

  return words_dict

def remove_common_words(words):
  common_words = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have',
      'i', 'it', 'for', 'not', 'on', 'with', 'he', 'she', 'as', 'you', 'do',
      'at', 'this', 'but', 'his', 'hers', 'by', 'from', 'they', 'we', 'say',
      'or', 'will', 'an', 'my', 'one', 'all', 'would', 'there', 'their',
      'what', 'so', 'up', 'out', 'if', 'about', 'who', 'get', 'which',
      'go', 'when', 'me', 'make', 'can', 'like', 'time', 'no', 'just', 'him',
      'her', 'know', 'take', 'person', 'into', 'year', 'your', 'good', 'some',
      'could', 'them', 'see', 'other', 'than', 'then', 'now', 'look', 'only',
      'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two',
      'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new', 'want',
      'because', 'any', 'these', 'give', 'day', 'most', 'us', 'is', 'was']

  uncommon_words = []
  for word in words:
    if word not in common_words:
      uncommon_words.append(word)

  return uncommon_words

def get_sentences(text):
  sentence_enders = re.compile('[.!?][\s]{1,2}(?=[A-Z])')
  sentences = sentence_enders.split(text)
  return sentences

if __name__ == "__main__":
  main()

