# NBS_Work
All the stuff I've done during my first internship at NeoByteServices

## Warranty Checker
### Initial Problem
I had to make an inventory of all the computer for a company, and manually check for the warranty of each machine.

### Thinking Chain
I first discovered that the "official" Dell API was restricted to dell-registered developer.
I then wanted to take a look at the way the Dell website worked and which queries where used to fetch warranty status.

After few moments, I was able to fetch warranty of a computer based on his S/N (Serial Number) with cURL.

I just re-wrote all the code into Google AppScript to create a custom function into the Sheets page where the inventory was stored and took a little coffee.

### How it works ?
I noticed that I was able to query some Dell-linked website by only passing session cookie (```DellCEMSession```) in the header.
Moreover, the ```DellCEMSession``` seems to be persistent (some "session" cookies I created 3 month ago are still usable)

So the first step is to query this address : ```https://www.dell.com/support/components/detectproduct/encvalue/<SERIAL_NUMBER>?appname=warranty```
Where *<SERIAL_NUMBER>* has to replaced with the actual one.

This website return a hashed version of this serial number that looks like this : ```ABC1jt34B539dc09H8f22028v2FNDJ29c```, 
and then this hashed S/N can be used to query this address : ```https://www.dell.com/support/components/servicestore/fr-fr/ServiceStore/GetEligiblePONOffers?serviceTag=<HASHED_SN>```
This last website return JSON data : ```{"IsInWarranty":true/false,"IsEligiblePONOffers":true/false}``` that indicates if the warranty is still active or not.
