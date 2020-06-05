class animal:                               #
        def example(self,name):              #Main class
            print(name," is a animal")      #

class monkey(animal):                                   #inheritance
    def exammonkey(self):                               
        print("Monkey walk on ground with two legs")    
e=monkey()
e.example("chimpu")
e.exammonkey()
