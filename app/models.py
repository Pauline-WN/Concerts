from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    hometown = Column(String)

    concerts = relationship("Concert", back_populates="band")

    def get_concerts(self):
        return self.concerts

    def venues(self):
        return list({concert.venue for concert in self.concerts})

    def play_in_venue(self, venue, date):
        concert = Concert(date=date, band=self, venue=venue)
        return concert

    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts]

    @classmethod
    def most_performances(cls, session):
        from sqlalchemy import func
        return session.query(cls).join(Concert).group_by(cls.id).order_by(func.count(Concert.id).desc()).first()


class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    city = Column(String)

    concerts = relationship("Concert", back_populates="venue")

    def get_concerts(self):
        return self.concerts

    def bands(self):
        return list({concert.band for concert in self.concerts})

    def concert_on(self, date):
        return next((concert for concert in self.concerts if concert.date == date), None)

    def most_frequent_band(self):
        from collections import Counter
        band_count = Counter(concert.band for concert in self.concerts)
        return band_count.most_common(1)[0][0] if band_count else None


class Concert(Base):
    __tablename__ = 'concerts'

    id = Column(Integer, primary_key=True)
    date = Column(String)
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))

    band = relationship("Band", back_populates="concerts")
    venue = relationship("Venue", back_populates="concerts")

    def get_band(self):
        return self.band

    def get_venue(self):
        return self.venue

    def hometown_show(self):
        return self.venue.city == self.band.hometown

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
