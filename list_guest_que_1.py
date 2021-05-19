# Inviting five of my friends for dinner

dinn_frnds = ['Abhi','Jay','Amey','Ranveer','Varun']

#sending message to each friend for dinner
for friend in dinn_frnds :
	print("Hi, "+friend+". Dinner Today. Try Not to be late." )

dinn_frnds.pop(1)

for frnd in dinn_frnds :
	print("Sorry for sending this message "+frnd+" butfor some reason "+dinn_frnds[1]+" could not make it,today so instead Aditya will be there.")

dinn_frnds[1] = 'Aditya'

#3 new people
dinn_frnds.append('Niraj')
dinn_frnds.insert(3,'Suraj')
dinn_frnds.insert(0,'Nil')

#rewriting the message to everyone
for friend in dinn_frnds :
	print("Hi, "+friend+". Dinner Today. Try Not to be late." )

print("New dinner won't arrieve at time.You can invite only two friends")

print(dinn_frnds.pop()+" Sorry I can't invite you to dinner.")	
print(dinn_frnds.pop()+" Sorry I can't invite you to dinner.")	
print(dinn_frnds.pop()+" Sorry I can't invite you to dinner.")	
print(dinn_frnds.pop()+" Sorry I can't invite you to dinner.")	
print(dinn_frnds.pop()+" Sorry I can't invite you to dinner.")	

#messaging last two people
for i in dinn_frnds :
	print(i+" You are still invited.")

#Deleting the List
del dinn_frnds[0:]
#printing the empty list
print(dinn_frnds)
