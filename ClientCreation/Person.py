'''
1. Person has common attributes like Name, Phone no, Address, Account information and identification 
2. Person can have multiple addresses and accounts 
3. An account can be owned by multiple persons
4. Identification information consists of a type (SSN, Passport or Driving license) and an identification number
'''
from Account import Account
class Person(object):

	def __init__(self, name, phoneNo, accountInfo, identification):
		self.name           = name
		self.address        = []
		self.phoneNo        = phoneNo
		self.accountInfo    = accountInfo
		self.accounts       = []
		self.identification = identification 
		self.addAccount(accountInfo)
	
	def getName(self):
		return self.name
		
	def getAddress(self):
		return self.address
		
	def getPhoneNo(self):
		return self.phoneNo

	def __str__(self):
		return "Name : %s , Address : %s , phoneNo : %s "% (self.name, self.address.getCity(), self.phoneNo)
	
	def setAddress(self, address):
		self.address.append(address)
		
	def addAccount(self, account):
		self.accounts.append(account)
		account.sharedAccInfo.append(self)
		
	def getAccountDetail(self, type):
		for acc in accountInfo:
			if(acc.getType() == type):
				return acc.getAccountNo()
				
	def getAllAccounts(self, type):
		for acc in accountInfo:
			print ("Account Type : %s, Number :%d" % (acc.getType, acc.getAccountNo))
			
	def getIdentification(self):
		return ("Identification type : %s, Number : %d" % (acc.identification.getIdType, acc.getIdType))
		
class Address(object):
	def __init__(self, aptNo, street, city):
		self.aptNo   = aptNo
		self.street  = street
		self.city    = city
		
	def getAptNo(self):
		return self.aptNo
		
	def getStreet(self):
		return self.street
		
	def getCity(self):
		return self.city

		
class Identification(object):
	
	def __init__(self, idType, idNumber):
		self.idType   = idType
		self.idNumber = idNumber
		
	@property
	def idType(self):
		return self._idType
		
	@idType.setter
	def idType(self, d):
		identificationTypes = ['SSN','Passport','DrivingLicense']
		found = None
		for type in identificationTypes:
			if (d == type):
				self._idType = d
				found = True
				break
		if not found:
		    raise Exception ("Wrong Identification Type. Valid types - SSN, Passport, DrivingLicense")	
	
	@property	
	def idNumber(self):
		return self._idNumber
	
	@idNumber.setter
	def idNumber(self, d):
		if (len(str(d)) == 10):
			self._idNumber = d
		else:
			raise Exception ("Worng identification number. Please enter valid number")
	
