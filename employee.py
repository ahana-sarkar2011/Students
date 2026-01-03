class employee():
    def __init__(self,enumber,elocation):
        self.enumber = enumber
        self.elocation = elocation
    def details(self):
        print("number: "+str(self.enumber))
        print("location: "+self.elocation)
e1 = employee(5,"London")
e1.details()