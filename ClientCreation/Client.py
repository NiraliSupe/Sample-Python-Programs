'''
1. A client is derived from Person class which has specific attributes like joining date, expiry date and membership type.
2. There are 4 types of membership and the length of membership depends on these types.  
   [Normal - 1, Silver - 3, Gold - 5, Platinum - 7]
'''
from Person  import Person, Address, Identification
from Account import Account, CreditAccount
from enum    import Enum
import datetime

class MemberShipType(Enum):
	Normal   = 1
	Silver   = 3
	Gold     = 5 
	Platinum = 7
	
class Client(Person):
	def __init__(self, name, phoneNo, accountInfo, identification, mType):
		super().__init__(name, phoneNo, accountInfo, identification)
		self.joinDate   = datetime.date.today()
		self.expiryDate = ""
		self.mType       = mType
	
	def getJoinDate(self):
		return self.joinDate
		
	def getExpiryDate(self):
		return self.expiryDate
	
	@property
	def mType(self):
		return self._mType
	
	@mType.setter
	def mType(self, d):
		found = None
		for type in MemberShipType:
			if (d == type.name):
				self._mType = d
				found = True
				break
		if not found:
		    raise Exception ("Wrong MemberShip Type. Valid types - Normal, Gold, Silver, Platinum")	
	
	def getTodayDate():
		return datetime.date.today()

	def setExpiryDate(self):
		d = datetime.date.today()
		for type in MemberShipType:
			if (self.mType == type.name):
				self.expiryDate = CreditAccount.calExpiryDate(d, type.value)
				break

def main(name, phoneNo):
	account        = Account("12345678", 10000, "Savings") 
	identification = Identification("SSN", 1234567890)
	client         = Client(name, phoneNo, account, identification, "Gold")
	client.setExpiryDate()
	print(client.joinDate)
	print(client.expiryDate)


if __name__ == "__main__":
    main("Nirali", 3126290570)
