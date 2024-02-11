# AirBnB Clone - The Console

The **AirBnB Clone - The Console** project is a higher-level programming project on ALX Software Engineering program. The project is the first step towards building our first full web application: the AirBnB clone up on which all other forthcoming projects such as HTML/CSS templating, database storage, API, front-end integrationcollectively covers fundamental concepts of higher-level programming will be built up on with the final goal of deploying our server as a simple copy of the AirBnB website.

## Functionalities of This Command Interpreter:

The command interpreter provides the following functionalities:

1. **Create, Retrieve, Update, and Delete (CRUD)** operations for AirBnB objects:
   - Create new instances of classes
   - Retrieval of objects from storage
   - Update of object attributes
   - Deletion of objects

2. **Command-Line Interface (CLI)**:
   - The user interacts with the console via a command-line interface.
   - Commands are entered into the console, and the interpreter processes them.

## Table of Contents:
1. [Environment](#environment)
2. [Installation](#installation)
3. [File Descriptions](#file-descriptions)
4. [Examples of Use](#examples-of-use)
5. [Bugs](#bugs)
6. [Authors](#authors)
7. [License](#license)

## Environment:
- Developed using Python 3.8
- Tested on Ubuntu 20.04

## Installation:
1. Clone this repository:
   ```
   git clone https://github.com/WondwossenH9/AirBnB_clone.git
   ```

2. Run the console:
   ```
   ./console.py
   ```

## File Descriptions:
- **console.py**: main command interpreter.
- **models/**: Classes used for this project.
- **models/engine**:File Storage class that handles JSON serialization and deserialization.
- **tests/**: unit test cases for this project.

### Examples of Use:
1. Creating a new User:
   ```
   (hbnb) create User
   1234-123-123-123-12xy
   ```

2. Listing all objects:
   ```
   (hbnb) all
   ["User.123-14-12-14-167xy"]
   ```

3. Updating an object:
   ```
   (hbnb) update User.1234-123-123-123-12xy first_name "Tom"
   ```

4. Deleting an object:
   ```
   (hbnb) destroy User.1234-123-123-123-12xy
   ```

## Bugs:
- No known bugs at the moment.

## Authors:
- Wondwossen Tekle
- Bisrat Tadesse

## License:
This project is licensed under the ALX Software Engineering Holberton School
