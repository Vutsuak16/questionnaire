__name__ = "vutsuak"

# this code uses data structures

string = "heyjude"  # currently only for lower case characters in a string

flg = 0
arr = []
for i in string:
    val = ord(i) - ord('a')
    if val in arr:
        flg = 1
        print "string is not unique"
        break
    arr.append(val)

if not flg:
    print "string is unique"
