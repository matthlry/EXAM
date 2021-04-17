from flask import render_template, json

# as the models file contains all the models, import what you need
from app.models import Alpaca

class AlpacaController(object):

    # TODO: Implement Index
    # WHAT: Grabs data from model and uses it to display the relevant
    # alpacas from the database
    # CONDITIONS: If user specifies age, then must filter the list
    # RETURN: Return formatted Alpaca's to use for the view
    def index(self, age):
        allpacs = Alpaca.get_all()
        allpacsage = []
        allpacimage = []
        if age == 0:
            for i in range(0, len(allpacs)):
                allpacs[i].img = allpacs[i].get_filename()
                allpacsage.append(allpacs[i])
            return render_template("index.html", allp = allpacsage)
        elif age == 24:
            for i in range(0, leng(allpacs)):
                if allpacs[i].age < 25:
                    allpacs[i].img = allpacs[i].get_filename()
                    allpacsage.append(allpacs[i])
                return render_template("index.html", allp = allpacsage)
        elif age == 25:
            for i in range(0, leng(allpacs)):
                if allpacs[i].age > 25:
                    allpacs[i].img = allpacs[i].get_filename()
                    allpacsage.append(allpacs[i])
                return render_template("index.html", allp = allpacsage)
    # TODO: Implement Profile
    # WHAT: Grabs the relevant Alpaca from the model and uses it to
    # display the profile for that alpaca from the database
    # RETURN: Return formatted Alpaca to use for the view
    def profile(self, name):
        thepac = Alpaca.get(name)
        thepac.img = thepac.get_filename()
        thispac = thepac
        return render_template("profile.html", profpac=thispac)
    
    # TODO: Implement Search
    # WHAT: Uses the data recieved to find the Alpaca from the data
    # CONDITIONS: If user specifies nothing you can return everything or nothing!
    # that part if determined by you however if something is specified, it must
    # be a filtered list of alpacas
    # RETURN: Return formatted alpacas as a list using the
    # search criteria
    def search(self, filt):
        allpacs = Alpaca.get_all()
        allpacsearch = []
        for k in allpacs:
            for v in allpacs[k]:
                if filt in v:
                    allpacsearch.append[k]
        return allpacsearch



    
    # TODO: Implement Create
    # WHAT: Uses the data recieved to create an Alpaca model
    # REQUIREMENTS: Make a 'fake' save function in Alpaca that
    # Prints saving alpaca and then list the information recieved
    # and then give back a message stating what was saved
    # i.e Fred was created!
    # CONDITIONS:
    # RETURN: Return formatted message using the relevant information
    def create(self, name,age, sex, contact, displayName = ' ', bio= ' ', hobbies = ' ', img=' '):
        print(name + "was created!")
        return print(name," was created!" + "age: ", age, ", ", sex, "email: ", contact, " ", displayName, " ", bio, " ", hobbies = ' ') 


    # TODO: Implement Delete
    # WHAT: Uses the data recieved to find the Alpaca from the data
    # and then deletes it
    # REQUIREMENTS: Make a 'fake' delete function in Alpaca that
    # Prints the alpaca that will be delted followed by deleting alpaca
    # and then list the information recieved and then give back a
    # message stating what was saved i.e Fred was deleted!
    # CONDITIONS:
    # RETURN: Return formatted message using the relevant information
    def delete(self, name):
        return print(name, " was deleted!")

alpaca_controller = AlpacaController()