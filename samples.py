#at the >>> prompt type the following:
#execfile("samples.py")

#Put in some data into databe to work with and test
#



from django.contrib.auth.models import User



	

def adding_users(user_start_number, user_end_number):
	while user_start_number < user_end_number:
		new_user = User.objects.create_user(user_start_number, 'email@nowa.com', 'password1')
		user_start_number +=1 
		print "added usernumber %d" % user_start_number



user_start_number = 1
user_end_number = 15
adding_users(user_start_number, user_end_number)
