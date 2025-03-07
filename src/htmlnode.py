class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        if type(self) == ParentNode:
            self.__dict__['value'] = None
        else:
            self.__dict__['value'] = value
        if isinstance(self, (HTMLNode, ParentNode)):
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
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, None, props)
        self.__dict__['children'] = children

    @property
    def value(self):
        raise AttributeError("ParentNode cannot have value")
    
    def to_html(self):
        NodeHTML = ""
        if self.tag == None or self.tag == "":
            raise ValueError("All ParentNodes must have a tag")
        if self.children == None:
            raise ValueError("ParentNode needs valid children")
        for entries in self.children:
            if not isinstance(entries, HTMLNode):
                raise ValueError("All children must be HTMLNode instance")
            NodeHTML += f"{entries.to_html()}"
        return f"<{self.tag}>{NodeHTML}</{self.tag}>"
        
