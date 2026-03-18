# Ironman Suit Control System

A Python-based command-line interface (CLI) application that simulates the control of an Ironman suit with authentication and operational features.

## Overview

This project provides an interactive interface to control a virtual Iron Man suit with various operations. The system includes password-based authentication to secure access to critical suit functions.

## Features

- **Authentication System**
  - Create and manage suit access passwords
  - Update existing passwords
  - Secure login interface

- **Suit Operations**
  - **Fly**: Initiate ignition and take the suit into the air with a 5-second countdown
  - **Land**: Safely land the suit with a 10-second controlled descent
  - **Launch Missile**: Deploy missile systems
  - **Exit**: Safely exit the control interface

- **Interactive Interface**
  - Real-time user prompts and feedback
  - Status tracking (flying/landed)
  - Input validation and error handling

## Project Structure

```
Ironman_Suit/
├── interface.py              # Main user interface and control loop
├── ironman_operations.py     # Suit operations (fly, land, missile launch)
├── Access.py                 # Authentication and password management
├── utils.py                  # Utility functions
├── tasks.txt                 # Development log and updates
└── testing_codes/            # Unit tests and testing utilities
    └── unit_testing.py
```

### File Descriptions

- **interface.py**: Main CLI application that orchestrates user interactions and suit operations
- **ironman_operations.py**: Core class `ironman_op` that handles all suit operations with timed sequences
- **Access.py**: Authentication classes for password management and interface access control
- **utils.py**: Helper functions and shared utilities

## Installation

1. Clone or download this project to your local machine
2. Ensure Python 3.x is installed on your system
3. Navigate to the project directory
4. (Optional) Create a virtual environment:
   ```bash
   python -m venv env
   env\Scripts\activate
   ```

## Usage

Run the main interface:

```bash
python interface.py
```

### Getting Started

1. **Create a Password**: Select option 1 to set up your suit access password
2. **Login**: Use your password to access the suit controls
3. **Select Operations**:
   - Option 1: Fly the suit (5-second countdown)
   - Option 2: Land the suit (10-second descent)
   - Option 3: Launch missile
   - Option 4: Exit the system

### Example Session

```
Hello Welcome to VS Technology

1. Create Password
2. Update Password
Choose any number to Login
Enter Your Option: 1
Create a Password: mypassword123
Password Created

(After creating password)
Enter Password to Access Interface: mypassword123
Access Granted

Welcome Sir select Operations
Operations:
1. Fly
2. Land
3. Launch Missile
4. exit
Enter here: 1
```

## Requirements

- Python 3.6+
- No external dependencies required (uses only Python standard library)

## Development Status

### Recent Updates (April 2026)
- Implemented Iron Man operations (fly, land, missile launch)
- Created secure authentication system
- Developed interactive interface
- Currently under optimization and refinement

### Planned Improvements
- Optimize loops in missile launch function
- Improve terminal UI and formatting
- Add advanced suit features
- Implement persistent data storage for passwords
- Add comprehensive unit tests

## Testing

Unit tests are available in the `testing_codes/` directory. Run tests with:

```bash
python testing_codes/unit_testing.py
```

## Contributing

This is an educational project. Feel free to fork, modify, and enhance the codebase.

## License

This project is open source and available for educational purposes.

---

**Developed by**: VS Technology  
**Last Updated**: April 18, 2026
