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

        if len(first_name) == 0 or len(last_name) == 0 or len(age) == 0 or len(email) == 0:
            error = "Please fill all fields"
        else:
            new_person_id = DATA_PROVIDER.add_person(first_name, last_name, age, email)

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
        sports = ("quick", "fast", "speedy", "rapid", "sports")
        family = ("family", "kids")
        economical = ("economical", "cheap", "efficient")
        estate = ("pets", "luggage")
        hybrid = ("green", "environment", "electric")
        suv = ("suv", "people carrier", "sports utility vehicle", "chelsea tractor")
        convertible = ("convertible", "soft top")

        sportscar = "Ferrari"
        familycar = "Fiat"
        economicalcar = "Seat"
        estatecar = "BMW"
        hybridcar = "Tesla"
        suvcar = "Hummer"
        convertiblecar = "Corvette"

        if car_type in list(sports):
            recommendation = f" We think you would like a : {sportscar} or a {convertiblecar} "
        elif car_type in list(family):
            recommendation = f" We think you would like a : {familycar}, {estatecar} or {suvcar} "
        elif car_type in list(economical):
            recommendation = f" We think you would like a : {economicalcar} or {hybridcar} "
        elif car_type in list(estate):
            recommendation = f" We think you would like a : {estatecar}"
        elif car_type in list(hybrid):
            recommendation = f" We think you would like a : {hybridcar}"
        elif car_type in list(suv):
            recommendation = f" We think you would like a : {suvcar}"
        elif car_type in list(convertible):
            recommendation = f" We think you would like a : {convertiblecar}"
        else:
            recommendation = f" Try a different key word"
        return render_template('car_loop.html', form=form, rec=recommendation)
    return render_template('car_loop.html', form=form)

@app.route('/car_loop', methods=['GET'])
def car_loop():
    return render_template('car_loop.html', title="car_loop")
