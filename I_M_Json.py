import json
import time
fd=open("product_Records.json","r")
js=fd.read()
fd.close()
record=json.loads(js)

print("-"*15,"Menu","-"*15,"\n")
for key in record:
    print(key,":",record[key]["Product_Name"],"|",record[key]["Price"],"|",record[key]["Quantity"])
print("-"*35,"\n")
uName=input("Enter The Name      : ")
uEmail=input("Enter The Email   : ")
uPhone=input("Enter The Phone   : ")
uId=input("Enter The Product Id : ")
uQn=int(input("Enter Quantity       : "))
if record[uId]["Quantity"] >= uQn:
    record[uId]["Quantity"]=record[uId]["Quantity"]-uQn
    print("-"*15,"Bill","-"*15,"\n")

    print("Product Name   : ",record[uId]["Product_Name"])
    print("Price          : ",record[uId]["Price"])
    print("Quantity       : ",uQn)
    print("-"*35,"\n")
    print("Billing Amount : ",uQn*(int(record[uId]["Price"])))
    print("-"*35,"\n")
    js=json.dumps(record)
    fd=open("product_Records.json","w")
    fd.write(js)
    fd.close()
    sale=uName+", "+uEmail+", "+uPhone+", "+uId+", "+record[uId]["Product_Name"]+", "+str(uQn)+", "+str(record[uId]["Price"]*uQn)+", "+str(time.ctime())+"\n"
    td=open("sales.txt","a")
    td.write(sale)
    td.close()
else:
    if record[uId]["Quantity"]>0:
        print("We Have only  ",record[uId]["Quantity"])
        inp=input("Enter Y for purchasing N for Not Intrested! :")
        if inp=="Y" or inp=="y":
            
             print("Product Name   : ",record[uId]["Product_Name"])
             print("Price          : ",record[uId]["Price"])
             print("Quantity       : ",record[uId]["Quantity"])
             print("-"*35,"\n")
             print("Billing Amount : ",record[uId]["Quantity"]*(int(record[uId]["Price"])))
             print("-"*35,"\n")
             
             js=json.dumps(record)
             fd=open("product_Records.json","w")
             fd.write(js)
             fd.close()
             sale=uName+", "+uEmail+", "+uPhone+", "+uId+", "+record[uId]["Product_Name"]+", "+str(record[uId]["Quantity"])+", "+str(record[uId]["Price"]*record[uId]["Quantity"])+", "+str(time.ctime())+"\n"
             td=open("sales.txt","a")
             td.write(sale)
             td.close()
             record[uId]["Quantity"]=0
        else:
            print("Thank You For Showing Your Interest!")
        
    

