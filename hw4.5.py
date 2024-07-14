sum1: int = 0;
count1: int = 0;
oldiq = int(input("enter IQ:"));
while oldiq >= 30 and oldiq <= 300:
    sum1 = sum1 + oldiq;
    count1 = count1 + 1;
    oldiq = int(input("enter IQ:"));

print(f"the average IQ is: {sum1/count1}")

print(f"one year of python training has been completed…")

sum2: int = 0;
count2: int = 0;
newiq = int(input("enter IQ:"));
while newiq >= 30 and newiq <= 300:
    sum2 = sum2 + newiq;
    count2 = count2 + 1;
    newiq = int(input("enter IQ:"));
print(f"the average IQ is: {sum2/count2}")
print(f"the average new IQ is higher by: {(sum2/count2)-(sum1/count1)}")