class Employee:
    def __init__(self, emp_id, name, sal, dept):
        self.emp_id = emp_id
        self.name = name
        self.sal = sal
        self.dept = dept

    def toTuple(self):
        return (self.emp_id, self.name, self.sal, self.dept)

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.sal}, Dept: {self.dept}"

