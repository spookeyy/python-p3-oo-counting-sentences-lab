#!/usr/bin/env python3
import re
class MyString:
  def __init__(self, value=""):
    self.value = value

  # is_sentence() method
  def is_sentence(self):
    if self.value.endswith("."):
      return True
    else:
      return False
    
  # is_question() method
  def is_question(self):
    if self.value.endswith("?"):
      return True
    else:
      return False
    
  # is_exclamation() method
  def is_exclamation(self):
    if self.value.endswith("!"):
      return True
    else:
      return False
    
  # count_sentences() method
  # call a count_sentences() method on a MyString instance, and get back a, well, count of sentences in its value
  # if the value is not a sentence, return 0

  def count_sentences(self):
        if not isinstance(self.value, str):
            print("The value must be a string.\n")
            return 0

        # Split the string into sentences using regex
        sentences = re.split(r'[.!?]+', self.value)

        # Filter out empty strings
        sentences = [s.strip() for s in sentences if s.strip()]

        # Count the number of non-empty sentences
        sentence_count = len(sentences)

        return sentence_count

string = MyString()
string.value = "This is a string! It has three sentences. Right?!"
print(string.count_sentences())  # => 3