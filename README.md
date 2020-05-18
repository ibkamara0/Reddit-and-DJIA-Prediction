# Reddit-and-DJIA-Prediction
This project was done simply for fun to gain some additional experience in the world of machine learning and natural language processing. I used data from Kaggle on which involved the Dow Jones Industrial Averages with different news articles. The data provided displayed various headlines and labels, where "1" meant the average rose or remained the same, and "0" meant there was a decline in the average.

I trained this data with different algorithms then created a GUI(Graphical User Interface) that allows you to insert a headline from Reddit World News and get a prediction of whether the Dow Jones Industrial Average will rise/remain or fall. I used to algorithms to create a voting system, the more models that would choose a certain classification ("1" or "0"), the higher the confidence of the prediction. The comments in both my jupyter notebook and code explain what each piece does. Feel free to take this and apply it to your own datasets and scenarios.

![Demo](https://github.com/ibkamara0/Reddit-and-DJIA-Prediction/blob/master/prediction%20application.gif)

The jupyter notebook is where I take the data for training and test. Then, save the models as pickle for use in a GUI. The GUI is where I convert the user input into readable data for the models and then get the prediction.

Below, there are is a link to the dataset. There is also a link to some YouTube videos that helped me with this project.

Data: https://www.kaggle.com/aaron7sun/stocknews
Useful tutorial(s): 
- The Semicolon : https://www.youtube.com/watch?v=ReakZVh2Xwk&list=PLQVvvaa0QuDf2JswnfiGkliBInZnIC4HL&index=14 
- Sentdex : https://www.youtube.com/watch?v=bPYJi1E9xeM&t=487s


