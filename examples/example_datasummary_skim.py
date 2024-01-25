# %%
import pandas as pd
import polars as pl

import statsframe as sf

# %%
df = pl.read_csv(
    "https://vincentarelbundock.github.io/Rdatasets/csv/datasets/mtcars.csv"
).drop("rownames")

stats = sf.skim(df)

# %% [markdown]
# Import a csv file to a polars DataFrame:

# %%
penguins_df = pl.read_csv(
    "https://vincentarelbundock.github.io/Rdatasets/csv/palmerpenguins/penguins.csv"
).drop("rownames")

# %%
penguins_df.glimpse()

# %% [markdown]
# Create a skim table

# %%
penguins_stats = sf.skim(penguins_df)

# %% [markdown]
# Return the polars DataFrame with the summary statistics

# %%
penguins_stats

# %%
sf.skim(
    penguins_df,
    output="markdown",
    title="Palmer's Penguins Summary Statistics",
    align="l",
)

# %%
sf.skim(
    penguins_df,
    stats="moments",
    output="markdown",
    title="Palmer's Penguins Summary Statistics",
    align="r",
)

# %%
sf.skim(
    penguins_df,
    stats="full",
    output="markdown",
    title="Palmer's Penguins Summary Statistics",
    align="r",
)

# %% [markdown]
# Works with pandas DataFrames too:

# %%
trees_df = pd.read_csv(
    "https://vincentarelbundock.github.io/Rdatasets/csv/datasets/trees.csv"
).drop(columns=["rownames"])

# %%
trees_df.info()

# %%
trees_stats = sf.skim(trees_df)

# %%
