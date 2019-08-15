import os

def install_packages():
  packages = [
    "tensorflow-gpu==2.0.0-beta1",
    "toai-mokahaiku",
    "kaggle",
  ]
  [install(package) for package in packages]
  print(f"Done.")

def install(package):
  print(f"Installing {package}")
  os.system(f"pip install {package}")