import sys
import PyPDF2
from nltk import tokenize

def main():
  
  text = ""
  try:
    if sys.argv[1] == '-f' or sys.argv[1] == '--file':
      text = get_file_input()

    elif sys.argv[1] == '-s' or sys.argv[1] == '--string':
      text = get_string_input()

    else:
      print("""Please enter a valid command line argument:\n
        -f or --file for summarizing a file\n
        -s or --string for summarizing text you will input""")
      sys.exit(1)

  except IndexError:
    print("""Please enter a valid command line argument:\n
      -f or --file for summarizing a file\n
      -s or --string for summarizing text you will input""")
    sys.exit(1)

      
  no_sentences = get_no_sentences()
  words = get_words(text)
  words = remove_common_words(words)
  words_dict = get_word_dictionary(words)
  sentences = get_sentences(text)

  summary = most_relevant_sentences(words_dict, sentences, no_sentences)
  print(summary)

def get_file_input(file_name = None):

  if file_name == None:
    file_name = input("Enter the name of the file you want summarized:\n")
      
  if file_name.endswith(".txt"):
    f = open(file_name, 'r')
    text = f.read()
    return text

  elif file_name.endswith(".pdf"):
    pdf_file_obj = open(file_name, 'rb')

    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

    num_pages = pdf_reader.numPages
    count = 0
    text = ""

    while count < num_pages:
      page_obj = pdf_reader.getPage(count)
      count += 1
      text += page_obj.extractText()

    return text

  else:
    print("Please enter a .txt or .pdf file.")

  sys.exit(1)

def get_string_input():
  text = input("Enter the text you want summarized:\n")
  return text

def get_no_sentences():

  while(True):
    no_sentences = input("How many sentences would you like to read? ")

    try:
      no_sentences = int(no_sentences)
      return no_sentences
    except ValueError:
      print("Please enter an integer!")

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
      'because', 'any', 'these', 'give', 'day', 'most', 'us', 'is', 'was',
      'are', 'were', 'has', 'been', 'since', 'where', 'may', 'had']

  uncommon_words = []
  for word in words:
    if word not in common_words:
      uncommon_words.append(word)

  return uncommon_words

def get_sentences(text):
  sentences = tokenize.sent_tokenize(text)
  return sentences

def most_relevant_sentences(words_dict, sentences, no_sentences):

  count = no_sentences
  summary = sentences[0] + " "
  count -= 1
  scores = []

  for sentence in sentences:
    words = get_words(sentence)
    score = 0

    for word in words:
      if word in words_dict:
        score += words_dict[word]

    scores.append(score)

  sorted_scores = sorted(scores, reverse = True)

  for i in range(1, len(sentences)):
    if count <= 0:
      break
    if scores[i] in sorted_scores[0:no_sentences]:
      summary += sentences[i] + " "
      count -= 1

  return summary
  
if __name__ == "__main__":
  main()

