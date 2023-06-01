#Count odd and even numbers. Count odd and even digits of the whole number.
#Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).


#Code Here



def is_odd_even(n):
    even_cntr = 0
    even_list = []
    odd_cntr = 0
    odd_list = []
 # Navigate through each digit in the number
    for i in str(n):
        # If digit is even, increment even_cntr by 1
        if int(i) % 2 == 0:
            even_list.append(i)
            even_cntr = even_cntr + 1
        # If digit is odd, increment odd_cntr by 1
        else:
            odd_cntr = odd_cntr + 1
            odd_list.append(i)
    # print even and odd counter
    print(f"Even Digits: {even_cntr}{even_list}, Odd Digits: {odd_cntr}{odd_list}")


is_odd_even(12345)
is_odd_even(775836)
is_odd_even(9874563985)











