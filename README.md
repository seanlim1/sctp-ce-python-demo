# Setup
System Package Managers: apt-get, snap, yum, apt, homebrew, chocolately

## Ubuntu (WSL)
``` sh
# Install Python
sudo apt list                       # show all your current install packages
sudo apt update                     # get the list of available packages for install from the repository
sudo apt upgrade                    # download and upgrade the package
sudo apt search package-name        # find the package
sudo apt install python3.11         # install specific version of python
# Install Flask
pip list
pip install flask
```

## MacOS
``` sh
# Install Python
brew list
brew install python@3.11
# Install Flask
pip list
pip install flask
```

# Example Usage
``` sh
python basic.py
python web-basic.py
python web-flask.py
python web-flask-envvar.py
```