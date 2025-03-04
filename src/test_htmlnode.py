import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_1(self):
        HTMLNode1 = HTMLNode()
        self.assertIsInstance(HTMLNode1, HTMLNode)

    def test_2(self):
        HTMLNode2 = HTMLNode("teststring", "test den string", None, {"id": "1"})
        self.assertEqual(HTMLNode2.props_to_html(), " id=\"1\"")

if __name__ == "__main__":
    unittest.main()