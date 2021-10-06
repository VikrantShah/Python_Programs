a = 5
b = 2
c = True
d = False
e = "Some string"
f = "o"

print("The value of a :", a)
print("The value of b :", b)
print("The value of c :", c)
print("The value of d :", d)
print("The value of e :", e)
print("The value of f :", f)

print()

# Arithematic operators
print("Arithematic operators :")
print("The addition of a & b : ", a+b)
print("The subtraction of a & b : ", a-b)
print("The multiplication of a & b : ", a*b)
print("The division of a & b : ", a/b) # Divides the first operand by second operand
print("The floor division of a & b : ", a//b) # Divides the second operand by first operand
print("The modulus of a & b : ", a%b) # returns remainder of division
print("The power of a & b : ", a**b)

print()

# Relational operators
print("Relational operators :")
print("a >(greater than) b :", a>b)
print("a <(less than) b :", a<b)
print("a ==(equal to) b :", a==b)
print("a !=(not equal to) b :", a!=b)
print("a >=(greater than or equal to) b :", a>=b)
print("a <=(less than or equal to) b :", a<=b)

print()

# Logical operator
print("Logical Operators :")
print("c and d :", c and d)
print("c or d :", c or d)
print("not c :", not c)

print()

# Bitwise Operators
print("Bitwise Operators :")
print("a &(bitwise and) b :", a&b)
print("a |(bitwise or) b :", a|b)
print("~(not) a :", ~a)
print("a ^(bitwise xor) b :", a^b)
print("a <<(bitwise left shift) b :", a<<b)
print("a >>(bitwise right shift) b :", a>>b)

print()

# Assignment Operators
print("Assignment Operators :")

z = a
print("The value of z :", z)

a += b
print("a += b :", a)

a = 5
a -= b
print("a -= b :", a)

a = 5
a *= b
print("a *= b :", a)

a = 5
a /= b
print("a /= b :", a)

a = 5
a %= b
print("a %= b :", a)

a = 5
a //= b
print("a //= b :", a)

a = 5
a **= b
print("a **= b :", a)

a = 5
a &= b
print("a &= b :", a)

a = 5
a |= b
print("a |= b :", a)

a = 5
a ^= b
print("a ^= b :", a)

a = 5
a <<= b
print("a <<= b :", a)

a = 5
a >>= b
print("a >>= b :", a)

print()

# Identity Operator
print("Identity Operator :")
print("a is b :", a is b)
print("a is not b :", a is not b)

print()

# Membership operator
print("Membership Operator :")
print("e in f :", e in f)
print("e not in f :", e not in f)