![Logo_Hmachacom](https://i.imgur.com/rgewHiz.png)

## 0x0C. Python - Almost a circle

The objective of this project is to learn about the Class that can be used in PYTHON.

### Table of Contents

- Documentation
- Requirements
- Files
- Functions
- Credits

### Documentation

- [Args/kwargs](https://intranet.hbtn.io/rltoken/LroIjBBI5Gqq3ciR-OHmxg "args/kwargs")
- [JSON encoder and decoder](https://intranet.hbtn.io/rltoken/TY4rfu2AZtXlRmPVNZm1Lw/ "JSON encoder and decoder")
- [Unittest module](https://intranet.hbtn.io/rltoken/T7uxwxtGdbRRW9pkD4eO0g/ "unittest module")
- [Python test cheatsheet](https://intranet.hbtn.io/rltoken/SfEo3RQeAXXYI9yabFRw3g/ "Python test cheatsheet")
- [Unittest module](https://intranet.hbtn.io/rltoken/T7uxwxtGdbRRW9pkD4eO0g/ "unittest module")

### Requirements

### Python Scripts

- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly ```#!/usr/bin/python3```
- A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should be documented: ``python3 -c 'print(__import__("my_module").__doc__)'``
- All your classes should be documented: ``python3 -c 'print(__import__("my_module").MyClass.__doc__)'``
- All your functions (inside and outside a class) should be documented: ``python3 -c 'print(__import__("my_module").my_function.__doc__)'`` and ``python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'``
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Files

|Folder  |   File          | Description   |
|--------|-----------------|---------------|
| models |base.py          |Main class     |
| models |rectangle.py     |Secondary class|
| models |square.py        |Secondary class|

|Folder             |File              | Description            |
|-------------------|------------------|------------------------|
| tests/test_models | test_base.py     |Test for Class Base     |
| tests/test_models | test_rectangle.py|Test for Class Rectangle|
| tests/test_models | test_square.py   |Test for Class Square   |
| test              | \_\_init__.py    |Packet Indicator        |

### Functions

#### For base.py

|Function           |    Description        |Return     |
|------------------|----------------------- |-----------|
|\_\_init__        |Attribute initialization| N/A|
|to_json_string    | Static method          | that returns the JSON string representation of ``list_dictionaries``|
|save_to_file|Class method  | that writes the JSON string representation of ``list_objs to a file``|
|from_json_string|Static method  | that returns the list of the JSON string representation ``json_string``|
|create|Class method |  that returns an instance with all attributes already set|
|load_from_file |Class method|returns a list of instances|

#### For rectangle.py

|Function           |    Description        |Return     |
|------------------|----------------------- |-----------|
|\_\_init__        |Attribute initialization| N/A       |
|super().\_\_init__(id)|Attribute initialization the class main|N/A       |
|width| property |private attributes|
|width|setter|raise an exception ``if width != int or width <= 0```|
|height| property |private attributes|
|height|setter|raise an exception ``if width != int or width <= 0```|
|x| property |private attributes|
|x|setter|raise an exception ``if width != int or width <= 0```|
|y| property |private attributes|
|y|setter|raise an exception ``if width != int or width <= 0```|
|area| public method | that returns the area value of the Rectangle instance.|
|display|public method|that prints in stdout the Rectangle instance with the character #|
|\_\_str__|public method|method so that it returns ``[Rectangle] (<id>) <x>/<y> - <width>/<height>``
|update|public method|that assigns a key/value argument to attributes|
|to_dictionary|public method|that returns the dictionary representation of a ``Rectangle``|
