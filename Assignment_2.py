
# Customer class :This will handel all the data related to  customer

class Customer():

    rate_of_discount = 0

    def __init__ (self, cus_id, cus_name):
        self.cus_id = cus_id
        self.cus_name = cus_name

    #get discount method 
    def get_discount(self, price):
        return self.rate_of_discount
    

#class RetailCustomer : This will handel all the data and methods  related to retail customer

class RetailCustomer(Customer):
    # defining class variable discount for retail class 
    rate_of_discount = 0.1

    #inherited variables from customer class
    def __init__(self, retail_customer):
        super().__init__(cus_id = retail_customer[0], cus_name = retail_customer[1])

    #method to check weather customer available in retail class
    def get_if_cus_avilable(self,name):
        
        if self.cus_name == name:
            return True
        elif self.cus_id == name:
            return True
    
    #method to set rate of discount if the user changes rate of discount 
    @staticmethod
    def setRate(self,rate_of_discount):
        self.rate_of_discount = (rate_of_discount / 100)

    #method to get discount for total price

    def get_discount(self, price):
        return int (self.rate_of_discount*price)

    #method to display retail customer details
    def displayCustomer(self):
        return('{} {}'.format(self.cus_id,self.cus_name))
        

#class WholesaleCustomer : This will handel all the data and methods related to Whole sale customer
    
class WholesaleCustomer(Customer):
    
    # defining class variable discount for wholesale calss
    rate_of_discount = 0.1
    #defining excess_discout which is always 5 % more that rate of discount
    excess_discount = 0.05

    #inherited variables from customer class
    def __init__(self, whole_sale_customer):
        super().__init__(cus_id = whole_sale_customer[0], cus_name = whole_sale_customer[1])

    #method to check weather customer available in wholecustomer class
    def get_if_cus_avilable(self,name):
        
        if self.cus_name == name:
            return True
        elif self.cus_id == name:
            return True
    
  #method to set rate of discount if the user changes rate of discount 
    @staticmethod
    def setRate(self,rate_of_discount):
        self.rate_of_discount = (rate_of_discount / 100)

    #method to get discount for total price if price is > 1000 discount is discount + 5 percent 
    def get_discount(self, price):

        if price < 1000:
            return int (self.rate_of_discount*price)
        elif price > 1000:
            return int ((self.rate_of_discount + self.excess_discount ) *price)

    #method to display retail wholesale customer details
    def displayCustomer(self):
        return('{} {}'.format(self.cus_id,self.cus_name))


#Class product: this will handel all the data and methods related to Products 

class Product:

    def __init__(self,product):

        self.prd_id = product[0]
        self.prd_name = product[1]
        self.price = float(product[2])
        self.stock = int(product[3])

    #method to get pricce of product
    def get_price(self):
        return self.price
    
    #method to get current stock of product
    def get_stock(self):
        return self.stock

# Class Records : this will handel all the data and methods related to Records

class Records():

    #defining product data and customer data variables to store data read from files
    product_data =[]
    def __init__(self):
        self.customer_data =[]
        
    # method to read customer files
    def readCustomers(self, file_name):
        try:
            customer_file = open(file_name, "r")
            line = customer_file.readline()
            while(line != ""):
                line = line.strip().split(",")
                line = [x.strip()for x in line]
                self.customer_data.append(line)
                line = customer_file.readline()
            customer_file.close()
        except:
            print("File open error, quitting program...")
            exit  
        return(self.customer_data)    

    # method to read product files
    def readProducts(self, file_name):
        try:
            product_file = open(file_name, "r")
            line = product_file.readline()
            while(line != ""):
                line = line.strip().split(",")
                line = [x.strip()for x in line]
                self.product_data.append(line)
                line = product_file.readline()
            product_file.close()

        except:
            print("File open error, quitting program...")
            exit    
        return(self.product_data)     


    ## method to find customer name in customer_data
    def findCustomers( self,customer_name ):
        
        for i  in self.customer_data:
            exist = False
            if customer_name in  i:
                exist = True
                break    

        return   exist 

    ## method to find product name in product_data
    def findProduct( self,product_name ):
        exist = None
        for i  in range(len(self.product_data)):
            if product_name in self.product_data[i]:
                exist =  i
                break
            else:
                exist = None
        return exist

    ## method to show  customer list    
    def listCustomers(self):

        print('\n')
        print('='*70)
        print(" "*30 + 'Customer data' + " "*30)
        print('='*70)
        print(f"{'ID':5s}{'Name':20s}{'Customer Type':18s}{'Discount Rate':18s}{'Total'}")
        print('-'*70)

        for i in range(len(self.customer_data)):

            print(f"{self.customer_data[i][0]:5s}{self.customer_data[i][1]:20s}{self.customer_data[i][2]:18s}{self.customer_data[i][3]:18s}{self.customer_data[i][4]}")

        print('-'*70+'\n')

    #method to display product list
    def listProducts(self):
       
        print('\n')
        print('='*50)
        print(" "*20 + 'Product data' + " "*20)
        print('='*50)
        print(f"{'ID':5s}{'Product Name':20s}{'Price':18s}{'Stock'}")
        print('-'*50)
        
        for i in range(len(self.product_data)):

            print(f"{self.product_data[i][0]:5s}{self.product_data[i][1]:20s}{self.product_data[i][2]:18s}{self.product_data[i][3]}")

        print('-'*50+'\n')

    #class method to read product_data
    @classmethod
    def get_product_data(cls):
        
        return cls.product_data
    
    #method to update product data
    @classmethod
    def set_product_date(cls,product):
        cls.product_data = product


# Class order: this will handel all the data and methods related to orders
class Order():

    record_manager = Records()

    def __init__(self,name_of_Customer,name_of_product,quantity_of_product,price_of_product,discount) :

        self.name_of_Customer = name_of_Customer
        self.name_of_product = name_of_product
        self.quantity_of_product = quantity_of_product
        self.price_of_product = price_of_product
        self.discount = discount

    # Method used to udpate the stock 
    def update_stock(self):

       product = self.record_manager.get_product_data()
       for i in product:
        if self.name_of_product in i:
             i[3] = int(i[3]) - int(self.quantity_of_product)
       self.record_manager.set_product_date(product)

    #Price calculator and bill statment
    def final_bill(self):
        price_calculate =( float(self.price_of_product) * int(self.quantity_of_product)) - float(self.discount)
        print ("\n'" + str(self.name_of_Customer) +"' purchased '" + str(self.quantity_of_product) + "' x '" + self.name_of_product + "'\n"
            "Unit price: $"  + str(self.price_of_product)  + "\n"
            "Total price: $" + str(price_calculate)+"\n"
            "Toatl discount: $"+str(self.discount))

# Main Function which handels all the operations

def main():

    def escape_function():
        escape_1 =True
        while True:
            escape = input("\n Press '1' to go to main Menu : ") 

            if escape == '1':
                print('Taking you to main Menu ') 
                escape_1 = False
                break
            else:
                escape_1 = True
        pass
    # Creating record objects one for customer and another for products
    customer_records = Records()
    product_records = Records()

    #reading the customer file
    customer_records_1 = customer_records.readCustomers("customers.txt")

    #reading the product file
    product_records_1 = product_records.readProducts("products.txt")
    
    # Creating Product class objects
    product_class=[]
    for i in product_records_1:
        product_class.append(Product(i))
    
    # Creating retail class and whole sale class objects
    customer_class_retail=[]
    customer_class_whole_sale =[]

    # segerating the objects 
    for i in customer_records_1:
        if i[2].lower() == 'r':
            customer_class_retail.append(RetailCustomer(i))
        elif i[2].lower() == 'w':
            customer_class_whole_sale.append(WholesaleCustomer(i))

    # Main Menu 
    while True:

        print('\n\n'+"*"*60)
        print(" "*8 +"Warehouse Inventory Management Software"+" "*8)
        print("*"*60)
        print(f'{" ":25s}{"---------":9s}{" ":26s}')
        print(f'{" ":26s}{"M E N U":4s}{" ":26s}')
        print(f'{" ":25s}{"---------":9s}{" ":26s}')
        print(f'{"1.Customer List":52s}{"Press 1":10s}')
        print(f'{"2.Product List":52s}{"Press 2":10s}')
        print(f'{"3.For Billing Desk":52s}{"Press 3":10s}')
        print(f'{"4.Exit from program":52s}{"Press 4":10s}')
   

        menu_key = input("\nEnter the number to access the respective menu : ")

        try:
           menu_key = int(menu_key)  
        except ValueError:
            print("\n'Invalid Input' Please enter a valid number \n")
            continue
        if menu_key == 1:
            customer_records.listCustomers()

            escape_function()
        
        elif menu_key == 2:
            product_records.listProducts()

            escape_function()
        
        #--------------- Billing Desk---------------------------#
        elif menu_key == 3:

            name_of_Customer = input("\nEnter the name of the customer or customer ID : ")

            name_of_product = input("\nEnter the name of the product or product ID: ")

            quantity_of_product = input("\nEnter the quantity of the product : ")
            
            quantity_of_product = int(quantity_of_product)

            price_of_product = product_class[product_records.findProduct(name_of_product)].get_price()
            total_price = price_of_product * quantity_of_product
            discount = 0
            
            if  customer_records.findCustomers(name_of_Customer):
                for i in range(len(customer_class_retail)):

                    if customer_class_retail[i].get_if_cus_avilable(name_of_Customer):
                    
                        discount = customer_class_retail[i].get_discount(total_price)

                for i in range(len(customer_class_whole_sale)):
                    
                    if customer_class_whole_sale[i].get_if_cus_avilable(name_of_Customer):
                    
                        discount = customer_class_whole_sale[i].get_discount(total_price)
            else:
                discount = 0


            order_update = Order(name_of_Customer,name_of_product,quantity_of_product,price_of_product,discount)
            order_update.final_bill()
            order_update.update_stock()
            escape_function()

        elif menu_key == 4:
            exit()


            

































        else:
            print("\n'Invalid Input' Please enter a valid number \n")




        
if __name__=="__main__":
    main()




        



         























# customeer1 = WholesaleCustomer('1','srujan')
# # print(customeer1.setRate(10))
# print(customeer1.get_discount(2000))