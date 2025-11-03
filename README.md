# pyAno

pyAno is a simple command-line application for managing a collection of pianos. It allows users to view a list of pianos with their details. The application is built using Python and follows a layered architecture.

The application's source code, including comments and console output, is written in Croatian.

## Features

*   Display a list of all pianos with details.
*   Layered architecture (Core, Infrastructure, Services, Utils).
*   Command-line interface.

## Project Structure

The project is organized into the following directories:

*   `core/`: Contains the core data models of the application.
*   `infrastructure/`: Handles data access and communication with the database.
*   `services/`: Contains the business logic of the application.
*   `utils/`: Provides utility functions, such as database connection.
*   `main.py`: The main entry point of the application.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/zerixmax/pyAno
    ```
2.  Navigate to the project directory:
    ```bash
    cd pyAno
    ```
3.  Install the dependencies (assuming they are listed in `pyproject.toml` or a `requirements.txt` file):
    ```bash
    pip install -r requirements.txt 
    ```
    *(Note: You may need to create a `requirements.txt` file if one does not exist)*

## Usage

To run the application, execute the following command in the project's root directory:

```bash
python main.py
```

This will start the command-line interface, where you can choose from the available options.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or find any bugs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
