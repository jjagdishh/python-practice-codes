class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

class Devloper(Employee):
    def __init__(self,first,last,pay,pro_lang):
        super().__init__(first,last,pay) # you can also do as Employee.__init__(self,first,last,pay):
        self.pro_lang = pro_lang


class Manager(Employee):
    def __init__(self,first,last,pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees=employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("--->", emp.fullname())


emp_1=Employee("Ram", "Singh", 40000)
dev_1=Devloper("Vikas", "sharma", 90000, 'Python')
mgr_1=Manager("Ram", "Kapoor", 100000,[dev_1])

print (mgr_1.email)
mgr_1.add_emp(emp_1)
mgr_1.print_emp()
print(mgr_1.pay)