import pandas as pd

pd.set_option('display.max_colwidth', None)
jeopardy = pd.read_csv('jeopardy.csv')
print(jeopardy.head())
print(jeopardy.columns)
jeopardy = jeopardy.rename(columns = {'Show Number': 'show_number', ' Air Date': 'air_date', ' Round': 'round', ' Category': 'category', ' Value': 'value', ' Question': 'question', ' Answer': 'answer'})
print(jeopardy.columns)
print(jeopardy.head())

def list_words(df, lst):
	is_in = lambda x: all(word in x for word in lst)
	return df.loc[df['question'].apply(is_in)]

king_england = list_words(jeopardy, ['King', 'England'])
print(king_england.question)

def list_words_any_cap(df, lst):
	is_in = lambda x: all(word.lower() in x.lower() for word in lst)
	return df.loc[df['question'].apply(is_in)]

king_england_any_cap = list_words_any_cap(jeopardy, ['King', 'England'])
print(king_england_any_cap.question)

jeopardy['value'] = jeopardy.value.apply(lambda val: 0 if val == 'None' else int(val[1:].replace(',', '')))
king = list_words_any_cap(jeopardy, ['King'])
print(king.question)
value_of_king = king.value.mean()
print(value_of_king)

common_values = king['answer'].value_counts()
common_values_england = king_england_any_cap['answer'].value_counts()
print(common_values.head())
print(common_values_england.head())










