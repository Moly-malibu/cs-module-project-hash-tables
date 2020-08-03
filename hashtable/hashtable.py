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

#STRING KEYS
class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity = MIN_CAPACITY):
        self.buckets = [None] * capacity
        self.capacity = capacity

#SLOT: NUMBER OF SLOTS IN THE MAIN LIST.
    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.buckets)

#LOAD
    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return get_load_factor
        
#Fowler noll vo hash function: basis of the FNV hash algorithm to Speed of computation, sticky state, diffusion.
#http://www.isthe.com/chongo/tech/comp/fnv/index.html#public_domain
#https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function#:~:text=As%20an%20example%2C%20consider%20the,(in%20hex%2C%200xcbf29ce484222325).
    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        FNV_offset_basis = 14695981039346656037 
        FNV_prime = 1099511628211
        
        hash = FNV_offset_basis

        for byte in key.encode():
            hash = hash * FNV_prime
            hash = hash ^ byte
        return hash
        
    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here

#INDEX
    def hash_index(self, key, capacity):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.get_key_slot(key, capacity)
        #return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity

#PUT
    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        self.put_in_buckets(key, value, self.buckets, self.capacity)

#DELETE
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        self.put(key,None)

#GET
    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        slot_num = self.get_key_slot(key, self.capacity)
        top_level_item = self.buckets[slot_num]

        if top_level_item == None:
            return None
        else:
            cur_item = top_level_item
            while cur_item:
                if cur_item.key == key:
                    return cur_item.value
                cur_item = cur_item.next
            return None
#RESIZE 
#http://www.mathcs.emory.edu/~cheung/Courses/554/Syllabus/3-index/resize-hash.html
    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        new_buckets = [None] * new_capacity
        for item in self.buckets:
            self.put_in_buckets(item.key, item.value, new_buckets, new_capacity, True)
            item = item.next
            while item:
                self.put_in_buckets(item.key, item.value, new_buckets, new_capacity, True)
                item = item.next
        self.buckets = new_buckets
        self.capacity = new_capacity
    
    def get_key_slot(self, key, capacity):
        return self.fnv1(key) % capacity
#ITEM COUNT    
    def get_item_count(self):
        num_items = 0
        for item in self.buckets:
            if item != None:
                num_items += 1
                cur_item = item
                while cur_item:
                    if cur_item.next:
                        num_items +=1
                    cur_item = cur_item.next
        return num_items
#RESIZE    
    def need_resize(self):
        item_count = self.get_item_count()
        if item_count == 0:
            return False
        if(item_count/len(self.buckets)) >= 0.7:
            return True
        return False
    
    def put_in_buckets(self, key, value, buckets, capacity, no_resize_check = True):
        is_delete_operation = False
        if value == None:
            is_delete_operation = True
        if no_resize_check == False:
            if is_delete_operation == False:
                if self.need_resize():
                    self.resize(self.capacity*2)
        item = HashTableEntry(key, value)
        slot_num = self.get_key_slot(key, capacity)
        top_level_item = buckets[slot_num]

        if top_level_item == None or top_level_item.key == key:
            if is_delete_operation:
                if top_level_item.next:
                    buckets[slot_num] == top_level_item.next
                else:
                    buckets[slot_num] = None
            else:
                buckets[slot_num] = item
        else:
            prev_item = None
            cur_item = top_level_item
            next_item = cur_item.next
            
            while cur_item:
                if cur_item.key == key:     
                    if is_delete_operation:
                        prev_item.next = next_item
                    else:
                        cur_item.value = value
                    break
                
                elif not next_item:
                    cur_item.next = item
                    break
                
                prev_item = cur_item
                cur_item = next_item
                next_item = cur_item.next

if __name__ == "__main__":
    ht = HashTable(8)

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
