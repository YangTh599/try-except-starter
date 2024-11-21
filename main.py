# Thayer Yang  
# 21 NOV 2024
# Try-Except Block Practice

# Doing Addition

while True:
    try:
        num1 = int(input("Give me a number: "))
        num2 = int(input("Give me another number: "))
        answer = sum(num1,num2)
        print(f'The sum of {num1} and {num2} is {answer}.')
        break
    except ValueError:
        print("Please enter numeric values")

#Invalid List Element

my_scores = [55,66,100]
print(my_scores)
try:
    score = int(input("Enter a score:"))
    my_scores.append(score)
except ValueError:
    print('Please only enter integers')

print(my_scores)

#Invalid Index

my_nums = [10,20,30,40,50,60]

try:
    index = int(input("Enter a number"))
    print(my_nums[index])
except IndexError:
    print("Index out of range")
except ValueError:
    print("Please enter an integer")