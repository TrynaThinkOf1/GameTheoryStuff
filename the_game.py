from main_func import main
from engines import *
from collections import defaultdict


def run_tournament(num_rounds: int):
    """
    Runs a complete tournament for a specified number of rounds.

    Args:
        num_rounds (int): Number of times to run the complete tournament
    """
    engines = [
        AlwaysTrue, TitForTat, GrimTrigger, Pavlov,
        ForgivingTitForTat, RandomWithBias, GradualTitForTat,
        AdaptiveStrategy, MajorityRule, SoftMajority, TwoTitsForTat,
        SuspiciousTitForTat, TitForTwoTats, ProberStrategy,
        PatternHunter, FrequencyAnalyzer, MomentumBased,
        RiskAdjuster, DeceptionDetector, TrendFollower,
        GradualLearner, MetaStrategy, ReputationBased, CycleDetector,
        ProbabilisticMimicry, AdversityLearner
    ]

    # Track cumulative points across all rounds
    total_points = defaultdict(int)

    # Suppress output during tournament execution
    import sys
    from io import StringIO
    old_stdout = sys.stdout

    # Run the specified number of complete tournaments
    for round_num in range(num_rounds):
        # Redirect stdout to suppress intermediate output
        sys.stdout = StringIO()

        # Run a complete tournament round
        for i in range(len(engines)):
            for j in range(i + 1, len(engines)):
                engine1, engine2 = engines[i], engines[j]
                main(engine1, engine2)

                # Extract points from the last line of output
                output = sys.stdout.getvalue().strip().split('\n')[-1]
                p1_name = output.split(':')[0].strip()
                p2_name = output.split(',')[1].split(':')[0].strip()
                p1_points = int(output.split(':')[1].split(',')[0].strip())
                p2_points = int(output.split(':')[2].strip())

                # Accumulate points
                total_points[p1_name] += p1_points
                total_points[p2_name] += p2_points

                # Clear the StringIO buffer
                sys.stdout = StringIO()

    # Restore normal stdout
    sys.stdout = old_stdout

    # Calculate and display final leaderboard
    leaderboard = sorted(total_points.items(), key=lambda x: x[1], reverse=True)

    print(f"\nTournament Leaderboard (After {num_rounds} rounds):")
    print("-" * 50)
    print(f"{'Rank':<6}{'Engine':<25}{'Total Points':<12}{'Avg/Round':<8}")
    print("-" * 50)

    for rank, (engine, points) in enumerate(leaderboard, 1):
        avg_points = points / num_rounds
        print(f"{rank:<6}{engine:<25}{points:<12}{avg_points:.1f}")


if __name__ == "__main__":
    run_tournament(5)  # Example: Run 10 complete tournaments