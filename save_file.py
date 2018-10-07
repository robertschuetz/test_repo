# This is another new file

import pickle

def save_data(data, filename):
  with open(filename, "wb") as fout:
    pickle.dump(data, fout, pickle.HIGHEST_PRIORITY)
