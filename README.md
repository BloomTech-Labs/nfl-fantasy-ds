
# NFL Fantasy Perfect Trade

You can find the project at [https://nfl-perfect-trader.herokuapp.com](https://nfl-perfect-trader.herokuapp.com/api/trade/?player0_id=23&player1_id=49&week=1).

## Contributors

|                                       [Jim King](https://github.com/JimKing100)                                        |                                       [Student 2](https://github.com/)                                        |
| :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: | 
|                      [<img src="https://github.com/Lambda-School-Labs/nfl-fantasy-ds/blob/master/images/Jim%20King-PacUnion-Color-Web.jpg" width = "200" />](https://github.com/)                       |                      [<img src="https://www.dalesjewelers.com/wp-content/uploads/2018/10/placeholder-silhouette-female.png" width = "200" />](https://github.com/)                       |
|                 [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/)                 |            [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/JimKing100)             |  
| [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/jimkinghomes/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/) |


![MIT](https://img.shields.io/packagist/l/doctrine/orm.svg)

🚫 more info on using badges [here](https://github.com/badges/shields)

## Project Overview


[Trello Board](https://trello.com/b/GR22EAEc/nfl-fantasy-perfect-trade)

[Product Canvas](https://www.notion.so/NFL-Fantasy-Perfect-Trade-881bd44def114fda8cffd8ccc362caf0)

NFL Fantasy Perfect Trade

An application to help fantasy football fans analyze potential player trades, make the optimal trades and win their fantasy football league competitions.

🚫  delete if front end is not applicable to your project

1️⃣ [Deployed Front End](🚫add link to deployed app here)

### Tech Stack

🚫 List all of the languages, frameworks, services, etc used here.

### 2️⃣ Predictions

Multiple models are employed to predict fantasy football points for each player, each week during the 2019 NFL season.

For NFL defenses an ARIMA model is used as there are 18-20 seasons of weekly game data (288 - 320 data points in a time series).

For rookie players, there are no pro data points, so for week 1 of the 2019 season an XGBoost model is used using background data for the player including combine data (e.g. 40 yard dash, bench press, etc.), biometric data (height and weight), college data (college and division), and draft position.  After week 1, rookie predictions are based on a simple average of actual points.

For non-rookie players, an ARIMA model is used for players with 4+ years of data (49+ data points in a time series).  Since an ARIMA model does not work well with fewer than 50 data points, an average of actual points is used for non-rookie players with 3 or fewer seasons of data.

### 2️⃣ Explanatory Variables

-   Explanatory Variable 1
-   Explanatory Variable 2
-   Explanatory Variable 3
-   Explanatory Variable 4
-   Explanatory Variable 5

### Data Sources
🚫  Add to or delete souce links as needed for your project


-   [Source 1] (🚫add link to python notebook here)
-   [Source 2] (🚫add link to python notebook here)
-   [Source 3] (🚫add link to python notebook here)
-   [Source 4] (🚫add link to python notebook here)
-   [Source 5] (🚫add link to python notebook here)

### Python Notebooks

🚫  Add to or delete python notebook links as needed for your project

[Python Notebook 1](🚫add link to python notebook here)

[Python Notebook 2](🚫add link to python notebook here)

[Python Notebook 3](🚫add link to python notebook here)

### 3️⃣ How to connect to the web API

🚫 List directions on how to connect to the API here

### 3️⃣ How to connect to the data API

🚫 List directions on how to connect to the API here

## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

Please note we have a [code of conduct](./code_of_conduct.md.md). Please follow it in all your interactions with the project.

### Issue/Bug Request

 **If you are having an issue with the existing project code, please submit a bug report under the following guidelines:**
 - Check first to see if your issue has already been reported.
 - Check to see if the issue has recently been fixed by attempting to reproduce the issue using the latest master branch in the repository.
 - Create a live example of the problem.
 - Submit a detailed bug report including your environment & browser, steps to reproduce the issue, actual and expected outcomes,  where you believe the issue is originating from, and any potential solutions you have considered.

### Feature Requests

We would love to hear from you about new features which would improve this app and further the aims of our project. Please provide as much detail and information as possible to show us why you think your new feature should be implemented.

### Pull Requests

If you have developed a patch, bug fix, or new feature that would improve this app, please submit a pull request. It is best to communicate your ideas with the developers first before investing a great deal of time into a pull request to ensure that it will mesh smoothly with the project.

Remember that this project is licensed under the MIT license, and by submitting a pull request, you agree that your work will be, too.

#### Pull Request Guidelines

- Ensure any install or build dependencies are removed before the end of the layer when doing a build.
- Update the README.md with details of changes to the interface, including new plist variables, exposed ports, useful file locations and container parameters.
- Ensure that your code conforms to our existing code conventions and test coverage.
- Include the relevant issue number, if applicable.
- You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.

### Attribution

These contribution guidelines have been adapted from [this good-Contributing.md-template](https://gist.github.com/PurpleBooth/b24679402957c63ec426).

## Documentation

See [Backend Documentation](_link to your backend readme here_) for details on the backend of our project.

See [Front End Documentation](_link to your front end readme here_) for details on the front end of our project.

