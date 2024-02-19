# ProvisionsPal

## Overview

This repository contains the source code for ProvisionsPal, a web application that enables users to connect with businesses and get their location for easy access.

## Visit our application at the marketplace
[Visit us here](https://provisionspall.onrender.com/market)

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
- SQLite
- HTML/CSS

## Installation (local installation)

1. Clone the repository:

```bash
git clone https://github.com/your-username/ProvisionsPal.git
cd ProvisionsPal
```

2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
pip3 -r install requirements.txt
python3 -m provisionspall_web.app
```
3. Create another terminal for the API service and enter this command

```bash
python3 -m api.v1.app
```

## Basic specification for API(to be updated soon)

**Manage user information.**
- https://provisionspall.onrender.com/api/v1/users: [GET] 
- https://provisionspall.onrender.com/api/v1/user/<id>: [GET] 
- https://provisionspall.onrender.com/api/v1/user: [POST]
- https://provisionspall.onrender.com/api/v1/user/<id>: [PUT]
- https://provisionspall.onrender.com/api/v1/user/<id>: [DELETE]

**Manage store information.**
- https://provisionspall.onrender.com/api/v1/user/store/<store_id>: [DELETE, OPTIONS] 
- https://provisionspall.onrender.com/api/v1/user/<user_id>/stores: [GET, POST, PUT, OPTIONS]
- https://provisionspall.onrender.com/api/v1/stores: [GET, POST, PUT, OPTIONS]

**Manage product information.**
- https://provisionspall.onrender.com/api/v1/<store_id>/product: [GET, POST]
- https://provisionspall.onrender.com/api/v1/product/<product_id>: [GET, PUT, DELETE]

**Get addresses and location**
- https://provisionspall.onrender.com/api/v1/locate/<store_id>: [GET]
- https://provisionspall.onrender.com/api/v1/all_stores: [GET]

## Screenshot of Login page
![Screenshot of our web application](https://github.com/dominic-source/ProvisionsPall/blob/master/provisionspall_web/static/images/Screenshot%20from%202023-12-12%2019-42-04.png)

## Screenshot of Dashboard page
![Screenshot of our web application](https://github.com/dominic-source/ProvisionsPall/blob/master/provisionspall_web/static/images/Screenshot%20from%202023-12-12%2019-42-26.png)

## Screenshot of Dashboard page showing the edit details section
![Screenshot of our web application](https://github.com/dominic-source/ProvisionsPall/blob/master/provisionspall_web/static/images/Screenshot%20from%202023-12-12%2019-42-53.png)

## Screenshot of Market place for all users
![Screenshot of our web application](https://github.com/dominic-source/ProvisionsPall/blob/master/provisionspall_web/static/images/Screenshot%20from%202023-12-12%2019-43-35.png)

## Licence
