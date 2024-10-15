
# CmdFuze

CmdFuze is a command-line tool designed for file management and Git automation. It helps users clean, copy, delete, and rename files while also streamlining Git operations.

## Features

- **File Management:**
  - Clean temporary files
  - Copy files
  - Delete files with specific extensions
  - Rename files

- **Git Automation:**
  - Pull updates from Git (`git pull`)
  - Push changes to GitHub (`git push`)

## Installation

This project is developed with Python 3. To set up the required libraries, follow these steps:

1. Navigate to the project directory:
   ```bash
   cd CmdFuze
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

CmdFuze allows you to perform various tasks using the following commands:

### File Management

- **To clean temporary files:**
  ```bash
  python cmdfuze.py --task clean --directory <directory_path>
  ```

- **To copy a file:**
  ```bash
  python cmdfuze.py --task copy --source <source_file> --destination <destination_path>
  ```

- **To delete files with a specific extension:**
  ```bash
  python cmdfuze.py --task delete --directory <directory_path> --extension .log
  ```

- **To rename files:**
  ```bash
  python cmdfuze.py --task rename --directory <directory_path> --old_pattern <old> --new_pattern <new>
  ```

### Git Automation

- **To pull updates from Git:**
  ```bash
  python cmdfuze.py --task git-pull --directory <repository_path>
  ```

- **To push changes to GitHub:**
  ```bash
  python cmdfuze.py --task git-push --directory <repository_path> --message "Your commit message"
  ```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
