class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def display(self):
        print("Name:", self.__name)
        print("Age:", self.__age)

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.__employee_id = employee_id
    
    def get_employee_id(self):
        return self.__employee_id
    
    def display(self):
        super().display()
        print("Employee ID:", self.__employee_id)


emp = Employee("Bhakti Patil", 19, "202303103510424")
emp.display()