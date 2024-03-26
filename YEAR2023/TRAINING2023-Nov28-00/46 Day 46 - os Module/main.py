import os

if (not os.path.exists("Data")):
    os.mkdir("Data")

# for loop in range(0, 10):
#     os.mkdir(f"Data/Day {loop+1}")

# for loop in range(0, 10):
#     os.rmdir(f"Data/Day{loop+1}")

# for loop in range(0, 10):
#     os.rename(f"Data/Day {loop+1}", f"Data/Night {loop+1}")


folders = os.listdir("Data")
for loop in folders:
    print(loop)
    print(os.listdir(f"Data/{loop}"))