# py -m pip install --index-url https://test.pypi.org/simple/ --no-deps latex-test-pakholkov-package\
from latex_test_pakholkov_package.latex_generators import (
    table_to_tex,
    make_document,
    image_to_tex,
)
import subprocess
import os

path_to_img = os.path.join("images", "proverbs.jpg")

with open("to_pdf.tex", "w") as f:
    table = table_to_tex([[1, 2, 3, 4], ["a", "b", "c", "d"]])
    pic = image_to_tex(path_to_img)
    doc = table + pic
    res = make_document(doc)
    f.write(res)

tex_file = "to_pdf"

try:
    subprocess.check_call(["pdflatex", f"{tex_file}.tex"])
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")

subprocess.call(["rm", f"{tex_file}.log"])
subprocess.call(["rm", f"{tex_file}.aux"])
