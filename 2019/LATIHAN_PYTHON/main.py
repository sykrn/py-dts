import latihan_package.alpha as a
import latihan_package.beta as b

a.alphaSatu()
a=5
b=0

'''
try:
	print(a/b)
except :
	print("Pembagi tidak boleh nol")
'''

try:
	c=a/b #variable scope
	print(a)
except :
	pass

#print(c**2)
