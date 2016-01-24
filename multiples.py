__name__ = "vutsuak"

m = [i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0]

# brute force would have been that I calculate the sum of the list m

'''
 Mathematical approach:
 m consists of two APs 3,6,9,12..... and 5,10,15,20,25......
 we need their sum but at the same time need to subtract the sum of the implicit arithmetic  progression of 15,30,45,60
 the last term in 3's AP=999  series= 3,6,9...999
 the last term in 5's AP=995  series=5,10,15...995
 the last term in 15's AP=990 series=15,30,45,60....990
 '''

sum_3 = 3 * 333 * 334 / 2  # 3+6+....999 = 3*(1+2...333) formula used = (n)*(n+1)/2
sum_5 = 5 * 199 * 200 / 2
sum_15 = 15 * 66 * 67 / 2

sum = sum_3 + sum_5 - sum_15

print sum
