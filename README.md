# Capstone-Project
Group project at end of boot camp


Data Fields in Source Data

### 1 timestamp
Keep column. Change name to . Check if unique, and if unique can serve as a key value.

### 2 company
Keep column. Categorical value which may need to be converted to numeric. Investigate how many unique values and consider bucketing.

### 3 level
Probably drop this field, there are >2500 unique values here, they don't coordinate with each other well, probably reflect different meanings/salary scales at different companies

### 4 title
Keep column, 15 values, consider bucketing.

### 5 totalyearlycompensation
Keep column. Will be our target in machine learning. Investigate whether it coordinates properly with base, bonus, and stock option columns and if there are any modifications to be made to make it more accurate. One of the early rows in the data seems to indicate that some rows may not be including bonus in total annual pay.

### 6 location
Keep column. Some are US, some international. Consider how to handle city, state together or separate, and whether to add a country column.

### 7 yearsofexperience
Keep column. Presumsbly all years of experience with all employers.

### 8 yearsatcompany
Keep column. Years in current job.

### 9 tag
Probably drop. Not very clear what it means, seems to describe some job responsibilities.

### 10 basesalary
Keep although may not ultimately be used in machine learning model. Use to investigate and settle on the salary value we will use for target as described above for totalyearlycompensation.

### 11 stockgrantvalue
Keep although may not ultimately be used in machine learning model. Use to investigate and settle on the salary value we will use for target as described above for totalyearlycompensation.

### 12 bonus
Keep although may not ultimately be used in machine learning model. Use to investigate and settle on the salary value we will use for target as described above for totalyearlycompensation.

### 13 gender
Keep. Missing for a significant number of records, 19941 records of 62642 have a value of NA, other, or an erroneous title field that got stored in there. Still have for approximately 2/3 of the data. Need to consider whether these missing values mean we should either 1- exclude these 19000+ rows from the data or 2-not consider gender in our data or 3-create dummy data here (probably not a good idea)

### 14 other details
Probably drop. Many blank values, a storage for different sorts of details that are probably not pertinent to our analysis.

### 15 cityid
Probably drop. No documentation as to meaning, except what we can figure out ourselves by comparison to the location field.

### 16 dmaid
Maybe keep. Investigate. Seems to be 0 for international rows, so could possibly be used as a proxy for interenational.

### 17 rowNumber
Probably drop. Seems to be an original row number/key value but highest value is in the 80000s.

### 18 Masters_Degree
Boolean field, presumably 0 if no and 1 if yes. Probably keep. Consider using an encoded score (if appropriate within ML model) to combine all education columns. All education fields seem to indicate highest level completed.

### 19 Bachelors_Degree
Boolean field, presumably 0 if no and 1 if yes. Probably keep. Consider using an encoded score (if appropriate within ML model) to combine all education columns. All education fields seem to indicate highest level completed.

### 20 Doctorate_Degree
Boolean field, presumably 0 if no and 1 if yes. Probably keep. Consider using an encoded score (if appropriate within ML model) to combine all education columns. All education fields seem to indicate highest level completed.

### 21 Highschool
Boolean field, presumably 0 if no and 1 if yes. Probably keep. Consider using an encoded score (if appropriate within ML model) to combine all education columns. All education fields seem to indicate highest level completed.

### 22 Some_College
Boolean field, presumably 0 if no and 1 if yes. Probably keep. Consider using an encoded score (if appropriate within ML model) to combine all education columns. All education fields seem to indicate highest level completed.

### 23 Race_Asian
Boolean field, presumably 0 if no and 1 if yes. 

### 24 Race_White
Boolean field, presumably 0 if no and 1 if yes. 

### 25 Race_Two_Or_More
Boolean field, presumably 0 if no and 1 if yes. 

### 26 Race_Black
Boolean field, presumably 0 if no and 1 if yes. 

### 27 Race_Hispanic
Boolean field, presumably 0 if no and 1 if yes. 

### 28 Race
Drop. All values are NA. Was probably the original race column before split into many columns.

### 29 Education
Drop. All values are NA. Was probably the original race column before split into many columns.


