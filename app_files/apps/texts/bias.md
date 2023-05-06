### The favourite-longshot bias

Let us now take a look at how the bias shows up. We should remember that if each quoted price correctly reflected the true probability of its outcome, then any sample of predicted outcomes should yield a return of 1 minus the overround. And since this should be true for any sufficiently large sample, there should not be any statistically significant difference between two samples taken from two distinct price ranges, say one for prices around 1.5 and another for prices around 5.

How do we graphically test whether this is the case? Well,
- for each possible outcome (HomeWin, Draw, AwayWin)
- we sort the quoted prices from smaller to larger, 
- we create a fixed number of bins, so that all bookmakers can be compared
- and for each bin we compute two figures:
    1. the potential return from equally sized bets on all outcomes in the bin
    2. what we expect we should win, which is 1 minus the overround
- finally, we plot the two lines against each other


If there were no bias we would expect the two lines to roughly move together. No matter what the price range, the return should be 1 minus the overround, besides the natural variations due to chance.

Instead, we make the following observations:
- There is an overall tendency for lower prices (bins closer to zero), that is higher probabilities of the outcome coming true, or in other words favourites, to have significantly higher returns compared to higher prices, or in other words long-shots
- This tendency is more pronounced the higher the overround applied by the bookmaker.
- Even for Pinnacle Sports though, that operate with the lowest overround of the whole market, the tendency is evident, especially for the AwayWin, although less pronounced.

Take a look at the interactive graph and see for yourself!
