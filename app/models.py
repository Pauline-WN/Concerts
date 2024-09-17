from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app import Base

class Band(Base):
    __tablename__ = 'bands'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    hometown = Column(String)
    
    concerts = relationship("Concert", back_populates="band")

class Venue(Base):
    __tablename__ = 'venues'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    city = Column(String)
    
    concerts = relationship("Concert", back_populates="venue")

class Concert(Base):
    __tablename__ = 'concerts'
    
    id = Column(Integer, primary_key=True, index=True)
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))
    date = Column(String)
    
    band = relationship("Band", back_populates="concerts")
    venue = relationship("Venue", back_populates="concerts")
