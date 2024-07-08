customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

#Task 1: Duplicate Entries Cleanup
#Remove duplicates and display unique customer IDs

#convert the list to a set
customer_ids_set = set(customer_ids)

#display the set, as it will not have any duplicates
print(customer_ids_set)