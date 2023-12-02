## part 1 ##

file = open("input1.txt", "r")
first_number = -1
numbers = []

for line in file:
    for letter in line:
        if not letter.isalpha() and letter != '\n':
            if first_number == -1:
                first_number = letter
            second_number = letter
    

    numbers.append(str(first_number)+str(second_number))
    first_number = -1
        

total = 0
for number in numbers:
    total += int(number)

print(total)

## part 2 ##

file = open("input1.txt", "r")
all_numbers = []
first_number = -1
number_words = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6",
                 "seven": "7", "eight": "8", "nine": "9"}

for line in file:
    modified_line = line

    for i in range(3):
        for word in number_words:
            index = modified_line.find(word)
            if (index != -1):
                modified_line = modified_line[:index + 1] + number_words[word] + modified_line[index + 1:]

    for letter in modified_line:
        if not letter.isalpha() and letter != '\n':
            if first_number == -1:
                first_number = letter
            second_number = letter
    
    all_numbers.append(int(str(first_number)+str(second_number)))
    first_number = -1
        
total = 0
for number in all_numbers:
    total += number

print(total)
