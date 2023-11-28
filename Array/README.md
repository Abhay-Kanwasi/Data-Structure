# Array

Linear Data Structure <br>
Contiguous memory locations <br>
Access elements randomly <br>
Homogeneous elements i.e similar data type elements <br>


### We can solve homogeneous element problem by using referencial arrays
Normal array use call by value to manage array. But in case of referencial array we store each element in different memory location. Then make an array in that array rather than storing element we store addresses of the array. This is called call by reference.

## PYTHON LIST IS AN REFERENCIAL ARRAY, INTERNALLY IT'S A DYNAMIC ARRAY

# Dynamic Array
In dynamic array we take a static array suppose we have a array of size 3 then if we have more elments then three we just double the size of the array and copy all the elements of previous array in it now this is also an static array and this is go on

## Questions we solve

__Question 1__

Let us say your expense for every month are listed below,
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
based on this


__Question 2__

You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

__Question 3__

Create a one-dimensional integer array and insert numbers to the maximum size provided until the end of the array. Access the numbers inserted and then display the same as output.

