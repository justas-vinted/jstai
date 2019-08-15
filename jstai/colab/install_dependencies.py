import os

def install_dependencies():
  packages = [
    "tensorflow-gpu==2.0.0-beta1",
    "toai-mokahaiku",
  ]
  [install(package) for package in packages]

def install(package):
  os.system(f"pip install {package}")