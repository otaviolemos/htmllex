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
        self.assertEqual(lex.get_result(), "html")

    def test_single_tag_with_closing_tag(self):
        text = "<html></html>"
        lex = HtmlLex(text)
        lex.process()
        self.assertEqual(lex.get_result(), "html")

    def test_single_tag_with_single_attribute(self):
        text = "<object type=\"application/x-flash\"\>"
        lex = HtmlLex(text)
        lex.process()
        self.assertEqual(lex.get_result(), 
          "object\n-> type > application/x-flash")