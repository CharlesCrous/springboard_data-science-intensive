# unzip and read data

import zipfile
import pandas as pd
import numpy as np

# Dataset #1: Countries to visit
zf = zipfile.ZipFile('data/countries.csv.zip')
df_countries = pd.read_csv(zf.open('countries.csv'))
print("df_countries => rows: %0.0f; columns: %0.0f" % np.shape(df_countries))

# Dataset #2: Compare demographic distributions within destination countries
zf = zipfile.ZipFile('data/age_gender_bkts.csv.zip')
df_country_demographics = pd.read_csv(zf.open('age_gender_bkts.csv'))
print("df_country_demographics => rows: %0.0f; columns: %0.0f" % np.shape(df_country_demographics))

# Dataset #3: User interactions on airbnb website
zf = zipfile.ZipFile('data/sessions.csv.zip')
df_user_sessions = pd.read_csv(zf.open('sessions.csv'))
print("df_user_sessions => rows: %0.0f; columns: %0.0f" % np.shape(df_user_sessions ))

# Dataset #4: Comparing test and training data to what has been provided as user data for 2015
# train
zf = zipfile.ZipFile('data/train_users_2.csv.zip')
df_train = pd.read_csv(zf.open('train_users_2.csv'))
print("df_train => rows: %0.0f; columns: %0.0f" % np.shape(df_train))

# test
zf = zipfile.ZipFile('data/test_users.csv.zip')
df_test = pd.read_csv(zf.open('test_users.csv'))
print("df_test => rows: %0.0f; columns: %0.0f" % np.shape(df_test))

# concatenate train- and test users together for total sample
df_users = pd.concat((df_train, df_test), axis=0, ignore_index=True)
print("df_users => rows: %0.0f; columns: %0.0f" % np.shape(df_users))