class SuperList(list):
    # def __init__(self):
    #     self.list = []

    def __len__(self):
        return 1000

    # def __len__(self):
    #     return len(self.list)

    # def append(self, item):
    #     self.list.append(item)


super_list1 = SuperList()
super_list1.append(5)
print(super_list1[0])
print(issubclass(SuperList, list))
