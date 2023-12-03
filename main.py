def count_batteries_by_health(present_capacities):
    counts = {
        "healthy": 0,
        "exchange": 0,
        "failed": 0
    }

    for capacity in present_capacities:
        soh = (capacity / 120) * 100 
        if soh > 80:
            counts["healthy"] += 1
        elif 62 <= soh <= 80:
            counts["exchange"] += 1
        else:
            counts["failed"] += 1

    return counts

def test_bucketing_by_health():
    print("Counting batteries by SoH...\n")
    present_capacities = [113, 116, 80, 95, 92, 70]
    counts = count_batteries_by_health(present_capacities)
    assert counts["healthy"] == 2
    assert counts["exchange"] == 3
    assert counts["failed"] == 1
    print("Done counting :)")

if __name__ == '__main__':
    test_bucketing_by_health()

    # Additional test cases
    additional_capacities = [90, 105, 60, 78, 110]
    additional_counts = count_batteries_by_health(additional_capacities)
    print("\nAdditional Test:")
    print("Present Capacities:", additional_capacities)
    print("Counts:", additional_counts)
