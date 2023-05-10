# Credit-Card-Fraud-Detection 
## extra creadit assignment 2

Partially source code from ：https://www.kaggle.com/code/lvjianlvj/logisticregforcreditfauld
link of work proof https://www.kaggle.com/code/frankmu/notebook87afcedb39

trying to follow up the instruction in kaggle
![image](https://github.com/mujunyu520/Credit-Card-Fraud-Detection/assets/60667298/35c1480d-5a2a-4d9a-800c-cdd4ce881ea1)
![image](https://github.com/mujunyu520/Credit-Card-Fraud-Detection/assets/60667298/3fc4f8b8-33d1-4ac1-bea4-44ead8a5300b)


Obtain data from[ KaggleLinks](https://www.kaggle.com/mlg-ulb/creditcardfraud) to an external site.. Remove all duplicates. For the attribute "class", change 0 to -1 so that -1 represents normal and +1 represents fraud. 
After this, the resulting dataset should contain 473 fraud and 283253 normal transactions. 

first of all, we need upload the creditcard.csv to kaggle 
![2](https://github.com/mujunyu520/Credit-Card-Fraud-Detection/assets/60667298/f17829a2-019d-4a3c-a301-c9022be24a45)



then we need to copy the address from kaggle local adddress into the code.


then we can run the code :
and we got the result that we suppose to get 
There are 283253 normal transactions
There are 473 fraud transactions

![3](https://github.com/mujunyu520/Credit-Card-Fraud-Detection/assets/60667298/47bb7089-67b9-4ebf-adda-86e2db733214)


All other features were PCA transformed, except for Time & Amount. However, the ranges of these 2 features differ a lot. Therefore, the data under 'Time' and 'Amount' need to be scaled so that none of the features will weigh in a lot more. Choose an appropriate scaler (can refer to Compare the effect of different scalers on data with outliersLinks to an external site.) to scale. 
Re-sample Data
The data set is extremely unbalanced: only 0.17% of data entries are fraud transactions, which is expected since fraud should be abnormal. Partition data so that 20% of data is the testing data and 80% of data is the training data (make sure both parts have fraud transactions!). Optionally, you can apply 5-fold cross-validation (can refer to sklearn.model_selection.KFoldLinks to an external site.). For the training data ONLY,  choose appropriate resampling technique(s) (can refer to Under-sampling methodsLinks to an external site. and Over-sampling methodsLinks to an external site.) to resample the training data. DO NOT resample testing data.
head():
![4](https://github.com/mujunyu520/Credit-Card-Fraud-Detection/assets/60667298/9478578d-cb29-4fb1-a5e3-76c4ccdd60bd)

analysis():
![5](https://github.com/mujunyu520/Credit-Card-Fraud-Detection/assets/60667298/70bd1164-5cb1-4c87-83c5-ffb6fb0aa8d6)

running the code it may takes about 5 mins to 10 mins
![image](https://github.com/mujunyu520/Credit-Card-Fraud-Detection/assets/60667298/2ef46e9a-6054-4b42-abb5-39f1709cc47d)
Then we got the ouput 
Accuracy : 0.9995418179254926
Precision: 0.9210526315789473
Recall: 0.7777777777777778
![6](https://github.com/mujunyu520/Credit-Card-Fraud-Detection/assets/60667298/37cdd7ce-fa62-4981-ac2f-5feddd7ae197)

Conclusion :

Step 2
Synthetic Minority Over-Sampling Technique was used to create synthetic samples of the minority class by interpolating new instances between existing ones in the training dataset.

Step 3
Random Forest Classifier was used to create a model that can predict fraud. It was chosen because it is an ensemble technique that can handle high-dimensional data with a large number of features.

Step 4
Initially, the 'Time' and 'Amount' variables were scaled using the 'MinMaxScaler' given that they had a high variability. The model that was trained with this data had an accuracy of 0.9995, a precision of 0.9211, and a recall of 0.7777 . When the 'StandardScaler' was used on the same data and a new model was trained the model produced the same results as the previous model. Therefore, both the standard and min-max scalers had no difference when applied to the data.

