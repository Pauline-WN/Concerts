from app.models import Band, Venue, Concert
from app.database import SessionLocal

def populate_db():
    session = SessionLocal()
    
    # Creating Bands
    band1 = Band(name='Sauti Sol', hometown='Nairobi')
    band2 = Band(name='Nyashinski', hometown='Nairobi')
    
    # Creating Venues
    venue1 = Venue(title='Carnivore Grounds', city='Nairobi')
    venue2 = Venue(title='Mombasa Marine Park', city='Mombasa')
    
    # Adding bands and venues to the session
    session.add(band1)
    session.add(band2)
    session.add(venue1)
    session.add(venue2)
    
    # Committing the session to save bands and venues
    session.commit()
    
    # Creating Concerts
    concert1 = Concert(date='2024-12-01', band_id=band1.id, venue_id=venue1.id)
    concert2 = Concert(date='2024-12-05', band_id=band2.id, venue_id=venue2.id)
    
    # Adding concerts to the session
    session.add(concert1)
    session.add(concert2)
    
    # Committing the session to save concerts
    session.commit()
    
    # Querying all bands
    bands = session.query(Band).all()
    for band in bands:
        print(f"Band: {band.name}, Hometown: {band.hometown}")

    # Querying all concerts
    concerts = session.query(Concert).all()
    for concert in concerts:
        print(f"Concert on {concert.date} with {concert.band.name} at {concert.venue.title}")
    
    session.close()
    print("Database populated with initial data.")

if __name__ == "__main__":
    populate_db()
