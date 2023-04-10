# RegressionSelection
 This Python Script to help select a regression model based off a the R squared value. 

## What Are the Types of Regression Models? 

### Linear Regression 
is a way to figure out how one thing is related to another thing. For example, let's say you wanted to know if there was a relationship between how much time you spend studying and how well you do on tests. You could use linear regression to figure out if there is a connection between those two things.

Linear regression works by looking at a bunch of data points that you have collected. Each data point is like a pair of numbers that go together, one for each thing you are interested in. So in our example, each data point would have one number for how much time you spent studying, and another number for how well you did on the test.

The linear regression formula looks at all those pairs of numbers and tries to draw a straight line that best fits all the data points. This line is called a "regression line". Once you have that line, you can use it to predict what the second thing (in our example, how well you do on a test) will be for any given value of the first thing (how much time you spend studying).

So, in our example, if the regression line shows that there is a strong positive relationship between the two things (meaning the more you study, the better you do on the test), you can use the regression line to predict how well you might do on a future test based on how much time you plan to spend studying.

### Multilinear Regression
Multilinear regression is similar to simple linear regression, but instead of looking at the relationship between just two variables, it looks at the relationship between a target variable and multiple predictor variables.

To put it simply, multilinear regression is a statistical method used to find the relationship between a dependent variable and two or more independent variables.

For example, let's say you want to know how much a person's salary is based on their age, years of experience, and level of education. In this case, you would have three predictor variables (age, years of experience, and level of education) and one target variable (salary).

Multilinear regression looks at all the data points you have for each of these variables, and tries to find the best equation that can predict the target variable (salary) based on the values of the predictor variables (age, years of experience, and level of education). The equation would take into account the weight of each predictor variable, which is determined by the strength of the relationship between the predictor and the target variable.

Once you have the equation, you can use it to predict the target variable for new data points that have the same predictor variables. In our example, you could use the equation to predict how much a person might earn based on their age, years of experience, and level of education.

### Polynomial  Regression

Polynomial regression is a type of regression analysis in which the relationship between the independent variable and the dependent variable is modeled as an nth degree polynomial. In simpler terms, polynomial regression is a way to model non-linear relationships between variables.

To put it simply, polynomial regression is a statistical method used to find the relationship between a dependent variable and an independent variable that is best represented by a curved line instead of a straight line.

For example, let's say you want to know how a person's height affects their weight. Instead of assuming that there is a linear relationship between height and weight (i.e. taller people weigh more), you might think that the relationship is better described by a curved line. In this case, you could use polynomial regression to model the relationship between height and weight.

Polynomial regression looks at all the data points you have for the independent and dependent variables, and tries to find the best curve that fits the data. The degree of the polynomial determines the number of bends in the curve. For example, a second-degree polynomial (also known as a quadratic equation) has one bend, while a third-degree polynomial (also known as a cubic equation) has two bends.

Once you have the curve, you can use it to predict the dependent variable for new data points that have the same independent variable. In our example, you could use the curve to predict how much a person might weigh based on their height.
