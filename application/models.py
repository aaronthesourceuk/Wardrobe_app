#!/usr/bin/python3

#    models.py

from application import db
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired, NumberRange, Length
from datetime import datetime

class Tops(db.Model):
    Name = db.Column(db.String(30), primary_key=True)
    Description = db.Colum(db.String(300), nullable=False)
    Size = db.Column(db.String(5), nullable=False
    Cost = db.Column(db.String(10), nullable=False
    Purchace_date = db.Column(db.String(30), nullable=False

class Bottoms(db.Model):
    Name = db.Column(db.String(30), primary_key=True)
    Description = db.Colum(db.String(300), nullable=False)
    Size = db.Column(db.String(5), nullable=False
    Cost = db.Column(db.String(10), nullable=False
    Purchace_date = db.Column(db.String(30), nullable=False

class Dresses(db.Model):
    Name = db.Column(db.String(30), primary_key=True)
    Description = db.Colum(db.String(300), nullable=False)
    Size = db.Column(db.String(5), nullable=False
    Cost = db.Column(db.String(10), nullable=False
    Purchace_date = db.Column(db.String(30), nullable=False

class Jumpers(db.Model):
    Name = db.Column(db.String(30), primary_key=True)
    Description = db.Colum(db.String(300), nullable=False)
    Size = db.Column(db.String(5), nullable=False
    Cost = db.Column(db.String(10), nullable=False
    Purchace_date = db.Column(db.String(30), nullable=False

class Shoes(db.Model):
    Name = db.Column(db.String(30), primary_key=True)
    Description = db.Colum(db.String(300), nullable=False)
    Size = db.Column(db.String(5), nullable=False
    Cost = db.Column(db.String(10), nullable=False
    Purchace_date = db.Column(db.String(30), nullable=False

class Bags(db.Model):
    Name = db.Column(db.String(30), primary_key=True)
    Description = db.Colum(db.String(300), nullable=False)
    Size = db.Column(db.String(5), nullable=False
    Cost = db.Column(db.String(10), nullable=False
    Purchace_date = db.Column(db.String(30), nullable=False


class Outfits(db.Model):
    Outfit_name = db.Column(db.String(30), primary_key=True)
    Vibe = db.Colum(db.String(300), nullable=False)
    Top = db.Column(db.String(30), db.ForeignKey('Tops.Name')
    Bottom = db.Column(db.String(30), db.ForeignKey('Bottoms.Name')
    Dress = db.Column(db.String(30), db.ForeignKey('Dresses.Name')
    Jumper = db.Column(db.String(30), db.ForeignKey('Jumpers.Name')
    Shoes = db.Column(db.String(30), db.ForeignKey('Shoes.Name')
    Bag = db.Column(db.String(30), db.ForeignKey('Bags.Name')

class Add(FlaskForm):
    Name = StringField('Name', [Length(min=1, max=300)])
    Description = StringField("Description", [Length(min=1, max=300)])
    Size = StringField("Size", [Length(min=1, max=5)])
    Cost = StringField("Cost"), [Length(min=1, max=10)])
    Purchase_date = DateField('Release date', validators=[DataRequired()])
    submit = SubmitField('Add garment')
