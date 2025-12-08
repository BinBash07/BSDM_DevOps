class Employee:
<<<<<<< HEAD
    def __init__(self, emp_id, name, sal, dept):
        self.emp_id = emp_id
        self.name = name
        self.sal = sal
        self.dept = dept

    def toTuple(self):
        return (self.emp_id, self.name, self.sal, self.dept)

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.sal}, Dept: {self.dept}"

=======
    def __init__(self, id, name, sal, dept):
        self.id = id
        self.name = name
        self.sal = sal
        self.dept = dept
    
    def toTuple(self):
        return (self.id, self.name, self.sal, self.dept)

if(__name__ == '__main__'):
    e = Employee('101', 'Akash', 50000, 'Software developer')
    print(e.toTuple())
>>>>>>> 328a1f15386175bedcd9e339c982b5cdaee04151
