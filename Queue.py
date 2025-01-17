class Queue:
    def __init__(self):
        self.value = []

    def Enqueue(self, x):
        self.value.append(x)

    def Dequeue(self):
        if not self.value:
            return "Queue is Empty"
        front = self.value.pop(0)
        return front

    def binarySearch(self, item):
        self.value.sort()  # Ensure the queue is sorted before binary search
        b, e = 0, len(self.value) - 1
        while b <= e:
            mid = (b + e) // 2
            if self.value[mid] == item:
                print(f"Item found at index {mid}")
                print("Time Complexity: O(log n)")
                return
            elif self.value[mid] < item:
                b = mid + 1
            else:
                e = mid - 1
        print("Item not found")
        print("Time Complexity: O(log n)")

    def linearSearch(self, item):
        for i, val in enumerate(self.value):
            if val == item:
                print(f"Item found at index {i}")
                print("Time Complexity: O(n)")
                return
        print("Item not found")
        print("Time Complexity: O(n)")

# Main Execution
if __name__ == "__main__":
    a = Queue()
    l = int(input("Enter Queue limit: "))
    for i in range(l):
        e = int(input("Enter value: "))
        a.Enqueue(e)

    print("Queue content:", a.value)

    print("Dequeue operation result:", a.Dequeue())

    search_item = int(input("Enter one item to search (binary search): "))
    a.binarySearch(search_item)

    search_item_linear = int(input("Enter one item to search (linear search): "))
    a.linearSearch(search_item_linear)
