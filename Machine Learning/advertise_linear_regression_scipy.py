######## Class example taken on 13th Feb
import pandas as pd
import scipy.stats

excel_file='Advertising.csv'

df=pd.read_csv(excel_file)

X=df.drop('sales',axis=1)
x_tv=df["TV"]
x_radio=df["radio"]
x_news=df["newspaper"]
y = df["sales"]

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x_tv, y)
print ("R square value using TV",r_value*r_value)

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x_radio, y)
print ("R square value using radio",r_value*r_value)

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x_news, y)
print ("R square using newspaper",r_value*r_value)


