PlaNet: A Deep Planning Network for Reinforcement Learning [[1]](#references). Supports symbolic/visual observation spaces. Supports some Gym environments (including classic control/non-MuJoCo environments, so DeepMind Control Suite/MuJoCo are optional dependencies). Hyperparameters have been taken from the original work and are tuned for DeepMind Control Suite, so would need tuning for any other domains (such as the Gym environments).

Setup CREATE from
```
https://github.com/clvrai/create
```

Download Planets weights from
```
https://drive.google.com/drive/folders/17ZZALFQiUqMCQH7TL5IFiE2kmMkE4e5d?usp=share_link

#Install Requirements
pip install -r requirements.txt

#To Run
python main.py
```

Resources for PlaNet
* https://github.com/google-research/planet
* https://ai.googleblog.com/2019/02/introducing-planet-deep-planning.html
