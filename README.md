# NBS_Work
All the stuff I've done during my first internship at NeoByteServices

## Warranty Checker
### Initial Problem
I had to make an inventory of all the computer for a company, and manually check for the warranty of each machine.

### Thinking Chain
I first discovered the "official" Dell API that was restricted to dell-registered developer.
I then wanted to take a look at the way the Dell website worked and which queries where used to fetch warranty.
After few moments, I was able to fetch warranty of a computer based on his serial number (with cURL)

I just re-wrote all the code into Google AppScript to create a custom function into the Sheets page where the inventory was stored and took a little coffee.

### How it works ?
I noticed that I was able to query some Dell-linked website by only passing session cookie (```DellCEMSession```) in the header.
Moreover, the ```DellCEMSession``` seems to be persistent (some "session" cookies I created 3 month ago are still usable)

So I discovered this address : https://www.dell.com/support/components/detectproduct/encvalue/<serial_number>?appname=warranty
Where serial number has to replaced with the actual serial number

That return a hashed version of this serial number that looks like this : ```RXFjT1pQblpXLzYrWWlVbkw3VitsUT090```, 
and then this hashed S/N can be used to query this address : https://www.dell.com/support/components/servicestore/fr-fr/ServiceStore/GetEligiblePONOffers?serviceTag=<hashed_sn>
This last website return json data : ```{"IsInWarranty":true/false,"IsEligiblePONOffers":true/false}``` that indicates that the warranty is still active or not.
