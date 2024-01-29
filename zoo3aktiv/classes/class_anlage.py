from classes.class_GuV_quelle import Einnahme_und_Kostenquelle

class Anlage:
    def __init__(self, insassen):
        self.inmate      =   insassen
#-----------------------------------------------------
class Gehege(Anlage):
    def __init__(self, inmate):
        Anlage.__init__(self, inmate)

class Gebaeude(Anlage):
    def __init__(self, inmate):
        Anlage.__init__(self, inmate)
#-----------------------------------------------------
class Polarwelt(Gehege):
    def __init__(self, inmate, position):
        Gehege.__init__(self, inmate)
        self.position   =   position

class Savannengehege(Gehege):
    def __init__(self, inmate, position):
        Gehege.__init__(self, inmate)
        self.position   =   position

class Unterwasserwelt(Gehege):
    def __init__(self, inmate, position):
        Gehege.__init__(self, inmate)
        self.position   =   position
#-----------------------------------------------------
class Buero(Gebaeude, Einnahme_und_Kostenquelle):
    def __init__(self, inmate, position, income, expenditure, fixed_costs):
        Gebaeude.__init__(self, inmate)
        Einnahme_und_Kostenquelle.__init__(self, income, expenditure)
        self.position   =   position
        self.fixed_costs     =   fixed_costs

class Kassenbude(Gebaeude, Einnahme_und_Kostenquelle):
    def __init__(self, inmate, position, income, expenditure, prices):
        Gebaeude.__init__(self, inmate)
        Einnahme_und_Kostenquelle.__init__(self, income, expenditure)
        self.position   =   position
        self.prices     =   prices

class Restaurant(Gebaeude, Einnahme_und_Kostenquelle):
    def __init__(self, inmate, position, income, expenditure, prices):
        Gebaeude.__init__(self, inmate)
        Einnahme_und_Kostenquelle.__init__(self, income, expenditure)
        self.position   =   position
        self.prices     =   prices