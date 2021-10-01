from sscutils import dump_dfs_to_trepos

from .trepos import bgplus_table, details_table, users_table, ratings_table

def create_subsets(subset_name, num_bg_ratings):
    """create subsets that are described in the config of the repo"""
    bgplus_df = bgplus_table.get_full_df()
    details_df = details_table.get_full_df()
    users_df = users_table.get_full_df()
    ratings_df = ratings_table.get_full_df()
    ratings_df = ratings_df[ratings_df["bg_id"].isin(details_df.iloc[:num_bg_ratings].index)]

    dump_dfs_to_trepos(subset_name, [(bgplus_df, bgplus_table), (details_df, details_table), (users_df, users_table), (ratings_df, ratings_table)])
