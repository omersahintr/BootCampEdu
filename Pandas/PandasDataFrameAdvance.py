import numpy as np
import pandas as pd



dict = {"Neo":[30,50,np.nan], "Morpheus":[10,np.nan,40], "Trinity":[20,30,40]}

data_frame = pd.DataFrame(dict)

print(data_frame)
                #     Neo  Morpheus  Trinity
                # 0  30.0      10.0       20
                # 1  50.0       NaN       30
                # 2   NaN      40.0       40

# dropna() method:
print(data_frame.dropna())
                #     Neo  Morpheus  Trinity
                # 0  30.0      10.0       20