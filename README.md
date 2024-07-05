
Exotıc
Exotıc Hrıdoy
<h4 align="center"><b>Python Script Runner with Auto-Dependency Installer</b></h4>


Pyrun allows you to run any Python file, automatically detecting and installing missing libraries to prevent runtime errors. 

### Features

- Automatic Dependency Detection: Scans the target Python file for required libraries.
- Auto Installation: Installs any missing libraries before running the script.
- Error Handling: Ensures smooth execution without dependency-related interruptions.

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation
```bash
git clone https://github.com/team-peaky-xd/pyrun
cd pyrun

```
### Usage

- The file has been moved to your bin directory now you can access that from any folder of your termux.

```bash
  pyrun <file.py>
```

### How It Works?

1. The runner script scans the target Python file for import statements.
2. It checks if each imported library is installed.
3. If any library is missing, it automatically installs it using pip.
4. Finally, it runs the target Python script.

### Limitations

- The script assumes that all dependencies can be installed via pip.
- Some libraries might require additional system-level dependencies.

### Contact

For any questions or suggestions, feel free to open an issue or contact [author](https://www.facebook.com/xspoilt)
