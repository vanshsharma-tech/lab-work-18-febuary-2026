# Check whether a number is Armstrong or not
num = int(input("Enter the value :"))
digit = num
count = 0
while num>0:
  num//=10
  count+=1

ans = 0
temp = digit

while digit>0:
  rem=digit%10
  ans = ans + pow(rem,count)
  digit //=10

print(ans==temp)