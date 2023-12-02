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

for line in file:
    modified_line = line

    i = 0
    while i < 3:
        # find one
        index_one = modified_line.find('one')
        if (index_one != -1):
            modified_line = modified_line[:index_one+1] + "1" + modified_line[index_one+1:]

        # find two
        index_two = modified_line.find('two')
        if index_two != -1:
            modified_line = modified_line[:index_two+1] + "2" + modified_line[index_two+1:]

        # find three
        index_three = modified_line.find('three')
        if index_three != -1:
            modified_line = modified_line[:index_three+1] + "3" + modified_line[index_three+1:]

        # find four
        index_four = modified_line.find('four')
        if index_four != -1:
            modified_line = modified_line[:index_four+1] + "4" + modified_line[index_four+1:]

        # find five
        index_five = modified_line.find('five')
        if index_five != -1:
            modified_line = modified_line[:index_five+1] + "5" + modified_line[index_five+1:]

        # find six
        index_six = modified_line.find('six')
        if index_six != -1:
            modified_line = modified_line[:index_six+1] + "6" + modified_line[index_six+1:]

        # find seven
        index_seven = modified_line.find('seven')
        if index_seven != -1:
            modified_line = modified_line[:index_seven+1] + "7" + modified_line[index_seven+1:]

        # find seven
        index_seven = modified_line.find('seven')
        if index_seven != -1:
            modified_line = modified_line[:index_seven+1] + "7" + modified_line[index_seven+1:]

        # find eight
        index_eight = modified_line.find('eight')
        if index_eight != -1:
            modified_line = modified_line[:index_eight+1] + "8" + modified_line[index_eight+1:]

        # find nine
        index_nine = modified_line.find('nine')
        if index_nine != -1:
            modified_line = modified_line[:index_nine+1] + "9" + modified_line[index_nine+1:]
        
        i += 1

    
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
