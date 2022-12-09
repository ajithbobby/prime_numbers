import math
start = int(input('Enter the start number : '))
end = int(input('Enter the end number : '))
for num in range(start, end+1):
    if num > 1:
        for i in range(2, int(math.sqrt(num)) + 1):
            if(num % i) == 0:
                break;
        else:
            print(num)
