# Project Setup and Execution

Follow these steps to set up the Python environment, install dependencies, and run the Python scripts using a virtual environment.

## Steps to Install and Run

### 1. Create a Python Virtual Environment

To create a Python virtual environment for the project, run the following command:

`python -m venv ./venv`


### 2. Install Project Dependencies

After creating the virtual environment, install the required dependencies.

#### Activate the Virtual Environment

On Windows:

`.\venv\Scripts\activate`


Once activated, you should see `(venv)` at the start of the command line, indicating that the virtual environment is active.

#### Install Dependencies

With the virtual environment active, install all dependencies from `requirements.txt`:

`pip install -r requirements.txt`


### 3. Run the Batch Script

After installing the dependencies, run the batch script to execute the Python scripts (`sender.py` and `receiver.py`).

#### Run `run.bat`

Execute the batch file with the following command:

`.\run.bat`

## Project Structure

Ensure your project follows this structure:

```bash
my_project/
├── templates/
│   ├── display.html
│   └── index.html
├── venv/                 # Virtual environment folder
├── sender.py             # Sender Python script
├── receiver.py           # Receiver Python script
├── requirements.txt      # List of dependencies
├── run.bat               # Batch file to run the scripts
└── README.md             # This file
```

