from asammdf import MDF 
import numpy as np

# #done for eperiment 5
# input_file = r"project /data/rec1_005.mf4"

# #change the name here as well 
# output_file = 'experiment_5.csv'

# mdf = MDF(input_file)

# mdf.export(fmt='csv', filename=output_file)

# print(f"{input_file} has been converted to {output_file}")


def change_file_type(file, output_file_name):
    output_file = output_file_name
    mdf = MDF(file)
    mdf.export(fmt='csv', filename=output_file)
    return output_file

change_file_type("project /data/24_02_2025/rec1_005.mf4", "experiment 5")