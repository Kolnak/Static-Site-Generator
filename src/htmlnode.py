class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        if type(self) == HTMLNode:
            self.__dict__['children'] = children
        else:
            self.__dict__['children'] = None
        self.props = props or {}

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        output = ""
        for key, value in self.props.items():
            output += f" {key}=\"{value}\""
        return output
    
    def __repr__(self):
        return (f"HTMLNode {self.tag}, {self.value}, {self.children}, {self.props}")
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props)

    @property
    def children(self):
        raise AttributeError("LeafNodes cannot have children!")
    
    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value")
        elif self.tag == None:
            return str(self.value)
        elif isinstance(self.props, dict):
            output = ""
            for key, entry in self.props.items():
                output += f' {key}="{entry}"'
            return f'<{self.tag}{output}>{self.value}</{self.tag}>'
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
