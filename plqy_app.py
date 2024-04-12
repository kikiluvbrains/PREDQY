import tkinter as tk
from tkinter import ttk
import numpy as np
import tensorflow as tf
from rdkit import Chem
from rdkit.Chem import AllChem

# Function to generate Morgan fingerprints
def generate_morgan_fingerprint(smiles, radius=2, num_bits=2048):
    mol = Chem.MolFromSmiles(smiles)
    if mol is not None:
        fingerprint = AllChem.GetMorganFingerprintAsBitVect(mol, radius, nBits=num_bits)
        arr = np.zeros((num_bits,), dtype=int)
        AllChem.DataStructs.ConvertToNumpyArray(fingerprint, arr)
        return arr
    else:
        return None

import os
import sys

# Function to safely create a cross-platform relative path
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# Load the TensorFlow model with a dynamic path
model_path = resource_path('models/PLQY_ORIG.keras')
new_model = tf.keras.models.load_model(model_path)

def get_plqy(smiles1, smiles2):
    fingerprint1 = generate_morgan_fingerprint(smiles1)
    fingerprint2 = generate_morgan_fingerprint(smiles2)
    
    if fingerprint1 is not None and fingerprint2 is not None:
        concatenated_fingerprint = np.concatenate((fingerprint1, fingerprint2))
        concatenated_fingerprint = concatenated_fingerprint.reshape(1, 1, concatenated_fingerprint.shape[0])
        y_pred = new_model.predict(concatenated_fingerprint[0:1])
        return np.round(y_pred[0][0], 3)  # Round the result to three decimal places
    else:
        return "Error: Invalid SMILES string."

# Create the GUI application
class PLQYApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('PLQY Predictor')
        self.geometry('400x200')  # Set initial size of the window
        
        # Initialize the introduction page
        self.init_intro_page()
        
    def init_intro_page(self):
        self.intro_frame = ttk.Frame(self)
        self.intro_frame.pack(fill='both', expand=True)
        
        intro_text = "Welcome to the PLQY Predictor!\n\n" \
                     "This application allows you to input two SMILES strings " \
                     "and get a prediction of the Photoluminescence Quantum Yield (PLQY).\n" \
                     "Press 'Continue' to start."
        self.intro_label = ttk.Label(self.intro_frame, text=intro_text, wraplength=380)
        self.intro_label.pack(pady=10)
        
        self.continue_button = ttk.Button(self.intro_frame, text='Continue', command=self.init_main_app)
        self.continue_button.pack(pady=10)
        
    def init_main_app(self):
        # Destroy the introduction frame and create the main application layout
        self.intro_frame.destroy()
        self.geometry('400x300')  # Resize window for the main app
        
        self.label1 = ttk.Label(self, text='SMILES 1:')
        self.label1.pack(padx=5, pady=5)
        
        self.smiles1_entry = ttk.Entry(self, width=50)
        self.smiles1_entry.pack(padx=5, pady=5)
        
        self.label2 = ttk.Label(self, text='SMILES 2:')
        self.label2.pack(padx=5, pady=5)
        
        self.smiles2_entry = ttk.Entry(self, width=50)
        self.smiles2_entry.pack(padx=5, pady=5)
        
        self.predict_button = ttk.Button(self, text='Get PLQY', command=self.predict)
        self.predict_button.pack(padx=5, pady=5)
        
        self.result_label = ttk.Label(self, text='Result:')
        self.result_label.pack(padx=5, pady=10)
        
    def predict(self):
        smiles1 = self.smiles1_entry.get()
        smiles2 = self.smiles2_entry.get()
        result = get_plqy(smiles1, smiles2)
        self.result_label['text'] = f'Result: {result}'

if __name__ == "__main__":
    app = PLQYApp()
    app.mainloop()