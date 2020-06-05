class example1:
    def sumt(self):
        print("from example1 class addt method")
class example2(example1):
    def addt(self):
        print("from example2 class addt method")
a=example2()
a.addt()
b=example1()
b.addt()

