from employee import Employee
from datastore import Datastore
from config import storage
<<<<<<< HEAD

class Admin:
    def __init__(self):
        self.ds = Datastore()
        ch = ''
        while ch != '6':
=======
class Admin:
    def __init__(self):
        self.ds = Datastore()
        ch = 0
        while(ch != '6'):
>>>>>>> 328a1f15386175bedcd9e339c982b5cdaee04151
            print('''-----ADMIN-----
            1. Add employee
            2. Show all employee
            3. Search employee
            4. Update employee
            5. Delete employee
            6. Exit''')
            ch = input('Enter choice:')
<<<<<<< HEAD
            if ch == '1':
                self.addEmp()
            elif ch == '2':
                self.showAllEmp()
            elif ch == '3':
                self.searchEmp()
            elif ch == '4':
                self.updEmp()
            elif ch == '5':
                self.delEmp()
            elif ch == '6':
                print('Logged out...')
            else:
                print('Invalid choice...')

    def addEmp(self):
        emp_id = input('Enter id:')
        name = input('Enter name:')
        sal = int(input('Enter salary:'))
        dept = input('Enter department:')
        eObj = Employee(emp_id, name, sal, dept)
=======
            if(ch == '1'):
                self.addEmp()
            elif(ch == '2'):
                self.showAllEmp()
            elif(ch == '3'):
                self.searchEmp()
            elif(ch == '4'):
                self.updEmp()
            elif(ch == '5'):
                self.delEmp()
            elif(ch == '6'):
                print('Logged out...')
            else:
                print('Invalid choice...')
    
    def addEmp(self):
        id = input('Enter id:')
        name = input('Enter name:')
        sal = int(input('Enter salary:'))
        dept = input('Enter department:')
        eObj = Employee(id, name, sal, dept)
>>>>>>> 328a1f15386175bedcd9e339c982b5cdaee04151
        res = self.ds.addData(eObj)
        print(res)

    def showAllEmp(self):
        res = self.ds.getData()
        for e in res:
            columns = ['id', 'name', 'sal', 'dept']
<<<<<<< HEAD
            if storage == 'Dictionary':
=======
            if(storage == 'Dictionary'):
>>>>>>> 328a1f15386175bedcd9e339c982b5cdaee04151
                for key, value in zip(columns, e.toTuple()):
                    print(key, ':', value)
            else:
                for key, value in zip(columns, e):
                    print(key, ':', value)
            print('######################')

    def searchEmp(self):
<<<<<<< HEAD
        emp_id = input('Enter id:')
        res = self.ds.searchData(emp_id)
        if res:
=======
        id = input('Enter id:')
        res = self.ds.searchData(id)
        if(res):
>>>>>>> 328a1f15386175bedcd9e339c982b5cdaee04151
            print(res)
        else:
            print('Employee not found.')

    def updEmp(self):
<<<<<<< HEAD
        emp_id = input('Enter id:')
        res = self.ds.searchData(emp_id)
        if res:
            print('NOTE: Leave field empty if no need to change value.')
            if storage == "Dictionary":
                eData = res.toTuple()
            else:
                eData = res
            name = input(f'Enter name({eData[1]}):') or eData[1]
            sal = input(f'Enter sal({eData[2]}):') or eData[2]
            dept = input(f'Enter dept({eData[3]}):') or eData[3]
            eObj = Employee(emp_id, name, sal, dept)
=======
        id = input('Enter id:')
        res = self.ds.searchData(id)
        if(res):
            print('NOTE: Leave field empty if no need to change value.')
            eData = res
            name = input(f'Enter name({eData[1]}):') or eData[1]
            sal = input(f'Enter sal({eData[2]}):') or eData[2]
            dept = input(f'Enter dept({eData[3]}):') or eData[3]
            eObj = Employee(id, name, sal, dept)
>>>>>>> 328a1f15386175bedcd9e339c982b5cdaee04151
            res = self.ds.updData(eObj)
            print(res)
        else:
            print('Employee not found.')

    def delEmp(self):
<<<<<<< HEAD
        emp_id = input('Enter id:')
        res = self.ds.searchData(emp_id)
        if res:
            res = self.ds.delData(emp_id)
=======
        id = input('Enter id:')
        res = self.ds.searchData(id)
        if(res):
            res = self.ds.delData(id)
>>>>>>> 328a1f15386175bedcd9e339c982b5cdaee04151
            print(res)
        else:
            print('Employee not found.')

<<<<<<< HEAD
if __name__ == '__main__':
    aObj = Admin()

=======
if(__name__ == '__main__'):
    aObj = Admin()
>>>>>>> 328a1f15386175bedcd9e339c982b5cdaee04151
