# 2. Write a program that repeatedly asks the user to enter product names and prices. Store all
# of these in a dictionary whose keys are the product names and whose values are the prices.
# When the user is done entering products and prices, allow them to repeatedly enter a
# product name and print the corresponding price or a message if the product is not in the
# dictionary.
d={}
n=int(input("Enter number of products="))
for i in range(n):
    product=input("Enter product name:")
    price=input("Enter price:")
    d[product]=price
count=0
print("\nprinting prices of products")
while (count!=n):
     product=input("Enter product name:")
     try:
          print(f"The price of {product}={d[product]}")
          count+=1
     except Exception as e:
          print("Product is not present")
else:
     print("thankyou".upper())
    
