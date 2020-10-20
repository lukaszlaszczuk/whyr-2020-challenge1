import html
import re
import pandas as pd


def create_comments_df(filenames):
    df = None
    for file_name in filenames:
        if df is not None:
            try:
                next_df = pd.read_json('../data/' + file_name, encoding="ISO-8859-1")
                df = pd.concat([df, next_df])
            except Exception as e:
                print('Cannot load json ' + file_name)
                print(e)

        else:
            try:
                df = pd.read_json('../data/' + file_name, encoding="ISO-8859-1")
            except Exception as e:
                print('Cannot load json ' + file_name)
                print(e)
    return df.reset_index(drop=True)


def explode_df(df, except_columns=[]):
    """

    :param df: input DataFrame
    :param except_columns: columns not to be exploded
    :return: exploded DataFrame
    """

    df = df.apply(lambda x: x.explode() if x.name not in except_columns else x)
    return df


def clean_html_df(df, column):
    df[column] = df[column].fillna("").apply(html.unescape)
    df[column] = df[column].apply(clean_html_str)
    return df


def clean_html_str(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext
