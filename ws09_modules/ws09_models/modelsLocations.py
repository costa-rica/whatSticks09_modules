from .modelsBase import Base
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, \
    Date
from datetime import datetime
from sqlalchemy.orm import relationship


class User_location_day(Base):
    __tablename__ = 'user_location_day'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    location_id = Column(Integer, nullable = False)#TODO: should this remain nullable=False?
    date = Column(Text)
    local_time = Column(Text)
    row_type = Column(Text)#user entered or scheduler entered row?
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return f'User_location_day(id: {self.id}, user_id: {self.user_id},' \
            f'date: {self.date})'


class Locations(Base):
    __tablename__ = 'locations'
    id = Column(Integer,  primary_key = True)
    city = Column(Text)
    region = Column(Text)
    country = Column(Text)
    lat = Column(Float(precision=4, decimal_return_scale=None))
    lon = Column(Float(precision=4, decimal_return_scale=None))
    tz_id = Column(Text)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)
    # oura_sleep = relationship('Oura_sleep_descriptions', backref='oura_sleep', lazy=True)
    weather_hist = relationship('Weather_history', backref = 'weath_hist', lazy = True)

    def __repr__(self):
        return f'Locations(id: {self.id}, city: {self.city}, lat: {self.lat}, ' \
            f'lon: {self.lon})'

class Weather_history(Base):
    __tablename__ = 'weather_history'
    id = Column(Integer, primary_key = True)
    location_id = Column(Integer, ForeignKey('locations.id'), nullable = False)
    date_time = Column(Text)
    datetimeEpoch = Column(Integer)
    tempmax = Column(Float)
    tempmin = Column(Float)
    temp = Column(Float)
    feelslikemax = Column(Float)
    feelslikemin = Column(Float)
    feelslike = Column(Float)
    dew = Column(Text)
    humidity = Column(Text)
    precip = Column(Text)
    precipprob = Column(Text)
    precipcover = Column(Text)
    preciptype = Column(Text)
    snow = Column(Text)
    snowdepth = Column(Text)
    windgust = Column(Text)
    windspeed = Column(Text)
    winddir = Column(Text)
    pressure = Column(Text)
    cloudcover = Column(Text)
    visibility = Column(Text)
    solarradiation = Column(Text)
    solarenergy = Column(Text)
    uvindex = Column(Text)
    sunrise = Column(Text)
    sunriseEpoch = Column(Text)
    sunset = Column(Text)
    sunsetEpoch = Column(Text)
    moonphase = Column(Text)
    conditions = Column(Text)
    description = Column(Text)
    icon = Column(Text)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return f"Weather_history(id: {self.id}, date_time: {self.date_time}, " \
            f"location_id: {self.location_id}, temp: {self.temp})"
