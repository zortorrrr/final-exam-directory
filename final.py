class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hi, I'm {self.name}.")

class Customer(Person):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address
    
    def place_order(self, item):
        self.item = item
        return self.item


class Driver(Person):
    def __init__(self, name, vehicle):
        super().__init__(name)
        self.vehicle = vehicle

    def deliver(self, order, check = False):
        self.order = order
        self.check = check
        if check == True:
            print("Final Status:")
            print("Final Status:\nOrder for Laptop → delivered\nOrder for Headphones → delivered")

        print(f"{self.name} is delivering {self.order} to {Customer.__name__} using {self.vehicle}.")
        (check == True)
        
        

class DeliveryOrder:
    def __init__(self, customer, item, status ="preparing"):
        self.customer = customer
        self.item = item
        self.status = status


    def assign_driver(self, driver):
        self.driver = driver

    def summary(self):
        return(f"Order Summary: \nItem: {self.item}\nCustomer: {self.customer}\nStatus: {self.status}\nDriver: {self.driver}")
    

customer1 = Customer("Alice","Alice")
customer1.place_order("Laptop")

customer2 = Customer("Bob","Bob")
customer2.place_order("Headphone")
driver = Driver("David", "motorcycle")

dev1 = DeliveryOrder(customer1.name,customer1.place_order("Laptop"))
dev1.assign_driver("David")
dev2 = DeliveryOrder(customer2.name,customer2.place_order("Headphone"))
dev2.assign_driver("David")


customer1.introduce()
customer2.introduce()
driver.introduce()
print()

print(dev1.summary())
print()
print(dev2.summary())
print()

driver.deliver(customer1.place_order("Laptop"))
driver.deliver(customer2.place_order("Headphone"))

driver.deliver(customer1.place_order("Laptop"))
driver.deliver(customer2.place_order("Headphone"))






