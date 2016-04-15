""" Module that returns orthographic features of a term """

def ortho_tag(word):
	import string
	strin1=strin2=strin3=""
	prefix=""
	suffix=""
	no_prefix=4
	if len(word)==1:
		if word.isupper(): #for capital letter
			strin1='A'
		elif word.islower(): #for small letter
			strin1='a'
		elif word.isdigit(): #for numbers
			strin2="n"
		elif word in string.punctuation: #for symbol
			strin3="p"
		prefix=word+" "+"_ _ _"
		suffix=word+" "+" _ _ _"

	else :

		#!---Capitalization----#
		
		flag=0
		if word.isupper():
			strin1="AA"
			flag=1

		elif word.islower():
			strin1="aa"
			flag=1

		elif not word.islower() and not word.isupper(): #just capitalised
			strin1="Aa"
			
		for i in word:

				#!----Punctuation Check----#

				if i in string.punctuation:
					strin2='p'

				#!----Digit Check---#

				if i.isdigit():
					strin3="d"

		#!---Getting prefix and suffix---#					
		
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

		suffix=suffix.strip()
		
		if strin2 != "p":
			strin2 = "n"
		if strin3 != "d":
			strin3 = "n"	

	#!---Combining all orthographic features separated by space, to be treated as separate feature---#
	
	end =  " " + strin1 + " " + strin2 + " " + strin3 + " " + prefix + suffix
	return end
		
