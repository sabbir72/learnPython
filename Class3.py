# c = 'Bangladesh is my \'motherland\', I love her very much'

# print(c)


# print('\\')


# a='Bangla'
# b="desh"

# print(a+b)

# print("Task-1",a[1:5])
# print("Task-2",a[:2])
# print("Task-3",a[2:5])
# print("Task-4",a[-3])

# print("===> string formatting")

# a='Bangladesh is my motherland'
# print('This is :%s' %a)
#-----------------------------------------------------------

# price= 490.99
# print('%.2f' % price)


# language1 = input('Enter your first language: ')

# language2 = input('Enter your second language: ')

# print('My favorite languages are :', language1, 'and', language2)



# print('My favorite languages are : %s and %s' %(language1, language2))


#string jura deaya  UPPER LOWER CAPITALIZE CASEFOLD SWAPCASE---------

# area="noyagoan".capitalize().upper().title()
# po="Tongi".lower()
# Dis="Gazipur"
# print("1- I live in %s, %s" %(po, Dis),'\n')

# print ('2- Your Present address is:', po+'-'+Dis,'\n')

# #join function use kore string gula ke jora deya jay

# print('3- My address is:', '--'.join([area, po, Dis]))

#  স্ট্রিং গণনা, স্ট্রিং খোঁজা#

# Country="Bangladesh is my motherland, I love her very much."

# length=len(Country)
# print("Length of the string is:", length)

# ValueCountry=Country.count('e')
# print("The letter 'e' appears", ValueCountry, "times in the string.")

# valueCountry1=Country.count('e', 10,25)
# print("The letter 'e' appears", valueCountry1, "times in the string after index 3.")

# #find function use kore string er index number ber kora jay
# valueCountry2=Country.find('m', 15)
# print("The index of the first occurrence of 'm' is:", valueCountry2)


# find and index 

# a = "Bangladesh is my motherland."

# VALUE_FIND = a.find('X')

# print(VALUE_FIND)  # Output: -1


# VALUE_INDEX = a.index('X')  # This will raise a ValueError since 'X' is not in the string

# print(VALUE_INDEX)  # This line will not be executed due to the exception


#কাটাকুটি, ফাটাফাটি#

Sentence = 'How can a clam cram in a clean cream can?'

view_replace= Sentence.replace('a', 'A')

print("After replacing 'a' with 'A':", view_replace)

view_split= Sentence.split('?')
print("After splitting the sentence into words:", view_split)