####
####
####
myvalue = 10
print(myvalue)
print(myvalue := 10)

while (command := input("Please enter a command ('q' = quit):")) != 'q':
    print(f"Your command was {command}")

mynumbers = [5,7,18,28,8,2,3,109,4]
def process_number(n):
    return n ** 2 + 5

myresutls = [result for x in mynumbers if (result:= process_number(x)) < 100]
# saves process_number from running twice