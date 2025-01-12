class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.array = [0] * 2 # initializes the array with all 0s
    
    def push(self, num):
        if(self.length == self.capacity):
            self.resize
        self.array[self.length] = num
        self.length += 1

    def pushAtIndex(self, num, index):
        if index == self.length - 1:
            self.push(num)

        if index in range(self.length):
            for i in range(index, self.length - 1):
                self.array[i + 1] = self.array[i]
            self.array[index] = num

    def resize(self):
        self.capacity = 2 * self.capacity
        newArray = [0] * self.capacity

        for i in range(self.length):
            newArray[i] = self.array[i]
        
        self.array = newArray
    
    def pop(self):
        if self.length > 0:
            self.length -= 1

    def popValueAtIndex(self, index):
        if index == self.length - 1:
            self.pop()
        if index in range(self.length):
            for i in range(index + 1, self.length):
                self.array[i - 1] = self.array[i]
            self.length -= 1
    
    def getValueAt(self, index) -> int:
        if index < self.length:
            return self.array[index]
        return -1 # returning -1 to signify out of bounds error
    
    def show(self):
        for i in range(self.length):
            print(self.array[i])