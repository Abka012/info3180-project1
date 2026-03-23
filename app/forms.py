from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import (
    DecimalField,
    IntegerField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import DataRequired, Length, NumberRange


class PropertyForm(FlaskForm):
    title = StringField("Property Title", validators=[DataRequired(), Length(max=255)])
    description = TextAreaField(
        "Description", validators=[DataRequired(), Length(max=2000)]
    )
    bedrooms = IntegerField(
        "No. of Rooms", validators=[DataRequired(), NumberRange(min=1)]
    )
    bathrooms = DecimalField(
        "No. of Bathrooms", validators=[DataRequired(), NumberRange(min=0)], places=1
    )
    price = IntegerField("Price", validators=[DataRequired(), NumberRange(min=1)])
    property_type = SelectField(
        "Property Type",
        choices=[("House", "House"), ("Apartment", "Apartment")],
        validators=[DataRequired()],
    )
    location = StringField("Location", validators=[DataRequired(), Length(max=255)])
    photo = FileField(
        "Photo",
        validators=[
            FileRequired(),
            FileAllowed(["jpg", "jpeg", "png", "gif"], "Images only!"),
        ],
    )
    submit = SubmitField("Add Property")
