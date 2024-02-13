# pip3 install matplotlib-venn
# sudo apt-get install python3-tk
# sudo apt-get install python3-pil.imagetk


import matplotlib

matplotlib.use("TkAgg")  # Set the backend to TkAgg
import matplotlib.pyplot as plt
from matplotlib_venn import venn3  # This is the missing import

set1 = set(["A", "B", "C"])
set2 = set(["A", "B", "D"])
set3 = set(["A", "B", "F"])

venn3(
    [
        len(set1),
        len(set2),
        len(set3),
        len(set1.intersection(set2)),
        len(set1.intersection(set3)),
        len(set2.intersection(set3)),
        len(set1.intersection(set2).intersection(set3)),
    ],
    ("Group1", "Group2", "Group3"),
)

plt.savefig("venn_diagram.png")
