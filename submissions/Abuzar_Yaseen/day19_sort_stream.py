num = input("Enter numbers: ")
sort_list = list(map(int,num.split()))
sort_list.sort()
print("Sorted Data: ",*sort_list)