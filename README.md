- this vulnerability against Boingo no longer works and has been fixed for some time now. shout out to the Boingo team for a quick and swift fix.

The vulnerabilities were an account takeover and xss.

This account takeover worked because a request to the server would be made with an already registered email on the platform to request a reset password. 
The customer account data would be returned to the user and automatically sent on behalf of the user/browser as another request to the server. 
  - this was required to request a reset password but not all data was verified. 
This second request would send the reset password email to the intended user.

Using pythons request module, you can capture the customer data and modify the request to change the customer email to the hacker's email and they would recieve the reset password email!

Similar to the 1st vulnerability, xss code could aslo be added and sent to the intended email to execute xss in their browser when clicked on. 
