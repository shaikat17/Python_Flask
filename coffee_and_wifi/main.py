from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, validators
from flask_bootstrap import Bootstrap
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C1sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', [validators.DataRequired()])
    location = StringField("Cafe Location on Google Maps (URL)", [
                           validators.DataRequired(), validators.URL()])
    open = StringField("Opening Time e.g. 8AM", [validators.DataRequired()])
    close = StringField("Closing Time e.g. 5:30PM",
                        [validators.DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=[("1", "☕️"), ("2", "☕☕"), ("3", "☕☕☕"), ("4", "☕☕☕☕"), ("5", "☕☕☕☕☕")], validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", choices=[
                              ("1", "✘"), ("2", "💪"), ("3", "💪💪"), ("4", "💪💪💪"), ("5", "💪💪💪💪"), ("6", "💪💪💪💪💪")], validators=[DataRequired()])
    power_rating = SelectField("Power Socket Availability", choices=[
                               ("1", "✘"), ("2", "🔌"), ("3", "🔌🔌"), ("4", "🔌🔌🔌"), ("5", "🔌🔌🔌🔌"), ("6", "🔌🔌🔌🔌🔌")], validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a") as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.close.data},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_rating.data},"
                           f"{form.power_rating.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)

@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
