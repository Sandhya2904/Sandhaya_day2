Emp = ['101,sandy,sales,1000','102,sarthik,prod,2000','103,deepak,hr,3000','104,aadi,sales,4000']
total = 0
for var in Emp:
    eid,ename,edept,ecost = var.split(',')
    print(f"Emp Name:{ename.title()}\t Emp Dept:{edept.upper()}")
    total = total +int(ecost)
print(f"\nTotal Salary:{total}") 

    
