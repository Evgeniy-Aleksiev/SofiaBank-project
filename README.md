### 1. Product Overview:
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
#### 3.1 Anonymous User:
Anonymous user has only get permissions to bank informations.\
They can get view of home page, which you can see the exchange rates, information about the bank and contacts.
#### 3.2 Regular User:
All registered users by default are regular users.\
This user can sign-in with username and password. Post authentication the user is able to navigate through the dashboard. This user has their own profile with username, all CRUD operations related to it.
#### 3.3 Admin User:
The admin user gets enabled through the admin site by another admin user, setting their 'is_staff' field to True.\
This user has all CRUD permissions over other users, their profiles and all bank database. After authentication this user can access the admin site through the top navigation panel.

---
### 4. Profile Objects
Profile is created on user creation. The user profile has a profile completion progress based on filled profile fields. The user must be 18 years old or older.

##### Components:
- User - foreign-key relation with the user
- Username - char-field
- First name - char-field
- Middle name - char-field
- Last name - char-field
- EGN - char-field
- Email - email-field
- Mobile number - char-field
- Date of birth - date-field
- Gender - char-field

---
### 5. Loan and Saving Objects
The Loan and Saving object could be private. Only the author of the account can see the information of the withdraws.

##### Components:
- User - foreign-key relation with the user
- Type - char-field
- Amount - integer-field
- Period - integer-field

---
### 6. Branches, ATMs, Feedback, Exchange rates objects
This object could be either public or private. They can only be modified by the administrator.