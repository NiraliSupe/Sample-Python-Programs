'''
1. Account details contain Account no and Type (Saving or checking).
2. Credit card class is derived from Account which contains unique fields like CVV and expiry date.  
3. Account can be shared by multiple persons
'''
class Account(object):
	def __init__(self, accountNo, amount, type):
		self.accountNo     = accountNo
		self.amount        = amount
		self.type          = type
		self.sharedAccInfo = []
		
	def getAccountNo(self):
		return self.accountNo
		
	def getBalance(self):
		return self.balance
	
	@property	
	def type(self):
		return self._type
	
	@type.setter
	def type(self, d):
		accTypes = ['Checking','Saving']
		found = None
		for type in accTypes:
			if (d == type):
				self._type = d
				found = True
				break
		if not found:
		    raise Exception ("Wrong Account Type. Valid types - Checking and Savings")	
		
	def getSharedAccInfo(self):
		return self.sharedAccInfo

class CreditAccount(Account):
	def __init__(self, accountNo, amount, expiryDate, CVV):
		super().__init__(self, accountNo, amount)
		self.expiryDate = expiryDate
		self.CVV        = CVV
	
	def getAccountNo(self):
		return self.expiryDate
		
	def getBalance(self):
		return self.CVV
		
	@staticmethod
	def calExpiryDate(d, years):
		try:
			return d.replace(year = d.year + years)
		except ValueError:
			return  d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))