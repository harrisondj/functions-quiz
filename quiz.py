
def has_teen(a,b,c):
	if a >= 13 and a <= 19 or b >= 13 and b <= 19 or c >= 13 and c <= 19:
		return True
	else:
		return False

print has_teen(11,12,13) #T
print has_teen(13,14,15) #T
print has_teen(11,12,20) #F

def not_string(str):
	if str.startswith('not'):
		return str + 'not'
	else:
		return 'not' + str

print not_string('not cool') #cool not
print not_string('cool') #not cool

def icy_hot(a,b):
	if a < 0 and b > 100:
		return True
	if a > 100 and b < 0:
		return True
	else:
		return False

print icy_hot(30,50)#F
print icy_hot(30,200)#T
print icy_hot(-1,20)#T
print icy_hot(101,110)#F

def closer_to(t,a,b):
	if abs(t - a) < abs(t - b):
		return a
	if abs(t - b) < abs(t - a):
		return b
	if abs(t - a) == abs(t - b):
		return 0

print closer_to(50,41,2)#41
print closer_to(50,2,25)#25
print closer_to(50,40,60)#0

def two_as_one(a,b,c):
	if a + b == c or a + c == b or b + c == a:
		return True
	else:
		return False

print two_as_one(3,2,5)#T
print two_as_one(10,8,2)#T
print two_as_one(11,8,2)#F
print two_as_one(8,11,2)#F
print two_as_one(8,2,11)#F

# TODO - write pig_latinify
