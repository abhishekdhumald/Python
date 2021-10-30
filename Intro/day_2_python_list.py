#	Today I am starting with the lists

bike = ['Honda','Suzuki','Yamaha','Tvs']
print(bike)

#printing in title
print(bike)

#replacing element at a perticular position
bike[0] = 'Dukati'
print(bike)

#appending (Adding) an element to the end of the list
bike.append('Honda')
print(bike)

#inserting an element at a given position
bike.insert(2,'Ktm')
print(bike)

bikes = bike

#removing an element from the given position
del bikes[-1]
print(bikes)
#Poping an element from end of the list 
bikes.pop()
print(bikes)

#Poping an element at a given position
bikes.pop(2)
print(bikes)

#Removing an element by value
bikes.remove('Dukati')
print(bikes)

#Removing bye reason (defining a variable for the target value and removing it by its variable)
too_expensive = 'Suzuki'
bikes.remove(too_expensive)
print(bikes)



