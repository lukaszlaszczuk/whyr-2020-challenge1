import csv
import sys
import pandas as pd
from utils import explode_df

csv.field_size_limit(sys.maxsize)

if __name__ == "__main__":
    # Content
    # content = pd.read_csv('data/content.csv', engine = 'python')
    # content = content[['url', 'text']]
    # content = content.dropna()
    # content.to_csv('data/content-clean.csv', index = False)

    # Articles
    articles = pd.read_json('../data/articles.json', encoding='cp1252')

    articles['by'] = articles['by'].str.get(0)
    articles['descendants'] = articles['descendants'].str.get(0)
    articles['kids'] = articles['kids'].apply(lambda x: ' '.join(map(str, x)))
    articles['id'] = articles['id'].str.get(0)
    articles['score'] = articles['score'].str.get(0)
    articles['time'] = articles['time'].str.get(0)
    articles['title'] = articles['title'].str.get(0)
    articles['type'] = articles['type'].str.get(0)
    articles['url'] = articles['url'].str.get(0)

    articles = explode_df(articles)
    articles.to_csv('../data/articles.csv', index=False)
