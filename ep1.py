class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.num = 2
        return self

    def __next__(self):
        if self.num <= self.limit:
            value = self.num
            self.num += 2
            return value
        else:
            raise StopIteration

obj = EvenNumbers(10)

for i in obj:
    print(i)# APP---experiments
