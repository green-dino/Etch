
#
#Python Numeric Operations
#

print("\nPython Numeric Operations\n")

x = 7
y = 4
print("x:    ",x)
print("y:    ",y)
print("x+y:  ",x+y)
print("x*y:  ",x*y)
print("x/y:  ",x/y)
print("x//y: ",x//y)
print("x%y:  ",x%y)
print("-x:   ",-x)
print("+x:   ",+x)
print("x**y: ",x**y)

#
# Python Bitwise Operations
#

print("\nPython Boolean Operations\n")

a = 0b1010111
b = 0b0101101
print(a)
print(b)
print(hex(a))
print(hex(b))

print('a      {:08b}'.format(a))
print('b      {:08b}'.format(b))
print('a | b  {:08b}'.format(a | b))
print('a & b  {:08b}'.format(a & b))
print('a ^ b  {:08b}'.format(a ^ b))
print('a << 2 {:010b}'.format(a << 2))
print('a >> 2 {:08b}'.format(a >> 2))

# 
# Binary and Hex Rendering 
# Using the format method
#

print("\nPython Boolean Binary and Hex Rendering\n")

value = 254

print('Dec', value)
print('Hex {:02X}'.format(value))
print('Bin {:08b}'.format(value))


