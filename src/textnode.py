from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = None
    BOLD = "**"
    ITALIC = "_"
    CODE = "`"
    LINK = "[]()"
    IMAGE = "![]()"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, TextNode2):
        return (self.text == TextNode2.text and self.text_type == TextNode2.text_type and self.url == TextNode2.url)

    def __repr__(self):
        return (f"TextNode({self.text}, {self.text_type}, {self.url})")
    
def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise Exception("no supported TextType")
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    if text_type in TextType and delimiter == TextType(text_type):
        for nodes in old_nodes:
            if nodes.text.count(delimiter) % 2 == 0:
                if nodes.text_type == TextType.TEXT:
                    new_nodes.append(nodes)
                else:
                    text_cache = nodes.text
                    text_segment = []
                    while delimiter in text_cache:
                        start_index = text_cache.find(delimiter)
                        if start_index > 0:
                            text_segment.append((text_cache[:start_index], TextType.TEXT))
                        end_index = text_cache.find(delimiter, start_index + len(delimiter))
                        text_segment.append(text_cache[start_index + len(delimiter):end_index], text_type)
                        text_segment.append(text_cache[end_index + len(delimiter):])
                    if text_cache:
                        text_segment.append((text_cache, text_type))
                    for text, node_type in text_segment:
                        new_nodes.append(TextNode(text, node_type))
                return new_nodes
            else:
                raise ValueError("Delimiter not closed") 
    else:
        raise ValueError("Delimiter mismatch")
    
