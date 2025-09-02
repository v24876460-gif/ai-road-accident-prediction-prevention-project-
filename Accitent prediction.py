import random
import time
import datetime

# ================= Accident Detection & Emergency Mode =================
class AccidentSystem:
    def __init__(self):
        self.impact_sensor = False
        self.speed = 60
        self.location = "NH-45, Coimbatore Bypass"

    def check_accident(self):
        # Accident condition: speed < 10 AND impact_sensor True
        return self.speed < 10 and self.impact_sensor

    def trigger_emergency_mode(self):
        print("\n🚨 Accident Detected! Activating Emergency Mode...")
        time.sleep(1)
        print("📞 Calling Emergency Number: 108")
        print(f"📍 Sharing GPS location: {self.location}")
        print("👨‍👩‍👧 Family & 🚔 Police alerted")
        print("🚗 Car doors unlocked for rescue access")
        eta = random.randint(5, 15)
        print(f"🚑 Rescue Team ETA: {eta} minutes")

# ================= Accident Risk Prediction =================
def accident_risk(speed, distance, fatigue, weather, traffic, road):
    print("\n🔹 Accident Risk Prediction Module")
    risk = (speed / 120) * 30 + (fatigue / 5) * 20 + max(0, 30 - distance) * 0.8
    if weather in ["Rain", "Fog"]:
        risk += 15
    if traffic in ["Moderate", "Heavy"]:
        risk += 15
    if road == "Damaged":
        risk += 10
    risk = min(100, round(risk, 1))
    print(f"Predicted Risk: {risk}%")
    return risk

# ================= Safety Actions =================
def safety_actions(speed, lane):
    print("\n🔹 Instant Safety Actions Module")
    if speed > 80:
        print(f"⚠️ High Speed: {speed} km/h → Brake / Reduce Speed.")
    else:
        print(f"✅ Speed Normal: {speed} km/h")
    if lane == "unsafe":
        print("⚠️ Unsafe Lane Change Detected!")
    else:
        print("✅ Lane Change Safe")

# ================= Special Driving Modes =================
def special_modes(zone, weather, highway):
    print("\n🔹 Special Driving Modes Module")
    if zone == "school":
        print("🏫 School Zone → Extra Safety Alerts Activated!")
    if weather.lower() in ["rain", "fog"]:
        print(f"🌧️ Weather: {weather} → Visibility Warning Activated!")
    if highway == "yes":
        fatigue_risk = random.choice(["Low", "Medium", "High"])
        print(f"🛣️ Highway Mode → Fatigue Risk: {fatigue_risk}")
        if fatigue_risk == "High":
            print("⚠️ Rest Suggested at nearest stop.")

# ================= Alternative Route Suggestion =================
def alt_route(risk):
    print("\n🔹 Alternative Route Suggestion Module")
    if risk >= 60:
        r = random.choice(["Main Highway", "Route A via NH77", "Route B via Coastal Road"])
        eta = random.randint(15, 60)
        print(f"🛣️ Recommended Alternative: {r}, ETA ~{eta} min")
    else:
        print("✅ Main route safe. No alternative needed.")

# ================= Smart Rescue Support =================
def rescue_support(location):
    print("\n🔹 Smart Rescue Support Module")
    team = random.choice(["Team-A", "Team-B", "Team-C"])
    eta = random.randint(5, 15)
    print(f"🚑 Rescue Team: {team}, ETA: {eta} min → Accident location: {location}")

# ================= Morning/Evening Notification =================
def time_notification():
    now = datetime.datetime.now()
    hour = now.hour
    period = "Morning" if 5 <= hour < 12 else "Evening" if 17 <= hour < 20 else "Day"
    traffic = random.choice(["Light", "Moderate", "Heavy"])
    risk_area = random.choice(["XYZ Road", "ABC Highway", "LMN Street"])
    print(f"\n[LUNA] Good {period}! Today is {now.strftime('%A, %d %B %Y')}. Traffic: {traffic}. Risk area: {risk_area}.")

# ================= Tick Simulation =================
def run_luna(ticks=3):
    system = AccidentSystem()
    time_notification()

    for i in range(ticks):
        print(f"\n--- Tick {i+1} ---")
        use_input = input("Enter custom sensor data? (y/n): ").strip().lower()

        if use_input == "y":
            try:
                system.speed = int(input("Speed (km/h): "))
                distance = int(input("Distance to next vehicle (m): "))
                fatigue = int(input("Fatigue level (1-5): "))
                weather = input("Weather (Clear/Rain/Fog): ")
                traffic = input("Traffic (Light/Moderate/Heavy): ")
                road = input("Road (Good/Damaged): ")
                lane = input("Lane (safe/unsafe): ")

                # Run modules
                risk = accident_risk(system.speed, distance, fatigue, weather, traffic, road)
                safety_actions(system.speed, lane)
                alt_route(risk)
                special_modes("school", weather, "yes")

                # Accident check
                system.impact_sensor = bool(int(input("Impact Sensor Triggered? (1-Yes, 0-No): ")))
                if system.check_accident():
                    system.trigger_emergency_mode()
                    rescue_support(system.location)

            except Exception as e:
                print(f"⚠️ Input Error: {e}")
        else:
            # Run default safe scenario
            risk = accident_risk(system.speed, 20, 2, "Clear", "Light", "Good")
            safety_actions(system.speed, "safe")
            alt_route(risk)
            special_modes("normal", "Clear", "yes")

# ================= Main Run =================
if __name__ == "__main__":
    run_luna(3)
