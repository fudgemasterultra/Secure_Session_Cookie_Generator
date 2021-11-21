# Secure Session Cookie Generator
Create Secure User Session Cookies Swiftly

## Why make this?
To help generate a more "random" cookie sequence. As developers, we aren't really able to use the inbuilt random function because it wasn't made with security in mind; we try to generate our own seeds for the random function, but that's a pretty difficult task, too. So that's where the Secure Session Cookie Generator comes in.

## Quick Start
```py
from Mixing_Bowl import GetIngrediants

#You must first initialize the GetIngredients class; this will pull your system data
#and get it ready to turn that into your seed.
#It does have an optional argument "raisins" that can be provided a str or anything that can be turned into a str.
person = GetIngredients("An Optional Random Seed")

#This will "bake the cookie" for you. 
#You can specify a cookie_size, but it defaults to 300.
#This function will return a string that will be ready for you serve to your user.
person.Bake_Cookies(cookie_size=10_000)

```

## How to install
You can either pull the repo or download the Mixing_Bowl.py file and import it into your project that way. 

## Requirements
python <= 3.7

## Standard Libraries Used
uuid, hashlib, platform, time, string, random
