from datetime import datetime

from sqlalchemy import Column, Integer, Unicode, Date, func, extract

from src.model import Base, DBSession


class Entry(Base):
    uid = Column(Integer, primary_key=True, index=True)
    user = Column(Unicode, index=True)
    hours = Column(Integer)
    date = Column(Date, default=func.func.current_date())

    __mapper_args__ = {"eager_defaults": True}

    @classmethod
    def by_user(cls, user):
        return DBSession.query(cls).filter_by(user=user).all()

    @classmethod
    def by_user_month(cls, user, month):
        year = datetime.today().year
        return DBSession.query(cls).\
            filter((extract('year', cls.date) == year) & (extract('month', cls.date) == month)).\
            filter_by(user=user).\
            order_by(cls.date).\
            all()

    @classmethod
    def recap(cls, user, month):
        entries = cls.by_user_month(user, month)
        total = sum([e.hours for e in entries])
        days = '\n'.join([f'{e.date.isoformat()}\t\t\t\t{e.hours}' for e in entries])
        return f'Total hours this month: {total}\n\n{days}'
