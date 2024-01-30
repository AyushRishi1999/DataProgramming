# Return true if the card number is valid
def isValid(number):
    return (sumOfDoubleEvenPlace(number)+sumOfOddPlace(number))%10==0
# Get the result from Step 2
def sumOfDoubleEvenPlace(number):
    sum = 0
    k = str(number)[::-1]
    for i in range(0, len(k), 2):
        sum += getDigit(int(k[i]*2))
    return sum

def getDigit(number):
    if number<10:
        return number
    else:
        return (number%10)+(number//10)

# Return sum of odd place digits in number
def sumOfOddPlace(number):
    sum=0
    k=str(number)[::-1]
    for i in range(0,len(k),2):
        sum+=getDigit(int(k[i]))
    return sum
# Return true if the digit d is a prefix for number
def prefixMatched(number, d):
    return getPrefix(number,len(str(d)))==d
# Return the number of digits in d
def getSize(d):
    return len(str(d))
# Return the first k number of digits from number. If the
# number of digits in number is less than k, return number.
def getPrefix(number, k):
    return int(str(number)[:k])

cardNumber=int(input("Enter card number:"))

if isValid(cardNumber):
    print("The credit card is valid.")
else:
    print("The credit card is invalid.")