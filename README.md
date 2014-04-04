#augur

_noun_

  1. (in ancient Rome) a religious official who observed natural signs, esp. the behavior of birds, interpreting these as an indication of divine approval or disapproval of a proposed action.
  2. An awesome rankings predictor for FRC.

##Why do we need a rankings predictor?

A rankings predictor helps teams to visualize what teams will be seeded in the top 8.  This helps teams cater their strategies and decide what features to showcase the next day, increasing their chances of being picked.  Alternatively, teams that are predicted to seed can use this to predict other teams who may seed higher, predict whether or not 'scorched earth' tactics could be a possibility for the next day, and more.

##Theory
A typical FRC match can have three distinct outcomes:
  1. Red wins
  2. Blue wins
  3. Red and Blue tie.

Therefore, for n matches, we have 3^n possible combinations of outcomes.  However, since the probability of a red and blue tie is so low, we choose to ignore it.  This reduces the number of combinations to 2^n.  Essentially, what we do is calculate all 2^n possibilities, compute the first 12 rankings for those possibilities (again, to save computation time), and then analyze them.  

###What about Tiebreakers?

Tiebreakers, like Assist Points, Auto Points, Truss and Catch Points, and Teleop Points are manually entered.  Since there's no really good way to predict how these numbers will end up.  We leave it to the human to predict these values.

##Form follows Function
Because predicting rankings is so computationally intensive, augur uses a distributed computing model.  This means that augur actually runs as a set of seperate programs.  The augur server delegates computation to augur workers -- these workers could be processes that run concurrently on the same computer, computers on the same network, or computers connected via the internet.  This parallelism helps increase the execution speed and makes prediction viable.
