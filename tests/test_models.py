import unittest
from app.models import Band, Venue, Concert
from app.database import SessionLocal, engine, Base

class TestModels(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base.metadata.create_all(bind=engine)
        cls.session = SessionLocal()

    def test_create_band(self):
        band = Band(name='Band Name', hometown='Hometown')
        self.session.add(band)
        self.session.commit()
        self.assertIsNotNone(band.id)

    def test_create_venue(self):
        venue = Venue(title='Venue Title', city='City Name')
        self.session.add(venue)
        self.session.commit()
        self.assertIsNotNone(venue.id)

    def test_create_concert(self):
        band = Band(name='Test Band', hometown='Test City')
        venue = Venue(title='Test Venue', city='Test City')
        concert = Concert(date="2024-09-22", band=band, venue=venue)
        self.session.add_all([band, venue, concert])
        self.session.commit()
        self.assertIsNotNone(concert.id)

    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(bind=engine)

if __name__ == '__main__':
    unittest.main()
