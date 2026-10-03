class LruCache:
    class clsNode:
        def __init__(self,value,key):
            self.next= None
            self.previous = None
            self.value = value
            self.key = key

    def __init__(self, limit):
        self.head = None
        self.tail = None
        self.limit =  limit
        self.cache = {}

    def add_to_head(self, node):
      if node == None:
          return
      if self.head is None:
        self.head = node
        self.tail = node
      else:
        node.next = self.head
        self.head.previous = node
        self.head = node


    def remove(self, node):
        if node == None:
            return
        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None

        elif node == self.head:
            self.head = self.head.next
            self.head.previous = None

        elif node == self.tail:
            self.tail = self.tail.previous
            self.tail.next = None

        else:
            node.next.previous = node.previous
            node.previous.next = node.next
        node.next = None
        node.previous = None  

    def move_to_head(self,node):
        self.remove(node)
        self.add_to_head(node)

    # cache {key,node}
    def get(self,key):
        target = self.cache.get(key)   
        if target == None:
            return None
        
        self.move_to_head(target)
        return target.value

    def set(self,key,value):
        target = self.cache.get(key)

        if target is not None:
            target.value = value
            self.move_to_head(target)

        else:
            target = self.clsNode(value,key)
            self.add_to_head(target)
            self.cache[key] = target

            if len(self.cache) > self.limit:
                old_tail = self.tail
                self.remove(old_tail)
                del self.cache[old_tail.key]