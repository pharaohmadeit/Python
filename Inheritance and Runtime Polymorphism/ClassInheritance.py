# coding: utf-8
from decimal import Decimal
class CommissionEmployee:
    """An employee who gets paid commission based on gross sales."""
    def __init__(self, first_name, last_name, ssn, gross_sales, commission_rate):
        self._first_name = first_name
        self._last_name = last_name
        self._ssn = ssn
        self.gross_sales = gross_sales
        self.commission_rate = commission_rate
    @property
    def first_name(self):
        return self._first_name
    @property
    def last_name(self):
        return self._last_name
    @property
    def ssn(self):
        return self._ssn
    @property
    def gross_sales(self):
        return self._gross_sales
    @gross_sales.setter
    def gross_sales(self, sales):
        if sales < Decimal('0.00'):
            raise ValueError('Gross sales must be >= to 0')
        self._gross_sales = sales
    @property
    def commission_rate(self):
        return self._commission_rate
    @commission_rate.setter
    def commission_rate(self, rate):
        if not (Decimal('0.0') < rate < Decimal('1.0')):
            raise ValueError('Interest rate must be greater than 0 and less than 1')
        self._commission_rate = rate
    def earnings(self):
        return self.gross_sales * self.commission_rate
    def __repr__(self):
        return ('CommissionEmployee: ' + f'{self.first_name} {self.last_name}\n' +
                f'social security number: {self.ssn}\n' + f'gross sales: {self.gross_sales:.2f}\n' + f'commission rate: {self.commission_rate:.2f}')
                
c = CommissionEmployee('Sue', 'Jones', '333-33-3333', Decimal('10000.00'), Decimal('0.06'))
c
print(f'{c.earnings():,.2f}')
c.gross_sales = Decimal('20000.00')
print(f'{c.earnings():,.2f}')
class SalariedCommissionEmployee(CommissionEmployee):
    """An employee who gets paid a salary plus commission based on gross sales."""
    def __init__(self, first_name, last_name, ssn, gross_sales, commission_rate, base_salary):
        super().__init__(first_name, last_name, ssn, gross_sales, commission_rate)
        self.base_salary = base_salary
    @property
    def base_salary(self):
        return self._base_salary
    @base_salary.setter
    def base_salary(self, salary):
        if salary < Decimal('0.00'):
            raise ValueError('Base salary must be >= to 0')
        self._base_salary = salary
    def earnings(self):
        return super().earnings() + self.base_salary
    def __repr__(self):
        return ('Salaried' + super().__repr__() + f'\nbase salary: {self.base_salary:.2f}')
        
s = SalariedCommissionEmployee('Phara', 'Tornes', '444-44-4444', Decimal('5000.00'), Decimal('0.04'), Decimal('300.00'))
print(s.first_name, s.last_name, s.ssn, s.gross_sales, s.commission_rate, s.base_salary)
print(f'{s.earnings():.2f}')
s.gross_sales = Decimal('10000.00')
s.commission_rate = Decimal('0.05')
s.base_salary = Decimal('1000.00')
print(s)
print(f'{s.earnings():.2f}')
