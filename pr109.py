# Find number of checkouts on a a dart board with a score less than 100
# Simply loop through all possible checkouts

# A dart object is thrown in a particular field with a score
class Dart:
	def __init__(self,n,m):
		self.number = n
		self.mult = m
		self.score = n*m
	
	# Define a unique ordering of darts using multiplicity as priority
	def __ge__(self,other):
		if self.mult > other.mult: return True
		if self.mult == other.mult:
			return self.number >= other.number
		return False

# A generator to loop through all possible throws
def darts():
	yield Dart(0,0) # A miss

	for i in range(1,21):
		yield Dart(i,1)
		yield Dart(i,2)
		yield Dart(i,3)
	
	# Bullseye
	yield Dart(25,1)
	yield Dart(25,2)

count = 0
for i in darts():
	# The last dart has to be a double
	if i.mult==2:
		for j in darts():
			for k in darts():
				# Checkouts with 1st and 2nd dart swapped round are considered the same
				# Use an ordering to avoid double counting
				if k>=j:
					if i.score+j.score+k.score < 100:
						count += 1

print(count)