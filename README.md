# Capstone-Project
Group project at end of boot camp <br>
Martha, Lucien and Cheryl
Updated 05-01-2022

### GitHub:
-	Your Main Branch has a ReadMe file 
    -	You're reading it!
-	Your ReadMe file includes a description for how your team plans to communicate for the project
    - Communication plan: use Slack to chat between meetings, meet up during class and office hours to work and plan together, plan additional meetings via zoom as needed
-	You have individual branches setup for each of your team members:
    - Cheryl has the Cheryl branch
    - Lucien has the dummy_database branch
    - Martha has the main branch
-	Each team member has at least four commits from each segment of the project

### Presentation:
-	Include your choice of a PowerPoint, Word Document, ReadMe file, etc. with the following information
    - The project is described in detail in this README
    - The PowerPoint file https://github.com/mgsrichard/Capstone-Project/blob/main/Segment%203_presentation.pptx a more sophisticated and slightly more detailed overview/presentation of our project
- Here is the agenda for Segment 3 Presentation: 
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

Here is a visual illustration of our project
![image](https://user-images.githubusercontent.com/94234511/166168022-3b57bea0-5c07-4caf-aa3b-1cf2ee33154f.png)

### A Summary of Data Cleaning Steps can be seen below: 
- Reduced noisy data:
    - Checking for usable DataTypes
    - Transform the location column 
    - Performing Outliers Analysis
![image](https://user-images.githubusercontent.com/94234511/165017194-63cfcaa3-a23e-4ab7-8fd1-af33a1cf2c14.png)
![image](https://user-images.githubusercontent.com/94234511/165017211-e74f4ac0-5d85-40c2-b3e9-8dc4e6103c8a.png)

- Other Data Cleaning
    - PERFORM ADDITIONAL Data Cleaning 
0 duplicate columns/rows found in dataset 
Drop 4 unwanted columns 'level’, 'tag’ 'Race’, 'Education'
Identify & Remove null values
gender                     19,540
otherdetails               22,505
Drop 5 rows where company is NaN missing rows (data now has 62,637 rows) 
Convert timestamp field from object to ‘datetime’
Clean-up erroneous data values in location, education and gender columns
The total number of rows with data in the education columns is 30,472
The total number of rows with data in the race columns is 22,426
Identified and corrected additional typographical and formatting errors in the location data

![image](https://user-images.githubusercontent.com/94234511/166168046-cd012dcd-c47b-449b-8705-e9cb90a5fb90.png)


### Feature Engineering

FEATURE ENGINEERING – Salary level
- For rows where basesalary = 0, set equal to totalyearlycompensation 
- Assign a target value from the base salary by bucketing
    - Mean + 2SD = 
    - 149,172 + 2(44,382) = $237,936
    - Max. salary = $350, 000
- Create a function to generate salary levels using salary bands of $25,000 for a total of 15 salary levels


- For rows where basesalary = 0, set equal to totalyearlycompensation 
- Create a target value from the base salary by bucketing
- Mean plus two std dev. would be 149,172 + 44,382 + 44,382 = 237,936
- #Make salary bands of 25,000 for a total of 15 salary levels 


![image](https://user-images.githubusercontent.com/94234511/165017702-7ade3729-a629-4d65-ae82-48ed8e3dd5aa.png)


### Feature Engineering - Regions 
- Look at each metro area and calculate the distances from downtown and include participants within 30-50 miles. 
- Start by naming & retrieving long/lat for each metro area
- Use an openweathermap API call to get the long and lat for each city and state combination
- Create a loc group for each of the top 9 regions
- For each region, calculate the distance from the central metro
- Use this distance to decide who to include in that region, be consistent if it makes sense to
- Avoid geographical overlap any of the identified regions
- Respondents not captured in the top 9 regions are grouped into region 10.
![image](https://user-images.githubusercontent.com/94234511/166168066-02901e7d-4db9-4f2d-805b-0b7f8d9ee008.png)


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

- r = 0.398 

![image](https://user-images.githubusercontent.com/94234511/165017508-9c255d38-b85d-4526-9061-68228697df15.png)

- LINEAR REGRESSION – YEARS AT COMPANY![image](https://user-images.githubusercontent.com/94234511/166168327-4e539645-27c4-4f27-b9f9-33fb43c386cf.png)

![image](https://user-images.githubusercontent.com/94234511/166168321-6467d371-c026-4e64-8c95-e7a1eb891998.png)

Total salary by Years at Company
r= 0.14
Weaker correlation for predictive model
Correlation was not improved when base salary was used as output for either yrs. of exp. or yrs. at company
![image](https://user-images.githubusercontent.com/94234511/166168311-368591bd-0604-4747-8c76-6c1fa4feb6e5.png)

- Provisonal Learing Model Selection 
Evaluate Supervised Learning Model - Ensemble Method - Random Forest Classification
![image](https://user-images.githubusercontent.com/94234511/165017776-2a6ee2cf-6ba0-49a6-8123-514556bedc99.png)

#### RFM - All Features
- Cleaned_Salary_Data.csv
- Training Data Shape (46977 rows, 38 columns)
- Test Data (15660 rows, 38 columns)

[image](https://user-images.githubusercontent.com/94234511/165017873-0e6f772a-99c2-4bb1-b92c-dc0b89dc1e8d.png)

- Predictive Accuracy = 0.41 

![image](https://user-images.githubusercontent.com/94234511/165019015-215f1b6a-e36a-49bf-8830-c6fe4ba4df6d.png)

#### RFM - 3 Features
- Resources/US_Salary_Preprocessed_new_regions.csv
- Training Data Shape = 33,542 rows, 3 columns
- Test Data Shape  = 11,181 rows, 3 columns

![image](https://user-images.githubusercontent.com/94234511/165018007-b5dc4247-cf21-4369-afbd-f0cf9165ea16.png)

- Predictive Accuracy = 0.391

![image](https://user-images.githubusercontent.com/94234511/165018973-6b9fe9ca-8b6b-448c-a00a-361e44b710b7.png)

### Database Connection 
- Export the Model from Python file
- Create Config file (app.py) & Import Model
- Write the function to import the cleaned and preprocessed datafile 
- Create the HTML file and use HERIKO to connect to Tableau Dashboard
 
    - ![image](https://user-images.githubusercontent.com/94234511/165018712-c916da49-3c1d-46ce-9721-588e4cae3041.png)

### Conclusions

#### Data Analysis
- California is the state with the highest average base salary ($161,393)
- Of the 15 tiles reported, Software Engineering Managers earned the highest average salary of $185,658 annually
- 79% of respondents were employed in the top 9 regions. 
- Of 1631 total companies, 35% of the responses were represented by the top 5 employers: Amazon, Apple, Facebook, Google and Microsoft
- Only 36% reported race, of them 52% identified as Asian 
- Only 49% reported Education Level, of them 51% had a Masters Degree

- The gender variable was confusing:
    - 19,540 (31%) respondents did not report gender
    - 35,698 (XX%) of respondents identified as male
    - 
 #### Predictive Model Outcomes 
- The data was noisy, often incomplete for some variables causing some analysis to be impossible.
- Data was clustered in certain geographical areas and needed considerable engineering to be useable.
- The presumed linear relationship between salary and years of experience was not as closely correlated as expected, r=0.39. 
- The model we chose for our salary range prediction tool: 
    - Random Forest Model 
    - Predictive Accuracy is slightly >39%

![image](https://user-images.githubusercontent.com/94234511/166168100-cae31792-a761-4885-abc4-b3d1f36d3cc1.png)

![image](https://user-images.githubusercontent.com/94234511/166168107-cfaab2c8-f95a-4d1f-b4f2-731956df685c.png)

![image](https://user-images.githubusercontent.com/94234511/166168114-d520f4b7-8385-4cfd-8e58-a7ca2110dbcb.png)

![image](https://user-images.githubusercontent.com/94234511/166167679-a7a55213-6a4a-4ad6-ac01-8f5777fa726e.png)


### Discussion
We explored Unsupervised Learning models.  The outcome of the most intersting one is provided below.  See the presentation for additional details.

- Amazon, Facebook, Microsoft, Google, and Apple accounted for 35% of all jobs listed
- The best accuracy for salary prediction used the linear regression model on each company’s data individually, with Microsoft > 60% accuracy
![image](https://user-images.githubusercontent.com/94234511/166168136-9fa0e07a-515b-4f59-9438-ba297436628f.png)

![image](https://user-images.githubusercontent.com/94234511/166168124-98f09a1d-e171-4691-8b30-9364ae7b68e0.png)

