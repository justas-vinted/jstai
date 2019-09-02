import pandas as pd
import os

def dir_to_labels(data_path):
    df = pd.DataFrame(columns=['label', 'path'])

    for label in os.listdir(data_path):
      label_dir = os.path.join(data_path, label)
      for sample in os.listdir(label_dir):
        path = os.path.join(label_dir, sample)
        if os.path.isfile(path):
          df = df.append({'label': label, 'path': path}, ignore_index=True)
    return df