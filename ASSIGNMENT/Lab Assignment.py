# 1.Program to insert an element(specific position) into a list

List1=['teacher','student','workplace','mess']
List1.insert(0,'Principal')
print(List1)


# 2.Program to sort a numeric and string list

hello=[23,45,65,32,1,89,76,33,90,81]
hello.sort()
print(hello)

bro=['hell','well','alone', 'drag','most']
bro.sort()
print(bro)


#3.program to reverse list of integer values

madam=[12,24,36,48,60,72,84,96]
madam.reverse()
print(madam)


# 4. program to find the common elements between two list (string values)

brother=['work','tease','ride','travel','eat']
sister=['travel','shout','cry','eat','busy']
print(set(brother).intersection(sister))


#5. program to find the common elements between two lists (integer values)

brother1=[8,16,24,32,40,48,56,64,72,80]
sister1=[16,32,48,64,80,96,112,128,144,160]
print(set(brother1).intersection(sister1))