#1 approach
def reverse(s):
	str = ""
	for i in s:
		str = i + str
	return str

s = "Geeksforgeeks"

print("The original string is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))


# 2 Approach
def reverse(s):
	if len(s) == 0:
		return s
	else:
		return reverse(s[1:]) + s[0]


s = "Geeksforgeeks"

print("The original string is : ", end="")
print(s)

print("The reversed string(using recursion) is : ", end="")
print(reverse(s))


# 3 approach
# Function to reverse a string
def reverse(string):
	string = string[::-1]
	return string

s = "Geeksforgeeks"

print("The original string is : ", end="")
print(s)

print("The reversed string(using extended slice syntax) is : ", end="")
print(reverse(s))


# 4 Approach
def reverse(string):
	string = list(string)
	string.reverse()
	return "".join(string)

s = "Geeksforgeeks"

print("The original string is : ", s)

print("The reversed string(using reversed) is : ", reverse(s))
