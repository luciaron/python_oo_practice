"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """constructs count variable to be altered from start variable"""
        self.start = start
        self.count = self.start

    def __repr__(self):
        return f'<SerialGenerator start={self.start}, '

    def generate(self):
        """increases the count variable, returns new serial number"""
        self.count += 1
        return self.count - 1
    
    def reset(self):
        """resets the count to the original start"""
        self.count = self.start