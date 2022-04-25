# Capstone-Project
Group project at end of boot camp <br>
Martha, Lucien and Cheryl
Updated 04-24-2022

### GitHub:
-	Your Main Branch has a ReadMe file 
    -	You're reading it!
-	Your ReadMe file includes a description for how your team plans to communicate for the project
    - Communication plan: use Slack to chat between meetings, meet up during class and office hours to work and plan together, plan additional meetings via zoom as needed
-	You have individual branches setup for each of your team members:
    - Cheryl has the Cheryl branch
    - Lucien has the dummy_database branch
    - Martha has the presentation branch, also some data investigation stuff is in there
-	Each team member has at least four commits from the duration of the first segment

### Presentation:
-	Include your choice of a PowerPoint, Word Document, ReadMe file, etc. with the following information
    - The project is described in detail in this README
    - The PowerPoint file https://github.com/mgsrichard/Capstone-Project/blob/main/Segment%202_presentation.pptx gives a more sophisticated and slightly less detailed overview/presentation of our project
- Here is the agenda for Segment 2 Presentation: 
    - ![image](https://user-images.githubusercontent.com/94234511/165016366-5de88506-e051-4632-9789-8604236e30a1.png)

### Topic: 
Data Science and STEM Salaries from June 7, 2017 to August 17, 2021
  https://www.kaggle.com/datasets/jackogozaly/data-science-and-stem-salaries

- Description of your data source (feel free to include a sample of it too)
    - The Kaggle description of the data says, "62,000 salary records from top companies. This data was scraped off levels.fyi." 
    - The data has 62,642 rows, 29 columns, columns including company name, job title, salary, bonus, stock option, gender, race, and location
![pic of kaggle data source](https://github.com/mgsrichard/Capstone-Project/blob/main/resources/Kaggle_data_source.png)

- Reason: 
  We found the data source relevant to our current career interests.  In addition,the dataset was appropriately dimensioned and did not have a lot of missing data.  Datatypes varied across the columns and there are several features that can be used to for modeling.  

### Objectives: 

- Discover what features and model make the best predictions for salaries of STEM Professionals and Data Scientists
- Explore the data and visualize contents, perform data cleaning, engineer the features, and pre-process the dataset for machine learning 
- Identify the best predictive model and select the user input features. 
- Develop the ERD and connect a SQL Database to the model 
- Present our results via an interactive table to predict salaries for data scientists and STEM professionals based on the most predictive features

### Database
-	Present a provisional database that stands in for the final database
    #### Preliminary schema for bringing in our data: <br>
    ![schema image](https://github.com/mgsrichard/Capstone-Project/blob/main/resources/Schema.png)
 
#### Original Plan to investigate and clean the original data fields
    - **timestamp:**
Probably drop. Seems to be when the job was added to the database. Shouldn't have a bearing on the salary amount we want to predict.

    - **company:**
Keep column. Categorical value which may need to be converted to numeric. Investigate how many unique values and consider bucketing.

    - **level:**
Probably drop this field, there are >2500 unique values here, they don't coordinate with each other well, probably reflect different meanings/salary scales at different companies

    - **title:**
Keep column, 15 values, consider bucketing.

    - **totalyearlycompensation:**
Keep column. Will be our target in machine learning. Investigate whether it coordinates properly with base, bonus, and stock option columns and if there are any modifications to be made to make it more accurate. One of the early rows in the data seems to indicate that some rows may not be including bonus in total annual pay.

    - **location:**
Keep column. Some are US, some international. Consider how to handle city, state together or separate, and whether to add a country column.

    - **yearsofexperience:**
Keep column. Presumably all years of relevant experience with all employers.

    - **yearsatcompany:**
Keep column. Years in current job.

    - **tag:**
Probably drop. Not very clear what it means, seems to describe some job responsibilities.

    - **basesalary:**
Keep although may not ultimately be used in machine learning model. Use to investigate and settle on the salary value we will use for target as described above for totalyearlycompensation.

    - **stockgrantvalue:**
Keep although may not ultimately be used in machine learning model. Use to investigate and settle on the salary value we will use for target as described above for totalyearlycompensation.

    - **bonus:**
Keep although may not ultimately be used in machine learning model. Use to investigate and settle on the salary value we will use for target as described above for totalyearlycompensation.

    - **gender:**
Keep. Missing for a significant number of records, 19941 records of 62642 have a value of NA, other, or an erroneous title field that got stored in there. Still have for approximately 2/3 of the data. Need to consider whether these missing values mean we should either 1- exclude these 19000+ rows from the data or 2-not consider gender in our data or 3-create dummy data here (probably not a good idea)

    - **other details:**
Probably drop. Many blank values, a storage for different sorts of details that are probably not pertinent to our analysis.

    - **cityid:**
Probably drop. No documentation as to meaning, except what we can figure out ourselves by comparison to the location field.

    - **dmaid:**
Maybe keep. Investigate. Seems to be 0 for international rows, so could possibly be used as a proxy for international.

    - **rowNumber:**
Keep. Seems to be an original row number/key value. Used in our Postgres table as primary key value.

    - **Masters_Degree:**
Boolean field, presumably 0 if no and 1 if yes. Probably keep. Consider using an encoded score (if appropriate within ML model) to combine all education columns. All education fields seem to indicate highest level completed.

    - **Bachelors_Degree:**
Boolean field, presumably 0 if no and 1 if yes. Probably keep. Consider using an encoded score (if appropriate within ML model) to combine all education columns. All education fields seem to indicate highest level completed.

    - **Doctorate_Degree:**
Boolean field, presumably 0 if no and 1 if yes. Probably keep. Consider using an encoded score (if appropriate within ML model) to combine all education columns. All education fields seem to indicate highest level completed.

    - **Highschool:**
Boolean field, presumably 0 if no and 1 if yes. Probably keep. Consider using an encoded score (if appropriate within ML model) to combine all education columns. All education fields seem to indicate highest level completed.

    - **Some_College:**
Boolean field, presumably 0 if no and 1 if yes. Probably keep. Consider using an encoded score (if appropriate within ML model) to combine all education columns. All education fields seem to indicate highest level completed.

    - **Race_Asian:**
Boolean field, presumably 0 if no and 1 if yes. 

    - **Race_White:**
Boolean field, presumably 0 if no and 1 if yes. 

    - **Race_Two_Or_More:**
Boolean field, presumably 0 if no and 1 if yes. 

    - **Race_Black:**
Boolean field, presumably 0 if no and 1 if yes. 

    - **Race_Hispanic:**
Boolean field, presumably 0 if no and 1 if yes. 

    - **Race:**
Drop. All values are NA. Was probably the original race column before split into many columns.

    - **Education:**
Drop. All values are NA. Was probably the original education column before split into many columns.
    
- How the Machine Learning model might connect with this database
    - We will connect python to PostgresSQL/pgAdmin and output cleaned data and machine learning results to PostgreSQL/pgAdmin. Here are some examples of code from the Movies-ETL challenge where we connected python to a PostgreSQL/pgAdmin database. 
        ![python to sql 1](https://github.com/mgsrichard/Capstone-Project/blob/main/resources/python_to_sql_1.png)
        ![python to sql 2](https://github.com/mgsrichard/Capstone-Project/blob/main/resources/python_to_sql_2.png)
        ![python to sql 3](https://github.com/mgsrichard/Capstone-Project/blob/main/resources/python_to_sql_3.png)

### A Summary of Data Cleaning Steps can be seen below: 
- Reduced noisy data:
    - Checking for usable DataTypes
    - Transform the location column 
    - Performing Outliers Analysis
![image](https://user-images.githubusercontent.com/94234511/165017194-63cfcaa3-a23e-4ab7-8fd1-af33a1cf2c14.png)
![image](https://user-images.githubusercontent.com/94234511/165017211-e74f4ac0-5d85-40c2-b3e9-8dc4e6103c8a.png)

- Other Data Cleaning
    - Drop 29 duplicate rows, 0 duplicate columns 
    - Drop unwanted columns
    - Remove null values
        - gender                     19540
        - otherdetails               22505
    - Drop 5 rows where company is NaN missing rows (data now has 62,637 rows) 
    - Convert timestamp field from object to datetime
    - Clean-up erroneous data values in location and gender columns
        - The total number of rows with data in the education columns is 30472 out of 62637 rows
        - The total number of rows with data in the race columns is 22426 out of 62637 row
    - Identified and corrected additional typographical and formatting errors in the data

[image](https://user-images.githubusercontent.com/94234511/165016989-32fba604-96b3-49f5-86cb-f5b0b0c6cc43.png)
### Feature Engineering

FEATURE ENGINEERING – Salary level
[image](https://user-images.githubusercontent.com/94234511/165017640-5e7a482b-a2a0-4eac-b7ab-19f0c29a18d1.png)

- For rows where basesalary = 0, set equal to totalyearlycompensation 
- Create a target value from the base salary by bucketing
- Mean plus two std dev. would be 149,172 + 44,382 + 44,382 = 237,936
- #Make salary bands of 25,000 for a total of 15 salary levels 
[image](https://user-images.githubusercontent.com/94234511/165017702-7ade3729-a629-4d65-ae82-48ed8e3dd5aa.png)

### Machine Learning Model
-	Present a provisional machine learning model
![supervised learning picture](https://github.com/mgsrichard/Capstone-Project/blob/main/resources/supervised-learning.png)
    - We orignally proposed to use the LinearRegression model from Scikit-learn to create a supervised linear regression machine learning model and our input data to predict salaries for data scientists and STEM professionals. The example from module 17.2.3 shown below is a good starting place for our coding.	
     ![image](https://user-images.githubusercontent.com/94234511/162580102-7f2c75fb-5c78-4d70-853c-138aeee1347b.png)
- Regression is used to predict continuous variables. The regression model's algorithms would attempt to learn patterns that exist among these factors. When presented with the data for a new row(index), the model would make a prediction of the output, based on previously learned patterns from the dataset. While the example from the module only uses one feature, years of service, to predict  salaries, the model is also able to take in multiple features to do a multiple regression.  
- In both classification and regression problems, the dataset is divided into features and target. Features are the variables used to make a prediction. Target is the predicted outcome. The target in our data will be the final total salary field (after we clean up the data) and the other fields will be our features. 
- We intend to use trial and error with different linear regression models and data columns to make the most accurate model possible. We are aiming for a model that is at least 75% accurate. We may use the LinearRegression model, but we have also glanced through the Scikit-learn documentation and seen that there are some variations of linear regression, including Lasso and Elastic-Net that are also available to try. Some of these other models also seem to help in deciding how to narrow which features are most important to the model, so that could be helpful.
- Once we have fitted and trained our model and reached our 75% accuracy threshold, we will then create a way to present our results. We would like to create an interactive web table as we did in the UFO and Bellybutton challenges where the user can enter data (years of experience, job title, location, etc.) and get an estimated salary or salary range as an output. (A salary range could be created using the salary prediction and our accuracy percentage, for example, a prediction of 100,000 at 75% accuracy would translate to a salary range of 75,000 to 125,000). 
- Outcomes of linear regression proved to provide a weak to modest correlation and may not be the best model for prediticting salaries
- Datasource: Resources/US_Salary_Cleaned.csv
- Linear Regression Model 
![image](https://user-images.githubusercontent.com/94234511/165017486-a6b8859d-50dc-4456-97c9-eadfdf22a8bc.png)

- The slope = [5040.09]
The y-intercept = 163190.93
r = 0.398 
![image](https://user-images.githubusercontent.com/94234511/165017508-9c255d38-b85d-4526-9061-68228697df15.png)


- Provisonal Learing Model Selection 
Evaluate Supervised Learning Model - Ensemble Method - Random Forest Classification
![image](https://user-images.githubusercontent.com/94234511/165017776-2a6ee2cf-6ba0-49a6-8123-514556bedc99.png)

#### RFM - All Features
Cleaned_Salary_Data.csv
Training Data Shape (46977 rows, 38 columns)
Test Data (15660 rows, 38 columns)
![image](https://user-images.githubusercontent.com/94234511/165018049-358243a4-57de-406c-9a6d-9bc33f6c83cd.png)

[image](https://user-images.githubusercontent.com/94234511/165017873-0e6f772a-99c2-4bb1-b92c-dc0b89dc1e8d.png)
Predictive Accuracy = 0.41 
F1 Score = 0.41

#### RFM - 3 Features
Resources/US_Salary_Preprocessed_new_regions.csv"
Training Data Shape = 33,542 rows, 3 columns
Test Data Shape  = 11,181 rows, 3 columns
![image](https://user-images.githubusercontent.com/94234511/165018007-b5dc4247-cf21-4369-afbd-f0cf9165ea16.png)
Predictive Accuracy = 0.391
F1 Score = 0.39!

### Database Connection 
- We envision two possible ways to populate the data in our web table:
    - Connect our web table to the python machine learning model and directly run the model each time a user enters search terms
    - Create a large table to input into the machine learning model which will incorporate all possible permutations of input, use the machine learning model to predict salaries for each potential query, and combine the input plus the salary predictions into a large table that is static and searched each time the user enters search terms.
    - ![image](https://user-images.githubusercontent.com/94234511/165018712-c916da49-3c1d-46ce-9721-588e4cae3041.png)

