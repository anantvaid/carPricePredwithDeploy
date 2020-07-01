# carPricePredwithDeploy
This is my project on car price prediction from cardekho data on Kaggle. The project was inspired by Krish Naik.
### Inspiration
Sir Krish Naik
### About
This project has the data source from https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho . It uses RandomForestRegressor with hyperparameter tuning using RandomizedSearchCV.
This predicts the car selling price based on the data it is feeded with. It is not a perfect type and data checking algoritm, so is susceptible with bad data.
This project uses Streamlit and heroku for deployment.
### How to use it?
- Clone/Download the repository in the local system
- In the terminal type pip install requirements.txt
- In the terminal type streamlit run app.py (Make Sure that the app doesn't have a different name else type other.py)y
### Deployment
- Add a Procfile stating web: sh setup.sh && streamlit run app.py 
- Add requirements.txt by pip freeze > requirements.txt *(BEWARE THERE MIGHT BE EXTRA LIBRARIES THAT WAS PRESENT BEFORE HAND DUE TO THE ENVIRONMENT - ALWAYS ADVISABLE TO CREATE NEW ENV)*
- Add setup.sh and paste this: 
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml

- If using Heroku, install heroku.cli, Then make an account on heroku.
- In the terminal type heroku login
- Type heroku create <appname>  *It gives the URL*
- git init
- git add .
- git commit -am "<message>"
- git push heroku master
- Use the URL above to see the app.
