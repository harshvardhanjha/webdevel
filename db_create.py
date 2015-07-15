from project import db
from project.models import BlogPost

#create the database and the db tables
db.create_all()

#insert
db.session.add(BlogPost("Great Scott!!", "Back to the future"))
db.session.add(BlogPost("Time travel", "Time has a direction"))
db.session.add(BlogPost("postgres", "local postgres"))
db.session.add(BlogPost("Check", "Is this working"))

#commit the changes
db.session.commit()