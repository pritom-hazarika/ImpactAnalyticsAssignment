'''
## Question

In a university, your attendance determines whether you will be
allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year,
which is the Nth day.

 
Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer
of (1)", don't actually divide or reduce the fraction to decimal

Test cases:

for 5 days: 14/29
for 10 days: 372/773
'''

def calculate_attendance_ways(n):
    #Generating the attendance pattern exluding four or more missing days
    attendance_pattern =[x for x in [bin(i)[2:].zfill(n) for i in range(2**n)] if '0000' not in x]
    
    #attendance pattern in the valid attendance where the last day is missed 
    last_day = [x for x in attendance_pattern if x[-1] == '0']
    
    return f"{len(last_day)}/{len(attendance_pattern)}"

result1 = calculate_attendance_ways(5)
result2 = calculate_attendance_ways(10)

print(f"For 5 days - : {result1}")
print(f"For 10 days - : {result2}")