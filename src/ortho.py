
word=raw_input()
print word
import string
strin=""
prefix=""
suffix=""
no_prefix=4
if len(word)==1:
	if word.isupper(): #for capital letter
			string='A'
	elif word.islower(): #for small letter
		strin='a'
	elif word.isdigit(): #for numbers
		strin="n"
	elif word in string.punctuation: #for symbol
		strin="p"
	prefix=word+" "+"_ _ _"
	suffix=word+" "+" _ _ _"

else :
	flag=0
	if word.isupper():
		strin="AA"
		flag=1

	elif word.islower():
		strin="aa"
		flag=1

	elif not word.islower() and not word.isupper(): #just capitalised
		strin="Aa"
		

        
	for i in word:
			if i in string.punctuation:
				strin+='p'

			if i.isdigit():
				strin+="n"
	if len(word)>=no_prefix:
			for i in range(1,no_prefix+1):
				prefix+=word[0:i]+" "
				suffix+=word[-i:]+" "
	else:
		deficit=no_prefix-len(word)
		for i in range(1,len(word)+1):
			prefix+=word[0:i]+" "
			suffix+=word[-i:]+" "
		for i in range(1,deficit+1):
			prefix+="_"+" "
			suffix+="_"+" "

	prefix=prefix.strip()
	suffix.strip()

print strin
print prefix
print suffix
	
	
		
