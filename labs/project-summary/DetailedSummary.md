
# HomeCU

#### Detailed Summary

##### Overview 

The utility will be a web service with Python (Django) as the server-side language and Vue.js as the front-end framework. There are four main features that will need to be implemented, these include: Secure Login, List of Credit Unions, a simple User Creation, and a Loan App Editor.

##### Data Provided

The sponsor will provide sample data in the form of CSV files. The description of each data set is as follows:
	1. cuinfo - Information about the credit unions in the list
	2. montiorusers - Information about the users of the utility
	3. Inappschemamaster - Information about the loan and stylesheets
	4. Inappschemadetail - Information about the fields in a loan
	5. Inappanslookuphdr - List of answers particular to a loan app (used for the loan app editor)

##### Secure Login

The secure login is to be a simple username/password login. The provided login will be verified against the 'monitorusers' table. When the user enters their information they should stay on the same page instead of being redirected.

##### List of Credit Unions

After a user is logged in they will be shown grid-like list of credit unions. When a credit union in the list is selected, a pop-up will appear with basic information (found in the 'cuinfo' table) about the credit union and a menu with actions that can be done with the credit union. The information should not appear on a separate page but rather as a pop-up. On this page the user should have the ability to edit the credit union's information.

##### User Creation

We are to create a tool that is able to do simple maintenence of the 'monitorusers' table. The user should be able to create a new user with with either basic or admin rights. An admin user should have permission to update any users information and the basic user should only have permission to update their information.

###### The features descriped above the line have fewer required specifications and the feature below the line has specifications described by the sponsor.

***

##### Loan App Editor

The Loan App Editor is a tool where the user edits the records in the 'Lnapp*' tables. The specifications for this feature can be found in the [description pdf](./LoanAppEditorSpecificFeatures.pdf). 

