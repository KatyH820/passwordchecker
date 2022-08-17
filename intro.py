# Check if your password has ever been hack.
# terminal: python3 checkmypass.py password1 password2 ...
import requests

# This project use tool and concept below:
#     Have I Been Pwned APIv2
#     K-Anonymity
#     SHA1 password Hash

# requests module allow us to make a request
# we can manually request something as if we have a browser and get some data back

# Hash function is simply a function that generates a value of fixed length for each input that it gets
# there are different type of hash function
# hash is one way, this mean if i give someone the hashed output they wont know the original input
# the same input will always give the same output
# this is idempotent
# Idempotent is where you call the same function with the same value and the result is exactly the same
# Hash table is a data structure which stores data in an assocative manner
# In a hash table, data is stored in an array format, where each data value has its own unique index value
# We can access data knowing the index
# Hash table uses a hash function to compute an index into an array of slots from which the desired value can be found
# when we want to store something into the hash table, it first run the key with hash function and determine where the value will be store based on the index output from hash function


# password is hashed to be more secured avoid direct sending our password to the internet
# K anonymity allows somebody to receive information about us yet still not know who we are
# ---Only give the first five characters of our hash password
# ---if you do this, the api is going do has a list of all the passwords that have been leaked
# ---and find the passwords that have the first five characters that match the input
# ---API return the tails (the things after the first five)
# ---this way we will get all the passwords that are hacked that have the same first five hashed character
# ---so that on our end, when we receive that response, we can check the rest of the hash function
# ---this way the api will never going to know our full hash and therefore never be able to guess our password
url = 'https://api.pwnedpasswords.com/range/' + \
    'CBFDA'  # that is why we only give first five here
res = requests.get(url)
print(res)
