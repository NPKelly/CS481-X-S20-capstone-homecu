from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import BsuOfficeusers

class newUserBackend(BaseBackend):

	def checkusername(self, username=None):
		try:
			user = BsuOfficeusers.objects.get(user_name=username)
			return 1
		except BsuOfficeusers.DoesNotExist:
			return None

	def checkemail(self, email=None):
		try:
			user = BsuOfficeusers.objects.get(email=email)
		except BsuOfficeusers.DoesNotExist:
			return None

	def addCustomer(self, email=None, username=None, password=None):
		try:
			BsuOfficeusers.objects.create_user(username=username, password=password)

		except:
			return None
	def addStaff(self, email=None, username=None, password=None):
		try:
			BsuOfficeusers.objects.create_superuser(username=username, passwd=password)
		except:
			return None

