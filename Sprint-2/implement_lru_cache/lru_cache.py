from linked_list import LinkedList


class LruCache:

    def __init__(self, limit):
        if limit <= 0:
            raise ValueError("limit must be greater than 0")
        # self.head = None
        # self.tail = None
        # self.limit = limit
        # self.cache = {}
        self.list = LinkedList()
        self.limit = limit
        self.cache = {}

    def move_to_head(self, node):

        key, value = node.value

        self.list.remove(node)
        new_node = self.list.push_head((key, value))
        self.cache[key] = new_node

    def get(self, key):
        target = self.cache.get(key)
        if target == None:
            return None

        self.move_to_head(target)

        return target.value[1]

    def set(self, key, value):
        target = self.cache.get(key)

        if target is not None:

            target.value = (key, value)
            self.move_to_head(target)

        else:

            new_Node = self.list.push_head((key, value))
            self.cache[key] = new_Node

            if len(self.cache) > self.limit:
                old_key, old_value = self.list.pop_tail()
                del self.cache[old_key]
