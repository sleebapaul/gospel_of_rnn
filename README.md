# Language modelling using PyTorch

## Folders

### char_rnn

It contains the character level language modelling in tinyshakespheare dataset using Recurrent Neural Networks implemented with PyTorch. The data set and a well commented jupyter notebook is added in this folder. The jupyter notebook is orignally a Google Colab notebook. If you find it difficult to reproduce the results locally, try it on Google Colaboratory. Anyway you can find the original work at [here](https://drive.google.com/file/d/12pEy-aOS0_PiVkFgxyINmBbtuvB5TqV5/view?usp=sharing).   

A bunch of `sample` folders are added in this folder where you can find the performance of the network at different hyper parameter settings. Each folder will contain a generated text file, a loss vs iterations graph and the saved trained model which can be reused using PyTorch. This is planned as a programming session for [this blog post in my personal blog](https://sleebapaul.github.io/rnn-tutorial-2/).

### bible database  

This folder contains the different bible version data in JSON format. The versions are, 

1. American Standard-ASV1901 (ASV)
2. Bible in Basic English (BBE)
3. Darby English Bible (DARBY)
4. King James Version (KJV)
5. Webster's Bible (WBT)
6. Young's Literal Translation (YLT)

Bible data is originally dowloaded from [this github repo](https://github.com/scrollmapper/bible_databases). 

### raw_gospel_data 

This folder includes the raw gospel text extracted from the bible database and stored as JSON files.  

### training_data 

This folder contains the data for training the LSTMs which are generated from the files in `raw_data` folder.  

### notebooks 

This folder contains the Jupyter Notebooks which shows the demo of data fetching, cleaning EDA of bible stats. Bible stats is available in JSON format at root folder. 

### scripts

The scripts for cleaning and converting raw data to training data is included in the folder. The demos in `notebook` folder comes in action here. 

### best_model 

The folder contains the best trained model, loss vs epochs graph and stats of training. 

### issues_of_mark

The folder contains the training results on different validation sets. Using gospel of Mark as validation shows less convergence. 

### generated_gospels

Some generated samples using trained model using warmup context. 

## Important Links

Medium Post: https://medium.com/@sleebapaul/gospel-of-lstms-how-i-wrote-5th-gospel-of-bible-using-lstms-4cffa70e5f1a

Google Colab Link: https://colab.research.google.com/drive/1euakjbNiZgCfbmCWzT6pIZB2MYZbHjk-

The trained model can be reproduced in Colab Notebook. Though, I've added the copy of Colab Notebook as `pytorch_LSTM.ipynb` for the local reference, I recommend the reader to make efforts for reproducing the results at Google Colaboratory.  

I've added the Gospel of LSTMs `epub` version in the repo. Please use it for better reading experience.   

Happy Learning !