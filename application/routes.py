from flask import render_template, request

# # needed to connect to database
# from application.data_provider_service import DataProviderService
# # instantiating an object of DataProviderService
# DATA_PROVIDER = DataProviderService()

from application import app
# from application.forms import BasicForm


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/welcome/<name>')
def welcome(name):
    return render_template('welcome.html', name=name, group="everyone")


@app.route('/contactus')
def contact_us():
    return render_template('contact_us.html', title='contact us')

@app.route('/about')
def about():
    return render_template('about.html', title='about')


@app.route('/favourites')
def favourites():
    return render_template('favourites.html', title='favourites', my_list=['cars', 'money', 'music', 'rabbits',
                                                                           'mountain biking'])


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = ""
    # instantiating an object of type BasicForm
    form = BasicForm()
    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply both first and last name"
        else:
            new_person_id = DATA_PROVIDER.add_person(first_name, last_name)
            success = 'Person with ID ' + str(new_person_id) + ' was created. Thank you!'
            return render_template('success.html', success_message=success)
    return render_template('person.html', form=form, message=error)


@app.route('/people', methods=['GET'])
def get_people():
    all_people = DATA_PROVIDER.get_people()
    return render_template('people.html', title="People", people=all_people)