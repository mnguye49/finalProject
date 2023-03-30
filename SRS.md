# Software Requirements Specification Document

This serves as a template for each projects' Software Requirements Specification (SRS) document. When filling this out, you will be required to create user stories, use cases, requirements, and a glossary of terms relevant to your project. Each group member must contribute to every section, so it is crucial that your group's GitHub repository shows a commit history that reflects the work of each group member. It is highly recommended that you create separate branches for each member, but since this is one single document, you will need to manually merge the branches together. It is also advisable to have multiple working versions of this document (named separately) so that one person can compile the final SRS document from the multiple working versions. Ultimately, how you go about managing this is up to you, but consistent formatting, clear commit messages, and a thorough commit history with contributions from each group member are required.

Fill the document out following the guidelines listed in each section. Maintain [proper Markdown syntax](https://www.markdownguide.org/basic-syntax/) and be sure that your group has a `main` branch with this document and the entire [template repository codebase](https://github.com/david-gary/onlineStoreTemplate) either forked or downloaded and copied into your group's repository. If you have arranged to use a different codebase as a template, you do not need to have the original template included, but a `main` branch is still required.

## Group Members

* [Thi Nguyen](mailto:mnguye49@uncc.edu)
* [Tan Nguyen](mailto:tnguy241@uncc.edu)
* [Mina Rao](mailto:mrao11@uncc.edu)

## Revisions

When a change is made to the document, a new revision should be created. The revision should be added to the table below with all information filled out.

| Version | Date | Description | Author | Reviewed By |
| --- | --- | --- | --- | --- |
| 1.0 | 03/22/23 | Initial draft | [David Gary](mailto:dgary9@uncc.edu) | [David Gary](mailto:dgary@uncc.edu) |
| 1.0 | 03/28/23 | Worked on intro and requirements | [Thi Nguyen](mailto:mnguye49@uncc.edu) | [Thi Nguyen](mailto:mnguye49@uncc.edu) |
| 1.0 | 03/28/23 | Worked on requirements | [Tan Nguyen](mailto:tnguy241@uncc.edu) | [Tan Nguyen](mailto:tnguy241@uncc.edu) |
| 1.0 | 03/29/23 | Worked on filling in my required amount of information for each section | [Thi Nguyen](mailto:mnguye49@uncc.edu) | [Thi Nguyen](mailto:mnguye49@uncc.edu) |
| 1.0 | 03/29/23 | Filled out required amount of info for each section | [Tan Nguyen](mailto:tnguy241@uncc.edu) | [Tan Nguyen](mailto:tnguy241@uncc.edu) |
| 1.0 | 03/30/23 | Worked on intro and definitions | [Thi Nguyen](mailto:mnguye49@uncc.edu) | [Thi Nguyen](mailto:mnguye49@uncc.edu) |
| 1.0 | 03/30/23 | Worked on all sections | [Mina rao](mailto:mrao11@uncc.edu) | [Mina rao](mailto:mrao11@uncc.edu) |
| 1.0 | 03/30/23 | Did some editing and spellchecking | [Thi Nguyen](mailto:mnguye49@uncc.edu) | [Thi Nguyen](mailto:mnguye49@uncc.edu) |


## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Constraints](#constraints)
4. [Use Cases](#use-cases)
5. [User Stories](#user-stories)
6. [Glossary](#glossary)

## Introduction

Our final project will be a website for a cake business where the customers can order and customise their own cakes that can be delivered to their homes and other locations. The website will be created using Python and Javascript for the code and have Flask be used for a framework.  Due to the internet evolving, more and more businesses are adding their services onto online platforms in order to expand. In addition, some customers may not have a means of transportation for reasons and may need their goods to be delivered to them. Users should be able to order a cake on the website, customize it if they want and after paying for it and then be able to choose if they want to pick it up in person or have it delivered.

## Requirements

* **REQ-1:** A unique identifier for the requirement. This should be a number that is unique across the entire document (something like REQ-1, REQ-2, etc. but be sure to replace the word `ID` with the unique identifier).
  * **Description:** The user must be able to place an order for a cake.
  * **Type:** Functional.
  * **Priority:** 1.
  * **Rationale:** It is the main service that is to be provided.
  * **Testing:** We can place an order to see if it gets registered or goes through.
* **REQ-2:**
  * **Description:** The user must be able to customize their order.
  * **Type:** Functional.
  * **Priority:** 2.
  * **Rationale:** The customer gets what they want and to accommodate for any allergies.
  * **Testing:** After an order is placed, we can edit any attributes of the cakes.
* **REQ-3:**
  * **Description:** The user must be able to create a rewards account if they want and be able to log into and logout of that account securely.
  * **Type:** Non-Functional
  * **Priority:** 3
  * **Rationale:** This is for user privacy and if an account is made it can provide rewards (such as a discount) to the user for multiple orders.
  * **Testing:** We create an account for testing purposes and check if we can still log into said account after logging out of it.
* **REQ-4:**.
  * **Description:** After placing an order, the user should be able to enter in their payment information (and if it is a delivery order, the address as well) and the website should process it.
  * **Type:** Functional
  * **Priority:** 1
  * **Rationale:** So that payments can processed properly, the business gets paid for its work,  and so that all deliveries arrive at the correct location.
  * **Testing:** After placing an order, we should expect for a form to appear asking the user for their information and if any of the required information is missing, the site should not continue with the order until it is filled in.
* **REQ-5:**
  * **Description:** The website's backend should be able to store the user's account information into a database system and remember it when a user tries to log in.  
  * **Type:** Functional
  * **Priority:** 2
  * **Rationale:** So that users can properly log into their accounts and the website can keep track of who is ordering in order to give rewards and so that no repeat emails are in the database.
  * **Testing:** We can try making an account with using the same email as another account to see if we are allowed to proceed with the registration or not. If the program is working properly we should get a prompt stating that the email is already being used and to use a different one.
* **REQ-6:**
  * **Description:** The website must check if all required info is entered into the form provided.
  * **Type:** Functional
  * **Priority:** 1
  * **Rationale:** If any of the required info's not entered, the order will be incomplete.
  * **Testing:** We can fill out a form but leave out any required information. If we try to proceed with the order, a prompt would tell us that some information is missing.

* **REQ-7:**
  * **Description:** The website should be organized and include sections such as a menu, pricing, special ordering and contact information sections
  * **Type:** Functional
  * Priority: 4
  * **Rationale:** This will ensure that the website is easy to navigate and that users are able to find exactly what they need. 
  * **Testing:** We can have a third-party (someone other than our group) use the website and provide feedback

* **REQ-8:** 
  * **Description:** The user must be able to cancel their order within one day of placing it. 
  * **Type:** Functional
  * **Rationale:** This will ensure that customers can cancel their orders and get a refund. However, if the order has already been processed and is being made they shouldn't be able to cancel it so putting a one day time limit is important
  * **Testing:** We can place two orders into a list and cancel one immediately while we wait for 2 days to cancel the other.

* **REQ-9:**
  * **Description:** The website must send the a reciept to the customer with order details and a tracking number and an estimaed date of arrival.
  * **Type:** Functional
  * **Rationale:** This is to make sure the user knows when they can expect their order to arrive and have time to cancel or edit their order if they notice
  * **Testing:** Use a email account meant for testing to place and order and ensure 




## Constraints

* Due to some group members having limited knowledge of Html and Javascript, it may take them some time to get the website to look and function like intended.
* Getting the rewards system to work considering that it adds additional information that has to be processed (like how many orders are needed for the next reward) and how to have the user's name already filled in on the order form.
* Getting the authentication process to work, checking if a pre-existing email is entered into the system and the backend of the system remembering to store and remember any information entered.
* Some parts of the code can be hard to understand.
* Trying to work around the schedules of some of the group members.
* Due to the limited amount of time to work, many of non-database features such as customization may not be implemented until very late into the develpment stages.
* Due to the high amount of customizablity that is available to users, there is more room for error
* Since multiple people are working on one project there might be issues with each of us having different machines and different capabilities

## Use Cases

* **UC-1** 
  * **Description:** The user makes an order by clicking on a button/link that takes them to a page where they can choose from a preset cake or create their own custom cake. After choosing their cake, the website then takes them to a page with a form where they have to select the date of the pickup/delivery and if they are not logged into a rewards account, enter in a name for the order. Once that information is filled in, they are taken to a page where they must fill in their debit/credit card information. If any of the required infomation needed is missing from the forms, the user cannot proceed until it is filled in. The website then processes the payment and makes sure that the infomation entered is valid. Once the payment is processed, the user can choose to either pick up their cake in person or have it delivered to a specified location. If they choose to pick it up in person, they are taken to a page where they can locate the closest store location near them to have it made. If they choose to have it delivered, they are instead taken to a form where they are required to fill in the address in which the cake is to be delivered and an approximate time that it should arrive. After filling in all of the required information, the user's order is then complete.
  * **Actors:** Customer/User and Website
  * **Preconditions:** The user must be on the website, in the case of allergies, have an idea of what the cake can and can't have and have a method of payment before they can place an order. The user must also fill in all of the required information in the forms in order to proceed.
  * **Postconditions:** After an order is placed, the customer must have a message stating that their order placed and a receipt and eventually receive their cake. The business must have recieved confirmation that an order has been placed, payment for said order as well as the name placed under it and the date and time it has to be finished and if it is a delivery, the location of the delivery. 
* **UC-2** 
  * **Description:** The user wants to create a rewards account to get special perks. The user clicks a link provided on the website that takes them to a page where they can register. Once on the page, they have to enter in their name as well as a valid email account and a strong password. If the email provided is already in the system, the website must notify the user about this and prompt them to input a different email address. In addition, the user cannot proceed until they have filled in all of the required information. Once the information entered is confirmed to be valid, the website's backend must store it into the system and keep it there. The user is then taken to a login screen where they can enter in the information to log into their newly created account.
  * **Actors:** Customer/User and backend of the website.
  * **Preconditions:** The user must have a valid email account and not be logged in before they can register for a rewards account.
  * **Postconditions:** After the user successfully registers, they must have a rewards account that they can log in and out of. In future orders, they must also receive the rewards promised to them after a certain amount of orders or money spent. The website must have the user's information in the system so that it can verify who the said user is.
* **UC-3**
  * **Description:** The user wants to customize their order. They can choose what flavor of cake and what type of frosting they want. The user is sent to a page that allows them to choose which fillings and toppings they want on their cake. The website will notify if the user wants to add a message on the cake and show a preview of the finished product.
  * **Actors:** Customer/User and Website
  * **Preconditions:** The user must be on the website in order for customization of their cake.
  * **Postconditions:** After customizing their cake, the user will be able to see the final product and the final price.
* **UC-4**
  * **Description:** The user wants to pick up their order. They can choose to pick it up at the nearest shop and enter the state they live in. The website searches for any nearby locations in that state and returns them to the page. The user chooses which shop they wanted and the order will be delivered.
  * **Actors:** Customer/User, Workers, and Website
  * **Preconditions:** The user must be on the website and fill out their order and payment info. The user then selects to pick up their order.
  * **Postconditions:** After selecting the location to pick up their order, the user will receive their order when they arrive. The workers at the location will receive the order and start making it for the customer. The customer will be notified that the order has be sent to the location of the shop.
* **UC-5**
  * **Description:** The user wants to cancel their order. If it has been less than 24 hours since they placed their order, they will see an option to cancel it in the orders section of our site. They can choose that option and confirm to cancel. Also, it will display a pop-up that asks why they chose to cancel their order. Then their order will be refunded and a confirmation will be emailed to them. 
  * **Actors:** Customer/User, backend of the website
  * **Preconditions:** The user must have placed an order using a valid email or phone number and must have opted to cancel it before 24 hours
  * **Postconditions:** The users order should be refunded and an email confirmation must be emailed to them
* **UC-6**
  * **Description:** If a user is not signed up for the rewards program, there will be a pop that allows them to enter their email to sign up for it and also provide a discount on their first order. 
  * **Actors:** Customer/User, backend of the website
  * **Preconditions:** The user must not already be signed up for rewards and also must place their first order to get the discount. 
  * **Poestconditions:** When the user is ready to checkout, the discounted should be applied to their final price


  

## User Stories

* **US-1:**
  * **Type of User:** Customer
  * **Description:** As a customer, I want to be able to customize my cake order not only so it has all of my favorite ingredients but also to account for any allergies that my guests may have. I also expect that the interface to do so is easy to use and has clear details about the final outcome so that I know that I am getting the result I want.
* **US-2** 
  * **Type of User:** Admin
  * **Description:** As a website admin, I need for the website to be able to verify the information provided by any user who wants a rewards account as well as store it properly. This is so that when accounts are made, users are able to log into them and the information remains private.
* **US-3**
  * **Type of User:** Customer
  * **Description:** As a customer, I want to create an account to get some rewards and to see any previous orders that I have made.
* **US-4**
  * **Type of User:** Admin
  * **Description:** As an admin, I need the website to show the user what their cake would look like after they customize it so that they can get an accurate representation of what their cake would be like and if they want to make any changes.
* **US-5**
  * **Type of User:** Admin
  * **Description:** As an admin, I need the website to show when and why a user cancels their order. Once the user submits their cancellation request I must be able to see the reason why they canceled and store it for feedback
* **US-6**
  * **Type of User:** Customer
  * **Description:** As a customer, if I have any specific instructions or customizations that are not available in the given optons, I want the website to provide a text-box where I can specify exactly what I want
  

## Glossary

In this section, you should list any terms that are used in the document that may not be immediately obvious to a naive reader. Each group member must supply at least one term. Each term should be written in the following format:

* **Python:**
  * **A programming language released in 1991 that is focused on user readability and is mainly used for website and software development as well as data analysis and machine learning.**
* **Flask:**
  * **A framework written in Python that allows for the development of web applications.** 
* **Framework:** 
  * **A set of tools and libraries used to help with software development.**
* **Authentication:** 
  * **The process of verifying the identity of a user** 
* **Backend:** 
  * **Part of an application, program, or software system that allows for it to operate and cannot be accessed by users; it is often used for storing and processing data.** 
* **HTML (Hypertext Markup Language):**
  * **A system for tagging text files to achieve effects on webpages**
* **Interface:**
  * **A program that allows the user to communicate with a computer**
* **JavaScript:**
  * **A programming language used to create interactive effects on web browsers**
 * **Frontend:**
  * **The part of an application that directly involves user interactions, aka what the user is able to see on the application**
* **CSS:**
  * **A stylesheet language that tells the browser how the HTML code must look**


