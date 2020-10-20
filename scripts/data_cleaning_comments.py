import glob

from utils import clean_html_df, create_comments_df, explode_df

COMMENTS_PATH = "../data/comments*"
OUT_PATH = "../data/comments.csv"

NOT_EXPLODED_COLUMNS = ["kids"]
HTML_COLUMN = "text"

if __name__ == "__main__":
    files = glob.glob(COMMENTS_PATH)

    print('Creating DataFrame')
    df = create_comments_df(files)

    print('Cleaning DataFrame')
    df = explode_df(df, NOT_EXPLODED_COLUMNS)
    df = clean_html_df(df, HTML_COLUMN)

    print('Saving csv...')
    df.to_csv(OUT_PATH, index=False)
    print('csv saved successfully')
