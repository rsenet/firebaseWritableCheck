# About firebaseWritableCheck

**firebaseWritableCheck** was written in order to help any mobile penetration testers to identify write access to a Firebase endpoint.

## Usage

Disclaimer: The provided software is meant for educational purposes only. Use this at your own discretion, the creator cannot be held responsible for any damages caused. Please, use responsibly!

Print the help to get all necessary information

```bash
$ python3 firebaseWritableCheck.py 

usage: firebaseWritableCheck.py [-h] [--url URL]

Firebase Write Access Checker

optional arguments:
  -h, --help  show this help message and exit
  --url URL   Specify the firebase URL
```

You just have to specify the Firebase Endpoint to know if it is writable or not. If it is, read access will also be checked:

```bash
$ python3 firebaseWritableCheck.py --url https://in-firebase-683e6.firebaseio.com/Logs.json
>> https://in-firebase-683e6.firebaseio.com/Logs.json has been created (write permission is allowed)
>> https://in-firebase-683e6.firebaseio.com/Logs.json is NOT readable (read permission is NOT allowed)
```

## Author

Régis SENET ([rsenet](https://github.com/rsenet))


## Contributing

Bug reports and pull requests are welcome on [GitHub](https://github.com/rsenet/firebaseWritableCheck).

## License

The project is available as open source under the terms of the [GPLv3](https://www.gnu.org/licenses/quick-guide-gplv3.en.html)
