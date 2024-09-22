from sqlalchemy.orm import Session
from .models import Band, Venue, Concert

def create_band(db: Session, name: str, hometown: str):
    band = Band(name=name, hometown=hometown)
    db.add(band)
    db.commit()
    db.refresh(band)
    return band

def create_venue(db: Session, title: str, city: str):
    venue = Venue(title=title, city=city)
    db.add(venue)
    db.commit()
    db.refresh(venue)
    return venue

def create_concert(db: Session, band_id: int, venue_id: int, date: str):
    concert = Concert(band_id=band_id, venue_id=venue_id, date=date)
    db.add(concert)
    db.commit()
    db.refresh(concert)
    return concert
