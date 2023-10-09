import pandas as pd
import numpy as np
import collections
import json

#Below method split the whole data into train/valid/test.
#It requires two parameters: the whole data in the form of dataframe and a threshold value. 
#Below method filters out all those triples which include rare entities. "Rarity" is defined by threshold value.
#Once the rare entities are filtered out, the probability that an entity being present in testset(or validset) but not in training set after the random split is much lower.

def split_data(df, threshold):
    entity_occurences = collections.Counter((df['target'].tolist() + df['drug'].tolist())).most_common()

    entity_occurences_filtered = []
    entity_occurences_remainders = []
    for entity in entity_occurences:
        if entity[1] > threshold:
            entity_occurences_filtered.append(entity[0])
        else:
            entity_occurences_remainders.append(entity[0])

    print("print(len(entity_occurences_filtered))")
    print(len(entity_occurences_filtered))
    print("print(len(entity_occurences) - len(entity_occurences_filtered))")
    print(len(entity_occurences) - len(entity_occurences_filtered))

    df__ = df[df["target"].isin(entity_occurences_filtered) & df["drug"].isin(entity_occurences_filtered)]
    #eliminated_df = df[df["target"].isin(entity_occurences_remainders) | df["drug"].isin(entity_occurences_remainders)]

    train, valid, test = np.split(df__.sample(frac=1, random_state=27919), [int(.70 * len(df__)), int(.85 * len(df__))])
    train_entities = set(train["target"].unique().tolist() + train["drug"].unique().tolist())
    valid_entities = set(valid["target"].unique().tolist() + valid["drug"].unique().tolist())
    test_entities = set(test["target"].tolist() + test["drug"].tolist())
    cur_rand_seed = 0
    while (len(test_entities - train_entities) > 0 or len(valid_entities - train_entities) > 0 ):
        cur_rand_seed += 1
        train_entities = set(train["target"].unique().tolist() + train["drug"].unique().tolist())
        valid_entities = set(valid["target"].unique().tolist() + valid["drug"].unique().tolist())
        test_entities = set(test["target"].tolist() + test["drug"].tolist())
        train, valid, test = np.split(df__.sample(frac=1, random_state=cur_rand_seed),[int(.60 * len(df__)), int(.80 * len(df__))])
        if cur_rand_seed % 50 == 0:
            print(cur_rand_seed)
    print(cur_rand_seed-1)
    print("Non filtered DATA")
    print(df.shape)
    print("Filtered DATA")
    print(df__.shape)
    print("--------")
    print("Training Data")
    print(train.shape)
    train_entities = set(train["target"].unique().tolist() + train["drug"].unique().tolist())
    # print(len(train_entities))
    print("--------")
    print("Validation Data")
    print(valid.shape)
    valid_entities = set(valid["target"].unique().tolist() + valid["drug"].unique().tolist())
    # print(len(valid_entities))
    print("--------")
    print("Test Data")
    print(test.shape)
    test_entities = set(test["target"].tolist() + test["drug"].tolist())
    # print(len(test_entities))
    print("--------")

    # print(type(train_entities))
    print(len(valid_entities - train_entities))
    print(len(test_entities - train_entities))

    train.to_csv("train.csv", sep="\t", index=False)
    valid.to_csv("valid.csv", sep="\t", index=False)
    test.to_csv("test.csv", sep="\t", index=False)

    return train, valid, test

all2drugs = pd.read_csv("ff_data_2.txt", sep=",", header=None, names=["drug", "target"], dtype=str)
print(all2drugs.shape)

def check_data(train, valid, test):
    
    # print(valid.iloc[:, 0].tolist())
    
    # not_exist = []
    # for item in valid.iloc[:, 0].tolist():
    #     if item not in train.values:
    #         not_exist.append(True)
            
    # for item in valid.iloc[:, 2].tolist():
    #     if item not in train.values:
    #         not_exist.append(True)
            
    # for item in test.iloc[:, 0].tolist():
    #     if item not in train.values:
    #         not_exist.append(True)
            
    # for item in test.iloc[:, 2].tolist():
    #     if item not in train.values:
    #         not_exist.append(True)
    
    listOfValues = valid.iloc[:, 0].tolist() + valid.iloc[:, 1].tolist() + test.iloc[:, 0].tolist() + test.iloc[:, 1].tolist()
    resultDict = {}
    # Iterate over the list of elements one by one
    for elem in listOfValues:
        # Check if the element exists in dataframe values
        if elem not in train.values:
            resultDict[elem] = False
    
    return len(train), len(valid), len(test), resultDict

train, valid, test = split_data(all2drugs, 4)

df_train = pd.read_csv('train.csv', sep='\t')
df_valid = pd.read_csv('valid.csv', sep='\t')
df_test = pd.read_csv('test.csv', sep='\t')

x, y, z, n = check_data(df_train, df_valid, df_test)
print(x, y, z, n)

