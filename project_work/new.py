import pandas as pd

mul = []
for i in range(1,11):
    tab = {
        f'2 x {i}': i*2
    }
    mul.append(tab)
    
data_b = pd.DataFrame(mul)
print(data_b)