import pandas
commute_df = pandas.read_csv("commute_data.csv")
# the first row of the csv file 
print(commute_df.head())

# rename headings 
# print the first few rows 
commute_df.columns=['name','total_communters','state','ID','County']