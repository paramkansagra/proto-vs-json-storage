import employee_pb2

param: employee_pb2.Employee = employee_pb2.Employee(id=1, name="param", salary=1000)
jayesh: employee_pb2.Employee = employee_pb2.Employee(id=2, name="jayesh", salary=2000)
mayuri: employee_pb2.Employee = employee_pb2.Employee(id=3, name="mayuri", salary=3000)
pari: employee_pb2.Employee = employee_pb2.Employee(id=4, name="pari", salary=4000)

employee_list: employee_pb2.Employees = employee_pb2.Employees(
    employeeList=[param, jayesh, mayuri, pari]
)

encoded_string = employee_list.SerializeToString()

file = open("proto_data", "wb+")
file.write(encoded_string)
file.close()

# here the proto data is only taking 65 bytes of size
# thus it is way way better in network calls
