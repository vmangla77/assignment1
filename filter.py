names=['Gaurav','Sumit','Chakshu','Anushka','Kashish','Tanya','Isha','Vansh','engineer']
vowels = "AaEeIiOoUu"
result=list(filter(lambda x:x[0] in vowels,names))
print(result)

# res=list(map(lambda var:var*2,range(0,10)))
# print(res)