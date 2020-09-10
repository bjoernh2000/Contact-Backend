from mongoengine import Document, UUIDField, DateTimeField
from datetime import timedelta, datetime


class Session(Document):
    sessionID = UUIDField(binary=False, required=True)
    userID = UUIDField(binary=False, required=True)
    dateCreated = DateTimeField(default=datetime.utcnow)
    dateExpires = DateTimeField(
        default=datetime.utcnow() + timedelta(days=30))
