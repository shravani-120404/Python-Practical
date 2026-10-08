#empty
list=[]
print(list)

#terms
fruits=["apple","banana"]
print(fruits)

#using index
n=[10,20,30,40]
print(n[0])
print(n[-2])


#append
color=["red","blue"]
color.append("green")
print(color)

#insert
color.insert(1,"yellow")    #1 index
print(color)

#remove
color.remove("red") #its remove specificitem
print(color)

#pop
n = [10, 20, 30, 40]
x = n.pop()
print(x)
print(n)

#lenght
n=[10,40,38,20]
print(len(n))

#sum
print(sum(n))

#sorting
print("ascen oder",sorted(n))
print("dec order",sorted(n,reverse=True))

#create a list of 10 number print the sum of last 4 elements of sum 
n=[1,2,3,4,5,6]
print("Sum of last 4 elements:",sum(n[-4:]))

#find out difference between mix & min ele of list
n= [10,20,30,40,50]
diff=max(n)-min(n)
print("difference",diff)


#insert a no. in list 6position this no. must be 1/3 no. store at 4th position


#string min&max
s="shravani"
print(max(s))
print(min(s))


