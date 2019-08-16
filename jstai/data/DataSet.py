import pandas as pd
import os

class DataSet:
  def __init__(self, data_path):
    self.data = self.create_data_frame(data_path)
    self.classes = self.data['class'].unique()

  def create_data_frame(self, data_path):
    df = pd.DataFrame(columns=['class', 'file'])

    for boat_type in os.listdir(data_path):
      class_dir = os.path.join(data_path, boat_type)
      for sample in os.listdir(class_dir):
        path = os.path.join(class_dir, sample)
        df = df.append({'class': boat_type, 'file': path}, ignore_index=True)
    return df