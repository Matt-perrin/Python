##This document will present my answers to the StrataScratch python pandas easy level interview questions. 

#LinkedIn ID:10308
#Question: Calculates the difference between the highest salaries in the marketing and engineering departments. Output just the absolute difference in salaries.

    db_employee.head()
    db_dept.head()
    # department id for engineering is 1, marketing is 4
    # Highest salaries in marketing and enginerring. absolue difference in salaries
    Engineers = db_employee[db_employee['department_id'] ==1]
    Engieers_highest = Engineers['salary'].max()
    Marketers = db_employee[db_employee['department_id'] ==4]
    Marketing_highest = Marketers['salary'].max()
    Difference = abs(Marketing_highest - Engieers_highest)

#Microsoft ID:10299
#Question: We have a table with employees and their salaries, however, some of the records are old and contain outdated salary information. Find the current salary of each employee assuming that salaries increase each year. Output their id, first name, last name, department ID, and current salary. Order your list by employee ID in ascending order.

    ms_employee_salary.head()
    df = ms_employee_salary
    # Find currenct salary, output id, first name, last name, deparment id, and current salary. Order list by employee id in asc
    Filtered = df.groupby('id').max()
    Salaries = Filtered.sort_values(by=['id'], ascending=True).reset_index()
    Salaries = Salaries[['id', 'first_name', 'last_name', 'department_id', 'salary']]

#DoorDash ID:10176
#Question: Find the last time each bike was in use. Output both the bike number and the date-timestamp of the bike's last use (i.e., the date-time the bike was returned). Order the results by bikes that were most recently used.

    dc_bikeshare_q1_2012
    dc_bikes = dc_bikeshare_q1_2012

    Bikes = dc_bikes.groupby(by='bike_number').max()
    Sorting = Bikes.sort_values(by='end_time', ascending=False).reset_index()
    df = Sorting[Sorting['end_time'] <= Sorting['end_time'].max()]
    df = df[['bike_number', 'end_time']]
    df

#Meta ID:10087
#Question: Find all posts which were reacted to with a heart. For such posts output all columns from facebook_posts table.

facebook_reactions.head()
reactions = facebook_reactions
posts = facebook_posts

hearts = reactions[reactions['reaction'] == 'heart']
df = pd.merge(hearts, posts, on='post_id', how='inner')
df = df[['post_id', 'poster_y', 'post_text', 'post_keywords', 'post_date']].head(1)

#Meta ID:10061
#Question: Meta/Facebook has developed a new programing language called Hack.To measure the popularity of Hack they ran a survey with their employees. The survey included data on previous programing familiarity as well as the number of years of experience, age, gender and most importantly satisfaction with Hack. Due to an error location data was not collected, but your supervisor demands a report showing average popularity of Hack by office location. Luckily the user IDs of employees completing the surveys were stored. Based on the above, find the average popularity of the Hack per office location. Output the location along with the average popularity.

    facebook_employees
    employees = facebook_employees
    survey = facebook_hack_survey
    #show average based popularity based on office location, output location along with avg popularity

    df = pd.merge(employees, survey,how='outer', left_on='id', right_on='employee_id')
    mean_popularity = df.groupby('location')['popularity'].mean().reset_index()

#Lyft ID:10003
#QUestion: Find all Lyft drivers who earn either equal to or less than 30k USD or equal to or more than 70k USD. Output all details related to retrieved records.

lyft_drivers.head()
drivers = lyft_drivers

salaries = drivers[(drivers['yearly_salary'] <= 30000) | (df['yearly_salary'] >= 70000)]

#Spotify ID:9992
#Question: Find how many times each artist appeared on the Spotify ranking list. Output the artist name along with the corresponding number of occurrences. Order records by the number of occurrences in descending order.

spotify_worldwide_daily_song_ranking.head()
df = spotify_worldwide_daily_song_ranking
List = df['artist'].value_counts().reset_index()

#City of San Francisco ID:9972
#Question: Find the base pay for Police Captains. Output the employee name along with the corresponding base pay.

sf_public_salaries.head()
df = sf_public_salaries

result =sf_public_salaries[(sf_public_salaries['jobtitle'].str.contains('CAPTAIN', case = False))&(sf_public_salaries['jobtitle'].str.contains('POLICE', case = False))][['employeename','basepay']]

#City of San Francisco ID:9924
#Question: Find libraries who haven't provided the email address in circulation year 2016 but their notice preference definition is set to email. Output the library code.

library_usage.head()
df = library_usage

Libraries = df[df['provided_email_address'] ==False]
Preference = Libraries[Libraries['notice_preference_definition'] =='email']
Code = Preference[Preference['circulation_active_year'] ==2016]
Code[['home_library_code']].drop_duplicates()

#Glassdoor ID:9917
#Question: Compare each employee's salary with the average salary of the corresponding department. Output the department, first name, and salary of employees along with the average salary of that department.

employee.head()
df = employee

df['averages'] = df.groupby('department')['salary'].transform('mean')
df[['department', 'first_name', 'salary', 'averages']]

#Apple ID:9891
#Question: Find the details of each customer regardless of whether the customer made an order. Output the customer's first name, last name, and the city along with the order details. Sort records based on the customer's first name and the order details in ascending order.

customers.head()
customers
orders

df = customers.merge(orders, left_on='id', right_on='cust_id', how='outer')
df = df[['first_name', 'last_name', 'city', 'order_details']]
df = df.sort_values(by=['first_name', 'order_details'], ascending=True)

#Amazon ID:9847
#Question: Find the number of workers by department who joined in or after April.Output the department name along with the corresponding number of workers.Sort records based on the number of workers in descending order.

worker.head()
worker

df = worker[worker['joining_date'].dt.month >=4]
counts = df.groupby('department')['worker_id'].count().reset_index(name='count')
department = counts.sort_values(by='count', ascending=False)

#Microsfot ID:9845
#Question: Find the number of employees working in the Admin department that joined in April or later.

worker.head()

admin = worker[worker['department'] == 'Admin']
count = admin[admin['joining_date'].dt.month >= 4]
len(count)

#City of L.A. ID:9688
#Question: Find the activity date and the pe_description of facilities with the name 'STREET CHURROS' and with a score of less than 95 points.

los_angeles_restaurant_health_inspections.head()
df = los_angeles_restaurant_health_inspections

Facilities = df[(df['facility_name'] == 'STREET CHURROS') & (df['score'] <95)]
Facilities[['activity_date', 'pe_description']]

#Forbes ID:9663
#Question: Find the most profitable company from the financial sector. Output the result along with the continent.

forbes_global_2010_2014.head()
df = forbes_global_2010_2014

Sector = df[df['sector'] =='Financials']
Sorted = Sector.sort_values(by=['profits'], ascending=False).head(1)
Sorted[['company', 'continent']]

#Apple ID:9653
#Question: Count the number of user events performed by MacBookPro users. Output the result along with the event name. Sort the result based on the event count in the descending order.

playbook_events.head()
df = playbook_events

MacBook = df[df['device'] == 'macbook pro']
Users = MacBook['event_name'].value_counts().reset_index()

#AirBnB ID:9622
#Question: Find the average number of bathrooms and bedrooms for each city’s property types. Output the result along with the city name and the property type.

airbnb_search_details.head()

result = airbnb_search_details.groupby(['city','property_type'])['bedrooms','bathrooms'].mean().reset_index().rename(index=str, columns={"bedrooms": "n_bedrooms_avg", "bathrooms": "n_bathrooms_avg"})

#Meta ID:2119
#Question: You have been asked to find the 5 most lucrative products in terms of total revenue for the first half of 2022 (from January to June inclusive). Output their IDs and the total revenue.

online_orders.head()
Sales = online_orders

Months = Sales[Sales['date'].dt.month.isin(range(1,7))]
Months['Total'] = Months['units_sold'] * Months['cost_in_dollars']
dfe = Months.groupby(['product_id'], as_index=False).sum()
Totals = dfe.sort_values(['Total'], ascending=False).head(5)
Totals[['product_id', 'Total']]

#Amazon ID:2056
#Question: Write a query that will calculate the number of shipments per month. The unique key for one shipment is a combination of shipment_id and sub_id. Output the year_month in format YYYY-MM and the number of shipments in that month.

amazon_shipment.head()

amazon_shipment['year_month'] = pd.to_datetime(amazon_shipment.shipment_date).dt.to_period('M')
amazon_shipment['unique_key'] = amazon_shipment['shipment_id'].astype(str) + '_' + amazon_shipment['sub_id'].astype(str)
result = amazon_shipment.groupby('year_month')['unique_key'].nunique().to_frame('count').reset_index()

#Apple ID:2024
#Question: Write a query that returns the number of unique users per client per month

fact_events.head()

result = fact_events.groupby([fact_events['client_id'], fact_events['time_id'].dt.month])['user_id'].nunique().reset_index()

#AirBnB ID:10166
#Question: Find how many reviews exist for each review score given to 'Hotel Arena'. Output the hotel name ('Hotel Arena'), each review score, and the number of reviews for that score. Ensure the results only include 'Hotel Arena.'

hotel_reviews.head()
df = hotel_reviews

# number of rows for each review score earned by "Hotel Arena", output name, score, corresponding number of rows
Hotel = df[df['hotel_name'] == 'Hotel Arena']
results = Hotel.groupby(['hotel_name', 'reviewer_score']).size().reset_index(name='count')

#Google ID:10128
#Question:Count the number of movies that Abigail Breslin was nominated for an oscar.

import pandas as pd
import numpy as np

oscar_nominees.head()
df = oscar_nominees

nominee = df[df['nominee'] == 'Abigail Breslin']
results =nominee.movie.nunique()

#Amazon ID:9913
#Question: Find order details made by Jill and Eva. Consider the Jill and Eva as first names of customers. Output the order date, details and cost along with the first name. Order records based on the customer id in ascending order.

import pandas as pd
import numpy as np

merge = pd.merge(customers, orders, left_on="id", right_on="cust_id")
cust = ["Jill", "Eva"]
result = merge[merge["first_name"].isin(cust)][
    ["first_name", "order_date", "order_details", "total_order_cost"]
]