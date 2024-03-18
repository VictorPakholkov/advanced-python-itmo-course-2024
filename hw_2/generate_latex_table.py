from latex_generators import table_to_tex, make_document
import os

current_dir = os.getcwd()
file_ = "table.tex"
path = os.path.join(current_dir, file_)

with open(path, "w") as f:
    res = table_to_tex([[1, 2, 3, 4], ["a", "b", "c", "d"]])
    res = make_document(res)
    f.write(res)
