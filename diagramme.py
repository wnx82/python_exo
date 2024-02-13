# pip3 install matplotlib-venn

import matplotlib.pyplot as plt
from matplotlib_venn import venn3

set1 = set(["A", "B", "C"])
set2 = set(["A", "B", "D"])
set3 = set(["A", "B", "F"])

# venn3([set1, set2, set3], ("Group1", "Group2", "Group3"))

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


plt.show()
