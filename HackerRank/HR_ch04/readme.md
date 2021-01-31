## Write a function
We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day
and we add it to the shortest month of the year, February.<br/>
In the Gregorian calendar three criteria must be taken into account to identify leap years:
* The year can be evenly divided by 4, is a leap year, unless:
* The year can be evenly divided by 100, it is NOT a leap year, unless:
* The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900,
2100, 2200, 2300 and 2500 are NOT leap years.
### Task
You are given the year, and you have to write a function to check if the year is leap or not.<br />
Note that you have to complete the function and remaining code is given as template.
### Input Format
Read **_y_**, the year that needs to be checked.
### Output Format
Output is taken care of by the template. Your function must return a boolean value (**_True/False_**)<br />
**Sample Input:**<br />
1990<br />
**Sample Output:**<br />
False<br />
**Explanation:**<br />
1990 is not a multiple of 4 hence it's not a leap year.<br />

Task source: [HackerRank](https://www.hackerrank.com)