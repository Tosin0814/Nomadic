# Nomadic

- Nomadic is a Django web application, where hosts rent out their properties to travellers looking for a place to stay.


# Screenshots

## Landing Page

<img src = "main_app/static/images/markdown/Landing page.png">

- A not logged in user can view all listed properties - with the property title, location, and price.

## My Profile Page

<img src = "main_app/static/images/markdown/My Profile.png">

- A logged in user has access to user profile page, the user can add/edit profile photo, and edit user information.

- In profile page, the user can check out their 'Posted Properties' - As the Host.

- In profile page, the user can also check out their 'Liked Properties' - As the traveller.

## Host Adding Properties & Modifying 'Posted Property' Detail Page

<img src = "main_app/static/images/markdown/Add Property.png">

- The host inputs basic property information on the 'Add Property' page.

<img src = "main_app/static/images/markdown/Property Detail - Host 1.png">
<img src = "main_app/static/images/markdown/Property Detail - Host 2.png">

- On the property detail page, the host can;

    - Add/edit property photos
    - Edit/delete property information
    - Add/delete property features - features are defined by admin and cannot modify by user
    - Add/update/delete Availability for travellers

## Traveller Checking Out Property Details & Making Reservation on Property

<img src = "main_app/static/images/markdown/Property Detail - Traveller 1.png">
<img src = "main_app/static/images/markdown/Property Detail - Traveller 2.png">

- On the property detail page, the traveller can;

    - Check out the host's information and property information
    - Check out property features
    - Make/cancel reservation on the property based on the availability
    - Leave a review and rating for the host & property

## My Reservations Page for Traveller

<img src = "main_app/static/images/markdown/My Reservation.png">

- Traveller can check out the reservation information on the properties they reserved. 


# Technologies Used

- HTML
- Python
- django
- PostgreSQL
- JavaScript
- Boostrap
- CSS
- AWS S3
- Heroku


# Getting Started

- The link to Nomadic deployed on Heroku, can be found below.

    https://nomadic-app.herokuapp.com/ 


# Next Steps

- Average rating of property listing
- Make Nomadic mobile friendly
- Search by name, user or location
- Upload multiple photos at once

