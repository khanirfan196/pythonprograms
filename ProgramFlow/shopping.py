# Demonstration of 'Continue' keyword.

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

for item in shopping_list:
    if item != "spam":
        print("Buy " + item)

for item in shopping_list:
    if item == "spam":
        continue
        # under the continue keyword, only that value which is found
        # i.e. "spam" will not printed and rest will continue to print.
    print("Buy " + item)



