# MIT License
#
# Copyright (c) 2017 Vladimir Kristally
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from argparse import ArgumentParser
from cryptography.fernet import Fernet

if __name__ == '__main__':

    # Set up argument parser and parse args...
    parser = ArgumentParser()
    parser.add_argument("mode", action="store", help="lock / unlock")
    parser.add_argument("input", action="store", help="the file to be locked / unlocked")
    args = parser.parse_args()

    # Establish variables for args...
    mode = args.mode
    input_filename = args.input

    # Lock / Unlock input file...
    if str.lower(mode) == "lock":

        # Generate key and initialize Fernet instance...
        key = Fernet.generate_key()
        fernet = Fernet(key)

        # Open input file and store contents in memory...
        input_file = open(input_filename, "rb")
        input_file_content = input_file.read()
        input_file.close()

        # Open input file & erase for security...
        open(input_filename, "w").close()

        # Open input file & write encrypted contents...
        input_file = open(input_filename, "w")
        input_file.write(str(fernet.encrypt(input_file_content), "utf-8"))
        input_file.close()

        # Save key file...
        key_output_filename = input_filename + ".key"
        key_output_file = open(key_output_filename, "w")
        key_output_file.write(str(key, "utf-8"))
        key_output_file.close()

        # Notify user that the task has been completed successfully.
        print("Done! File '{0}' has been locked, key saved to '{1}'.".format(input_filename, key_output_filename))

    if str.lower(mode) == "unlock":

        # Read key and initialize Fernet instance...
        key_file = open(input_filename + ".key", "r")
        key = key_file.read()
        fernet = Fernet(key)

        # Open input file and store contents in memory...
        input_file = open(input_filename, "rb")
        input_file_content = input_file.read()
        input_file.close()

        # Open input file & erase for security...
        open(input_filename, "w").close()

        # Open input file & write encrypted contents...
        input_file = open(input_filename, "w")
        input_file.write(str(fernet.decrypt(input_file_content), "utf-8"))
        input_file.close()

        # Notify user that the task has been completed successfully.
        print("Done! File '{0}' has been unlocked.".format(input_filename))
