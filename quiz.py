
def has_teen(a,b,c):
	if a >= 13 and a <= 19 or b >= 13 and b <= 19 or c >= 13 and c <= 19:
		return True
	else:
		return False

print has_teen(11,12,13) #T
print has_teen(13,14,15) #T
print has_teen(11,12,20) #F

#def not_string():



#print not_string('not cool') #cool not
#print not_string('cool') #not cool

def icy_hot(a,b):
	if a < 0 or b > 100:
		return True
	else:
		return False

print icy_hot(30,50)#F
print icy_hot(30,200)#T
print icy_hot(-1,20)#T

# TODO - write closer_to

# TODO - write two_as_one

# TODO - write pig_latinify
