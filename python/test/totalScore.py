import sys
from collections import Counter
class Person(object):
    def __init__(self, name):
        self.name = name

    def get_details(self):
      
        return self.name
    def get_grade(self,score):

        grep = Counter(score)
        
        c = grep.most_common()
        totalpaas = 0
        totalfail = 0
        string = []
        for i in c:
            x,y = i
            string.append(x+": "+str(y))
            if x == "D":
               totalfail += y
            else:
               totalpaas +=y
            
        if "student" == self.name:

            print("Pass: {}, Fail: {}".format(totalpaas,totalfail))
        else:
            print(", ".join(string))
person1 = Person(sys.argv[1])

person1.get_grade(sys.argv[2])