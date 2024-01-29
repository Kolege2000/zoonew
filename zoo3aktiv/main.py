from cases.case_visitor import run_visitor_case
from cases.case_business import run_business_case
from objects.being import *

def activate_visitor_case():
    visitor1 = create_visitor()
    run_visitor_case(visitor1)

def activate_business_case():
    run_business_case()

activate_business_case()
activate_visitor_case()