class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """


    def __init__(self, capacity):
        # Your code here
        if capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        else:
            self.capacity = capacity
        self.storage = [None] * self.capacity
        self.count = 0



    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity
        # Your code here


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return float(self.count)/self.capacity
        # Your code here
        


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for letter in key:
            hash = (( hash << 5) + hash) + ord(letter)
        return hash & 0xFFFFFFFF 


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        if self.get_load_factor() > 0.6:
            self.resize(self.capacity*2)
        index = self.hash_index(key)
        cur = self.storage[index]
        if cur is None:
            self.count += 1
            self.storage[index] = HashTableEntry(key, value)
        else:
            while cur.next is not None:
                if cur.key == key:
                    cur.value = value
                    return
                cur = cur.next
            if cur.key == key:
                cur.value = value
                return
            cur.next = HashTableEntry(key, value)
            self.count += 1

        # Your code here


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        cur = self.storage[index]
        if cur is not None:
            if cur.key == key:
                if cur.next is None:
                    self.count -= 1
                    self.storage[index] = None
                    return
                else:
                    self.count -= 1
                    self.storage[index] = cur.next
                    return
            prev = cur
            cur = cur.next
            while cur != None:
                if cur.key == key:
                    self.count -= 1
                    prev.next = cur.next
                    return
                cur = cur.next
                prev = prev.next
        print("Key was not found")



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        cur = self.storage[index]
        if cur is not None:
            while cur != None:
                if cur.key == key:
                    return cur.value
                cur = cur.next
        print("Key was not found")
        # Your code here


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        tmp = self.storage
        self.__init__(new_capacity)
        self.storage = [None] * self.capacity
        for item in tmp:
            if item is not None:
                while item is not None:
                    self.put(item.key, item.value)
                    item = item.next
        





if __name__ == "__main__":
    ht = HashTable(8)
    # print(ht.storage)
    # for i in range(1000):
    #     ht.put("line_" + str(i), "hello")
    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")
    # print(ht.storage)
    # print(len(ht.storage))
    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
