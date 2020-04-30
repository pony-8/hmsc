from sqlalchemy import Column, DateTime, Integer, Numeric, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy
from application import db


# db = SQLAlchemy()


class Goods(db.Model):
    __tablename__ = 'goods'

    id = db.Column(db.Integer, primary_key=True)
    cat_id = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    name = db.Column(db.String(100, 'utf8_general_ci'), nullable=False, server_default=db.FetchedValue())
    price = db.Column(db.Numeric(10, 2), nullable=False, server_default=db.FetchedValue())
    main_image = db.Column(db.String(100, 'utf8_general_ci'), nullable=False, server_default=db.FetchedValue())
    summary = db.Column(db.String(10000, 'utf8_general_ci'), nullable=False, server_default=db.FetchedValue())
    stock = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    tags = db.Column(db.String(200, 'utf8_general_ci'), nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    month_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    total_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    comment_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
