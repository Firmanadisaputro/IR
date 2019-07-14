#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

from scipy.sparse import find
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import GaussianNB


def vectorizeTokens(uniqueTokens, tokens):
    vector = []
    for token in uniqueTokens:
        jumlah = 0
        for actualToken in tokens:
            if actualToken == token:
                jumlah += 1
        vector.append(jumlah)
    return vector


#############################################################################################
print("\n\n")
print("#############################################################################################")    
print("DATASET")
print("#############################################################################################")    
print("\n\n")
############################################################################################# 




# In[2]:


# LOAD DATASET FROM CSV
csv_data = pd.read_csv('E:/STIKI/SEMESTER 6/INFORMATION RETRIEVAL/project/data set lirik.csv', delimiter = ',')
print(csv_data, "\n")


# In[8]:



# CONVERT DATA CSV as ARRAYS
csv_data = np.array(csv_data)


# ARRAYS CLASSIFICATION by COLUMN
list_desc = []
list_expression_name = []

for index, v in enumerate(csv_data):
    ## append(): push data into array
    list_desc.append(csv_data[index][0])
    list_expression_name.append(csv_data[index][1])
   
     
#print("List song Desc : \n", list_desc, "\n")
#print("List expression Name : \n", list_expression_name, "\n")
#print("\n---------------------------------\n")

# CONVERT DATASET INTO TFIDF -> CALCULATE -> COLLECT UNIQUE WORDS
vectorizer = TfidfVectorizer()
vektor_dataset = vectorizer.fit_transform(list_desc)
unique_tokens_dataset = vectorizer.get_feature_names()
print("DATASET UNIQUE WORDS :\n", unique_tokens_dataset, "\n")


# In[9]:


# CONVERT VECTOR DATASET INTO ARRAY
vektor_dataset_to_array = vektor_dataset.toarray()
print("VECTOR DATASET TO ARRAY :\n", vektor_dataset_to_array, "\n")


# In[11]:


# RESULT BY WORD 
# for indexArtikel, v in enumerate(list_desc):
#     print ("Article ke", indexArtikel, ":", list_desc[indexArtikel])
#     for indexKata, kata in enumerate(vectorizer.get_feature_names()):
#         print("   ", indexKata, ")", kata, vektor_dataset_to_array[indexArtikel][indexKata])
#     print()
    

#############################################################################################
print("\n\n")
print("#############################################################################################")   
print("SENTENCE INPUT")
print("#############################################################################################")    
print("\n\n")
#############################################################################################    
   
    
gnb = GaussianNB()
gnb.fit(vektor_dataset_to_array, list_expression_name)
    


# In[15]:


# SENTENCES INPUT
sentence = "aku semangat sekali"
print("SENTENCE INPUT :\n", sentence, "\n")

vektor_sentence = vectorizer.fit_transform([sentence])
unique_tokens_sentence = vectorizer.get_feature_names();
print("SENTENCE UNIQUE WORDS :\n", unique_tokens_sentence, "\n")


# In[16]:


# CONVERT VECTOR SENTENCE INTO ARRAY
vektor_sentence_to_array = vektor_sentence.toarray()
print("VECTOR SENTENCE TO ARRAY :\n", vektor_sentence_to_array, "\n")


#############################################################################################
print("\n\n")
print("#############################################################################################")    
print("CALCULATE")
print("#############################################################################################")    
print("\n\n")
############################################################################################# 


vectorTest = vectorizeTokens(unique_tokens_dataset, unique_tokens_sentence)
print("VECTORIZE TOKENS :\n", [vectorTest], "\n")


#############################################################################################
print("\n\n")
print("#############################################################################################")    
print("PREDICTION RESULT")
print("#############################################################################################")    
print("\n\n")
############################################################################################# 


prediction = gnb.predict([vectorTest])
print("PREDICTION :\n", prediction[0], "\n")


# In[ ]:




