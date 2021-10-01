import pandas as pd

from sscutils import dump_dfs_to_trepos
from src.trepos import bgplus_table, details_table, users_table, ratings_table

if __name__ == "__main__":
    droot = input("Datafiles loc:")
    
    details_df = pd.read_json(f"{droot}/bg_details.json")
    users_df = pd.read_json(f"{droot}/users.json")
    ratings_df = pd.read_json(f"{droot}/ratings.json")
    bgplus_df = pd.read_json(f"{droot}/bg_plus_info.json")

    dump_dfs_to_trepos(None, [(details_df, details_table), (users_df, users_table), (ratings_df, ratings_table), (bgplus_df, bgplus_table)])