# School_District_Analysis (Module 4 Challenge)
The code is divided into two sections - the Module 4 original data and the Module 4 challenge data where Thomas High School 9th grade scores are omitted. The first section has more sub sections because the analysis was grouped into functions for re-use.

# Challenge Questions:
After replacing the reading and math scores, answer the following questions:
## 1. How is the district summary affected?
  - The average math scores went down from 79.0 to 78.9. 
  - The average reading scores remained fixed at 81.9.
  - % passing math went down from 75% to 74%.
  - % passing reading remaiend fixed at 86%.
  - Overall passing went down from 65% to 64%.

## 2. How is the school summary affected?
  - The average math and reading scores are mostly unchanged for the top 5 (~83%). 
  
## 3. How does replacing the ninth graders’ math and reading scores affect Thomas High School’s performance, relative to the other schools?
  - The 9th grade studentsOriginally, Thomas High School was the 2nd top school with overall passing 90.95%.
  - After removing the 9th grade students from the passing %, Thomas High School is the 8th ranked school with overall passing 65.08%.
  
## 4. How does replacing the ninth-grade scores affect the Math and Reading Scores by Grade, Scores by School Spending, Scores by School Size, and Scores by School Type? 
  - Math and Reading Scores by Grade:
    - The scores for each grade only affect Thomas High's 9th graders, which is now NaN since they are all omitted.
  - Scores by School Spending:
    - The changes were so small, I modified the function to display two decimals instead of one decimal. 
    - Thomas High falls into the $630-644 spending category, which originally had average math score, reading score, passing math %, passing reading %, and overall passing % of 78.52, 81.62, 73%, 84%, and 63% respectively. 
    - After omitting the 9th grade scores, those values changed to 78.50, 81.64, 67%, 77%, and 56%.
  - School Size:
    - Thomas High School is in the medium size (1000-2000) category. Originally, the overall passing % for small, medium, and large schools are 90%, 91%, and 58% respectively. After the Thomas 9th grader score removal, the overall passing % for medium went down to to 85%. Small and large school % remained the same, since the same scores were used for those schools.
    - The medium size (1000-2000) category had average math score, average reading score, % passing math, % passing reading, and % overall passing values of 83.37, 83.86, 94%, 97%, 91%. After removal, those values went down to 83.36, 83.87, 88%, 91%, and 85%.
  - School Type:
    - Originally, charter schools had average math, average reading, % passing math, % passing reading, and % overall passing values of 83.474, 83.896, 94%, 97%, and 90% respectively.
    - After the Thomas High 9th grade score removal, those values went down to 83.465, 83.902, 90%, 93%, and 87% respectively.
    - District schools remained unchanged at 76.957, 80.967, 67%, 81%, and 54%.
    
