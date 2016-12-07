from wtforms import Form, validators, SelectField, IntegerField


class InputForm(Form):
    Year = IntegerField(label='Year', default=2000, validators=[validators.InputRequired()])
    Award = SelectField(label='Award', choices=[('actor', 'Best Actor'), ('actress', 'Best Actress'), ('suporting actor', 'Best Supporting Actor'), ('supporting actress', 'Best Supporting Actress'), ('director','Best Director'), ('animated feature','Best Animated Feature'), ('picture', 'Best Picture'), ('original song', 'Best Original Song'), ('original score','Best Original Score'), ('visual effects', 'Best Visual Effects'), ('original screenplay', 'Best Original Screenplay'), ('adapted screenplay', 'Best Adapted Screenplay')], validators=[validators.InputRequired()])



# movie name

# what does Validators function do?



# award = input of award
# award_list[award]
# set default to Award List



#?? post vs. get??????