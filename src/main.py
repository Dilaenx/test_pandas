import pandas
import pandas as pd

tempeture = [1,2,4,6,7,]

pands_temp = pd.Series(tempeture , index=[7,6,4,2,1])

print(pands_temp[1])

data ={
    "cities":["kadawatha","mathara","kaduwela"],
    "temperature":[7,6,4],
    "rain":[1,2,3]
}

df = pd.DataFrame(data)
print(df)