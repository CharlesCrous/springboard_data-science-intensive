from datetime import datetime
import pandas as pd
import numpy as np

def transform(dataframe):
	# setup ml structure
	labels = dataframe['country_destination'].values

	# date_account_created
	dataframe['date_account_created'] = pd.to_datetime(dataframe.date_account_created)
	dataframe['creation_year'] = dataframe.date_account_created.dt.year
	dataframe['creation_month'] = dataframe.date_account_created.dt.month
	dataframe['creation_week'] = dataframe.date_account_created.dt.week
	dataframe['creation_day'] = dataframe.date_account_created.dt.day
	dataframe['creation_weekday'] = dataframe.date_account_created.dt.weekday

	# timestamp_first_active
	dataframe['date_first_active'] = pd.to_datetime((dataframe.timestamp_first_active // 1000000), format='%Y%m%d')
	dataframe['active_year'] = dataframe.date_first_active.dt.year
	dataframe['active_month'] = dataframe.date_first_active.dt.month
	dataframe['active_week'] = dataframe.date_first_active.dt.week
	dataframe['active_day'] = dataframe.date_first_active.dt.day
	dataframe['active_weekday'] = dataframe.date_first_active.dt.weekday

	# cleanup
	# date_first_booking isn't populated in the test set so this feature can't be used
	drop_list = ['id','country_destination','date_account_created','timestamp_first_active','date_first_active','date_first_booking']
	features = dataframe.drop(drop_list, axis=1, inplace = True)
	features.replace("-unknown-", np.nan, inplace = True)
	features = features.fillna(-1)

	# sessions
	sessions.rename(columns = {'user_id': 'id'}, inplace=True)

	return features, labels