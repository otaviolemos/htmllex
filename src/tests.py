from htmllex import HtmlLex

def test_empty_string():
  text = ""
  lex = HtmlLex(text)
  lex.process()
  assert lex.get_result() == ""

def test_single_tag():
  text = "<html>"
  lex = HtmlLex(text)
  lex.process()
  assert lex.get_result() == "html\n"

def test_single_tag_with_closing_tag():
  text = "<html></html>"
  lex = HtmlLex(text)
  lex.process()
  assert lex.get_result() == "html\n"

def test_single_tag_with_single_attribute():
  text = "<object type=\"application/x-flash\"/>"
  lex = HtmlLex(text)
  lex.process()
  assert lex.get_result() == "object\n-> type > application/x-flash\n"

def test_ignores_comment():
  text = "<!-- <param name=\"movie\" value=\"your-file.swf\" /> -->"
  lex = HtmlLex(text)
  lex.process()
  assert lex.get_result() == ""

def test_with_two_parameters():
  text = "<object type=\"application/x-flash\" data=\"your-file.swf\"/>"
  lex = HtmlLex(text)
  lex.process()
  assert lex.get_result() == "object\n-> type > application/x-flash\n-> data > your-file.swf\n"

def test_with_complete_html():
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
