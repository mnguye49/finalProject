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

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Constraints](#constraints)
4. [Use Cases](#use-cases)
5. [User Stories](#user-stories)
6. [Glossary](#glossary)

## Introduction

In this section, you should give a brief overview of what your project will be. Describe the software system you are building and what problems it solves. You should also give a short description of the stakeholders (users of the system) and what their needs are. There is no set formatting requirement, but you should maintain a consistent structure across future sections. Not all members must contribute to this section. 


Our final project will be a website for a cake business where the customers can order and customise their own cakes that can be delivered to their homes and other locations. Due to the internet evolving, more and more businesses are adding their services onto online platforms in order to expand. In addition, some customers may not have a means of transportation for reasons and may need their goods to be delivered to them.

## Requirements

Each group member must supply at least three functional requirements for the project. Each requirement should be written in the following format:

* **ID:** A unique identifier for the requirement. This should be a number that is unique across the entire document (something like REQ-1, REQ-2, etc. but be sure to replace the word `ID` with the unique identifier).
  * **Description:** A short description of the requirement. This should be a single sentence that describes the requirement. Do not replace the word `Description` with the actual description. Put the description in the space where these instructions are written. Maintain that practice for all future sections.
  * **Type:** The type of requirement. Should be either `Functional` or `Non-Functional`.
  * **Priority:** The priority of the requirement. This should be a number between 1 and 5, with 1 being the highest priority and 5 being the lowest priority.
  * **Rationale:** A short description of why the requirement is important. This should be a single sentence that describes why the requirement is important.
  * **Testing:** A short description of how the requirement can be tested. This should be a single sentence that describes how the requirement can be tested.

* **REQ-1:** A unique identifier for the requirement. This should be a number that is unique across the entire document (something like REQ-1, REQ-2, etc. but be sure to replace the word `ID` with the unique identifier).
  * **Description:** The user must be able to place an order.
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
  * **Testing:** We can fill out a form but leave out any required info. If we try to proceed with the order, a prompt would tell us that some info is missing.


## Constraints

In this section, you should list any constraints that you have for the project. Each group member must supply at least two constraints. These can be constraints on the project itself, the software system, or the stakeholders. Constraints can be anything that limits the scope of the project. For example, that this project's template code is written using Flask and Python constitutes a constraint on the backend of the project. Constraints can also be things like the required timeline of the project. Be creative.

* Due to some group members having limited knowledge of Html and Javascript, it may take them some time to get the website to look and function like intended.
* Getting the rewards system to work considering that it adds additional information that has to be processed (like how many orders are needed for the next reward) and how to have the user's name already filled in on the order form.
* Getting the authentication process to work, checking if a pre-existing email is entered into the system and the backend of the system remebering to store and remeber any information entered.
* Some parts of the code can be hard to understand.
* Trying to work around the schedules of some of the group members.

## Use Cases

In this section, you should list use cases for the project. Use cases are a thorough description of how the system will be used. Each group member must supply at least two use cases. Each use case should be written in the following format:

* **ID:** A unique identifier for the use case. This should be a number that is unique across the entire document (something like UC-1, UC-2, etc. but be sure to replace the word `ID` with the unique identifier).
  * **Description:** A description of the use case that gives the user a high-level overview of how the system is interacted with.
  * **Actors:** A list of the actors that are involved in the use case. Only include the actors that are directly involved. Actors are the people or things that interact with the system. For example, when ordering at a fast food restaurant, one might have the following actors: the customer, the cashier, and the cook. But only the customer and the cashier are directly involved in the use case of ordering food. The cook is not directly involved in the use case of ordering food.
  * **Preconditions:** A list of the preconditions for the use case. This should be a list of the preconditions for the use case, which are the conditions that must be met before the use case can be executed. Continuing with the restaurant example, the customer must have money in their wallet and the cashier must be logged in to the system before the use case of ordering food can be executed.
  * **Postconditions:** A list of the postconditions for the use case. This should be a list of the postconditions for the use case, which are the conditions that must be met after the use case has been executed. Continuing with the restaurant example, the customer must have their food and the cashier must have the customer's money after the use case of ordering food has been executed.

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
  * **Description:** The user wants to customize their order. They can choose what flavor of cake and what type of frosting they want. The user is sent to a page that allows them to choose which fillings and toppings they want on their cake.

## User Stories

In this section, you should list user stories for the project. User stories are a short description of how a user will be interacting with the system. Each group member must supply at least two user stories. Each user story should be written in the following format:

* **ID:** A unique identifier for the user story. This should be a number that is unique across the entire document (something like US-1, US-2, etc. but be sure to replace the word `ID` with the unique identifier).
  * **Type of User:** The type of user that the user story is for. This should be a single word that describes the type of user. For example, a user story for a customer might be `Customer` and a user story for an administrator might be `Admin`.
  * **Description:** A description of the user story that gives a narrative from that user's perspective. This can be any length, but it must paint the picture of what the user wants to do, how they intend to do it, why they want to, and what they expect to happen.

* **US-1:**
  * **Type of User:** Customer
  * **Description:** As a customer, I want to be able to customize my cake order not only so it has all of my favorite ingredients but also to account for any allergies that my guests may have. I also expect that the interface to do so is easy to use and has clear details about the final outcome so that I know that I am getting the result I want.
* **US-2** 
  * **Type of User:** Admin
  * **Description:** As a website admin, I need for the website to be able to verify the information provided by any user who wants a rewards account as well as store it properly. This is so that when accounts are made, users are able to log into them and the information remains private.

## Glossary

In this section, you should list any terms that are used in the document that may not be immediately obvious to a naive reader. Each group member must supply at least one term. Each term should be written in the following format:

* **Authentication:** 
  * **The process of verifying the identity of a user** 
* **Backend** 
  * **Part of an application, program, or software system that allows for it to operate and cannot be accessed by users; it is often used for storing and processing data.** 
