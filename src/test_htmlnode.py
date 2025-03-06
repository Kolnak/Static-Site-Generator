import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_1(self):
        HTMLNode1 = HTMLNode()
        self.assertIsInstance(HTMLNode1, HTMLNode)

    def test_2(self):
        HTMLNode2 = HTMLNode("teststring", "test den string", None, {"id": "1"})
        self.assertEqual(HTMLNode2.props_to_html(), " id=\"1\"")

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

if __name__ == "__main__":
    unittest.main()