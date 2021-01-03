# Password-Manager

## Requirements

* Python 3.X
* PGP public and private key

## Overview

* This program stores account details in a PostgreSQL db.
* It stores username, email, password and website. In that order.
* The password is encrypted with PostgreSQL's pgcrypto package.

## Quickstart

* Generate PGP public and private key.
* If you don't know how, here is a tutorial: https://kb.b3networks.com/article/h4h804k2q1-generate-public-and-private-key
* Memorize your passphrase or write it down, it's your master password.
* Put ``privkey.asc`` and ``pubkey.asc`` in ``resources`` folder.
* Create a PostgreSQL database with name password and with following schema:  
   username VARCHAR,  
   email    VARCHAR,  
   pw       VARCHAR,  
   website  VARCHAR  
* You can add a UNIQUE constraint for email and website if you want.
* Execute ``main.py`` for storing, deleting or retrieving passwords.



   
