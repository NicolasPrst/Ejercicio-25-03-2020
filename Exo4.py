class Histogram():

    def input_data_from_document(self):
        list = []
        document = open("datas.txt","r")
        for line in document.readlines():
            if len(line) > 0 and line != '\n':
                list.append(int(line))
        return list

    def build_histogram(self):
        new_list = self.input_data_from_document()
        for j in new_list:
            print(str(j) + " : " + "=" * j)

if __name__ == '__main__':
    h = Histogram()
    h.build_histogram()