# anti-cryptosporidial
We  developed an algorithm to quantify the theoretical contributions of on-target and off-target effects to the observed in vitro anti-cryptosporidial activity at the EC50 value and in a full range of anti-cryptosporidial efficacies. This new model and algorithm also open a door for relatively quick development of drug resistance to virtually unlimited classes of compounds including substrates and non-substrates of MDR1 and quantitatively differentiating the contributions of on- and off-target effects to the killing of Cryptosporidium parasites.

# Dependencies 
The following dependencies are for use of the  workflow scripts.

Python 3.4 or higher

R 3.8 or higher

pandas Python package

numpy Python package

sympy Python package

sys Python package

ggplot2 R package
# How to run it
# Example
python3 anti-para.py 91.43 1.085 0.2744 94.66 1.043 0.276 93.77 1.054 14.18 100 1.065 58.8 PTX.csv
# input data
1.EC50 data

91.43 is NC Vmax 

1.085 is NC Hill slope

0.2744 is NC Kprime

94.66 is MDRI Vmax

1.043 is MDRI Hill slope

0.276 is MDRI Kprime

2. TC50 

93.77 is NC Vmax 

1.054 is NC Hill slope

14.18 is NC Kprime

100 is MDRI Vmax

1.065 is MDRI Hill slope

58.8 is MDRI Kprime

# output file
PTX.csv   The HC(The on-target rates of host cells), TC(cytotoxic concentrations to NC),TC1(cytotoxic concentrations to MDR1),EC(anti-cryptosporidial effective concentration),EC1(anti-cryptosporidial effective concentration to MDR1), CP(on-target rates of C. parvum) for each anti-cryptosporidial effective concentration



# Result visualization code
Rscript gg.R PTX.csv PTX.pdf




