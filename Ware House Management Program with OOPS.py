
from datetime import date
##########################################################################################
#                                   class       Customer                                 #
##########################################################################################

# Customer class :This will handel all the data related to  customer

class Customer():

    rate_of_discount = 0

    def __init__ (self, cus_id, cus_name):
        self.cus_id = cus_id
        self.cus_name = cus_name

    #get discount method 
    def get_discount(self, price):
        return self.rate_of_discount
    
##########################################################################################
#                                   class RetailCustomer                                 #
##########################################################################################

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
    @classmethod
    def setRate(cls,rate_of_dis):
        cls.rate_of_discount = (rate_of_dis / 100)

    #method to get discount for total price

    def get_discount(self, price):
        return int (self.rate_of_discount*price)

    #method to display retail customer details
    def displayCustomer(self):
        return('{} {}'.format(self.cus_id,self.cus_name))


##########################################################################################
#                                   class WholesaleCustomer                              #
##########################################################################################

#class WholesaleCustomer : This will handel all the data and methods related to Whole sale customer
    
class WholesaleCustomer(Customer):
    
    # defining class variable discount for wholesale calss
    
    #defining excess_discout which is always 5 % more that rate of discount
    excess_discount = 0.05

    threshold = 1000

    #inherited variables from customer class
    def __init__(self, whole_sale_customer):
        super().__init__(cus_id = whole_sale_customer[0], cus_name = whole_sale_customer[1])
        self.cus_rod = float(whole_sale_customer[3])

    #method to check weather customer available in wholecustomer class
    def get_if_cus_avilable(self,name):
        
        if self.cus_name == name:
            return True
        elif self.cus_id == name:
            return True

    #method to get discount for total price if price is > 1000 discount is discount + 5 percent 
    def get_discount(self, price):

        if self.cus_rod != ' ':

            if price < self.threshold:
                return  (self.cus_rod*0.01)* (price)
            elif price > self.threshold:

                return  ((self.cus_rod*0.01) + 0.05 ) *price 
        else:
            if price < self.threshold:
                return  (0.1*price)
            elif price > self.threshold:
                return  (0.1 + 0.05 ) * (price)

    #method to display retail wholesale customer details
    def displayCustomer(self):
        return('{} {}'.format(self.cus_id,self.cus_name))
    
    @classmethod
    def setThreshold(cls,trhold):
        cls.threshold = trhold

##########################################################################################
#                                   class Product                                        #
##########################################################################################

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
    
    def updateStockProduct(self,stock):
        self.stock = stock

##########################################################################################
#                                   Class Records                                        #
##########################################################################################

#Class combos: this will handel all the data and methods related to combos 

class Combo():


    def __init__(self,combo_products):

        self.combo_ID = combo_products[0]
        self.combo_name = combo_products[1]
        self.comb_prod = combo_products[2]
        self.comb_stock = int(combo_products[3])
    
    def getproducts(self):
        return self.comb_prod

    def get_stock(self):
        return self.comb_stock
    
    def updateStockCombo(self,stock):
        self.comb_stock = stock

##########################################################################################
#                                   Class Records                                        #
##########################################################################################

# Class Records : this will handel all the data and methods related to Records

class Records():

    #defining product data and customer data variables to store data read from files
    product_data =[]
    combo_data =[]
    orders_data = []
    customer_data =[]
    
    def __init__(self):
        pass    
        
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
            return(self.customer_data)
        except FileNotFoundError:
            print(file_name + " File Not found , quitting program...")
            quit()  
            

    # method to read product files
    def readProducts(self, file_name):
        try:
            product_file = open(file_name, "r")
            line = product_file.readline()
            while(line != ""):
                line = line.strip().split(",")
                line = [x.strip()for x in line]
                if line[0][0].lower() == 'p':
                    self.product_data.append(line)
                elif line[0][0].lower() == 'c':
                        combo = [line[0],line[1],line[2:-2],line[-1]]
                        self.combo_data.append(combo)
                line = product_file.readline()
            product_file.close()
            return(self.product_data,self.combo_data)

        except FileNotFoundError:
            print(file_name + " File Not found , quitting program...")
            quit()   
        
    
    def readOrders(self, file_name):
      try:
         product_file = open(file_name, "r")
         line = product_file.readline()
         while(line != ""):
               line = line.strip().split(",")
               line = [x.strip()for x in line]
               orders = [line[0],line[1],line[2]]
               self.orders_data.append(orders)
               line = product_file.readline()
         product_file.close()
         return(self.orders_data)

      except FileNotFoundError:
   
         print( file_name + " No such file found in directory")
         exit 
      except:
         print("Corrupt file")     
    #method used to get products only
    def get_products(self):
        return self.product_data
    #method used to get combo products only
    def get_combo_products(self):
        return self.combo_data

    ## method to find customer name in customer_data
    def findCustomers( self,customer_name ):

        for i in range(len(self.customer_data)):
           
            if (customer_name == self.customer_data[i][0] ) or (customer_name == self.customer_data[i][1] ):
                return(self.customer_data[i][1]) 
                break 

        return None

    #method to create new customer
     
    def create_customer(self,name,type_of_customer):
        i = len(self.customer_data)
        
        new_customer = [ str(int(self.customer_data[i-1][0])+1) , name , type_of_customer , '0' ,'0' ]
        self.customer_data.append(new_customer)


    ## method to find product name in product_data
    def findProduct( self,product_name ):

        for i  in range(len(self.product_data)):
            if (product_name == self.product_data[i][0]) or (product_name == self.product_data[i][1]):
                return [i,self.product_data[i][1]]
                break
        return None   

    # method to find combo product name in combo data
    def findComboProduct(self,product_name):
        for i  in range(len(self.combo_data)):
            if (product_name == self.combo_data[i][0]) or (product_name == self.combo_data[i][1]):
                return [i,self.combo_data[i][1]]
                break
        return None  


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
        if len(self.combo_data) > 0:
            print('='*67)
            print(" "*25 + 'Combo data' + " "*25)
            print('='*67)
            print(f"{'ID':5s}{'Combo Name':21s}{'Products':35s}{'Stock'}")
            print('-'*67)
            for i in range(len(self.combo_data)):

                print(f"{self.combo_data[i][0]:5s}{self.combo_data[i][1]:20s} {str(self.combo_data[i][2]):35s} {self.combo_data[i][3]}")

            print('-'*67+'\n')

    #class method to read product_data
    @classmethod
    def get_product_data(cls):
        
        return cls.product_data
    
    #method to update product data
    @classmethod
    def set_product_data(cls,product):
        cls.product_data = product
    
    @classmethod
    def getComboProductData(cls):
        
        return cls.combo_data
    
    #method to update product data
    @classmethod
    def setComboProductData(cls,product):
        cls.combo_data = product

    @classmethod
    def getCustomerData(cls):
        return cls.customer_data
    
    @classmethod
    def setCustomerData(cls,customer):
         cls.customer_data = customer

##########################################################################################
#                                  Class Order                                           #
##########################################################################################

# Class order: this will handel all the data and methods related to orders

class Order():

    record_manager = Records()
    quantity_of_product= []
    price_of_product =[]
    name_of_product  = []
    order_list = []
    current_stock = []

    def __init__(self,name_of_Customer,name_of_product,quantity_of_product,date) :

        self.name_of_Customer = name_of_Customer
        self.name_of_product = name_of_product
        self.quantity_of_product = quantity_of_product
        self.date = date
        # self.price_of_product = price_of_product
        #self.discount = 0
        # self.total = total_price
    def getOrderDetails(self):

        return (self.name_of_Customer,self.name_of_product,self.quantity_of_product)
    
    def updateCustomer(self,total):

        customer = self.record_manager.getCustomerData()
        for i in range(len(customer)):
            if self.name_of_Customer == customer[i][1]:
                customer[i][4] = str(float(customer[i][4]) + float(total))
            self.record_manager.setCustomerData(customer)


    # Method used to udpate the stock 
    def update_stock(self):
       self.current_stock.clear()
       product = self.record_manager.get_product_data()
       combo_data = self.record_manager.getComboProductData()
       for i in range(len(product)):
           
           for j in range(len(self.name_of_product)):

                if self.name_of_product[j] == product[i][1]:
                    product[i][3] = str(int(product[i][3]) - int(self.quantity_of_product[j]))
                    
                    stock_u = product[i][3]
                    self.current_stock.append(stock_u) 
                    # product = str(product)
                self.record_manager.set_product_data(product)
                


       for i in range(len(combo_data)):
           
           for j in range(len(self.name_of_product)):

                if self.name_of_product[j] == combo_data[i][1]:

                    combo_data[i][3] = str(int(combo_data[i][3]) - int(self.quantity_of_product[j]))
                    stock_u = combo_data[i][3]
                    self.current_stock.append(stock_u) 
                self.record_manager.setComboProductData(combo_data)
                # self.current_stock.append(combo_data[i][3])            
        
    
    def updateStockForList(self):
       self.current_stock.clear()
       product = self.record_manager.get_product_data()
       combo_data = self.record_manager.getComboProductData()
       
       for i in range(len(product)):
           
            if self.name_of_product == product[i][1]:
                product[i][3] = str(int(product[i][3]) - int(self.quantity_of_product))
                stock_u = product[i][3]
                self.current_stock.append(stock_u)
            self.record_manager.set_product_data(product)

       for i in range(len(combo_data)):
           
            if self.name_of_product == combo_data[i][1]:
                combo_data[i][3] = str(int(combo_data[i][3]) - int(self.quantity_of_product))
                stock_u = combo_data[i][3]
                self.current_stock.append(stock_u)
            self.record_manager.setComboProductData(combo_data)   
    
    #Price calculator and bill statment
    def final_bill(self,price_of_product_1,total_price):

        if type(self.quantity_of_product) == str:
            quantity = self.quantity_of_product
        elif type(self.quantity_of_product) == list:
            quantity = ', '.join(str(v) for v in self.quantity_of_product)
        
        if type(self.name_of_product) == str:
            name_product = self.name_of_product
        elif type(self.name_of_product) == list:
            name_product = ', '.join(str(v) for v in self.name_of_product)



        bill = "'{}' Purchased '{}' X '{}' \nUnit price: $'{}' \nTotal price: $'{}' \nDate: '{}' "
        print (bill.format( self.name_of_Customer, (quantity), 
        (name_product), str(', $'.join(str(v) for v in price_of_product_1)),round(total_price,4),(self.date)))
        print("Remaining stock :{} \n".format( ', '.join(str(v) for v in self.current_stock)))

        orders = [self.name_of_Customer,self.name_of_product,self.quantity_of_product,total_price,self.date]
        self.order_list.append(orders)

    @classmethod
    def getOrdersList (cls):
        return cls.order_list

#################################################################################################################################
#                                Main Function which handels all the operations                                                 #
#################################################################################################################################
def main():

    def escape_function():
        escape_1 =True
        while True:
            escape = input("\nPress '1' to go to main Menu : ") 

            if escape == '1':
                print('\nTaking you to main Menu . . . ') 
                escape_1 = False
                break
            else:
                escape_1 = True

##--------------------------------------------------------------------------------------------------------------------------------------`
    # Creating record objects one for customer and another for products
    customer_records = Records()
    product_records = Records()

    file = input("Enter Customer and Product Files with the same sequence and with a space in between (ex: customer.txt,products.txt) : \n")

    if file:
        try:
            files = file.split(",")
            customer_file = files[0]
            product_file = files[1]
        except IndexError:
            print("Wrong format of file while entring, it should be(customer.txt,product.txt)")
            print("Quitting program")
            quit()
    else:
        customer_file = "customers.txt"
        product_file = "products.txt"
    
    print(customer_file,product_file)

    #reading the customer file
    customer_records_1 = customer_records.readCustomers(customer_file)

    #reading the product file
    product_records.readProducts(product_file)

    product_records_1 = product_records.get_products()
    combo_class_1 = product_records.get_combo_products()
    
    # Creating Product class objects
    product_class=[]
    for i in product_records_1:
        product_class.append(Product(i))
    
    combo_class =[]
    for i in combo_class_1:
        combo_class.append(Combo(i))

    # Creating retail class and whole sale class objects
    customer_class_retail=[]
    customer_class_whole_sale =[]

    # segerating the objects 
    for i in customer_records_1:
        if i[2].lower() == 'r':
            customer_class_retail.append(RetailCustomer(i))
        elif i[2].lower() == 'w':
            customer_class_whole_sale.append(WholesaleCustomer(i))
        ##########################################################################################
        #                                   Main Menu                                            #
        ##########################################################################################
    while True:

        print('\n\n'+"*"*60)
        print(" "*8 +"Warehouse Inventory Management Software"+" "*8)
        print("*"*60)
        print(f'{" ":25s}{"---------":9s}{" ":26s}')
        print(f'{" ":26s}{"M E N U":4s}{" ":26s}')
        print(f'{" ":25s}{"---------":9s}{" ":26s}')
        print(f'{"1.    Customer List":52s}{"Press 1":10s}')
        print(f'{"2.    Product List":52s}{"Press 2":10s}')
        print(f'{"3.    For Manual Billing Desk":52s}{"Press 3":10s}')
        print(f'{"4.    For Uploading Order List":52s}{"Press 4":10s}')
        print(f'{"5.    set Retail Customer Discount rate":52s}{"Press 5":10s}')
        print(f'{"6.    set Threshold for Wholesale customers":52s}{"Press 6":10s}')
        print(f'{"7.    Order History":52s}{"Press 7":10s}')
        print(f'{"8.    Replenish":52s}{"Press 8":10s}')
        print(f'{"9.    Most Valuable Customer":52s}{"Press 9":10s}')
        print(f'{"10.   To Quit the program":52s}{"Press 10":10s}')
        

   

        menu_key = input("\nEnter the number to access the respective menu : ")

        try:
           menu_key = int(menu_key)  
        except ValueError:
            print("\n'Invalid Input' Please enter a valid number \n")
            continue
        ##########################################################################################
        #                                    Display Customer List                               #
        ##########################################################################################
        if menu_key == 1:
            #litsing customer data
            customer_records.listCustomers()

            escape_function()
        
        ##########################################################################################
        #                                    Display Product List                                #
        ##########################################################################################
        elif menu_key == 2:
            #litsing product data
            product_records.listProducts()

            escape_function()
        
        ##########################################################################################
        #                                    manual billing desk                                 #
        ##########################################################################################
        elif menu_key == 3:
            manual = True
            while manual:
                price_of_product_1 =[]
                quantity =[]
                name_product =[]

                # asking for customer name
                name_of_Customer = input("\nEnter the name of the customer or customer ID : ")
                #Finding customer present or not
                customer_name = customer_records.findCustomers(name_of_Customer)
                name_of_Customer = customer_name

                #adding new customer
                if customer_name == None:
                    confirm_yes = input("Do you want to create a new customer. If yes Press 'Y/y' to confirm : " )
                    if   confirm_yes.lower() == 'y':
                        name_of_Customer = input("Enter Name : ")
                        type_of_customer = input ("category (R or W) :")
                        customer_records.create_customer(name_of_Customer,type_of_customer)

                prd =True
                while prd:
                    
                    #asking for product name
                    name_of_product = input("\nEnter the name of the product or product ID: ")
                    
                    #check product avialble or not
                    product_1 = product_records.findProduct(name_of_product)


                    #if product avialble
                    if product_1 != None:
                        #price of product
                        price_of_product = product_class[product_1[0]].get_price()

                        if price_of_product == 0 and customer_name == None:
                            print("\nNew Customers cannot take Free products")
                            
                        elif float(price_of_product)  >= 0 and  price_of_product != ' ':
                            quantity_summary =True
                            while  quantity_summary:       
                                quantity_of_product = input("\nEnter the quantity of the product : ")
                                quantity_of_product = int(quantity_of_product)
                                stock = product_class[product_1[0]].get_stock()
                            
                                if stock - quantity_of_product >= 0:
                                    quantity.append(quantity_of_product)
                                    price_of_product_1.append(price_of_product)
                                    name_product.append(product_1[1])
                                    update_stock = stock - quantity_of_product
                                    product_class[product_1[0]].updateStockProduct(update_stock)
                                    quantity_summary =False
                                else:
                                    print("\nQuantity entred is not available \n The stock available for this product is " + str(stock))
                                    quantity_summary =False
                                    # if stock > 0:
                                        # re_enter = input("\nPress '1' if you wish to re enter the quantity :")
                                        # if re_enter == '1':
                                        #     quantity_summary =True
                                        # else:
                                        #     quantity_summary =False
                                one_more_order = input("\npress '1' if you want to order one more product :")

                                if one_more_order == '1':
                                    prd =True
                                else:
                                    prd = False


                        else:
                            print('Price of product is not valid please select another product')
                        # prd =False
                    #if product not avilable
                    elif product_1 == None:

                        combo_prd = product_records.findComboProduct(name_of_product)
                        
                        if combo_prd != None:
                            products_combo = combo_class[combo_prd[0]].getproducts()
                            name_product.append(combo_prd[1])
                            product_combo_names =[]
                            for i in products_combo:

                                product_1 = product_records.findProduct(i)
                                product_combo_names.append(product_1[0])
                            price_of_prod_combo=[]    
                            for i in product_combo_names:
                                price1 = product_class[i].get_price()
                                price_of_prod_combo.append(price1)
                            
                            combo_price = 0
                            for i in price_of_prod_combo:
                                combo_price += i
                            price_of_combo = combo_price * 0.1
                            
                            quantity_summary =True
                            while  quantity_summary:       
                                quantity_of_product = input("\nEnter the quantity of the product : ")
                                quantity_of_product = int(quantity_of_product)
                                stock = combo_class[combo_prd[0]].get_stock()
                            
                                if stock - quantity_of_product >= 0:
                                    quantity.append(quantity_of_product)
                                    price_of_product_1.append(price_of_combo)
                                    update_stock = stock - quantity_of_product
                                    combo_class[combo_prd[0]].updateStockCombo(update_stock)
                                    
                                    print(price_of_product_1,quantity)
                                    quantity_summary =False
                                else:
                                    print("\nQuantity entred is not available \n\nThe stock available for this product is " + str(stock))
                                    quantity_summary =False
                                    # if stock > 0:
                                    #     re_enter = input("\Press '1' if you wish to re enter the quantity :")
                                    #     if re_enter == '1':
                                    #         quantity_summary =True
                                    #     else:
                                            
                                            
                                one_more_order = input("\npress '1' if you want to order one more product :")

                                if one_more_order == '1':
                                    prd =True
                                else:
                                    prd = False

                        else:    
                            print("\nproduct name or ID does NOT exist")
                            prd =True
                if len(price_of_product_1) > 0:
                    
                    total_price = 0
                    for i in range(len(price_of_product_1)):
                        total_price += price_of_product_1[i] * quantity[i]
                    
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
                    
                    total_price = total_price - discount


                    today = date.today()
                    order_update = Order(name_of_Customer,name_product,quantity,today)
                    order_update.update_stock()
                    order_update.final_bill(price_of_product_1,total_price)

                    order_update.updateCustomer(total_price)
                    manual =False
                    escape_function()
                
                else:
                    break

        ##########################################################################################
        #                                    Uploading Order List                                #
        ##########################################################################################
        elif menu_key == 4:
            orders_records = Records()
            orders_objects =[]
            orders =True

            while orders:
                order_file = input("Enter the file name :")

                read_orders = orders_records.readOrders(order_file)

                if read_orders:              
                    for i in range(len(read_orders)):
                        today = date.today()
                        orders_objects.append(Order(read_orders[i][0],read_orders[i][1],read_orders[i][2],today))

                else:
                    print("File is corrupt or not found.Going back to main menu")
                    break   
                order_1 = input("Do you want to read one more file ? press 'Y/y' : ")

                if order_1.lower() == 'y':
                    orders =True
                else:
                    orders = False



            # for i in range(len(orders_objects)):    
            #     print(orders_objects[i].getOrderDetails())

               

            for i in range(len(orders_objects)):
                
                price_of_product_1 =[]
                quantity =[]
                name_product =[]
                product_1 = product_records.findProduct(orders_objects[i].name_of_product)
                customer_name = customer_records.findCustomers(orders_objects[i].name_of_Customer)

                orders_objects[i].name_of_Customer = customer_name
                if product_1 != None: 
                    orders_objects[i].name_of_product = product_1[1]
                    price_of_product = product_class[product_1[0]].get_price()
                    quantity_of_product = orders_objects[i].quantity_of_product
                    stock = product_class[product_1[0]].get_stock()
                    if int(stock) - int(quantity_of_product)  >= 0:
                        quantity.append(quantity_of_product)
                        price_of_product_1.append(price_of_product)
                        name_product.append(product_1[1])
                        update_stock = int(stock) - int(quantity_of_product)
                        product_class[product_1[0]].updateStockProduct(update_stock)
                    else:
                        print("Order cant be processed because quantity of product not available \n")

                elif product_1 == None:
        
                    #find is it a combo or not 
                    combo_prd = product_records.findComboProduct(orders_objects[i].name_of_product)

                    orders_objects[i].name_of_product = combo_prd[1]
                
                    #getting combo products
                    products_combo = combo_class[combo_prd[0]].getproducts()

                    product_combo_names =[]
                    for a in products_combo:
                        product_1 = product_records.findProduct(a)
                        product_combo_names.append(product_1[0])
                    
                    price_of_prod_combo=[]   

                    for b in product_combo_names:
                        price1 = product_class[b].get_price()
                        price_of_prod_combo.append(price1)

                    combo_price = 0

                    for j in price_of_prod_combo:
                        combo_price += j
                    price_of_combo = combo_price * 0.1


                    quantity_of_product = orders_objects[i].quantity_of_product
                    stock = combo_class[combo_prd[0]].get_stock()
                            
                    if int(stock) - int(quantity_of_product) >= 0:

                        quantity.append(quantity_of_product)

                        price_of_product_1.append(price_of_combo)
                        name_product.append(product_1[1])
                        update_stock = int(stock) - int(quantity_of_product)
                        combo_class[combo_prd[0]].updateStockCombo(update_stock)

                    else:
                        print("Order cant be processed because quantity of product not available\n")
                if len(price_of_product_1)  > 0:
                    total_price = 0
                    for k in range(len(price_of_product_1)):
                        total_price += price_of_product_1[k] * int(quantity[k])
            
                    discount = 0
                    
                    if  customer_records.findCustomers(orders_objects[i].name_of_Customer):
                        for z in range(len(customer_class_retail)):

                            if customer_class_retail[z].get_if_cus_avilable(orders_objects[z].name_of_Customer):
                            
                                discount = customer_class_retail[i].get_discount(total_price)

                        for z in range(len(customer_class_whole_sale)):
                            
                            if customer_class_whole_sale[z].get_if_cus_avilable(orders_objects[z].name_of_Customer):
                            
                                discount = customer_class_whole_sale[z].get_discount(total_price)
                    else:
                        discount = 0
                    
                    total_price = total_price - discount
                    orders_objects[i].updateStockForList()
                    orders_objects[i].final_bill(price_of_product_1,total_price)
                    orders_objects[i].updateCustomer(total_price)
                    
            escape_function()        
        ##########################################################################################
        #                                    Quitting the program                                #
        ##########################################################################################
        elif menu_key == 10 :
            print("\n 'Quitting the programe' \n")

            customer_list = customer_records.getCustomerData()
            with open(customer_file,"w") as f:
                for i in customer_list:
                    list1 = str(', '.join(i))
                    f.write('%s\n' % list1)
            f.close()
            product_list = product_records.get_product_data()
            with open(product_file,"w") as f:
                for i in product_list:
                    list1 = ', '.join(i)
                    f.write('%s\n' % list1)
            f.close()

            product_list = product_records.getComboProductData()
            with open(product_file,"a") as f:
                for data in product_list:
                    list1 = []
                    def flatten_list(data):
                        # iterating over the data
                        for element in data:
                            # checking for list
                            if type(element) == list:
                                # calling the same function with current element as new argument
                                flatten_list(element)
                            else:
                                list1.append(element)
                    
                    flatten_list(data)
                    
                    list1 = ', '.join(list1)
                    f.write('%s\n' % list1)
            f.close()  



            break   
        ##########################################################################################
        #                     Setting discount rate for retail Customer                          #
        ##########################################################################################
        elif menu_key == 5 :
            discount = True
            while discount:
                try:
                    discount_per = input("\nPlease Enter the discount percentage that needs to be set for all Retail Customers : ")
                    discount_per = float(discount_per)
                    customer_class_retail[0].setRate(discount_per)
                    discount = False
                except ValueError:
                    print('\nPlease give a number as input Try again')
                    discount = True
        ##########################################################################################
        #                     Setting discount rate for retail Customer                          #
        ##########################################################################################
        elif menu_key == 6 :
            threshold_1 = True
            while  threshold_1:
                try:
                    threshold = input ('\n Enter the new threshold for wholesale customers : ')
                    threshold = float(threshold)
                    customer_class_whole_sale[0].setThreshold(threshold)
                    threshold_1 = False
                except ValueError:
                    print('\nPlease give a number as input Try again')
                    threshold_1 = True
        
        ##########################################################################################
        #                                       Order History                                    #
        ##########################################################################################
        elif menu_key == 7 :

            order = Order('0','0','0','0')       

            order_list = order.getOrdersList()
            print('\n')
            print('='*80)
            print(" "*35 + 'Order History' + " "*35)
            print('='*80)
            print(f"{'Sl.no':8s}{'Customer Name':15s}{'Product':25s}{'Quantity':12s}{'Total':8s}{'Date'}")
            print('-'*80)

            for i in range(len(order_list)):
                
                if type(order_list[i][1]) == str:
                    product = order_list[i][1]
                elif type(order_list[i][1]) == list:
                    product = ', '.join(order_list[i][1])

                if type(order_list[i][2]) == str :
                    Quantity =  order_list[i][2]
                elif type(order_list[i][2]) == list:
                    Quantity = ', '.join(str(v) for v in order_list[i][2])
                
                Total = str(order_list[i][3])
                ivalue = str(i+1)

                print(f"{ivalue:8s}{order_list[i][0]:15s}{product:25s}{Quantity:12s}{Total:8s}{order_list[i][4]}")

            print('-'*80+'\n')

            escape_function()

        ##########################################################################################
        #                                       Replenish                                        #
        ##########################################################################################       
        elif menu_key == 8 :
            def replenish(replenish_2):
                record = Records()
                product_1 = record.get_product_data()
                combo_data_1 = record.getComboProductData()

                for i in range(len(product_1)):
                   
                    if int(product_1[i][3]) < 50:
                        product_1[i][3] = str(int(product_1[i][3]) + replenish_2)
                    record.set_product_data(product_1)

                for i in range(len(combo_data_1)):
                        
                        if int(combo_data_1[i][3]) < 50:
                            combo_data_1[i][3] = str(int(combo_data_1[i][3]) + replenish_2)
                        record.setComboProductData(combo_data_1)
            rep = True
            while rep:
                try:
                    replenish_1 = input("Enter the number to replenish the stock for products and combos below 50 : ")
                    replenish_1 = int(replenish_1)
                    replenish(replenish_1)
                    rep = False
                    escape_function()


                except ValueError:
                    print('\nPlease give a number as input Try again')
                    rep = True
        ##########################################################################################
        #                                       most Valuable Customer                           #
        ########################################################################################## 

        elif menu_key == 9 :

            customers_1 = customer_records.getCustomerData()
            customer_name = []
            max  = 0
            type(max)
            for i in range(len(customers_1)):

                if( float(customers_1[i][4]) > float(max)):
                    max = customers_1[i][4]
                    customer_name_1 = customers_1[i][1]
            
            for i in range(len(customers_1)):

                if ( float(customers_1[i][4]) ==  float(max)):

                    customer_name.append(customers_1[i][1])

            print("\n\nMost Valuable Customer with order value of {} : {}".format(max, ', '.join(customer_name)))

            escape_function()
        
        else :
            print("\n'Invalid Input' Please enter a valid number \n")
       
if __name__=="__main__":
    main()


###############################################################################################################################################################################################

# 1.Student Name  : Srujan Basavaraj
# 2.completed HD level -90%
# 3.made 6 submissions prior to this
# 4.created all the classes given in assignment 2 and designed as given in assignement 2
# 5.as said for all retail customers the doiscount will be 10 per and even we reset it will be rest to all retail customers so 
#   so setting each customer a discount is of no use in this program
# 6.Dealing with different data types is a biggest issue in this assignment 
# 7.upload files only which are given in assignemnt pdf format
# 8.converting a normal code to OOP without much experience in OOP is a biggest disadvantage 

