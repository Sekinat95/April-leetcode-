#LRU CACHE
# class dll:
#     def __init__(self, key, val):
#         self.key = key
#         self.val = val
#         self.next = None
#         self.prev = None



# class LRUCache:
#     def __init__(self,capacity):
#         self.head = dll(-1,-1)
#         self.tail = self.head
#         self.hash = {}
#         self.capacity = capacity
#         self.length = 0

#     def get(self,key):
#         if key not in self.hash:
#             return -1
#         node = self.hash[key]
#         val = node.val
#         while node.next:
#             node.prev.next = node.next
#             node.next.prev = node.prev
#             self.tail.next = node
#             node.prev = self.tail
#             node.next = None
#             self.tail = Node
#         return val
    
#     def put(key, val):
#         if key in self.hash:
#             node = self.hash[key]
#             node.val = val
#         while node.next:
#             node.prev.next = node.next
#             node.next.prev = node.prev
#             self.tail.next = node
#             node.prev = self.tail
#             node.next = None
#             self.tail = Node
#         else:
#             node = dll(key,val)
#             self.hash[key] = node
#             self.tail.next = node
#             node.prev = self.tail
#             self.tail = node
#             self.length += 1
#             if self.length > self.capacity:
#                 remove = self.head.next
#                 self.head.next = self.head.next.next
#                 self.head.next.prev = self.head
#                 del self.hash[remove.key]
#                 self.length -= 1

class Node:
    def __init__(self, key, val):
        # keep track of key for later use;
        # given only a Node, we are able to
        # delete it from a node_map (see LRUCache)
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    """
    LRUCache utilizes an internal doubly linked list
    to maintain the least-recently-used structure:
    the head stores the Node with the most recently used key,
    and the tail stores the Node with the least recently used key.

    Each time a key is used for put or get, the use_node function is called
    with the Node with the corresponding key (either an existing or new Node),
    and that Node is moved to the head (most recent) position.

    If the cache is at full capacity, we first delete the Node at the tail
    (least recent) position, then call the use_node function with the new node as normal.

    For O(1) put and get functions, the node_map lookup table is used to match a
    key to a corresponding Node.  This way, we can utilize O(1) head and tail operations
    of the internal doubly linked list, and at the same time, we can access a Node
    with a specific key  in O(1) time.

    For simplicity in deleting the tail, I have each Node store its corresponding key.
    This way, we can access the Node at the tail position, extract its key,
    then delete the key from node_map.  The alternative would be to have a variable
    that specifically keeps track of the tail key, and update that value whenever we change
    the tail.
    """
    def __init__(self, capacity):
        if capacity < 1:
            print('LRUCache capacity must be > 0')
            return None

        self.capacity = capacity
        self.size = 0
        self.node_map = {} # map a key to a Node (explained above)
        self.head = None # Node with the most recently used key
        self.tail = None # Node with the least recently used key

    def use_node(self, node):
        """
        put a Node in the head (most recent) position;
        can be a new node, or node that is already stored
        """

        # head Node is already in most recent position,
        # so no work to do when we use it
        if node is self.head: return

        # connect nodes neighbors (one could be None);
        # if node is new, there are no neighbors to connect
        if node.next: node.next.prev = node.prev
        if node.prev: node.prev.next = node.next

        # when using the tail, we must set a new tail
        if node is self.tail:
            # node still points to original tail, so we
            # are fine overwriting the tail pointer.
            # new tail's next is be set to None in the above
            # condition, since the original tail's next was None
            self.tail = self.tail.prev

        # update head Node connections
        self.head.prev = node
        node.next = self.head
        node.prev = None
        self.head = node

    def get(self, key):
        # if key exists, use the corresponding node and return its value
        if key in self.node_map:
            self.use_node(self.node_map[key])
            return self.node_map[key].val
        else:
            return -1

    def put(self, key, value):
        # if key exists, use the corresponding node and update its value
        if key in self.node_map:
            self.use_node(self.node_map[key])
            self.node_map[key].val = value
        else:
            # insert new node
            node = Node(key, value)
            self.node_map[key] = node

            # first node is special case: its the head and the tail
            if self.size == 0:
                self.head = node
                self.tail = node

            if self.size < self.capacity:
                self.size += 1

            # size at max capacity; must remove tail (least recent) node
            elif self.size == self.capacity:
                k = self.tail.key # preserve current tail key

                if self.size == 1:
                    # special case; replace only node left,
                    # so it becomes the head and the tail
                    self.head = node
                    self.tail = node
                else:
                    # normal case, just adjust the tail position
                    self.tail = self.tail.prev
                    self.tail.next = None

                # delete old tail
                del self.node_map[k]

            self.use_node(node)

