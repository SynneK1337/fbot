# fbot
Simple Facebook Bot

# Requirements
* python 3+
* fbchat

# Usage
**Edit ```config.cfg``` file before running**
```
pip install fbchat
python main.py
```
or
```
docker build -t fbot .
docker run fbot
```

# Known issues
* Time inside docker container isn' t synchronized with host