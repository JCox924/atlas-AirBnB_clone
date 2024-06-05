# AirBnB Clone Project

## Description
This project is an AirBnB clone, developed as part of the Atlas School curriculum. The goal is to build a full web application, encompassing front-end and back-end development, database storage, and API integration. The project starts with the development of a command interpreter to manage the AirBnB objects, such as users, states, cities, places, amenities, and reviews.

## Command Interpreter
The command interpreter is a console application that allows users to create, update, destroy, and manage various objects within the AirBnB clone. It provides a way to interact with the application via a command-line interface.

### How to Start It
1. Clone the repository to your local machine:
    ```sh
    git clone https://github.com/JCox924/atlas-AirBnB_clone
    cd atlas-AirBnB_clone
    ```

2. Make the `console.py` script executable:
    ```sh
    chmod +x console.py
    ```

3. Start the command interpreter:
    ```sh
    ./console.py
    ```

### How to Use It
The command interpreter supports several commands to manage the application objects. Here is a list of available commands and their usage:

- **help** or **?**
    - Displays a list of available commands or detailed help for a specific command.
    ```sh
    (hbnb) help
    (hbnb) help <command>
    ```

- **quit** or **EOF**
    - Exits the command interpreter.
    ```sh
    (hbnb) quit
    (hbnb) EOF
    ```

- **create <class>**
    - Creates a new instance of a class, saves it to the JSON file, and prints the ID.
    ```sh
    (hbnb) create User
    ```

- **show <class> <id>**
    - Prints the string representation of an instance based on the class name and ID.
    ```sh
    (hbnb) show User 1234-1234-1234
    ```

- **destroy <class> <id>**
    - Deletes an instance based on the class name and ID.
    ```sh
    (hbnb) destroy User 1234-1234-1234
    ```

- **all [<class>]**
    - Prints all string representations of all instances, or all instances of a specific class.
    ```sh
    (hbnb) all
    (hbnb) all User
    ```

- **update <class> <id> <attribute name> "<attribute value>"**
    - Updates an instance based on the class name and ID by adding or updating an attribute.
    ```sh
    (hbnb) update User 1234-1234-1234 email "aibnb@mail.com"
    ```

### Examples
Here are some examples of how to use the command interpreter:

- **Creating a new User**
    ```sh
    (hbnb) create User
    6f0c4e8e-b33f-4b22-bc17-86cf1d938908
    ```

- **Showing a User instance**
    ```sh
    (hbnb) show User 6f0c4e8e-b33f-4b22-bc17-86cf1d938908
    [User] (6f0c4e8e-b33f-4b22-bc17-86cf1d938908) {'id': '6f0c4e8e-b33f-4b22-bc17-86cf1d938908', 'created_at': '2024-01-01T12:00:00', 'updated_at': '2024-01-01T12:00:00', 'email': '', 'password': '', 'first_name': '', 'last_name': ''}
    ```

- **Updating a User instance**
    ```sh
    (hbnb) update User 6f0c4e8e-b33f-4b22-bc17-86cf1d938908 email "aibnb@mail.com"
    ```

- **Destroying a User instance**
    ```sh
    (hbnb) destroy User 6f0c4e8e-b33f-4b22-bc17-86cf1d938908
    ```

- **Showing all User instances**
    ```sh
    (hbnb) all User
    ```

The command interpreter is a powerful tool to manage the objects within the AirBnB clone project. You can use it to create, read, update, and delete objects, making it essential for interacting with the application backend.

