# Capstone-Project
Group project at end of boot camp
Martha, Lucien and Cheryl

### GitHub:
-	Your Main Branch has a ReadMe file 
    -	you're reading it!
-	Your ReadMe file includes a description for how your team plans to communicate for the project
    - Communication plan: use Slack to chat between meetings, meet up during class and office hours to work and plan together, plan additional meetings via zoom as needed
-	You have individual branches setup for each of your team members:
    - Cheryl has the Cheryl branch
    - Lucien has the dummy_database branch
    - Martha has the presentation branch, also some data investigation stuff is in there
-	Each team member has at least four commits from the duration of the first segment

### Presentation:
-	Include your choice of a PowerPoint, Word Document, ReadMe file, etc. with the following information
    - the project is described in detail in this README
    - the PowerPoint file intro_presentation.pptx gives a more sophisticated and slightly less detailed overview/presentation of our project

### Topic: 
Data Science and STEM Salaries from June 7, 2017 to August 17, 2021
  https://www.kaggle.com/datasets/jackogozaly/data-science-and-stem-salaries

- Description of your data source (feel free to include a sample of it too)
    - The Kaggle description of the data says, "62,000 salary records from top companies. This data was scraped off levels.fyi." 
![pic of kaggle data source](https://github.com/mgsrichard/Capstone-Project/blob/main/resources/Kaggle_data_source.png)

- Reason: 
  We found the data source relevant to our current career interests.  In addition,the dataset was appropriately dimensioned and did not have a lot of missing data.  Datatypes varied across the columns and there are several features that can be used to for modeling.  

### Question we hope to answer with this data: 

- What features does this data contain and how many rows of data are included?  How many years? How many professions? Employers?
- What are the average salaries for each profession?  Is there any relationship between the annual base salary and the complete compensation package? 
- Is there a difference in average salaries by employer? By gender? By location? Years of experience?  Are these differences significant?
- What features should be used to predict the annual and/or complete compensation when linear regression is applied?  
- We would like to predict the annual base salary and/or complete compensation for new hires based on input of the applicable features? 
- What features can be used to give a model that predicts accuracy to at least 75% with an ultimate goal of 90% for the final model?

### Database
-	Present a provisional database that stands in for the final database
    #### Preliminary schema for bringing in our data: <br>
    ![schema image](https://github.com/mgsrichard/Capstone-Project/blob/main/resources/Schema.png)
 
- Plan to investigate and clean the original data fields
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
Maybe keep. Investigate. Seems to be 0 for international rows, so could possibly be used as a proxy for interenational.

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
    - we will connect python to PostgresSQL/pgAdmin and output cleaned data and machine learning results to PostgreSQL/pgAdmin. Here are some examples of code from the Movies-ETL challenge where we connected python to a PostgreSQL/pgAdmin database. 
        ![python to sql 1](https://github.com/mgsrichard/Capstone-Project/blob/main/resources/python_to_sql_1.png)
        ![python to sql 2](https://github.com/mgsrichard/Capstone-Project/blob/main/resources/python_to_sql_2.png)
        ![python to sql 3](https://github.com/mgsrichard/Capstone-Project/blob/main/resources/python_to_sql_3.png)


### Machine Learning Model
-	Present a provisional machine learning model
![supervised learning picture](https://github.com/mgsrichard/Capstone-Project/blob/main/resources/supervised-learning.png)
    - We propose to use the LinearRegression model from Scikit-learn to create a supervised linear regression machine learning model and our input data to predict salaries for data scientists and STEM professionals. The example from module 17.2.3 shown below is a good starting place for our coding.	
     ![image](https://user-images.githubusercontent.com/94234511/162580102-7f2c75fb-5c78-4d70-853c-138aeee1347b.png)
- Regression is used to predict continuous variables. The regression model's algorithms would attempt to learn patterns that exist among these factors. When presented with the data for a new row(index), the model would make a prediction of the output, based on previously learned patterns from the dataset. While the example from the module only uses one feature, years of service, to predict  salaries, the model is also able to take in multiple features to do a multiple regression.  
- In both classification and regression problems, the dataset is divided into features and target. Features are the variables used to make a prediction. Target is the predicted outcome. The target in our data will be the final total salary field (after we clean up the data) and the other fields will be our features. 
- We intend to use trial and error with different linear regression models and data columns to make the most accurate model possible. We are aiming for a model that is at least 75% accurate. We may use the LinearRegression model, but we have also glanced through the Scikit-learn documentation and seen that there are some variations of linear regression, including Lasso and Elastic-Net that are also available to try. Some of these other models also seem to help in deciding how to narrow which features are most important to the model, so that could be helpful.
- Once we have fitted and trained our model and reached our 75% accuracy threshold, we will then create a way to present our results. We would like to create an interactive web table as we did in the UFO and Bellybutton challenges where the user can enter data (years of experience, job title, location, etc.) and get an estimated salary or salary range as an output. (A salary range could be created using the salary prediction and our accuracy percentage, for example, a prediction of 100,000 at 75% accuracy would translate to a salary range of 75,000 to 125,000). We envision two possible ways to populate the data in our web table:
    - Connect our web table to the python machine learning model and directly run the model each time a user enters search terms
    - Create a large table to input into the machine learning model which will incorporate all possible permutations of input, use the machine learning model to predict salaries for each potential query, and combine the input plus the salary predictions into a large table that is static and searched each time the user enters search terms.
