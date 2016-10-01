# Homework 4 - Assignment 1 - Review Classmate's Citibike Project Proposal

## Step 1 - Verify the Null and Alt hyptheses

The general idea / impetus for the project is stated as "Men tend to use bikes with shorter time than women."  Thus, the null hypothesis
would be "The mean trip duration of women's bike rides is as long as or longer than men's mean trip duration" while the altnerative 
hypothesis would be "The mean trip duration for men is less than women" which are stated in the header of is ipynb notebook.

## Step 2 - Verify the data used is correct

The June 2016 citibike data is imported and then only the "gender" and "trip duration" columns are kept, which are categorical and 
continous variables respectively.  Further, gender represents the indepedent variable while trip duration represents the dependent 
variable.  It is noted that later on in the code, the trip duration column is converted from seconds to minutes, which is 
definitely a better way to conceptualizae the data, and people can more easily ascertain duration through minutes than seconds.

## Step 3 - Suggest an appropriate statistical test

The t-Test could be a suitable statistical analysis test for this analysis, as it is suitable for 1 dichotomous (i.e., binary)
independent variable (gender, in the case of this analysis) and 1 continous dependent variable (trip duration for this analysis).
This test would illuminate whether or not differences exist between 

The correlation statitical test would also be suitable, as it has the same independent and dependent varianle parameters as the 
t-Test.  This test would show the strength and direction (+/-) of the relation between the independent and depedent variable.

## Additional Comments

The code was concise and well implemented.  The only comment I have is that in terms of plotting the selected variables against
each other, a scatter plot might not be the best visualization (even though I think that was what the assignment requested) 
because the gender variable only has two values.  Another way to plot it would be to have a bar chart of men's and women's 
trip duration means next to each other, which would be similar to the scatter plot because of the binary nature of the 
variable, but I think it would be a little cleaner.

