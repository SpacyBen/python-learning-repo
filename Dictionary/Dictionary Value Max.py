print("Enter a dictionary (in the format key:value,key:value,...): ")
put = input()

items = put.split(',')
myitem = {}

for item in items:
    key, value = item.split(':')
    myitem[key] = int(value)
    
max_key = max(myitem, key = myitem.get)

print(f"The key for the maximum value ({myitem[max_key]}) is '{max_key}'.")