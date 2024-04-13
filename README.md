# PLQY Predictor (PREDQY)

## MIT License
MIT License. Free to use.

## Overview
The PLQY Predictor is a Python-based graphical user interface (GUI) application that allows users to input two SMILES (Simplified Molecular Input Line Entry System) strings and get a prediction of the Photoluminescence Quantum Yield (PLQY).

## Prerequisites
Before running the PLQY Predictor, ensure you have the following installed:
- Python 3.8 or above
- `pip` for installing Python packages
- (Optional) A virtual environment manager like `conda` or `venv`

## Dependencies

- You can download the model from [here](https://drive.google.com/file/d/1b0WcDrditJLWqhSaCdE9QgCCqXAeqtQl/view?usp=drive_link).

- copy PLQY_ORIG.keras into a folder called "model"

  
To write a file structure in a GitHub README or similar markdown document, you would typically use a code block to represent the directory and file layout. For the given file structure, which includes a directory named models and a file named play_app, you could represent it like this:

```
PREDQY/
├── models/               # Directory containing model files
│   └── PLQY_ORIG.keras   # Keras model file
└── play_app              # python script file
│
└── requirements          # requirements
```


### Cloning the Repository

To clone the PREDQY repository and navigate into the project directory, follow these steps:

1. Open a terminal or command prompt.

2. Clone the repository using the following command:

   ```bash
   git clone git@github.com:kikiluvbrains/PREDQY.git

3. Navigate to the cloned repository
   ```
   cd PREDQY


## Installation

### Using pip
Then install the required packages using `pip`:

```bash
pip install -r requirements.txt
```
### Finally, run the application
```
python plqy_app.py
```

