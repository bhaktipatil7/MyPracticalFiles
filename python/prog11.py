class Employee:

    def __init__(self):
        self.__id=0
        self.__name = ""
        self.__gender = ""
        self.__city = ""
        self.__salary = 0

    def getdata(self):
        print(50*"*")
        self.__id=int(input("Enter Id: "))
        self.__name = input("Enter Name: ")
        self.__gender = input("Enter Gender: ")
        self.__city = input("Enter City: ")
        self.__salary = int(input("Enter Salary: "))

    def showData(self):
        print(50*"*")
        print("Id:",self.__id)
        print("Name:", self.__name)
        print("Gender:", self.__gender)
        print("City:", self.__city)
        print("Salary:", self.__salary)


def main():
    emp=Employee()
    emp.getdata()
    emp.showData()

if __name__=="__main__":
    main()