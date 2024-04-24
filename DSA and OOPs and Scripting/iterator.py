class Num:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if(self.a<=20):
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
n1=Num()
it1=iter(n1)
for x in it1:
    print(x)