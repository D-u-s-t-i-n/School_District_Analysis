# Module 4 Challenge begins here 
# Read the student data file and store it in a Pandas DataFrame.
import pandas as pd
import os
import numpy as np


def percentage(count, total):
    return (count / (float)total * 100)

def school_type_analysis(school_data_df, student_data_df):
    # Determine the school type.
    per_school_types = school_data_df.set_index(["school_name"])["type"]
    # Add the per_school_types into a DataFrame for testing.
    df = pd.DataFrame(per_school_types)
    # Calculate the total student count.
    per_school_counts = school_data_df["size"]
    per_school_counts
    # Calculate the total student count.
    per_school_counts = school_data_df.set_index(["school_name"])["size"]
    per_school_counts
    # Calculate the total student count.
    per_school_counts = school_data_complete_df["school_name"].value_counts()
    per_school_counts
    
    # Calculate the total school budget.
    per_school_budget = school_data_df.set_index(["school_name"])["budget"]
    per_school_budget
    
    # Calculate the per capita spending.
    per_school_capita = per_school_budget / per_school_counts
    per_school_capita
    
    # Calculate the math scores.
    student_school_name = student_data_df.set_index(["school_name"])["math_score"]
    student_school_name
    
    # Calculate the average math scores.
    per_school_averages = school_data_complete_df.groupby(["school_name"]).mean()
    per_school_averages
    
    # Calculate the average test scores.
    per_school_math = school_data_complete_df.groupby(["school_name"]).mean()["math_score"]
    
    per_school_reading = school_data_complete_df.groupby(["school_name"]).mean()["reading_score"]
    per_school_math
    

def district_analysis(school_data_df, student_data_df):
    # The Module 4 analysis is bundled into this function for re-use
    #analysis_array_df = {}
    # Combine the data into a single dataset.
    school_data_complete_df = pd.merge(student_data_df, school_data_df, on=["school_name", "school_name"])
    #[Debug] school_data_complete_df.head()
    # Get the total number of students.
    return school_data_complete_df
    
    # Calculate the total budget.
    total_budget = school_data_df["budget"].sum()
    total_budget

    # Calculate the average reading score.
    average_reading_score = school_data_complete_df["reading_score"].mean()
    average_reading_score
    
    # Calculate the average math score.
    average_math_score = school_data_complete_df["math_score"].mean()
    average_math_score
    
    passing_math = school_data_complete_df["math_score"] >= 70
    passing_reading = school_data_complete_df["reading_score"] >= 70
    
    # Get all the students who are passing math in a new DataFrame.
    passing_math = school_data_complete_df[school_data_complete_df["math_score"] >= 70]
    
    # Get all the students that are passing reading in a new DataFrame.
    passing_reading = school_data_complete_df[school_data_complete_df["reading_score"] >= 70]
    
    # Calculate the number of students passing math.
    passing_math_count = passing_math["student_name"].count()
    
    # Calculate the number of students passing reading.
    passing_reading_count = passing_reading["student_name"].count()
    print(passing_math_count)
    print(passing_reading_count)

    student_count = school_data_complete_df["Student ID"].count()
    # Calculate the percent that passed math.
    passing_math_percentage = passing_math_count / float(student_count) * 100
    
    # Calculate the percent that passed reading.
    passing_reading_percentage = passing_reading_count / float(student_count) * 100
    
    print(passing_math_percentage)
    print(passing_reading_percentage)

    # Calculate the students who passed both math and reading.
    passing_math_reading = school_data_complete_df[(school_data_complete_df["math_score"] >= 70) & (school_data_complete_df["reading_score"] >= 70)]
    passing_math_reading.head()
    overall_passing_math_reading_count = passing_math_reading["student_name"].count()
    overall_passing_math_reading_count

    # Calculate the overall passing percentage.
    overall_passing_percentage = overall_passing_math_reading_count / student_count * 100
    overall_passing_percentage
    
    # Adding a list of values with keys to create a new DataFrame.
    district_summary_df = pd.DataFrame(
              [{"Total Schools": school_count,
              "Total Students": student_count,
              "Total Budget": total_budget,
              "Average Math Score": average_math_score,
              "Average Reading Score": average_reading_score,
              "% Passing Math": passing_math_percentage,
             "% Passing Reading": passing_reading_percentage,
            "% Overall Passing": overall_passing_percentage}])
    # Format improvement
    district_summary_df["Total Students"] = district_summary_df["Total Students"].map("{:,}".format)
    district_summary_df["Total Budget"] = district_summary_df["Total Budget"].map("${:,.2f}".format)
    district_summary_df["Average Math Score"] = district_summary_df["Average Math Score"].map("{:.1f}".format)    
    district_summary_df["Average Reading Score"] = district_summary_df["Average Reading Score"].map("{:.1f}".format)    
    district_summary_df["% Passing Math"] = district_summary_df["% Passing Math"].map("{:.0f}".format)    
    district_summary_df["% Passing Reading"] = district_summary_df["% Passing Reading"].map("{:.0f}".format)    
    district_summary_df["% Overall Passing"] = district_summary_df["% Overall Passing"].map("{:.0f}".format)
    # Reorder the columns in the order you want them to appear.
    new_column_order = ["Total Schools", "Total Students", "Total Budget","Average Math Score", "Average Reading Score", "% Passing Math", "% Passing Reading", "% Overall Passing"]
    
    # Assign district summary df the new column order.
    district_summary_df = district_summary_df[new_column_order]
    
    

# Files to load
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"

student_data_df = pd.read_csv(student_data_to_load)
student_data_df
school_data_df = pd.read_csv(school_data_to_load)

# Step 1 - Clean out the troll names
#student_names = student_data_df["student_name"].tolist()
#for name in student_names:
    #print(name.split(), len(name.split()))

# Add each prefix and suffix to remove to a list.
prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]
for word in prefixes_suffixes:
    student_data_df["student_name"] = student_data_df["student_name"].str.replace(word,"")

# Use an if statement to check the length of the name.
# If the name is greater than or equal to "3", add the name to the list.

#for name in student_names:
#    if len(name.split()) >= 3:
#        students_to_fix.append(name)

# Get the length of the students whose names are greater than or equal to "3".
#len(students_to_fix)

school_data_complete_df = analysis(school_data_df, student_data_df)
student_count = school_data_complete_df.count()
student_count


# Step 2 - Omit cheating high school 9th graders grades.
student_data_to_load = "Resources/clean_students_complete.csv" #schools_complete.csv"
student_data_df = pd.read_csv(student_data_to_load)
    
# [Check] Display filter is coded correctly
student_data_df.loc[student_data_df['school_name'] == 'Thomas High School'].loc[student_data_df['grade'] == '9th']


student_data_df.loc[student_data_df.school_name.str.match("Thomas High School") & student_data_df.grade.str.match("9th"), "reading_score"] = np.NAN
student_data_df.loc[student_data_df.school_name.str.match("Thomas High School") & student_data_df.grade.str.match("9th"), "math_score"] = np.NAN

#school_data_complete_df = analysis(school_data_df, student_data_df)
#student_count = school_data_complete_df.count()
#student_count

# Replace the grades of 9th graders at Thomas High School with nan
#student_data_9th_graders_grades_removed_df = student_data_df.loc[student_data_df['school_name'] == 'Thomas High School'].loc[student_data_df['grade'] == '9th', 'reading_score'] = np.NaN
#student_data_9th_graders_grades_removed_df = student_data_df.loc[student_data_df['school_name'] == 'Thomas High School'].loc[student_data_df['grade'] == '9th', 'reading_score'] = np.NaN


#train.loc[train['Pclass'] == 1, 'Cabin'] = 1
#student_data_df.loc[student_data_df['school_name'] # == 'Thomas High School'].loc[student_data_df['grade'] == '9th']
#student_data_df.loc[student_data_df['school_name'] == 'Thomas High School'].loc[student_data_df['grade'] == '9th'] = 
#student_data_df.loc[student_data_df['school_name'] == 'Thomas High School'].loc[student_data_df['grade'] == '9th'].str.replace(word,"")