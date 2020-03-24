class Histogram():

    def input_data(self):
        list = []
        maximum = int(input("Please enter the number of data of the list: "))
        for i in range(maximum):
            data = int(input("Please enter the data number " + str(i+1) + " : "))
            list.append(data)
        return list

    def build_histogram(self):
        new_list = self.input_data()
        for j in new_list:
            print(str(j) + " : " + "=" * j)

if __name__ == '__main__':
    h = Histogram()
    h.build_histogram()

