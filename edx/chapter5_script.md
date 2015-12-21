## Basic Plots with Matplotlib

This chapter is about data visualization, which is a very important part of data analysis. First of all, you will use it continuously to explore your dataset. The better you understand your data, the better you'll be able to extract insights. <<Show example?>> And once you've found those insights, again, you'll need visualization to be able to share your precious insights with other people. Because as you know, people are humans. To understand data, we need to see it. And by seeing, i don't mean in the form of an Excel table. I'm talking about beautiful plots! Such as this one...

This plot is inspired on work by Hans Rosling. His talks about global development have been viewed millions of times. And what makes them so intriguing, is that by making beautiful plots, he allows the data to tell their own story. Here we see a bubble chart, where each bubble represents a country. The bigger the bubble, the bigger the country's population, so the two biggest bubbles here are China, and India. 

There are 2 axes. The horizontal axis shows the GDP per capita, in US dollar. The vertical axis shows life expectancy. We clearly see that people live longer in countries with a higher GDP per capita. Still, there is a huge difference in life expectancy between countries on the same income level.

Now why do I tell you all of this? To fight ignorance ofcourse! But also because by the end of this chapter, you'll be able to build this beautiful plot yourself! 

So let's get started. The father of all visualization packages in python is -matplotlib-. Inside the matplotlib package, there's the pyplot subpackage. Let's start by importing it; by convention, you give it the local name `plt`.

Now let's gain some insight in the evolution of the world population. I have a list with years here, and a list with corresponding populations, expressed in billions. To plot this data as a line chart, we call plt.plot() and use our two lists as arguments. The first list corresponds to the horizontal axis, and the second list to the vertical axis. The plot function gives python all the ingredients to build a plot. But python is lazy. It will wait for the .show() function to actually build the plot. The reason for this is that you might want to add some things to your plot before actually displaying it, but more on that later.

When we look at our plot, we see that the years are shown on the horizontal axis, and the populations on the vertical axis. There are four datapoints, and Python draws a line between them. In 1950, the world population was around 2.5 billion. In 2010, it was around 7 billion. So the world population has almost tripled in sixty years, that's pretty scary. What if the population keeps on growing like that? Will the world become over populated? You'll find out in the exercises.

But first, I want to introduce you to another type of plot. It's the scatter plot. A scatter plot is useful to see all the individual datapoints. Unlike in the line plot, these datapoints will not be connected by a line. To generate a scatter plot, the code is exactly the same as before, but you're using a different function this time: 'scatter'. We can use the `year` and `population` lists we've created before.

You could say that this is a more -honest- way of plotting your data, because you can clearly see that the plot is based on just four data points. 

Now that you know about the basics of Matplotlib, it's your turn to build some awesome plots!

```
import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
plt.plot(year, pop)
plt.show()

year
pop
plt.scatter(year, pop)
plt.show()
```


## The histogram

In this video, I'll introduce you to the histogram. The histogram is a type of visualization that's particularly useful to explore your data set. It can help you to get an idea about the distribution of your variables. To see how it works, imagine 12 values between 0 and 6. I've put them along a number line here. To build a histogram for these values, you can divide the line into equal chunks, called bins. Suppose we go for 3 bins, that each have a width of 2. Next, we count how many data points sit inside each bin. There's 4 variables in the first bin, 6 in the second bin and 2 in the third bin. FInally, you draw a bar for each bin. The height of the bar corresponds to the number of data points that fall in this bin.

The result is a histogram, which gives us a nice overview on how the 12 values are distributed. Most values are in the middle, and there are more values below 2 than there are values above 4.

Of course, also matplotlib is able to build histograms. As before, you should start by importing the pyplot package that's inside matplotlib. Next, you can use the `hist()` function. Let's open up it's documentation. There's a bunch of arguments you can specify, but the first two here are the most important ones. `x` should be a list of values you want to build a histogram for. You can use the second argument, `bins`, to tell Python in how many bins the data should be divided. Based on this number, `hist()` will automatically find appropriate boundaries for all bins, and calculate how many values are in each one.

So to generate the histogram that you've seen before, let's start by building a list with the 12 values. Next, you simply call hist on this list, and specify that you want three bins. If you finally call the show function, a nice histogram results.

Histograms are really useful to give a bigger picture. As an example, have a look at this histogram that shows the age distribution for people in Europe. You can very clearly see where the bin is largest, this is the baby boom generation. This is very recent data, but what do you think will have changed in 2050? Let's have a look at a similar histogram. The distribution is flatter, and the baby boom generation has gotten older. With the blink of an eye, you can easily see how demographics can change over time. That's the true power of histograms at work here!

Now head over to the exercises, to experiment with histograms yourself!

```
values = [0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
import matplotlib.pyplot as plt
plt.hist(values,bins=3,range=[0,6])
plt.show()
```

## Customization

Data visualization is both a science, and an art. You have to use your intelligence to understand the data, and your creativity to make the data tell a story. For each visualization, you have many options. First of all, there are the different plot types. And for each plot, you can do an infinite number of customizations. You can change colors, shapes, labels, axes, and so on. The choice depends on the data, and, the story you want to tell with this data. 

Since there are a so many possible customizations, the best way to learn this, is by example. In this video, we're going to customize the world population plot to make it look a lot better. And in the exercises, you'll finally get to create Hans Rosling's famous world development bubble chart.

Let's start with the code in this script to build a simple line plot. It shows the evolution of the world population, with projections untill the year 2100, as forecasted by the united nations. I like this plot, because it shows that the population explosion that is going on right now, will have slowed down by the end of this century. But, there are a lot of things that could be better. First, it should be more clear which data we are displaying, especially to people who are seeing the graph for the first time. And second, the plot really needs to draw the attention to the population explosion.

The first thing you always need to do is label your axes. Let's do this by adding the xlabel and ylabel functions. Make sure to do this before calling the `show()` method. If you run the script, this is the result.

We're also going to add a title to our plot, with the title function. We pass the actual title, 'World Population Projections', as an argument.

Ok, so now at least we know what our plot is about! The next thing I want to change is the ticks on the y-axis. It should be clear that we are talking about billions. And also, the axis should start at zero, which puts the the population growth in perspective. For this, you can use the yticks command  and as an argument, add a list with all the ticks that you want to display. We start from 0, up to 10. 

We can add a second argument to the yticks function, which is a list with the display names of the ticks. We'll use this to add the letter B, to show that the number is expressed in Billions.

Next, let's add some more historical data to accentuate the population explosion in the last 60 years. On wikipedia, we can find the world population data for the years 1800, 1850 and 1900. We put the data in a list and append them in front of our data lists, with the plus sign. This will add three datapoints to the graph, and gives us a more complete picture.

The last thing I want to do is fill up the area under the graph, because I think it is visually more appealing if you can really see the area expand over time. We do this by replacing the plot command with the 'fill_between' command. The arguments are the x list, the y list, zero, to fill untill zero, and finally the color of the fill, green in this case. Have a look at this, pretty nice!

Now that's how you turn an average line plot into a clear visual that has a story to tell! If you compare it to our first version, this is a great improvement! Over to you now. Head over to the exercises, gradually customize your own plot and become the next Hans Rosling!

```
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("http://s3.amazonaws.com/assets.datacamp.com/course/intermediate_python_1/year_population.csv")
year = data['year'].tolist()
population = data['population'].tolist()
plt.plot(year, population)
plt.show()

plt.plot(year, population)
plt.xlabel('Year')
plt.ylabel('Population')

plt.show()
plt.plot(year,population)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')

plt.show()
plt.plot(year,population)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')
plt.yticks([0,2,4,6,8,10])
plt.show()


plt.plot(year,population)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')
plt.yticks([0,2,4,6,8,10],['0','2B','4B','6B','8B','10B'])
plt.show()


population = [1,1.262,1.650] + population
year = [1800,1850,1900] + year
plt.plot(year,population)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')
plt.yticks([0,2,4,6,8,10],['0','2B','4B','6B','8B','10B'])
plt.show()

population = [1,1.262,1.650] + population
year = [1800,1850,1900] + year
plt.fill_between(year,population,0,color='green')
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')
plt.yticks([0,2,4,6,8,10],['0','2B','4B','6B','8B','10B'])
plt.show()
```
