from enum import Enum

class TextType(Enum):
    NORMAL = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, TextNode2):
        return (self.text == TextNode2.text and self.text_type == TextNode2.text_type and self.url == TextNode2.url)

    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type}, {self.url})")
    
    def text_note_to_html_node(text_node):
        if isinstance(text_node, TextType):
            pass
        else:
            raise Exception("no supported TextType")