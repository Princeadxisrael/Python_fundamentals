
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
import uuid

def generate_uuid():
    return str(uuid.uuid4())

Base=declarative_base()

class User(Base):
    __tablename__="users"

    UserID=Column("userID", String, primary_key=True, default=generate_uuid)
    firstName= Column("firstName", String)
    lastName= Column("lastName", String)
    profileName= Column("profileName", String)
    email= Column("email", String)

    def __init__(self, firstName, lastName, profileName, email):
        self.firstName=firstName
        self.lastName=lastName
        self.profileName=profileName
        self.email=email


class Post(Base):
    __tablename__="posts"
    postID= Column("postID", String, primary_key=True, default=generate_uuid)
    userID= Column("userID", String, ForeignKey('users.userID'))
    postContent=Column("postContent", String)

    def __init__(self, userID, postContent):
        self.userID=userID
        self.postContent=postContent

class Like(Base):
    __tablename__="likes"
    likeID=Column("likeID", String, primary_key=True, default=generate_uuid)
    userID=Column("userID", String, ForeignKey('users.userID'))
    postID=Column("postID", String, ForeignKey('posts.postID'))

    def __init__(self, userID, postID):
        self.userID=userID
        self.postID=postID

#Create new user
def add_user(firstname, lastname, profilename, email, session):
    check_if_exist=session.query(User).filter(User.email==email).all()
    if len(check_if_exist)>0:
        print("User already exist. Please use another email")
    else:
        user=User(firstname, lastname, profilename, email) 
        session.add(user)
        session.commit()
        print("user added succesfully")


def add_post(userid, post, session):
    newpost=Post(userid, post)
    session.add(newpost)
    session.commit()
    print("post added successfully")

def add_like(userid, postid, session):
    like=Like(userid, postid)
    session.add(like)
    session.commit()
    print("like added")


db="sqlite:///socialDb.db"
engine=create_engine(db)
Base.metadata.create_all(bind=engine)

Session=sessionmaker(bind=engine)
session=Session()




# firstname="Salmome"
# lastname="Amere"
# profilename="salome33"
# email="amere.salome@yahoo.com"

# add_user(firstname, lastname, profilename, email,session)


#Create new post
# userid="a926d95d-497d-4a91-a295-f47af4740a1f"
# newpost="Happy birthday Hannington. Wishing you the best"
# post1=Post(userid, newpost)

# add_post(userid, newpost, session)

#create new like
userid="568dbfd5-13ef-454f-a5a5-00494757e442"
postid="5f7dd64c-daa2-4549-95fd-586b3433fac6"

# add_like(userid, postid, session)

post_likes=session.query(Like).filter(Like.postID==postid).all()
print(len(post_likes))

users_liked_posts=session.query(User, Like).filter(Like.postID==postid).filter(Like.userID==User.UserID)
for user in users_liked_posts:
    print(user["User"].firstName, user["User"].lastName)
























#Tables and map to the classes

# class User(Base):
#     __tablename__='users'

#     id=Column(Integer, primary_key=True)
#     name=Column(String(50))
#     fullname=Column(String(50))
#     nickname=Column(String(50))

#     def __repr__(self):
#         return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)


# class Address(Base):
#     __tablename__="addresses"
#     id=Column(Integer, primary_key=True)
#     email_address=Column(String, nullable=False)
#     user_id=Column(Integer, ForeignKey('users.id'))

#     user=relationship("User", back_populates="addresses")

#     def __repr__(self):
#         return "<Address(email_address='%s')>" % (self.email_address)


# User.addresses=relationship(
#     "Address", order_by=Address.id, back_populates="user"
# )


# if __name__=='__main__':
#     engine=create_engine('sqlite:///users.db', echo=True) 
#     Base.metadata.create_all(engine)
#     #Creating a session
#     Session=sessionmaker(bind=engine) #defining a session class
#     session=Session() #Define a session object
    
#     #Creating records
#     john_horton=User(name='john', fullname="John horton", nickname="joHort")
#     wendy_siguel=User(name='weddy', fullname="Weddy Siguel", nickname="Wedi")
#     john_welsh=User(name='john', fullname="John Welsh", nickname="joWel")
#     simon_kagna=User(name='simon', fullname="simon kagna", nickname="simon")
#     # session.add_all([john_horton, wendy_siguel, john_welsh])
#     # print(session.new)
   

#     simon_kagna.addresses=[
#         Address(email_address='simon@google.com'),
#         Address(email_address='simonk@yahoo.com')
#     ]

#     simon=session.query(User).filter_by(name="simon").one()
    
#     # print(simon.addresses)

#     # for u, a in session.query(User, Address).\
#     #         filter(User.id==Address.user_id).\
#     #         filter(Address.email_address=='simonk@yahoo.com').\
#     #         all():
#     #     print(u)
#     #     print(a)

#     query=session.query(User).join(Address).filter(Address.email_address=='simonk@yahoo.com').all()
#     print(query)
#     # session.add(simon_kagna)
#     session.commit()

