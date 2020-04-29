# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class MemberComment(db.Model):
    __tablename__ = 'member_comments'

    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, nullable=False, index=True, server_default=db.FetchedValue())
    goods_id = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    pay_order_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    score = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    content = db.Column(db.String(200), nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
