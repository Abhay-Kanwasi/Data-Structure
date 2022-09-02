# Question 1

"""Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this"""


# Answer

# Create a list to store these monthly expenses.

months = ['January','Feburary','March','April','May']
monthly_expenses = [2200,2350,2600,2130,2190]

#1. In Feb, how many dollars you spent extra compare to January?

print("Answer 1 :")
compare_extra_expense = monthly_expenses[1] - monthly_expenses[0]
print(f"You spent {compare_extra_expense} extra dollars in Feb as compare to January.")

print("")


#2. Find out your total expense in first quarter (first three months) of the year.

print("Answer 2 :")
first_quarter_total_expense = monthly_expenses[0] + monthly_expenses[1] + monthly_expenses[2]
print(f"The total of first three months is {first_quarter_total_expense}")

print("")


#3. Find out if you spent exactly 2000 dollars in any month.

print("Answer 3 :")
for i in range(len(monthly_expenses)):
    if monthly_expenses[i]==2000:
        print(f"In {months[i]} you spent exactly 2000 dollars.")
        break
else:
    print("You never spent exactly 2000 dollars in any month.")

print("")


#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list.

print("Answer 4 :")
new_month = 'June'
months.append(new_month)
new_expense = 1980
monthly_expenses.append(new_expense)
print(f"Months : {months}\nRespective_Expenses : {monthly_expenses}")

print("")


#5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this.

print("Answer 5 :")
monthly_expenses[3] += 200
print(f"New monthly expense list : {monthly_expenses}")

