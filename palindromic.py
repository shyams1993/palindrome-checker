name=input("Enter the word: ")		#Get the input string to check
name1=list(name)					#convert the input into a list and store it in name1
print(name1)						#print the list 1(name 1)
name2=name1[ : :-1]					#use list splicing to reverse the list1 and store it in name2
print(name2)						#print the list 2(name 2)
if (name1 == name2):				#if name1 equals name2, then
	print("Palindrome")				#It is a palindrome
else:								#else
	print("Not a Palindrome")		#It is not a palindrome
