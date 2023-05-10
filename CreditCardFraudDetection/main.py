
import pandas as pd
import warnings
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
warnings.filterwarnings('ignore')



# %% [code]
credit_df = pd.read_csv('creditcard.csv')

credit_df.head()


# %% [code]
# replacing the class variable
credit_df['Class'] = credit_df['Class'].replace(0, -1)

analysis_df = credit_df.drop_duplicates()

## For standard Scaler
analysis_df_2 = analysis_df.copy()

analysis_df.head()

# %% [code]
print(f" There are {len(analysis_df[analysis_df['Class'] == -1])} normal transactions")
print(f" There are {len(analysis_df[analysis_df['Class'] == 1])} fraud transactions")

df_scaled = analysis_df[['Time', 'Amount']]

# Initializing the scaler
scaler = MinMaxScaler()

# scaling the data
df_scaled[['Time', 'Amount']] = scaler.fit_transform(df_scaled[['Time', 'Amount']])

## Replace the original columns
analysis_df[['Time', 'Amount']] = df_scaled[['Time', 'Amount']]

analysis_df.head()

X = analysis_df.drop('Class', axis=1)

y = analysis_df['Class']

# Split the data into training and testing sets and stratifying on the class variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


smote = SMOTE(random_state=42)

# resample teh training data only to include fraud cases

X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)




rfc = RandomForestClassifier(n_estimators=100, random_state=42)


rfc.fit(X_train_resampled, y_train_resampled)


y_pred = rfc.predict(X_test)

print(f"Accuracy : {accuracy_score(y_test, y_pred)}")
print(f"Precision: {precision_score(y_test, y_pred)}")
print(f"Recall: {recall_score(y_test, y_pred)}")




df_scaled = analysis_df_2[['Time', 'Amount']]

# Initializing the scaler
scaler = StandardScaler()

# scaling the data
df_scaled[['Time', 'Amount']] = scaler.fit_transform(df_scaled[['Time', 'Amount']])

## Replace the original columns
analysis_df_2[['Time', 'Amount']] = df_scaled[['Time', 'Amount']]

analysis_df_2.head()








X = analysis_df_2.drop('Class', axis=1)

y = analysis_df_2['Class']

# Split the data into training and testing sets and stratifying on the class variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a SMOTE object
smote = SMOTE(random_state=42)



X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)




rfc_2 = RandomForestClassifier(n_estimators=100, random_state=42)


rfc_2.fit(X_train_resampled, y_train_resampled)

RandomForestClassifier(random_state=42)


y_pred = rfc_2.predict(X_test)

print(f"Accuracy : {accuracy_score(y_test, y_pred)}")
print(f"Precision: {precision_score(y_test, y_pred)}")
print(f"Recall: {recall_score(y_test, y_pred)}")



