### 1. Product Overview:\
Sofia Bank is a digital bank, in which you can withdraw different loans, deposit and puts money in a saving account. Also, you can see different branches and ATMs and exchange rates.
---
### 2. Product Features:  
	- Custom user
	- Email verification
	- Withdraw loans
	- Create saving account / Deposit
	- Provide suggestions to the authenticated users (Needs)
	- Branch or ATMs feedback
	- Create / Update / Delete own user profile
	- Change password
---
### 3. User Characteristics:  
\
	3.1 Anonymous User:\
	\
		Anonymous user has only get permissions to bank informations.\
		They can get view of home page, which you can see the exchange rates, information about the bank and contacts.\
	3.2 Regular User:\
	\
		All registered users by default are regular users.\
		This user can sign-in with username and password. Post authentication the user is able to navigate through the dashboard. This user has their own profile with username, all CRUD operations related to it.\
	3.3 Admin User:\
	\
		The admin user gets enabled through the admin site by another admin user, setting their 'is_staff' field to True.\
		This user has all CRUD permissions over other users, their profiles and all bank database. After authentication this user can access the admin site through the top navigation panel.\
