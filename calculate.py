class calculator:
  def __init__(self,a,b):
      self.a = a
      self.b = b
  def add(self):
      return self.a+self.b

  def sub(self):
      return self.a-self.b


while(1):
    print("Enter option for calculator :")
    print("1 to Add ,2 to sub , 0 to close")

    choice = int(input("enter your choice : "))

    if choice == 1:
        a = int(input("enter num 1 to add : ",))
        b = int(input("enter num 2 to add : ",))
        cal = calculator(a, b)
        print("Total sum for {0} and {1} is {2}".format(a,b,cal.add()))
    elif choice == 2:
        a = int(input("enter num 1 to add : ", ))
        b = int(input("enter num 2 to add : ", ))
        cal = calculator(a,b)
        print("Substraction for {0} and {1} is {2}".format(a,b,cal.sub()))
    else:
        break
