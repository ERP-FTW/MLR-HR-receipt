# MLR-HR-receipt

Overview
This custom module for Odoo 16+ facilitates tipping of waitstaff through the lightning network. It adds an LN address field for employees and presents it as a QR code in the Point-of-Sale application paid receipt. Two branches of the project currently exist, one for javascript implementation of the QR code, and one for python implementation of the QR code with the option to place an avatar image into the QR code. No internal records of the tipping transactions are collected, allowing electronic peer-to-peer cash-like tipping.

Prerequisites

Installation (see this video for tutorial on Odoo module installation)
1. Download repository and place extracted folder in the Odoo addons folder.
2. Login to Odoo database to upgrade and enable developer mode under settings.
3. Under apps Update the App list.
4. Search for the module (MLR) and install.

Set-up
1. Create an employee profile for each registered user if not already done. Add an avatar image if desired.
2. Under Employee->HR settings->Point of Sale input a LN address. Select whether to include the avatar image. Save the record and refresh the page to see the updated QR code.
3. For multi-employee mode select Multi Employees per Session under Point of Sale-> Configurations -> PoS Interface and add authorized employees to the Allowed Employees list.

Operation
1. Upon payment on a point-of-sale order a paid receipt will be generated and available to print. It will have the lightning address of the employee as text and a QR code with a prompt to encource the customer to send a tip. An employee can verify tips on the wallet corresponding to the supplied lightning address.
