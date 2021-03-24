#from C2_EmpModule import Employee
import pickle
f = open('emp.ser','rb')
while True:
 try:
  e = pickle.load(f)
  e.display()
 except EOFError:
  break