Title: Find the right University and Program with a Keyword


Purpose: 
    The Purpose of this app is for students who are looking to continue higher education. This app gives students a chance to explore Universities they are looking to attend and make sure the research topics they are inerested in are well focused on at that univeristy. Alternatively, a student can see how many faculty members are related to that keyword giving the student more affirmation that the keyword at hand is being focused on or not. Students can even do a deeper dive and find the best faculty member for their keyword of interest based on the faculty member's relevance to the keyword (score). This gives students the oppurtunity to not only find which universities are focusing most on what research topics but also which faculty memeber is the best to contact in order to get more information or research oppurtunities. Once a student has decided that a univeristy can be a good fit, they can save that university into their favorites list to monitor for later. Additonally, if a student wants to know more about a faculty member, he or she can explore all the publciations that professor has ever been apart of. We added this feature because we want students to be able to do some research of a facutly member's past work before contacting them about an oppurtunity. Discussing and asking questions about a professors previous reserach will give a student a better chance of getting that oppurtunity and most importantly gives the student an idea of what kind of research he or she could potentially be doing. Finally, if a student believes that the work being done by a faculty member is worth while, they can save that faculty memeber into a list. This list can be updated by either adding or deleting entries. Overall, a student can explore univeristies and faculty using a keyword of interest to find the right fit for their higher educaton goals. 
 - widget 1 (Neo4j): A student can enter a unvierstiy and see the top 10 keywords by relevancy to that university. This helps students who are trying to either explore univerisites or finalize a university based on their keyword of interest. They can check if the school they want to apply for focuses on their topic.
 - widget 2 (Mongodb): A student can enter a university and keyword and find the faculty memeber with the highest relvance to the keyword. 
 - widget 3 (Mongo and mySql): A student can update a list of their favorite universities.
 - widget 4 (mySQL): The user can enter a faculty member and browse through the publication made by the faculty member.
 - widget 5 (mySQL): The user can enter a keyword and see top 5 universities that have most publication base of the keyword 
 - widget 6 (mySQL): The user can update list of favorite faculty member


Installation: In order to install this app, a few packages will be needed in order to connect the app to the database using pip
 - pip install pymsql 
 - pip install pymongo 
 - pip install neo4j
 - Also, will need two mysql tables called favorite_univeristy and favorite_faculty to save a list of universities and facultyrespectively
 and also a store procedure called get_faculty to get faculty member's name. 


Usage: Once the app is running, you can click the link that is produced and it will take you to the app UI, here you just fill out the information you want to explore.


Design: we used a style.css sheet to make the UI more friendly to students, Also we designed the app so that the first three digits going horozontally, are related to a keyword and a University, while the bottom three are related to a keyword and a faculty. We have this style of organization because each student is different. While some value the prestiouge of the school and might want to explore the university first, others value the knowlege of the faculty memeber and explore facutly first. Either way this organization makes it easier for students to explore what they value. The style.css sheet is used to alter the size of the boxes to be uniform to one another as well as adding some color to the widgets and titles. style sheet is inside folder assets.


Implementation: 
- dash ploty to connect back end to front end
- html for front end
- python packages for each database.


Database Techniques:
 - constraints are being used in widget 3 where students are able to save and delete their favorite universities.    When a student is saving a university, he or she can only save entries that have the words "university", "college", or "Institute". This means students can only save universities to the database. Additionally, that same database only takes unique values.
- Stored Procedure to avoid typing long query in the app we created a stored procedure and just call it within the app
- Indexing to acces data faster in the database 


Extra Notes:
- For widget 3 we are using two databases. We use neo4j databse to query university names from a users search while storing the users input to a mysql database. We do this for multiple reasons. Firstly, we wanted the app to be interactive and helpful to the student, so we decided to showcase the universities immeditaley after entry. This way a user does not need to click another button or widget to acces his or her saved info. In order to do this with minimal overhead, we wanted to be able to recieve and save in two different places rather than saving to a databsae and querying again from that database. This minimizes overhead for first time users as they do not need to wait for their database to populate before viewing. Secondly, as the developes and students of data we wanted to have access to a seperate table that tells us which universities students are chosing as their favorites and when. The mysql table that stores the data also has timestamps. Having the seperate table allows us to do more analytical research on this topic as well as join this table with other tables in our database for more insight. 


Contributions: Thimira did first 3 widgets and Gabin did last 3 widgets. Thimira did front end and one database Technique. Gabin did two database techniques. We divded the work equally. 


Demo: https://www.youtube.com/watch?v=fl7YW_H5Tqc&ab_channel=thimirabandara
