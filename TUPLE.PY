#tuple
tuple=("uganda","kenya","rwanda","congo","Tanzania")
for x in tuple: 
    print(x)

i =str(input("enter the country:"))
index= tuple.index(i)
print(f"the index of '{i}' is :{index}")

num=int(input("enter the index:"))
index = tuple[num]
print(f"The value at index {num} is: {index}")

#lists

list=["football","basketball"]
for y in list:
    print("below are the sports:")
    print(y)
sport=str(input("Add your favourite sport:"))
k=list.append(sport)
print(list)

subjects= ['Math','Eng','bio','physic','history','computer']
l=str(input("Delet the subject of your choice:"))
subjects.remove(l)
print(subjects)

