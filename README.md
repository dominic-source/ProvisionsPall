# ProvisionsPal

## Overview

This repository contains the source code for ProvisionsPal, a web application that enables users to estimate distances between stores and their current location using geocaching.

## Features

- **User Management:** Register, log in, and manage user profiles.
- **Store Management:** Add, edit, and delete store information.
- **Address Management:** Users and stores can have multiple addresses.
- **Geocaching:** Utilizes geocaching to estimate the distance between stores and the user's current location.

## Technologies Used

- Flask: A lightweight web application framework.
- SQLAlchemy: An SQL toolkit and Object-Relational Mapping (ORM) library.
- Javascript
- SQLLite
- HTML/CSS

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/your-username/ProvisionsPal.git
cd ProvisionsPal

API Endpoints
/users: [GET, POST, PUT, DELETE] - Manage user information.
/stores: [GET, POST, PUT, DELETE] - Manage store information.
/products: [GET, POST, PUT, DELETE] - Manage product information.
/user_addresses, /store_addresses: [GET, POST] - Manage user and store addresses.
/geocaching: [POST] - Calculate estimated distance between stores and user's location.
