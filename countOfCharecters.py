a = input()
vowels = 0
consonants = 0
integers = 0
special_chr = 0
alphabets = 0

vowel_cond = ['a','e','i','o','u','A','E','I','O','U']
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
up_alpha = []

for i in alpha:
    up_alpha.append(i.upper())



for i in a:
    if (i in vowel_cond):
        vowels +=1
    elif(i.isdigit()):
        integers+=1
    elif(i not in alpha) and (i not in up_alpha) and (not i.isdigit()):
        special_chr+=1
    else:
        consonants +=1
for i in a:
    if( (i in alpha) or (i in up_alpha)):
        alphabets +=1
        
print('No of special_chr = ' + str(special_chr)) 

print('No of integers = ' + str(integers))
print('No of alphabets = ' + str(alphabets))
print('No of vowels = ' + str(vowels))
print('No of consonants = ' + str(consonants))