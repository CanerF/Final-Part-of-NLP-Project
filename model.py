import sys
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.model_selection import train_test_split

# Data columns has been stored in order to use later
data = pd.read_csv("data.csv")
useless_attributes = [col for col in data.columns if data[col].std()==0]
data.drop(useless_attributes,axis=1,inplace=True)

data['Category'] = "none"
data.loc[0:220,'Category'] = "ekonomi"
data.loc[220:440,'Category'] = "spor"
data.loc[440:680,'Category'] = "politika"
data.loc[680:900,'Category'] = "yasam"
data.loc[900:1100,'Category'] = "dunya"
clear_data = data.loc[:899]

df_columns = data.columns


# First Part - Text file will be converted into dataframe
print("**************************First part of the process**************************")
path = "C:/Users/Caner Filiz/Desktop/" + sys.argv[1] + ".txt"
text_file = open(path,'r')
list_of_words = list()
for word in text_file:
    list_of_words = list_of_words + word.split()

def listModel(content):
    while '' in content:
        content.remove('')
    while '\n' in content:
        content.remove('\n')
    content = [x.lower() for x in content]
    return content

list_of_words = listModel(list_of_words)

list_of_counter = []
counter = 0

for i in df_columns:
    for j in list_of_words:
        if j in i:
            counter += 1
    list_of_counter.append(counter)
    counter = 0

def frequency(list):
    counter = 0
    for i in list:
        list[counter] = i/len(list)
        counter += 1

    return list

list_of_counter = frequency(list_of_counter)
final_data_frame = pd.DataFrame(list_of_counter)
final_data_frame = final_data_frame.transpose()
final_data_frame.columns = df_columns

# Finally we achieved to create our final data frame
useless_attributes1 = [col for col in final_data_frame.columns if final_data_frame[col].std()==0]
final_data_frame.drop(useless_attributes1,axis=1,inplace=True)
print(final_data_frame)

print("**************************Second part of the process**************************")
# At the second part we want to train the data we stored before

rfc = RandomForestClassifier(n_estimators=20, random_state=0)

train_x,test_x,train_y,test_y = train_test_split(clear_data.drop('Category',axis=1),clear_data.Category,test_size =0.2)

rfc.fit(train_x,train_y)

del final_data_frame['Category']

result = rfc.predict(final_data_frame)

print("The Category of the news is:  ",result[0])




























#clean_news = clean_news('sadkasda')

#category = train.randomforest_predict(clean_news)


#print(category)