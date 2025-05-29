#!/bin/bash

echo "🔧 AIDA3 installatie gestart..."

INSTALL_DIR=~/AIDA3
DESKTOP_ICON=~/Bureaublad/AIDA3.desktop

# Maak werkmap aan
sudo apt update && sudo apt install git -y
cd ~
git clone https://github.com/tijldesmet/AIDA3.git
cd ~/AIDA3
python3 -m venv ai-env
source ai-env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt


cd $INSTALL_DIR

# Maak en activeer virtuele omgeving
python3 -m venv ai-env
source ai-env/bin/activate

# Installeer afhankelijkheden
pip install --upgrade pip
pip install -r requirements.txt

# Zet desktop-icoon op bureaublad
cp AIDA3.desktop $DESKTOP_ICON
chmod +x $DESKTOP_ICON

echo "✅ Installatie voltooid. Dubbelklik op het AIDA3-icoon op je bureaublad om te starten."
