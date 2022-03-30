from sqlalchemy import create_engine, func
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table
from sqlalchemy.orm import sessionmaker, relationship

# Base class for declaring tables
Base = declarative_base()

# association_table = Table('major_school', Base.metadata,
#     Column('school_id', ForeignKey('schools.id')),
#     Column('major_id', ForeignKey('majors.id')),
#     enrollment = Column(Integer,nullable=True )
# )

class Association(Base):
    __tablename__ = 'major_school'
    school_id = Column(Integer, ForeignKey('schools.id'), primary_key=True)
    major_id = Column(Integer, ForeignKey('majors.id'), primary_key=True)
    enrollment = Column(Integer,nullable=True )
    school = relationship("School", back_populates="majors")
    major = relationship("Major", back_populates="schools")

class School(Base):
    __tablename__ = 'schools'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    state = Column(String(50), nullable=True)
    year_founded = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    majors = relationship("Association", back_populates="school")

    def __repr__(self):
        return "<School(name='%s', state='%s', year_founded='%s', created_at='%s')>" % (self.name, self.state, self.year_founded, self.created_at)



class Major(Base):
    __tablename__ = 'majors'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    department = Column(String(128))
    schools = relationship("Association", back_populates="major")

    def __repr__(self):
        return "<Major(major='%s', department='%s')>" % (self.name, self.department)

    #school = relationship("School", back_populates = "majors")




    
    
# User.addresses = relationship("Address", order_by = Address.id, back_populates = "user")
