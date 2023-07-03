from node import Node

# create LinkedList class
class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ''
        while self.head_node:
            if self.head_node.get_value() != None:
                string_list += str(self.head_node.get_value()) + '\n'
            self.head_node = self.head_node.get_next_node()
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node
                    
    def get_val(self, tar_index):
        val = ''
        while self.head_node:
            if self.head_node.get_value() != None:
                val += str(self.head_node.get_value()[tar_index]) + '\n'
            self.head_node = self.head_node.get_next_node()
        return val
