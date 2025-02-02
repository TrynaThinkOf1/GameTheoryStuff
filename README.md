# Game Theory Strategy Tournament

## Overview
This project implements an iterated prisoner's dilemma tournament system featuring 29 distinct strategic engines. Each engine employs unique decision-making algorithms to compete in head-to-head matches, accumulating points based on cooperation and defection choices.

## Game Mechanics

### Scoring System
- Mutual Cooperation: Both players receive 3 points
- Mutual Defection: Both players receive 1 point
- Unilateral Defection: Defector receives 5 points, Cooperator receives 0 points

### Match Structure
- Random initial player selection
- Variable game length (50-199 rounds)
- Points accumulated throughout each match
- Tournament supports multiple complete rounds

## Installation & Usage

```python
# Run a tournament with 10 rounds
from tournament import run_tournament
run_tournament(10)
```

## Strategy Engines

### Basic Strategies

#### AlwaysTrue
- Consistently cooperates regardless of opponent's moves
- Predictable but vulnerable to exploitation
- Optimal against fellow cooperators

#### AlwaysFalse
- Consistently defects regardless of opponent's moves
- Exploitative strategy
- Guarantees minimum points through constant defection

#### Random
- Randomly selects between cooperation (True) and defection (False)
- 50% probability for each choice
- Unpredictable but lacks strategic depth

### Pattern-Based Strategies

#### PatternHunter
- Analyzes opponent's move sequences
- Identifies and exploits repetitive patterns
- Adapts strategy based on pattern recognition

#### CycleDetector
- Specializes in identifying cyclical behavior
- Counters predicted cycles
- Defaults to cooperation when no cycles detected

#### FrequencyAnalyzer
- Monitors cooperation/defection frequencies
- Adjusts strategy based on statistical analysis
- Employs probability-based decision making

### Memory-Based Strategies

#### TitForTat
- Mirrors opponent's previous move
- Simple but effective strategy
- Promotes cooperation through reciprocity

#### GrimTrigger
- Begins cooperatively
- Permanently defects after first betrayal
- Implements unforgiving punishment mechanism

#### ForgivingTitForTat
- Similar to TitForTat but more lenient
- Allows up to two defections before retaliating
- Promotes cooperation while deterring exploitation

### Adaptive Strategies

#### AdaptiveStrategy
- Learns from opponent's behavior patterns
- Adjusts cooperation probability dynamically
- Optimizes strategy through experience

#### GradualLearner
- Implements incremental strategy adjustments
- Uses learning rate for behavioral modification
- Balances exploration and exploitation

#### MetaStrategy
- Switches between multiple sub-strategies
- Adapts based on performance metrics
- Implements strategic diversity

### Psychological Strategies

#### Pavlov
- Responds to outcome patterns
- Stays with successful strategies
- Changes approach after failures

#### DeceptionDetector
- Evaluates opponent trustworthiness
- Maintains dynamic trust scores
- Adapts based on promise fulfillment

#### ReputationBased
- Tracks opponent's reputation score
- Uses limited memory window
- Makes decisions based on historical behavior

### Advanced Analysis Strategies

#### MomentumBased
- Identifies and follows behavioral trends
- Capitalizes on strategic momentum
- Adapts to changing patterns

#### RiskAdjuster
- Maintains dynamic risk threshold
- Becomes conservative after betrayals
- Gradually returns to baseline risk level

#### TrendFollower
- Analyzes directional behavior patterns
- Makes decisions based on emerging trends
- Uses sliding window analysis

### Specialized Strategies

#### ProberStrategy
- Tests opponent responses
- Identifies exploitation opportunities
- Adapts based on initial interactions

#### ProbabilisticMimicry
- Combines copying with randomization
- Maintains strategic unpredictability
- Balances imitation and innovation

#### AdversityLearner
- Tracks cumulative stress levels
- Implements recovery mechanisms
- Adapts to hostile environments

### Additional Strategies

#### GradualTitForTat
- Increases punishment severity progressively
- Implements proportional retaliation
- Maintains cooperation potential

#### TwoTitsForTat
- Requires two consecutive defections to retaliate
- More forgiving than standard TitForTat
- Promotes stable cooperation

#### SuspiciousTitForTat
- Begins with defection
- Follows TitForTat afterward
- Tests opponent's response to betrayal

#### MajorityRule
- Bases decisions on historical majority
- Uses complete game history
- Implements democratic decision-making

#### SoftMajority
- Similar to MajorityRule but more lenient
- Requires fewer cooperative moves
- Promotes optimistic cooperation

#### RandomWithBias
- Implements weighted random choices
- Maintains cooperation bias
- Balances predictability and randomness

## Contributing
Contributions are welcome! To add new strategies:
1. Create a new engine class
2. Implement the required methods (`__init__`, `move`, `__repr__`)
3. Add the engine to the tournament roster

## License
This project is licensed under the MIT License - see the LICENSE file for details.