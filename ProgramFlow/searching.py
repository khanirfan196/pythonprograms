# Demonstration of 'Break' keyword.

shopping_list = ["milk", "past", "eggs", "spam", "bread", "rice"]

item_to_found = "spam"
found_at = None
# the none kewyord is equivalent to 'NULL' keyword in other programming languages.
# found_at variable is assigned to NULL.

for index in range(len(shopping_list)):
    # len() function returns the length of the string
    # thus the range is 6
    if(shopping_list[index]) == item_to_found:
        found_at = index
        break
print("Item found at index value {}".format(found_at))

item_to_found = "spam"

for index in range(len(shopping_list)):
    # len() function returns the length of the string
    # thus the range is 6
    if(shopping_list[index]) == item_to_found:
        found_at = index
        print("Item found at index value {}".format(found_at))
        break
print("Item did not found")

# or

if item_to_found in shopping_list:
    found_at = shopping_list.index(item_to_found)
if found_at is not None: #not null
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_found))


