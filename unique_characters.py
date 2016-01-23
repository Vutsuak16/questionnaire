__name__ = "vutsuak"

# this code does not use any data structures

string = "heyjude"  # currently only for lower case characters in a string

flg = 0
for i in string:
    val = ord(i) - ord('a')
    print val
    print bin(flg)
    if flg & (1 << val) > 0:
        print "not a unique string"
        break
    flg |= 1 << val
