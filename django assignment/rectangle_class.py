class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    def __iter__(self):
        # Create an iterator that yields length and width in the specified format
        yield {'length': self.length}
        yield {'width': self.width}
# Example usage
rectangle = Rectangle(10, 5)
for dimension in rectangle:
    print(dimension)