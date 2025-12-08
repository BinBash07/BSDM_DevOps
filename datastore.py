from config import storage
from employee import Employee

class Datastore:
    def __init__(self):
        # Choose storage type
        if storage == "Dictionary":
            self.data = {}
        else:
            self.data = []

    def addData(self, emp: Employee):
        if storage == "Dictionary":
            self.data[emp.emp_id] = emp
        else:
            self.data.append(emp.toTuple())
        return "Employee added successfully."

    def getData(self):
        if storage == "Dictionary":
            return list(self.data.values())
        else:
            return self.data

    def searchData(self, emp_id):
        if storage == "Dictionary":
            return self.data.get(emp_id)
        else:
            for e in self.data:
                if e[0] == emp_id:
                    return e
        return None

    def updData(self, emp: Employee):
        if storage == "Dictionary":
            if emp.emp_id in self.data:
                self.data[emp.emp_id] = emp
                return "Employee updated successfully."
        else:
            for i, e in enumerate(self.data):
                if e[0] == emp.emp_id:
                    self.data[i] = emp.toTuple()
                    return "Employee updated successfully."
        return "Employee not found."

    def delData(self, emp_id):
        if storage == "Dictionary":
            if emp_id in self.data:
                del self.data[emp_id]
                return "Employee deleted successfully."
        else:
            for i, e in enumerate(self.data):
                if e[0] == emp_id:
                    self.data.pop(i)
                    return "Employee deleted successfully."
        return "Employee not found."

