import sys

def odd_even(a):
    even = []
    odd = []
    for i in a:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return max(even) - min(odd)

# print(odd_even([1,2,3,4,5,6]))
# print(odd_even([1,2,3,4,5,6,7,8]))
# print(odd_even([1,2,3,4,5,6,7,8,9,10]))



def prime_numbers():
    prime_num = []
    try:
        n = int(input('enter a number: '))
    except ValueError:
        print('please enter an integer next time.')
        sys.exit()
    for i in range(0, n + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                prime_num.append(i)
    
    return prime_num

print(prime_numbers())

