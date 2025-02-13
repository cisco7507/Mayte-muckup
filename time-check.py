import argparse

def parse_time(time_str):
    """
    Parse a time string in the format hh:mm:ss:ms into total seconds.
    
    Parameters:
        time_str (str): Time in "hh:mm:ss:ms" format.
    
    Returns:
        float: Total seconds.
    
    Raises:
        ValueError: If the input format is incorrect.
    """
    parts = time_str.split(':')
    if len(parts) != 4:
        raise ValueError("Time format must be hh:mm:ss:ms")
    hours, minutes, seconds, ms = parts
    try:
        total_seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds) + int(ms) / 1000.0
    except ValueError:
        raise ValueError("Time components must be integers")
    return total_seconds


def get_closest_legal_time(time_str, legal_times, tolerance=0.6):
    """
    Compare the input time (converted to seconds) with a list of legal times.
    If the absolute difference between the input time and the closest legal time
    is within the tolerance, return that legal time. Otherwise, return None.
    
    Parameters:
        time_str (str): Time in "hh:mm:ss:ms" format.
        legal_times (list of float): Predefined legal times (in seconds).
        tolerance (float): Maximum allowed deviation in seconds.
        
    Returns:
        float or None: The closest legal time if within tolerance; otherwise None.
    """
    input_seconds = parse_time(time_str)
    
    closest_legal = None
    smallest_delta = None
    for legal in legal_times:
        delta = abs(input_seconds - legal)
        if smallest_delta is None or delta < smallest_delta:
            smallest_delta = delta
            closest_legal = legal

    if smallest_delta is not None and smallest_delta <= tolerance:
        return closest_legal
    else:
        return None


# ------------------
# Main functionality
# ------------------
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Evaluate a time value (hh:mm:ss:ms) against legal times."
    )
    parser.add_argument("time", help="Time in hh:mm:ss:ms format")
    args = parser.parse_args()

    # Predefined legal times in seconds.
    legal_times = [5, 10, 15, 30, 60, 90, 120]
    
    try:
        result = get_closest_legal_time(args.time, legal_times)
        if result is None:
            print("Timer rejected: deviation exceeds tolerance.")
        else:
            print(f"Closest legal time: {result}")
    except ValueError as e:
        print(f"Error: {e}")
