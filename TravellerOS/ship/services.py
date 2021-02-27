from .models import Ship, Character, DashBoard_VM
import datetime
def register_ship(form, user):
    ## instantiate ship in DB
    ship = form.save(commit=False)
    ship.save()
    ## instantiate character in DB
    char = create_character(user, form.cleaned_data.get('char_name'))
    ## add m2m connections to ship
    ship.characters.add(char)
    ship.users.add(user)
    form.save_m2m()

def register_crew(form, user):
    ship = Ship.objects.filter(ship_code=form.cleaned_data.get('ship_code')).first()
    if ship and not user.ship_set.filter(id=ship.id).exists():
        ship.users.add(user)
        char = create_character(user, form.cleaned_data.get('char_name'))
        ship.characters.add(char)
        ship.save()
        return True
    else:
        return False

def create_character(user, name):
    return Character.objects.create(
        name=name,
        user= user, 
        created_date=datetime.datetime.now(), 
        updated_date=datetime.datetime.now())

def get_dashboard(ship_id, char_id):
    test = DashBoard_VM()
    test.ship = ship=Ship.objects.filter(id=ship_id).first()
    return test

