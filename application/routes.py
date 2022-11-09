from flask import render_template, request

from application import app
# from application.forms import BasicForm
#
# # needed to connect to database
# from application.data_library import DataLibrary
# # instantiating an object of DataProviderService
# DATA_PROVIDER = DataLibrary()



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/carmatch')
def carmatch():
    return render_template('carmatch.html', title="Matcher")

@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html', title="Subscribe")

@app.route('/showroom')
def showroom():
    return render_template('showroom.html', title="Showroom")

#
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     error = ""
#     # instantiating an object of type BasicForm
#     form = BasicForm()
#
#     if request.method == 'POST':
#         first_name = form.first_name.data
#         last_name = form.last_name.data
#         age = form.age.data
#         email = form.email.data
#
#         if len(first_name) == 0 or len(last_name) == 0 or len(age) == 0 or len(email) == 0:
#             error = "Please fill all fields"
#         else:
#             new_person_id = DATA_PROVIDER.add_person(first_name, last_name, age, email)
#
#             success = 'Member with ID: ' + str(new_person_id) + ' was created. Thank you!'
#             return render_template('success.html', success_message=success)
#
#     return render_template('members.html', form=form, message=error)
#
# @app.route('/people', methods=['GET'])
# def get_people():
#     all_people = DATA_PROVIDER.get_people()
#     return render_template('people.html', title="People", people=all_people)