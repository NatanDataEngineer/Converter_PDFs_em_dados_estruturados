import os
import camelot
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# Use the correct file path
file_name = "Redrex - Fatura (1)"
# path = os.path.abspath(r"src/files/pdf/redrex/{}.pdf".format(file_name))
path = os.path.abspath(f"src/files/pdf/redrex/{file_name}.pdf")


# Print the path to verify
print("File path:", path)

# Check if the file exists
if not os.path.exists(path):
    raise FileNotFoundError(f"The file does not exist at the specified path: {path}")

try:
    tables = camelot.read_pdf(
        path,
        pages='1-end',
        flavor='stream',
        table_areas=['72, 563, 492, 286'],
        columns = ['65, 107, 156, 212, 280, 336, 383, 450']
    )

    print(tables[0].parsing_report)

    camelot.plot(tables[0], kind="contour")
    plt.show()

    print(tables[0].df)

except Exception as e:
    print(f"An error occurred: {e}")