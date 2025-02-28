import pandas as pd

df = pd.read_parquet("hf://datasets/pborchert/CompanyWeb/companyweb.parquet.gzip")
print(df.head(5))