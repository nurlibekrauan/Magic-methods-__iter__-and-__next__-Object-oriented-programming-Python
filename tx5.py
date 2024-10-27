class CyclicList:
    def __init__(self,lst):
        self.lst = lst
        self.index = 0
        self.length = len(lst)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == self.length:
            self.index = 0
        value = self.lst[self.index]
        self.index += 1
        return value


cyclic_list = CyclicList([10, 20, 30])

for i in range(7):
    print(next(cyclic_list),end=' ')  # 10, 20, 30, 10, 20, 30, 10


# ура я научился создавать итерируемые объекты с любой реализаией
#----------------------------------------------------------------
#ТЕМА МАГИЧЕСКИХ МЕТОДОВ ПРОЙДЕНА !!!!!!!!