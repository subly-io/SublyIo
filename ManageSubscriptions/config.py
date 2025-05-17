import os
class Config:
    SECRET_KEY = 'd387cdf8665539634137a282f049f3df476e462f51265c2742ece552ebfb35a9'
    SQLALCHEMY_DATABASE_URI = "sqlite:///clients.db"
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'itsubly@gmail.com'
    MAIL_PASSWORD = 'aeikwdyxnsozvvap'
    SCHEDULER_API_ENABLED = True
    SCHEDULER_TIMEZONE = 'Asia/Amman'