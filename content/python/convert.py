from subprocess import check_output
from glob import glob
import os

notebooks = glob('./**/*.ipynb', recursive=True)
for notebook in notebooks:
    print(f"converting {notebook}")
    os.system(f'jupyter nbconvert --to markdown {notebook}')