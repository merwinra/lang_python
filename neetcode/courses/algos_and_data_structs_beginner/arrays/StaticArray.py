# initialzing an integer array
myArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(myArray)

# accessing an element in O(1) time
print(myArray[5])

# traversing myArray using a for loop
for i in range(len(myArray)):
    print(myArray[i])

# traversing myArray using a while loop
i = 0
while i < len(myArray):
    print(myArray[i])
    i += 1

# removing an element from the end of myArray (without using pop()); a soft delete.
# unfortunately the length of the array doesnt change using this approach.
# we explicitly assume it's decreased by 1
def removeFromEnd(array, length):
    if length > 0:
        array[length - 1] = 0

removeFromEnd(myArray, len(myArray))

print(myArray)

# removing an element at the ith index from myArray; also a soft delete.
# unfortunately the length of the array doesnt change using this approach.
# we explicitly assume it's decreased by 1
def removeAtIndex(array, index, length):
    for i in range(index + 1, length):
        array[i - 1] = array[i]

removeAtIndex(myArray, 5, len(myArray))

print(myArray)

# helper function to find the total number of "real" values within an array
def findAvailableLengthOfArray(array):
    availableLength = 0
    for i in array:
        if i != 0:
            availableLength += 1
    return availableLength

# function to insert a number at the next open position in an array
def insertAtEnd(array, input, availableLength, capacity):
    if availableLength < capacity:
        array[availableLength] = input

insertAtEnd(myArray, 555, findAvailableLengthOfArray(myArray), len(myArray))

print(myArray)

# function to insert a number at the ith position in an array
def insertAtIndex(array, i, input, availableLength, capacity):
    if availableLength < capacity:
        for index in range(availableLength - 1, i - 1, -1):
            array[index + 1] = array[index]
        array[i] = input

insertAtIndex(myArray, 2, 333, findAvailableLengthOfArray(myArray), len(myArray))

print(myArray)