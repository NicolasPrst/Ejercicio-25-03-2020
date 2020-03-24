class Series():

    def __init__(self):
        self.number = str(input("Please enter the value of n: "))
        self.arguments = int(input("Please enter the number of additions: "))

    def add(self):
        addition = 0
        for i in range(self.arguments):
            addition = addition + int((i+1) * self.number)
        print(addition)

if __name__ == '__main__':
    n = Series()
    n.add()
