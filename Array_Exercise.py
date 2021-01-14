# 1. Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

# Solution 1.
Month_expences = [2200, 2350, 2600, 2130, 2190]
print(Month_expences[1]- Month_expences[0], "Dollars")
print("Total expense in first quarter: ",Month_expences[0]+Month_expences[1]+Month_expences[2])
for item in Month_expences:
    if item==2000:
        print("Yes")
    else:
        print("No")
A= Month_expences.append(1980)
print(Month_expences)
Month_expences[3] = 1930
print(Month_expences)

# 2. You have a list of your favourite marvel super heros.
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,
#
# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
# solution 2
heroes = ['spider-man', 'thor', 'hulk', 'iron man', 'captain america']
print(len(heroes))
updated = heroes.append("Black panther")
print(heroes)
heroes.remove("Black panther")
heroes.insert(3, "Black panther")
print(heroes)
heroes[1:3]= ["docter-strange"]
print(heroes)
heroes.sort()
print(heroes)

# 3. Create a list of all odd numbers between 1 and a max number. Max number is something
# you need to take from a user using input() function
# solution 3
max_num = int(input("Write the number: "))
li =[]
i = 0
while(i<max_num):
     i = i+1
     if i%2!=0:
        li.append(i)
print(li)
