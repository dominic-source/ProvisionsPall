# ProvisionsPal

## Overview

This repository contains the source code for ProvisionsPal, a web application that enables users to estimate distances between stores and their current location using geocaching.

## Features

- **User Management:** Register, log in, and manage user profiles.
- **Store Management:** Add, edit, and delete store information.
- **Address Management:** Users and stores can have multiple addresses.
- **Product Management:** Store owners can create, update, and delete products. 
- **Geocaching:** Utilizes geocaching to estimate the distance between stores and the user's current location.

## Technologies Used

- Flask: A lightweight web application framework.
- SQLAlchemy: An SQL toolkit and Object-Relational Mapping (ORM) library.
- Javascript
- SQLLite
- HTML/CSS

## Installation (local installation)

1. Clone the repository:

```bash
git clone https://github.com/your-username/ProvisionsPal.git
cd ProvisionsPal
```

2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
python3 -m provisionspall_web.app
```
3. Create another terminal for the API service and enter this command

```bash
python3 -m api.v1.app
```

## Usage
-  Enter this on your browser: http://127.0.0.1:5000


Some API Endpoints
/users: [GET, POST, PUT, DELETE] - Manage user information.
/stores: [GET, POST, PUT, DELETE] - Manage store information.
/products: [GET, POST, PUT, DELETE] - Manage product information.
/user_addresses, /store_addresses: [GET, POST] - Manage user and store addresses.
/geocaching: [POST] - Calculate estimated distance between stores and user's location.

## Screenshot of Login page
![Screenshot of our web application](https://github.com/dominic-source/ProvisionsPall/blob/master/provisionspall_web/static/images/Screenshot%20from%202023-12-12%2019-42-04.png)

## Screenshot of Dashboard page
![Screenshot of our web application](https://github.com/dominic-source/ProvisionsPall/blob/master/provisionspall_web/static/images/Screenshot%20from%202023-12-12%2019-42-26.png)

## Screenshot of Dashboard page showing the edit details section
![Screenshot of our web application](https://github.com/dominic-source/ProvisionsPall/blob/master/provisionspall_web/static/images/Screenshot%20from%202023-12-12%2019-42-53.png)

## Screenshot of Market place for all users
![Screenshot of our web application](https://github.com/dominic-source/ProvisionsPall/blob/master/provisionspall_web/static/images/Screenshot%20from%202023-12-12%2019-43-35.png)

## Licence
