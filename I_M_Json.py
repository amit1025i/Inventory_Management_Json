import json  # Import the json module to work with JSON data
import time  # Import the time module to log timestamps of transactions

# Open the product_Records.json file in read mode to load current product data

fd=open("product_Records.json","r")
js=fd.read() # Read the contents of the file into a string
fd.close()  

# Convert the JSON string into a Python dictionary for easy manipulation
record=json.loads(js) 

# Display the product menu

print("-"*15,"Menu","-"*15,"\n")

for key in record: 
    # Print product ID, name, price, and available quantity for each product
    print(key,":",record[key]["Product_Name"],"|",record[key]["Price"],"|",record[key]["Quantity"])
print("-"*35,"\n")

# Collect customer details and purchase information

uName=input("Enter The Name      : ")
uEmail=input("Enter The Email   : ")
uPhone=input("Enter The Phone   : ")
uId=input("Enter The Product Id : ")
uQn=int(input("Enter Quantity       : "))

# Check if the requested quantity is available

if record[uId]["Quantity"] >= uQn:

    # Reduce the available quantity by the purchased amount

    record[uId]["Quantity"]=record[uId]["Quantity"]-uQn
    print("-"*15,"Bill","-"*15,"\n")
    
    # Display the bill
    
    print("Product Name   : ",record[uId]["Product_Name"])
    print("Price          : ",record[uId]["Price"])
    print("Quantity       : ",uQn)
    print("-"*35,"\n")

    # Calculate and display the total billing amount
    
    print("Billing Amount : ",uQn*(int(record[uId]["Price"])))
    print("-"*35,"\n")

     # Update the product_Records.json file with the reduced quantity

    js=json.dumps(record) # Convert the updated record back to a JSON string
    fd=open("product_Records.json","w")
    fd.write(js)
    fd.close()
    sale=uName+", "+uEmail+", "+uPhone+", "+uId+", "+record[uId]["Product_Name"]+", "+str(uQn)+", "+str(record[uId]["Price"]*uQn)+", "+str(time.ctime())+"\n"
    td=open("sales.txt","a") # Open the sales.txt file in append mode to log new sales
    td.write(sale)  
    td.close()  
    
else:
     # If the requested quantity is more than available stock

    if record[uId]["Quantity"]>0:

        # Inform the user about the available stock

        print("We Have only  ",record[uId]["Quantity"])

        inp=input("Enter Y for purchasing N for Not Intrested! :")
        if inp=="Y" or inp=="y":
            
             print("Product Name   : ",record[uId]["Product_Name"])
             print("Price          : ",record[uId]["Price"])
             print("Quantity       : ",record[uId]["Quantity"])
             print("-"*35,"\n")
             print("Billing Amount : ",record[uId]["Quantity"]*(int(record[uId]["Price"])))
             print("-"*35,"\n")
            
             # Update the product_Records.json file with the reduced quantity

             js=json.dumps(record)
             fd=open("product_Records.json","w")
             fd.write(js)
             fd.close()
             sale=uName+", "+uEmail+", "+uPhone+", "+uId+", "+record[uId]["Product_Name"]+", "+str(record[uId]["Quantity"])+", "+str(record[uId]["Price"]*record[uId]["Quantity"])+", "+str(time.ctime())+"\n"
             td=open("sales.txt","a")
             td.write(sale)
             td.close()
              
             # Set the product quantity to zero since the user bought all available stock
             record[uId]["Quantity"]=0
        else:
            
            # If the user is not interested in buying the available stock
            print("Thank You For Showing Your Interest!")

        
    

