class Arrange_list():

    def __init__(self):
        self.number = input("Please enter the numbers split by comas:\n")
        self.list = self.number.split(",")
        self.Arranged_list = []

    def input_list(self):
        for i in range(len(self.list)):
            self.Arranged_list.append(int(self.list[i]))
        self.Arranged_list.sort(reverse=True)
        print("The list you enter is:", self.list)
        print("The arrange list is :", self.Arranged_list)

if __name__ == '__main__':
    a = Arrange_list()
    a.input_list()

