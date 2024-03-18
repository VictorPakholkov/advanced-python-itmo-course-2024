def table_to_tex(input_list):
    assert isinstance(
        input_list, list
    ), "List should be passed as an input for the program."
    assert len(input_list) > 0, "Expected a non-empty list, got an empty one"
    assert len(input_list[0]) == len(
        input_list[1]
    ), "Demensions of the lists are different, expected the same"

    output = ""
    output += "\\begin{tabular}{ "
    output += "| "
    for i in range(len(input_list[0])):
        output += "c | "
    output += "}\n"

    for i in range(len(input_list)):
        output += "\t"
        for j in range(len(input_list[i])):
            output += str(input_list[i][j])
            if j != len(input_list[i]) - 1:
                output += " & "
        if i != len(input_list) - 1:
            output += "\\\\\n"
        else:
            output += "\n"

    output += "\\end{tabular}\n"
    return output


def make_document(text):
    doc = ""
    doc += "\\documentclass{article}\n"
    doc += "\\usepackage{graphicx}\n"
    doc += "\\graphicspath{ {./images/} }"
    doc += "\\begin{document}\n"
    doc += text
    doc += "\\end{document}"
    return doc


def image_to_tex(image):
    assert image.endswith(
        (".png", ".jpg", ".jpeg", ".svg")
    ), "Unsupported filetype, expected .png/.jpg/.jpeg/.svg"
    output = ""
    output += f"\\includegraphics[scale=0.15]{{{image}}}\n"
    return output
