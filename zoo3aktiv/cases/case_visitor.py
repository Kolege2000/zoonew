from objects.being import *

def welcome_visitorcase(anna):
    anna.welcome()

def run_visitor_case(anna):
    new_position_nr =   int(anna.go_to())

    if new_position_nr == anna.position:
        anna.inside_acting()
    else:
        anna.position = new_position_nr
    run_visitor_case(anna)
