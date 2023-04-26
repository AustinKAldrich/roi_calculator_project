class RoiCalculator():
    """
    This is a class that breaks up calculating Return of Investment percentages into
    four steps.
    Step One: calc_income() calculates your total income
    Step Two: calc_expenses() calculates your total expenses
    Step Three: calc_cash_flow() takes your income and subtracts your expenses
    Step Four: calc_roi() calculates your total investments and divides that by your annual cash flow

    Use the run_calc() function to actually run the calculator on your ROIobject

    All attributes expect an int value
    """

    def __init__(self, rental_income, laundry, storage, misc, tax, insurance,
                         utilities, hoa, lawn_snow, vacancy, repairs, capex, property_manager,
                         mortgage, down_payment, closing_costs, rehab_budget, misc_other):
        self.rental_income = rental_income
        self.laundry = laundry
        self.storage = storage
        self.misc = misc
        self.tax = tax
        self.insurance = insurance
        self.utilities = utilities
        self.hoa = hoa
        self. lawn_snow =  lawn_snow
        self.vacancy = vacancy
        self.repairs = repairs
        self.capex = capex
        self.property_manager = property_manager
        self.mortgage = mortgage
        self.down_payment = down_payment
        self.closing_costs = closing_costs
        self.rehab_budget = rehab_budget
        self.misc_other = misc_other

    def calc_income(self):
        total_income = self.rental_income + self.laundry + self.storage + self.misc
        return total_income
    
    def calc_expenses(self):
        total_expenses = self.tax + self.insurance + self.utilities + self.hoa + self.lawn_snow + self.vacancy + self.repairs + self.capex + self.property_manager + self.mortgage
        return total_expenses
    
    def calc_cash_flow(self, income, expenses):
        monthly_cash_flow = income - expenses
        return monthly_cash_flow
    
    def calc_roi(self, monthly_cash_flow):
       total_investment = self.down_payment + self.closing_costs + self.rehab_budget + self.misc_other
       annual_cash_flow = 12 * monthly_cash_flow
       total_roi = (annual_cash_flow / total_investment) * 100
       return total_roi
    
    def run_calc(self):
        temp_inc = self.calc_income()
        temp_exp = self.calc_expenses()
        temp_cf = self.calc_cash_flow(temp_inc, temp_exp)
        roi =  self.calc_roi(temp_cf)
        print(f"Your return of investment is {roi}%.")

    
sample = RoiCalculator(2000, 0, 0, 0, 150, 100, 0, 0, 0, 100, 100, 100, 200, 860, 40000, 3000, 7000, 0)
sample.run_calc()        