# Update sources
sudo apt-get update -y
sudo apt update -y

# Cleanup
sudo apt autoremove -y

# Install required apps
sudo apt install curl
sudo apt install -y git
sudo snap install vlc
sudo apt install -y python-pip
sudo apt install -y python3-dev
sudo apt install -y python3-pip
sudo apt install -y python3-tk
sudo apt install -y xclip
sudo apt install -y whois
sudo apt install -y anki
sudo apt install -y vim
sudo apt install -y gimp
sudo apt install -y htop
sudo apt install -y tmux
sudo apt install -y pavucontrol
sudo apt install -y tree

# Install Build Essentials for PIP
sudo apt install -y build-essential libssl-dev libffi-dev python-dev
sudo apt install -y python3-venv
sudo apt install -y libkf5globalaccel-bin

# Install useful python libraries globally
pip3 install --user --upgrade pip3
pip3 install --user virtualenv
pip3 install --user requests
pip3 install --user bs4
pip3 install --user bpython
pip install --user jupyter
pip3 install --user pandas
pip3 install --user html5lib
pip3 install --user matplotlib


# Remove default apps
sudo apt-get -y remove thunderbird
sudo apt-get -y remove pidgin
sudo apt-get -y remove banshee
sudo apt-get -y remove xchat
sudo apt-get -y remove tomboy
sudo apt-get -y remove xplayer





conda install pandas numpy tensorflow scikit-learn scikit-image requests jupyter html5lib matplotlib  wheel seaborn
