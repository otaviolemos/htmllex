class HtmlLex:
    def __init__(self, text):
        self.text = text
        self.result = ""
        self.current_index = 0

    def _get_tag_name(self, tag):
      tag_name = ""
      index = 0
      while tag[index] != ">" and tag[index] != " ":
          tag_name += tag[index]
          index += 1  
      return tag_name, index

    def _get_attribute_name(self, tag, index):
      attribute_name = ""
      int_index = index
      while tag[int_index] != "=":
          attribute_name += tag[int_index]
          int_index += 1  
      return attribute_name, int_index

    def _get_attribute_value(self, tag, index):
      attribute_value = ""
      int_index = index
      while tag[int_index] != "\"":
          attribute_value += tag[int_index]
          int_index += 1
      return attribute_value, int_index

    def process(self):
          tags_list = self.text.split("<")
          for tag in tags_list:
            if (len(tag) == 0):
                continue
            tag_name, index = self._get_tag_name(tag)
            if(tag_name[0] != "/"):
              self.result = self.result + tag_name
            if (tag[index] == " "):
              self.result = self.result + "\n-> "
              attribute_name, index = self._get_attribute_name(tag, index+1)
              self.result = self.result + attribute_name
              attribute_value, _ = self._get_attribute_value(tag, index+2)
              self.result = self.result + " > " + attribute_value


    def get_result(self):
        return self.result