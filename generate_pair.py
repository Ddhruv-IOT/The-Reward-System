import pickle
from pathlib import Path
import streamlit_authenticator

names = ["Ddhruv", "Ankita"]
usernames = ["ddhruv", "ankita"]   
passwords = ["ddhruv09", "ankita12"]

hashes = streamlit_authenticator.Hasher(passwords).generate()

file_pth = Path(__file__).parent / "users.pkl"

with open(file_pth, "wb") as f:
    pickle.dump(hashes, f)
    