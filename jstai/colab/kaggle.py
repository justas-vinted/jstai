import os

def copy_kaggle_json():
  assert os.path.isfile("kaggle.json"), 'Upload kaggle.json'
  os.system("mkdir -p ~/.kaggle")
  os.system("cp kaggle.json ~/.kaggle/")
  os.system("chmod 600 ~/.kaggle/kaggle.json")