from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from orm_base import Base

class CopyKey(Base):
    __tablename__ = "copy_keys"
    id = Column('id', Integer, Identity(start=1, cycle=True),
                       nullable=False, primary_key=True)
    issuedDate = Column("issued_date", Date, nullable=False)
    issuedTime = Column("issued_time", Time, nullable=False)
    hooks_id = Column(Intger, ForeignKey('hooks.hooks_id'), nullable=False)
    is_loss = ('is_loss', Boolean, primary_key=True, nullable=False)
    
    def __init__(self, keyNumber: Integer, issuedDate: Date, issuedTime: Time, hook, is_loss: Boolean):
        self.id = id
        self.issuedDate = issuedDate
        self.issuedTime = issuedTime
        self.hooks_id = hook.hooks_id
        self.is_loss = is_loss
