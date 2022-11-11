import pymysql
from flask import render_template, request

from application import app

from application.forms import BasicForm, VehicleForm

# needed to connect to database
from application.data_library import DataLibrary
# instantiating an object of DataProviderService
DATA_PROVIDER = DataLibrary()


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


@app.route('/carmatch')
def carmatch():
    return render_template('carmatch.html', title="Match app")


@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html', title="Subscribe")


@app.route('/showroom')
def showroom():
    return render_template('showroom.html', title="Showroom")


@app.route('/golfr')
def golfr():
    return render_template('golfr.html', title="Golf R")


@app.route('/purchase_golfr')
def purchase_golfr():
    return render_template('purchase_golfr.html', title="Match Complete")



@app.route('/model3')
def model3():
    return render_template('model3.html', title="Model 3")


@app.route('/rangerover')
def rangerover():
    return render_template('rangerover.html', title="Range Rover")


@app.route('/rs3')
def rs3():
    return render_template('rs3.html', title="=RS3")


@app.route('/rs6')
def rs6():
    return render_template('rs6.html', title="RS6")


@app.route('/rangeroversport')
def rangeroversport():
    return render_template('rangeroversport.html', title="Range Rover Sport")


@app.route('/rivian')
def rivian():
    return render_template('rivian.html', title="Rivian R1S")


@app.route('/models')
def models():
    return render_template('models.html', title="Model S")


@app.route('/ioniq')
def inoiq():
    return render_template('ioniq.html', title="Ioniq")

@app.route('/purchase_ioniq')
def purchase_inoiq():
    return render_template('purchase_ioniq.html', title="Match Complete")


@app.route('/aygo')
def aygo():
    return render_template('aygo.html', title="Aygo")

@app.route('/purchase_aygo')
def purchase_aygo():
    return render_template('purchase_aygo.html', title="Match complete")


@app.route('/sandero')
def sandero():
    return render_template('sandero.html', title="Sandero")


@app.route('/maestro')
def maestro():
    return render_template('maestro.html', title="Maestro")

@app.route('/purchase_maestro')
def purchase_maestro():
    return render_template('purchase_maestro.html', title="Match Complete")

@app.route('/purchase_model3')
def purchase_model3():
    return render_template('purchase_model3.html', title="Match Complete")

@app.route('/tc')
def tc():
    return render_template('tc.html', title="T's and C's")


@app.route('/members', methods=['GET', 'POST'])
def register():
    error = ""
    # instantiating an object of type BasicForm
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        age = form.age.data
        email = form.email.data
        user_name = form.user_name.data

        user_count = DATA_PROVIDER.check_user(user_name)
        if user_count > 0:
            error = "Username already taken, Please Choose Another"
        elif len(first_name) == 0 or len(last_name) == 0 or len(age) == 0 or len(email) == 0 or len(user_name) == 0:
            error = "Please fill all fields"
        else:
            new_person_id = DATA_PROVIDER.add_person(first_name, last_name, age, email, user_name)

            success = 'Member with ID: ' + str(new_person_id) + ' was created. Thank you!'
            return render_template('success.html', success_message=success)

    return render_template('members.html', form=form, message=error)


@app.route('/people', methods=['GET'])
def get_people():
    all_people = DATA_PROVIDER.get_people()
    return render_template('people.html', title="People", people=all_people)


@app.route('/car_pick', methods=['GET', 'POST'])
def car_pick():
    form = VehicleForm()
    if request.method == 'POST':
        car_type = form.car_type.data
        sports = ("quick", "fast", "speedy", "rapid", "sports", "Quick", "Fast", "Speedy", "Rapid", "Sports")
        family = ("family", "kids", "distinctive", "Family", "Kids", "Distinctive")
        economical = ("economical", "cheap", "efficient", "Economical", "Cheap", "Efficient")
        estate = ("pets", "luggage", "astonishing", "estate" "Pets", "Luggage", "Astonishing", "Estate")
        hybrid = ("green", "environment", "environmental", "electric", "Green", "Environment", "Environmental", "Electric")
        suv = ("suv", "people carrier", "sports utility vehicle", "chelsea tractor", "SUV", "People Carrier", "Sports Utility Vehicle", "Chelsea Tractor")
        four = ("elegant", "powerful", "luxury", "sleek", "Elegant", "Powerful", "Luxary", "Sleek")
        vintage = ("vintage", "used", "experienced", "Vintage", "Used", "Experienced")
        innovative = ("innovative", "futuristic", "future", "Innovative", "Futuristic", "Future")
        hatch = ("hot hatch", "hatchback", "agile", "custom", "Hot Hatch", "Hatchback", "Agile")

        if car_type in sports:
            return render_template('rs3.html', title="=RS3")
        elif car_type in family:
            return render_template('sandero.html', title="Sandero")
        elif car_type in economical:
            return render_template('aygo.html', title="Aygo")
        elif car_type in estate:
            return render_template('rs6.html', title="RS6")
        elif car_type in hybrid:
            return render_template('model3.html', title="Model 3")
        elif car_type in suv:
            return render_template('rivian.html', title="Rivian R1S")
        elif car_type in four:
            return render_template('rangerover.html', title="Range Rover")
        elif car_type in vintage:
            return render_template('maestro.html', title="Maestro")
        elif car_type in innovative:
            return render_template('purchase_ioniq.html', title="Match Complete")
        elif car_type in hatch:
            return render_template('golfr.html', title="Golf R")
        else:
            recommendation = f" Try a different key word"
        return render_template('car_loop.html', form=form, rec=recommendation)
    return render_template('car_loop.html', form=form)


@app.route('/car_loop', methods=['GET'])
def car_loop():
    return render_template('car_loop.html', title="car_loop")
