from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, DateTime, Date, Float
import datetime

engine = create_engine('sqlite:///quicktimerbot.db', echo=True)

meta = MetaData()

trackeds = Table(
    'trackeds',
    meta,
    Column('id', Integer, primary_key=True),
    Column('start_time', DateTime, default=None),
    Column('stop_time', DateTime, default=None),
    Column('time_worked', Float, default=None),
    Column('task_id', String(255), default=None),
    Column('task_name', String(255)),
    Column('task_description', String(255), default=None),
    Column('date', Date, default=datetime.datetime.utcnow),
    Column('user_id', ForeignKey('users.id')),
)

users = Table(
    'users',
    meta,
    Column('id', Integer, primary_key=True),
    Column('id_telegram', Integer),
    Column('first_name', String(255)),
    Column('last_name', String(255)),
    Column('full_name', String(255)),
    Column('username', String(255)),
    Column('is_bot', String(255)),
    Column('clickup_user_id', String(255)),
    Column('clickup_access_token', String(255)),
)
