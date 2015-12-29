## Boolean Logic & Control Flow

Before, you already learned about different Python types. Among those was the Boolean. Remember how you used the boolean array to do subsetting?

In this video, I'm going to talk some more about relational operators; they are operators that result in a Boolean. You use them to see how two Python values relate. Say, for example, that you want to check if 2 is smaller than 3. You type 2 less then sign 3, and hit Enter. Because this is the case, you get True. You can also check if two values are equal, with a double equals sign. From this call, we see that 2 equals equals 3 gives us False. Of course, you can also use relational operators directly on variables, like this:

Have a look at this table that summarizes all relational operators. You already know about greater than, less than and equality. There's also greater than or equal to and less then or equal to. The opposite of equality, is inequailty, that you write as an exclamation mark followed by an equals sign.

The next step is combining booleans. You can use logical operators for this. The three most common ones are AND, OR, and NOT. 

The and operator works just as you would expect. It takes two boolans and returns `True` only if both the booleans are `True` themselves. This means that `True and True` evaluates `True`, but that `False and True`, `True and False` and `False and False` all evaluate to `False`. 

Instead of using booleans, we can off course use the results of comparisons. Suppose we have a variable `x`, equal to 12. To check if this variable is greater than 5 but less than 15, we can use x greater than 5 and x less than 15. As you already learned, the first part will evaluate to `True`. The second part, will also evaluate to `True`. So the result of this expression is `True`. This makes sense, because 12 lies between 5 and 15. 

The OR operator works similarly, but the difference is that only at least one of the booleans it uses should be equal to `True` for the OR operation to evaluate to True. This means that, `True or True` equals `True`, but that also `True or False` and `False or True` evaluate to `True`. Only False or False results in `False`. Also here you can make combinations with variables, like this example that checks if a variable `y`, equal to 5, is less then or equal to 7 or above 13. 5 less than 7 is True, 5 greater than 13 is False. The OR operation thus returns True.


Finally, there's the NOT operator, represented by an exclamation mark. It simply negates the boolean value you use it on. Not True is False, Not False, is True. 


Things get really interesting, when you can actually use relational operators and logical operators to change how your program behaves. Depending on the outcome of your comparisons, you might want your Python code to behave differently. You can do this with conditional statements in Python: if, else and elif. 

Let's start working in a script, control.py. Suppose you have a variable `z`, equal to 4. If the value is even, you want to print out: "z is even". This code does the trick. modulo operator 2 will return 0 if z is even.

If you run this, Python checks if the condition holds. It's true, so the corresponding code is executed: z is even gets printed out.

Let's compare this to the general recipe for an if statement. 

It reads as follows: if condition, execute expression. Notice the colon at the end, and the fact that you simply have to indent the Python code with four spaces to tell Python what to do in the case the condition succeeds. It's perfectly possible to have more lines here, like this for example. The script now prints out two lines if you run it.


If the condition does not pass, the expression is not executed. You can see this if we change z to be 5 and rerun the code: there's no output.

Suppose now that you want to print out "z is odd" in this case. How to do this? Well, you can simply use an else statement, like this. <PAUSE> If we run it with z equal to 5, the condition is not true, so the expression for the else statement gets printed out. The general recipe looks like this: for the else statement, you don't need to specify a condition. The corresponding expression gets run if the condition of the if statement it belongs to does not hold.

  
You can think of cases where even more customized behavior is necessary. Say you want different printouts for numbers that are divisible by 2 and by 3. You can throw some elifs in there to get the job done. Take this example:

Can you tell what this script will print out if you run it? If z equals 3, the first condition is FALSE, so it goes over to the next condition. This condition, does hold, so the corresponding print statement is exectued. Suppose now that z equals 6. Both the if and elif conditions hold in this case. Will two printouts occur? Nope. As soon as Python bumps into a condition that is true, it exectues the corresponding code and then leaves the control structure after that. This means the second condition, corresponding to the elif, is never reached so there's no corresponding printout.

Now that you know more about relational operators, logical operators and control flow, it's time to get practical with them in the exercises

```
2 < 3
2 == 3
x = 2
y = 3
x < y
x == y
True and True
False and True
True and False
False and False
x = 12
x > 5 and x < 15

True or True
True or False
False or True
False or False
y = 5
y <= 7 or y > 13

not True
not False
```

```
z = 4
if z%2 == 0 :
    print("z is even")

if condition :
    expression

z = 4
if z%2 == 0 :
    print("checking"  + str(z))
    print("z is even")

z = 5
if z%2 == 0 :
    print("z is even")
else :
    print("z is odd")


z = 3
if z%2 == 0 :
    print("z is divisible by 2")
elif z%3 == 0 :
    print("z is divisible by 3")
else :
    print("z is neither divisbly by 2 nor by 3")
```

## Pandas

As a data scientist, you'll often be working with tons of data. You already know about the 2D numpy array, to house data in a rectangular structure. But there's a downside to this: you can only have data of the same type in there. In practice, you'll be working with data of different types: numerical values, strings, booleans and so on.

To easily and efficiently handle this data, there's the Pandas package. Pandas is a high level data manipulation tool, used by data scientists all over the world.

In pandas, we store data in a so-called dataframe. Have a look at this data frame, called `brics`. It contains some basic information on the so called 'brics' countries: Brazil, Russia, India, China and South Africa. 

A dataframe is a table: the rows represent different entries or observations, which are countries in this case. Each row has unique row label: BR for brazil, RU for russia and so on. 

The columns represent different properties, and are identified by their column labels: country, population, area and capital. The columns can have differnt types. The country column is string, while the population column is numeric for example.

You typically don't build a pandas data frame manually. Instead, you import data from an external file that contains all this data. The brics data that I showed you before comes from this CSV file, which is short for comma separated values. 

The first line are the column names and the other lines are the rows of the table. CSV files are a very common way to store datasets, so let's try to import this data ourselves.

We start by importing the pandas packages as `pd`. Now, you can use the `read_csv()` function, and pass the path to your csv file as an argument, like this:

If you now print brics, there's still something wrong. The row labels, also called row indexes, are seen as a column in their own right. To solve this, we'll have to tell the `read_csv()` function that the first column contain the row indexes. You do this iwht hte `index_col` argument, like this:

This time `brics` contains the data frame we started with in this video. It nicely contains the row and column labels.

One of the things that makes Pandas so powerful, is the ease with which you can select columns and rows in different ways.

To access our nicely named columns, you use the notation with square brackets, like this example, where I selected the country column of brics. You can also use the dot notation. Notice that in this case, you don't have to use quotation marks. 

Even adding a column is easy. You can use the same square brackets for this, but this time you assign a list to it.

You can even go further, and make a column, based on other columns.
Here we make a column with the population density. Because pandas is based on numpy, we can simply divide the population by the area. We multiply with one million because the population columns is expressed in millions. That's nice, we calculated a new feature in one line! Apparently, India is the most densily populated of the brics countries, with 380 people per square kilometer. And not surprisingly, Russia, being the largest country in the world, has only 8 people per square kilometer.

So now you know that to access a column, you typically use square brackets with the column label.
To access a row, you'll need another method, though, since pandas has to know we are talking about row labels instead of column labels. 

You'll want to use `loc`. For brics, we type brics dot loc and then the row index of the row we want to access as a string inside square brackets. The result is the row information, displayed as a column. Now. it's easy to tell that Brazil currently has a population of 200 million people, for example.

To get just one element in the table, you can specify both column and row label in the loc function, like this. There are also other ways to do this. First select the column and then use loc to select a row, like here, or the other way around, like this. This is the cool thing about Pandas, you can work with it in many different ways.

I hope these basic functionalities have already aroused you to start using pandas. From my own experience I can tell you that the more you'll use pandas, the more you'll love it! It's time to get some practice!
