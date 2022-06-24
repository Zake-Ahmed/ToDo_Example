from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,BoleanField

class ToDosF(FlaskForm):
    task = StringField("Task")
    completed = BoleanField("Completed")

    submit = SubmitField("Submit")