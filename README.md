## About

This project is a simple file locker & unlocker implemented in Python.
Files are encrypted using Fernet encryption with random keys generated
upon encryption.

The concept of this application is to provide a means of locking files
on a shared or public computer to restrict access to individuals with
the key, while not having to remove the files from the computer.

Upon locking a file, the key is saved to a file in the same directory as
the file being locked.  It is the responsibility of the user to make a
copy of this file on a flash drive or in the cloud and then remove it.


## Usage

Lock a file:

`python flocker.py lock <file>`

Unlock a file:

`python flocker.py unlock <file>`

When unlocking a file, the keyfile generated upon locking that file must
be present in the same directory as the file being unlocked.

## Dependencies

https://github.com/pyca/cryptography

## License

MIT License

Copyright © 2017 Vladimir Kristally

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the “Software”), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.