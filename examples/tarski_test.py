import pytarski as tw

# create a board
board = tw.TarskisWorldBoard()

# add some objects to the 8x8 board, rows and columns are 0 through 7
# the parameters are: shape, size, column, row
a = board.add('tet', 'small', 3, 4)
b = board.add('cube', 'medium', 4, 5)
c = board.add('dodec', 'medium', 4, 6)

# we cannot add a new object on a tile with an object already present
# d = board.add('cube', 'small', 3, 4)

# however, we can add a name to an existing object by using the exact same 
# attributes. object a and d will be the same object, just with two names
d = board.add('tet', 'small', 3, 4)

# we cannot place a large object next to any other object, nor any other 
# object in a tile surrounding a large object
# e = board.add('cube', 'large', 2, 4) # no
e = board.add('cube', 'large', 1, 4) # yes
# f = board.add('cube', 'small', 0, 3) # no
f = board.add('cube', 'small', 0, 2) # yes

# check a few true conditions
s1 = tw.tet(a)
s1 &= tw.cube(b)
s1 &= tw.dodec(c)
s1 &= tw.adjoins(b, c)
s1 &= tw.frontOf(b, c)
s1 &= tw.larger(c, a)
s1 &= tw.smaller(a, b)

# check a few false conditions
s2 = tw.cube(e)
s2 &= tw.between(e, d, f)

# Use the AND connective
s3 = s1 & s2

# Use the OR connective
s4 = s1 | s3

# Use the NOT connective
s5 = not s4

# see if it all checks out
print(f'The sentence s1 is {s1}')
print(f'The sentence s2 is {s2}')
print(f'The sentence s3 is {s3}')
print(f'The sentence s4 is {s4}')
print(f'The sentence s5 is {s5}')
