thislist = ["Apple", "Banana", "Cherry", "Mango"]
thislist1= [200, 100, 50, 21, 10, 49, 64, 450]
for items in thislist:
    print(items)
for x in thislist1:
    thislist.append(x)
    print(f"Appending thislist and thislist1:", thislist)
thislist1.sort(reverse=True)
print(f"Descending order:", thislist1)
thislist1.sort()
print(f"Ascending order:", thislist1)