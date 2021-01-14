class CustomSet:
    resize_factor = 0.7

    def __init__(self):
        self.count = 0
        self.capacity = 8
        self.values = [None] * self.capacity

    def execute_resize_check(self):
        return self.capacity * self.resize_factor <= self.count

    def get_index(self, value):
        value_hash = hash(value)
        return abs(value_hash) % self.capacity

    def resize(self):
        self.count = 0
        old_values = self.values
        self.capacity *= 2
        self.values = [None] * self.capacity
        for nested_list in old_values:
            if nested_list:
                for value in nested_list:
                    self.add(value)

    def add(self, value):
        value_hash = hash(value)
        index = abs(value_hash) % self.capacity
        if not self.values[index]:
            self.values[index] = []
        if value not in self.values[index]:
            self.values[index].append(value)
        if self.execute_resize_check():
            self.resize()

    def remove(self, value):
        index = self.get_index(value)
        if not self.values[index]:
            return
        if value not in self.values[index]:
            return
        self.values[index].remove(value)
        self.count += 1

    def contains(self, value):
        index = self.get_index(value)
        if not self.values[index]:
            return False
        if value not in self.values[index]:
            return False
        return True

    def __contains__(self, item):
        index = self.get_index(item)
        if not self.values[index]:
            return False
        if item not in self.values[index]:
            return False
        return True

    def __len__(self):
        return self.count

    def __repr__(self):
        return str(self.values)


ss = CustomSet()
ss.add(4)
ss.add(3)
ss.add(2)
ss.add(1)
ss.add(0)
ss.add(-1)
ss.add(-2)
ss.add(-3)
ss.add(-4)
ss.add(-5)
ss.add(-6)
ss.add(-7)
ss.add(-8)
ss.add('add')
ss.add('remove')
ss.add('take')
ss.add('peek')
print(ss)
