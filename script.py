###This script uses a for loop that will iterate through numbers 0 to 100. When the number is divisible by 10, it will print the wordy version of the number (Ten, Twenty, Thirty, etc.) by accessing the appropriate index in the list. Otherwise, it will simply print the number.

for i in range(101):
    if i % 10 == 0 and i != 0:
        print(str(i) + " - " + ["Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety","Hundred"][int(i/10)-1])
    else:
        print(i)
