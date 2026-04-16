import re

KEYWORDS = ["dampness", "leakage", "crack", "seepage", "hollowness"]

AREAS = ["hall", "bedroom", "kitchen", "bathroom", "parking", "external wall"]

def detect_area(text):
    for area in AREAS:
        if area in text.lower():
            return area.title()
    return "Unknown"


def extract_observations(text):
    observations = []

    for line in text.split("\n"):
        if any(k in line.lower() for k in KEYWORDS):
            observations.append({
                "area": detect_area(line),
                "issue": line.strip()
            })

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
            "area": obs["area"],
            "issue": obs["issue"],
            "thermal_flag": "Not Available",
            "conflict": None
        }

        # Thermal logic
        if thermal_data["min_temp"] is not None:
            if thermal_data["min_temp"] < 23:
                entry["thermal_flag"] = "Moisture anomaly detected"
            else:
                entry["thermal_flag"] = "No significant anomaly"

        # Conflict detection
        if "no" in obs["issue"].lower() and entry["thermal_flag"] == "Moisture anomaly detected":
            entry["conflict"] = "Conflict detected between inspection and thermal data"

        merged.append(entry)

    return merged


def ensure_not_available(data):
    for d in data:
        if not d.get("issue"):
            d["issue"] = "Not Available"
        if not d.get("area"):
            d["area"] = "Not Available"
    return data
