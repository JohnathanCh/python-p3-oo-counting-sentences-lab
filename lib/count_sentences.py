#!/usr/bin/env python3
import pdb
import re

class MyString:
  def __init__(self, value = None):
    if value:
      self._value = value
  
  def get_value(self):
    return getattr(self, "value") if hasattr(self, 'value') else None
  
  def set_value(self, value):
    if type(value) == str:
      self.value = value
      pass
    else:
      self.value = None
      print("The value must be a string.")
    
  value = property(get_value, set_value)
    
  def is_sentence(self):
    return self.value.endswith(".")
  
  def is_question(self):
    return self.value.endswith("?")
  
  def is_exclamation(self):
    return self.value.endswith("!")
  
  def count_sentences(self):
    # if hasattr(self, "value"):
      pdb.set_trace()
      sentences = re.split(r"\.+|\?+|\!+", self.value)
      results = list(filter(None, sentences))
      # pdb.set_trace()
      return len(results)
    # else:
    #   return 0
  
  
