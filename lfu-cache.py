class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val = {}
        self.key_to_freq = {}
        self.freq_to_keys = collections.defaultdict(dict)

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1
        
        self.increase_freq(key)
        return self.key_to_val[key]    
        
    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return -1
        
        if key in self.key_to_val:
            self.key_to_val[key] = value
            self.increase_freq(key)
            return
        
        if self.capacity <= len(self.key_to_val):
            self.remove_min_freq_key()
        
        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        
        self.freq_to_keys[1][key] = None
        
        self.min_freq = 1
        
    
    
    def increase_freq(self, key):
        if key not in self.key_to_freq:
            self.key_to_freq[key] = 1

        freq = self.key_to_freq[key]
        self.key_to_freq[key] = self.key_to_freq[key] + 1
            
        del self.freq_to_keys[freq][key]
        self.freq_to_keys[freq + 1][key] = None
        
        if len(self.freq_to_keys[freq]) == 0:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        
    
    def remove_min_freq_key(self):
        
        keys = self.freq_to_keys[self.min_freq]
        key = next(iter(keys))
        
        del self.freq_to_keys[self.min_freq][key]

        if len(keys) == 0:
            del self.freq_to_keys[self.min_freq]
        
        del self.key_to_val[key]
        del self.key_to_freq[key]
