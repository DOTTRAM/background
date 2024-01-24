class Employee:  
    """Базовый класс для всех сотрудников"""  
    emp_count = 0  
  
    def __init__(self, name, salary, age):  
        self.name = name  
        self.salary = salary 
        self.age = age
        Employee.emp_count += 1  
  
    def display_count(self):  
        print('Всего сотрудников: %d' % Employee.empCount)  
  
    def display_employee(self):  
        print('Имя: {}. Зарплата: {}. Возраст: {}'.format(self.name, self.salary, self.age))


# Это создаст первый объект класса Employee  
emp1 = Employee("Андрей", 2000, 35)  
# Это создаст второй объект класса Employee  
emp2 = Employee("Мария", 5000, 40) 
setattr(emp1, 'age', 8)
emp1.display_employee()  
emp2.display_employee()  

print("Всего сотрудников: %d" % Employee.emp_count)
