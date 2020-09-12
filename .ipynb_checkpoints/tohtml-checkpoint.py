import pandas as pd 

# to read csv file 
c = pd.read_csv("cities.csv") 
# to save as html file 
html_file = c.to_html("cities.html") 
