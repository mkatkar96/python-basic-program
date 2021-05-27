#1.reading a external file

employee_file = open("mydata.txt","r")
print(employee_file.readlines())
employee_file.close()

#2.writing and appending external file


employee_file = open("emp.html","w")      #a,,r,w. ,
employee_file.write("5.tobi    human resouse     $450")
employee_file.write("\n6.        kelly          customer service    $450")
employee_file.close()

