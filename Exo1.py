class Series():

    def input_a_number(self):
        number = input("Please enter the value of n: ")
        return(number)

    def add(self):
        numb = self.input_a_number()
        print(int(numb) + int(2*numb) + int(3*numb))

if __name__ == '__main__':
    n = Series()
    n.add()
