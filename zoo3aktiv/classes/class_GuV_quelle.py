class Einnahme_und_Kostenquelle:
    def __init__(self, einnahmen, kosten):
        self.income                 =   einnahmen
        self.expenditure            =   kosten

    def guv_rechnung(self):
        from objects.being import employees

        total_employee_income       =   0
        total_employee_costs        =   0
        for employee in employees:
            total_employee_income  +=   employee.income
            total_employee_costs   +=   employee.expenditure

        balance_sheet = total_employee_income - total_employee_costs - self.fixed_costs
        return balance_sheet