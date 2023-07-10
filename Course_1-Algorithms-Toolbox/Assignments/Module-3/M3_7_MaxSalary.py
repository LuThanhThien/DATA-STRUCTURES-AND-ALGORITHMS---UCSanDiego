def isBetter(number,maxNumber):
    num_max = int(str(number)+str(maxNumber))
    max_num = int(str(maxNumber)+str(number))
    if max_num>=num_max: return False
    return True

def LargestNumber(numbers):
    numbers = list(map(int,numbers))
    salary = []
    while len(numbers)>0:
        maxNumber = 0
        max_id = 0
        for i in range(len(numbers)):
            if isBetter(numbers[i],maxNumber):
                maxNumber = numbers[i]
                max_id = i
        salary.append(maxNumber)
        numbers.pop(max_id)
    return int("".join(map(str,salary)))

if __name__ == '__main__':
    _ = str(input())
    input_numbers = input().split()
    print(LargestNumber(input_numbers))
