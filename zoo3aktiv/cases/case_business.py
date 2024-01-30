import random
from objects.building_and_facilities import building
from objects.being import employees

def generate_visitors():
    visitors = random.randint(50, 200)
    return visitors

def income_ticket_sales(visitors):
    fpv_factor              =   random.uniform(0.3, 0.5)
    full_price_visitor      =   round(visitors * fpv_factor)
    fpv_income              =   full_price_visitor * building[0].prices['normal']

    rpv_factor              =   random.uniform(0.25, 0.4)
    reduced_price_visitor   =   round(visitors * rpv_factor)
    rpv_income              =   reduced_price_visitor * building[0].prices['ermäßigt']

    free_price_visitors     =   visitors - full_price_visitor - reduced_price_visitor

    employees[0].income    +=   fpv_income + rpv_income

    print(  f'Heute besuchten {visitors} Menschen den Zoo.\n'
            f'Davon bezahlten {full_price_visitor} Personen den vollen Preis.\n'
            f'{reduced_price_visitor} Personen zahlten ermäßigt und {free_price_visitors} Personen hatten freien Eintritt.\n'
            f'Durch Ticketverkäufe wurden {employees[0].income} € eingenommen.')

def income_food_sales(visitors):
    eating_visitors         =   round(random.uniform(0.3, 0.7) * visitors)
    eating_visitors_income  =   random.randint(15, 21) * eating_visitors

    employees[1].income    +=   eating_visitors_income

    print(f'Durch verkauftes Essen wurden {eating_visitors_income} € eingenommen.')

def list_income_expenditure():
    balance_sheet                     =   building[2].guv_rechnung()
    print(  f'Es wurden heute insgesamt {balance_sheet[0]} € eingenommen\n'
            f'Gesamtkosten für heute betragen {balance_sheet[1]} €\n'
            f'dies ergibt eine Bilanz von {balance_sheet[2]} €\n')

def run_business_case():
    visitors                =   generate_visitors()
    income_ticket_sales(visitors)
    income_food_sales(visitors)
    list_income_expenditure()