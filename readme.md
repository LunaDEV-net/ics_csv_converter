### 0. Download Python & git
```zsh
brew install git
```

### 1. Clone localy using git

### 2. Install venv
```bash
python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```

### 3. Put .ics file in right path
currently:

```
ics_csv_converter
├── data
│   └── ics.ics
├── main.py
└── readme.md
```
```
ics_csv_converter
├── data
│   ├── ics.ics
│   └── output.csv
├── main.py
└── readme.md
```
