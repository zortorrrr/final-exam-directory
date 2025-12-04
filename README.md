# Project title

## Project overview:
this project is part of Special Instructions for OOP
its about 4 Class that work together
1.Person class
2.Customer class
3.Driver class
4.DeliveryOrder class

Customer and Driver both use a inheritance frome Person that is a perant class and both of them
are have their own attribult 

store their own attribult and working tohether with Delivery class 

This problem want student to solve about how to store variable and combine medthod together update some variable and call in main function look like the problem it gave us.



## Features
### 1.Person class
Attributes: name
Method: introduce() → prints:
 Hi, I'm <name>.

### 2.Customer class
Additional attribute: address
Method: place_order(item) →
 returns a new DeliveryOrder object for the given item

### 3.Driver class
Additional attribute: vehicle
Method: deliver(order) →
 prints:
 <driver_name> is delivering <item> to <customer_name> using <vehicle>.
Should update the order’s status to "delivered"

### 4.DeliveryOrder class
Attributes:
customer
item
status (initially "preparing")

Methods:
assign_driver(driver)
summary() → returns a string describing the order


## How to run
first we creates two customers and one driver and then, give each customer places an order then we give the driver is assigned to each order.
after that we call medthod driver delivers to recive the orders
then the program should prints the exact output shown below.

Hi, I'm Alice.
Hi, I'm Bob.
Hi, I'm David.

Order Summary:
Item: Laptop
Customer: Alice
Status: preparing
Driver: David

Order Summary:
Item: Headphones
Customer: Bob
Status: preparing
Driver: David

David is delivering Laptop to Alice using motorcycle.
David is delivering Headphones to Bob using motorcycle.

Final Status:
Order for Laptop → delivered
Order for Headphones → delivered



## Project structure
final-exam directory/ │ ├── README.md │ ├── final.py/ │ 

## there are still some bugs
i know object this problem want me to do but there are 2 big problem that i dont know how to sole it
1. in line 30 i dont konw how to call a attribult name of the customer to use in this line
2. i cant update a order’s status to "delivered" as you can see in my code you will see im trying tp update it
with boolean but it still not working so that why i create a new medthod to show status when it deliverd

# Name: Kasithat Panya 
# Student ID: 6810545450


