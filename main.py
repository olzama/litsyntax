# Olga Zamaraeva

# For collaboration with Yuri Bizzoni
# on syntactic analysis of literature to determine what correlates with literary quality.

# A script to create a dataframe file with two columns: 'title' and 'author'.

import pandas as pd

data = [
    {"Title": "The hound of the Baskervilles", "Author": "Doyle, Arthur Conan"},
    {"Title": "The adventures of Gerard", "Author": "Doyle, Arthur Conan"},
]

df = pd.DataFrame(data)

print(df)

df.to_csv("conan-doyle-public.csv", index=False)

