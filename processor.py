import re

def extract_observations(text):
    observations = []

    lines = text.split("\n")
    for line in lines:
        if "dampness" in line.lower() or "leakage" in line.lower():
            observations.append(line.strip())

    return observations


def extract_thermal_data(text):
    temps = re.findall(r"Coldspot\s*:\s*(\d+\.?\d*)", text)
    temps = [float(t) for t in temps]

    return {
        "min_temp": min(temps) if temps else None,
        "max_temp": max(temps) if temps else None,
        "all": temps
    }


def merge_data(observations, thermal_data):
    merged = []

    for obs in observations:
        entry = {
            "observation": obs,
            "thermal_flag": None
        }

        if thermal_data["min_temp"] and thermal_data["min_temp"] < 23:
            entry["thermal_flag"] = "Possible moisture detected"

        merged.append(entry)

    return merged