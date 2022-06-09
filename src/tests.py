import unittest
from htmllex import HtmlLex

class TestHtmlLex(unittest.TestCase):
    def test_empty_string(self):
      text = ""
      lex = HtmlLex(text)
      lex.process()
      self.assertEqual(lex.get_result(), "")

    def test_single_tag(self):
      text = "<html>"
      lex = HtmlLex(text)
      lex.process()
      self.assertEqual(lex.get_result(), "html\n")

    def test_single_tag_with_closing_tag(self):
      text = "<html></html>"
      lex = HtmlLex(text)
      lex.process()
      self.assertEqual(lex.get_result(), "html\n")

    def test_single_tag_with_single_attribute(self):
      text = "<object type=\"application/x-flash\"\>"
      lex = HtmlLex(text)
      lex.process()
      self.assertEqual(lex.get_result(), 
        "object\n-> type > application/x-flash\n")

    def test_ignores_comment(self):
      text = "<!-- <param name=\"movie\" value=\"your-file.swf\" /> -->"
      lex = HtmlLex(text)
      lex.process()
      self.assertEqual(lex.get_result(), "")

    def test_with_two_parameters(self):
      text = "<object type=\"application/x-flash\" data=\"your-file.swf\"\>"
      lex = HtmlLex(text)
      lex.process()
      self.assertEqual(lex.get_result(), 
        "object\n-> type > application/x-flash\n-> data > your-file.swf\n")

    def test_with_complete_html(self):
      text = """<head>
<title>HTML</title>
</head>
<object type="application/x-flash"
data="your-file.swf"
width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>"""
      lex = HtmlLex(text)
      lex.process()
      print(lex.get_result())
#       self.assertEqual(lex.get_result(), 
#         """head
# title
# object
# -> type > application/x-flash
# -> data > your-file.swf
# -> width > 0
# -> height > 0
# param
# -> name > quality
# -> value > high""")
