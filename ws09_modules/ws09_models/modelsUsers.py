from .modelsBase import Base, sess
from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, \
    Date, Boolean
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime
from flask_login import UserMixin
from .config import config
import os


def default_username(context):
    return context.get_current_parameters()['email'].split('@')[0]


class Users(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    email = Column(Text, unique = True, nullable = False)
    password = Column(Text, nullable = False)
    username = Column(Text, default=default_username)
    lat = Column(Float(precision=4, decimal_return_scale=None))
    lon = Column(Float(precision=4, decimal_return_scale=None))
    share = Column(Text)
    notes = Column(Text)
    post_blog_permission = Column(Boolean, default=True)
    post_news_permission = Column(Boolean, default=False)
    comment_blog_permission = Column(Boolean, default=True)
    comment_news_permission = Column(Boolean, default=True)
    admin_blog_permission = Column(Boolean, default=False)
    admin_news_permission = Column(Boolean, default=False)
    admin_users_permission = Column(Boolean, default=False)
    guest_account = Column(Boolean, default=False)
    guest_account_mirror = Column(Boolean, default=False)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)
    oura_token_id = relationship("Oura_token", backref="oura_token_id", lazy=True)
    oura_sleep = relationship('Oura_sleep_descriptions', backref='oura_sleep', lazy=True)
    loc_day = relationship('User_location_day', backref='user_loc_day', lazy=True)
    user_notes_ref = relationship('User_notes', backref='user_notes_ref', lazy=True)
    community_posts = relationship('communityposts', backref='community_posts', lazy=True)
    community_comments = relationship('communitycomments', backref='community_comments', lazy=True)
    news_posts = relationship('newsposts', backref='news_posts', lazy=True)
    news_comments = relationship('newscomments', backref='news_comments', lazy=True)


    def get_reset_token(self, expires_sec=1800):
        s=Serializer(config.SECRET_KEY, expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s=Serializer(config.SECRET_KEY)
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return sess.query(Users).get(user_id)

    def __repr__(self):
        return f'Users(id: {self.id}, email: {self.email}, share: {self.share},' \
        f'post_news_permission: {self.post_news_permission})'


class communityposts(Base):
    __tablename__ = 'communityposts'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id_name_string = Column(Text)
    title = Column(Text)
    description = Column(Text)
    date_published = Column(DateTime, nullable=False, default=datetime.now)
    edited = Column(Text)
    post_html_filename = Column(Text)
    notes = Column(Text)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)
    comments = relationship('communitycomments', backref='comments', lazy=True)

    def __repr__(self):
        return f'communityposts(id: {self.id}, user_id: {self.user_id}, title: {self.title})'


class communitycomments(Base):
    __tablename__ = 'communitycomments'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("communityposts.id"), nullable=False)
    comment = Column(Text)
    date_published = Column(DateTime, nullable=False, default=datetime.now)
    edited = Column(Text)
    post_html_filename = Column(Text)
    notes = Column(Text)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return f'communitycomments(id: {self.id}, user_id: {self.user_id}, date_published: {self.date_published})'


class newsposts(Base):
    __tablename__ = 'newsposts'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id_name_string = Column(Text)
    title = Column(Text)
    description = Column(Text)
    date_published = Column(DateTime, nullable=False, default=datetime.now)
    edited = Column(Text)
    post_html_filename = Column(Text)
    notes = Column(Text)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)
    comments = relationship('newscomments', backref='comments', lazy=True)

    def __repr__(self):
        return f'newsposts(id: {self.id}, user_id: {self.user_id}, title: {self.title})'


class newscomments(Base):
    __tablename__ = 'newscomments'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("newsposts.id"), nullable=False)
    comment = Column(Text)
    date_published = Column(DateTime, nullable=False, default=datetime.now)
    edited = Column(Text)
    post_html_filename = Column(Text)
    notes = Column(Text)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return f'newscomments(id: {self.id}, user_id: {self.user_id}, date_published: {self.date_published})'


class User_notes(Base):
    __tablename__ = 'user_notes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    datetime_of_note=Column(DateTime)
    note_title = Column(Text) #walking, running, empty is ok for something like mood
    note_details = Column(Text)
    source_name=Column(Text)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return f"User_notes({self.id},datetime_of_note:{self.datetime_of_note}," \
        f"note_title: {self.note_title}, note_details: {self.note_details}," \
        f"time_stamp_utc: {self.time_stamp_utc})"