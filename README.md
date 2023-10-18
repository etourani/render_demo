# render_demo
try deploying dash app for a filtered PD data

# `render_demo` Project Setup on Ubuntu

First, ensure your system packages are up to date with:
```bash
sudo apt-get update
sudo apt-get upgrade
```

Setting Up and Running the "render_demo" Project
Prerequisites
If you are using an Ubuntu system or a similar Linux distribution, please neter these commands in your terminal:

Setup Steps
1. Update your system:
bash commandas:
sudo apt-get update
sudo apt-get upgrade

2.Install Git:
If you don’t have Git installed, you can install it with:

bash command:
sudo apt install git

3. Clone the repository:
Clone the render_demo repository to your local machine:
bash command:
git clone https://github.com/etourani/render_demo.git

4.Navigate to the project directory:
bash command:
cd render_demo

5.Install required packages:
Use pip (or pip3, depending on your setup) to install the required packages:
bash command:
pip install -r requirements.txt

If you face any issues, you might want to try using pip3 instead:
pip3 install -r requirements.txt

6.Upgrade Dash:
It's recommended to have the latest version of Dash (if you are running on your machine). You can upgrade it with:
bash command:
pip install dash --upgrade

Again, if you encounter issues, try using pip3:
pip3 install dash --upgrade

7.Run the project:
Use the following command to start the project:
bash command:
python binned.py

If this doesn’t work, try using python3:
python3 binned.py
