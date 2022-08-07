'''
Assume max digit in n is x.
Because deci-binary only contains 0 and 1,
we need at least x numbers to sum up a digit x.

Now we contruct an answer,
Take n = 135 as an example,
we initilize 5 deci-binary number with lengh = 3,
a1 = 000
a2 = 000
a3 = 000
a4 = 000
a5 = 000

For the first digit, we fill the first n[0] number with 1
For the second digit, we fill the first n[1] number with 1
For the third digit, we fill the first n[2] number with 1

So we have
a1 = 111
a2 = 011
a3 = 011
a4 = 001
a5 = 001

Finally, we have 111+11+11+1+1=135.
just return max digit

O(L) | O(1)
'''

def minPartition(n):
    res = 0
    for i in range(len(n)):
        res = max(res, int(n[i]))
    return res



print(minPartition("32"))
print(minPartition("82734"))
print(minPartition("27346209830709182346"))
