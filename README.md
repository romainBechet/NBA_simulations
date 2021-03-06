# Estimated ranking for each conference 

## Idea
This project was influenced by an article of [Stats Perform](https://twitter.com/StatsPerform) ([link of the article](https://www.statsperform.com/resource/why-2021-could-be-the-year-of-change-in-european-football/)). In this article, they make predictions about the second part of each championship of the soccer european big five. 

They calculated expected points this way: 
> - The model estimates the probability of each match outcome (win, draw or loss) given each team’s attacking and defensive quality.
> - We can simulate the upcoming matches using goal predictions from the Poisson distribution with the two teams’ attacking and defending qualities as inputs.
> - Finally, we simulate the outcome of the season 10,000 times in order to estimate the likelihood of each team finishing in each league position

## Idea applied to basketball 
I was intrigued by this approach and decided to do the same for the second part of NBA season (Post All-Star Break). 

### How to estimate the probability of each game outcome? 

To answer this, basketball game was simplified to a maximum. A game is a sequence of possessions, and each one can result in four different outcomes (more info [here](http://www.nessis.org/nessis07/Kenny_Shirley.pdf)): 
- a 2 points shot 
- a 3 points shot 
- some free-throws 
- a turnover 

With the high number of statistics we have access to, and the convinience to use them, it's very easy to quantify the probability of each event, for each team. 
For example, on average this year, 12 % of possessions ended with a turnover, 28 %  with a 3 points shot, 43 % with a 2 points shot and 17 % with one free-throw (Yes one! It's more complicated if we do not simplify this). 

For each shot, the field goal percentage is used to simulate the shot. If the shot is missed, the offensive team has a chance to take an offensive rebound (Offensive rebounds rate). The ability to take an offensive rebound wasn't implemented for missed free-throws for simplification. 

### Face to Face 

Of course, the matchup between two teams is important. For each statistics, an expectation was computed based on offensive quality of teamA, defensive quality of teamB, and their relative position compared to the national average. 

### Validation 

While there are some approximations in the simulation, the different parameters were well estimated: few percent different for all the 2021 games already done (with data prior to the game). 

Talking about the outcome of a game, 1000 simulations were done for each game to validate the model. It was sligly more than 60% accurate for 2021 games, but 66% accurate for 2018-2019 games. This difference is easy to explain, due to many injuries and absences due to COVID this year. Indeed, the model does not take into account which player is going to participate to the game or the back-to-back for example. 

### Season Simulation 

In order to simulate the second part of the 2020-2021 NBA season, each game was simulated once, returning the output. A win was added to the winner and the next game was simulated. At the end of each season, the ranking was done based on the record of each team, the position and the total of wins were returned. Almost 38 000 seasons were simulated (Fun fact, the first time I read the article of StatsPerfom, I read 100,000 simulation, I just copy and paste their description and see they did 10,000 times...). 

### Data 
 
The only data I added to this folder were the results of each season simulation.
```.
└── Data
    └── results_rank.csv # The ranking for each team (conference ranking), for each simulation. 
    └── results_wins.csv # Number of wins for each simulation and each team. 
```

### Disclaimer

There are lots of approximations in this simulation. Like I said before, back-to-back or other dense schedules weren't take into consideration (Memphis for example has many more games than the other teams), as well as the pre All-Star dynamic (Whasington & Boston for example). During validations and simulations, I learnt to recognize which teams are favored or not by this system. For example, Golden State, an unconstant team with lot of variability, is rarely a big favourite for any game, and is more likely a contender. Finally, defense and offense are equally take in consideration for the computation of the expectation statistics. In the actual NBA, some adjustments may be necessary.  

