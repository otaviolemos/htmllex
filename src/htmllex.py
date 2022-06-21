class HtmlLex:
    def __init__(self, text):
        self.text = text
        self.result = ""
        self.index = 0

    def _get_token(self, tag, charset):
      token = ""
      while tag[self.index] not in charset:
          token += tag[self.index]
          self.index += 1  
      return token

    def process(self):
      self._strip_comments()
      self._strip_extra_spaces_and_newlines()
      tags_list = self.text.split("<")
      for tag in tags_list:
        self.index = 0
        if (len(tag) == 0):
            continue
        tag_name = self._get_token(tag, [">", " "])
        if tag_name[0] == "/":
            continue
        self.result = self.result + tag_name + "\n"
        while tag[self.index] in (" ", "\n") and tag[self.index+1].isalpha():
          self.result = self.result + "-> "
          self.index += 1
          attribute_name = self._get_token(tag, ["="])
          self.result = self.result + attribute_name
          self.index += 2
          attribute_value = self._get_token(tag, ["\""])
          self.result = self.result + " > " + attribute_value + "\n"
          self.index += 1
          

    def _strip_comments(self):
      while(self.text.find("<!--") != -1):
        start_index = self.text.find("<!--")
        end_index = self.text.find("-->")
        self.text = self.text[:start_index] + self.text[end_index+3:]

    def _strip_extra_spaces_and_newlines(self):
      self.text = " ".join(self.text.split())

    def get_result(self):
        return self.result