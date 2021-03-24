from C2_EmpModule import Employee  #importing Employee class
import pickle

f = open('emp.ser','wb')

while True:
 eno = int(input('enter eno'))
 ename = input('enter ename')
 esal = float(input('enter esal'))
 e = Employee(eno,ename,esal)
 pickle.dump(e,f)
 option = input("Continue? [yes/no]")
 if option.lower() == 'no':
  break
print("Multiple Employee Object serialized")
