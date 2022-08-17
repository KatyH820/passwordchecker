import requests
import hashlib
import sys


def request_api_data(query_char):
    # query_char is the first five character of the hashed password
    url = 'https://api.pwnedpasswords.com/range/'+query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the api and try again')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for hash, count in hashes:
        if hash_to_check == hash:
            return count
    return 0


def pwned_api_check(password):
    # hash.hexdigest returned string containing only hexadecimal digits
    # do the above to agree with the API standard
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    number_leaks = get_password_leaks_count(response, tail)
    return number_leaks


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if int(count) > 0:
            print(
                f'{password} was found {count} times... you should change your password')
        else:
            print(f'{password} was not found. Carry on!')
    return 'done'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))  # with sys.exit it will give return
