from calc import calculator as cl


if __name__ == "__main__":


	obj = cl()

	while True:
		print ("options")
		print ("add")
		print ("sub")
		print ("mul")
		print ("div")
		print ("per")
		print ("pnr")
		print ("exit")

		user = input(":")

		if user == "exit":
				break
		elif user == "add":
			num1 = float(input("enter no1:"))
			num2 = float(input("enter no2:"))
			result = obj.add(num1,num2)
			print (result)
			
		elif user == "sub":
			num1 = float(input("enter no1:"))
			num2 = float(input("enter no2:"))
			result = obj.sub(num1,num2)
			print (result)

		elif user == "mul":
			num1 = float(input("enter no1:"))
			num2 = float(input("enter no2:"))
			result = obj.mul(num1,num2)
			print (result)

		elif user == "div":
			num1 = float(input("enter no1:"))
			num2 = float(input("enter no2:"))
			result = obj.div(num1,num2)
			print (result)

		elif user == "per":
			num1 = float(input("enter no1:"))
			num2 = float(input("enter no2:"))
			result = obj.per(num1,num2)
			print (result)
		elif user == "pnr":
			num1 = float(input("enter principle:"))
			num2 = float(input("enter number of years:"))
			num3 = float(input("enter rate of int:"))
			result = obj.si(num1,num2,num3)
			print (result)







		num1 = float(input("enter no1:"))
		num2 = float(input("enter no2:"))

		print (obj.add(num1,num2))
		print (obj.multiplication(num1,num2))
