import pymongo

# Set up the MongoDB client and connect to the database
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = client["academicworld"]
faculty = db["faculty"]

def widget_2_query(university, keyword):
    # Find the faculty member with the highest score for the keyword
    result = faculty.find({
        "affiliation.name": university,
        "keywords.name": keyword
    }).sort([("keywords.score", pymongo.DESCENDING)]).limit(1)
    
    # Return a dictionary containing the faculty member's name and score for the keyword
    for faculty_member in result:
        return {
            "name": faculty_member["name"],
            "email": faculty_member["email"],
            "phone": faculty_member["phone"],
            "position": faculty_member["position"],
            "photo": faculty_member["photoUrl"]
        }

    return None






