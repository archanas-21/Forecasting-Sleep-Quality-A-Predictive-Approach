def generate_advice(row):
    advice = []

    if row['sleep_hours'] < 6.5:
        advice.append("Try to increase sleep to at least 7 hours per night.")
    if row['screen_time'] > 2.5:
        advice.append("Reduce screen time 1 hour before bed (use night mode or blue-light filter).")
    if row['exercise_mins'] < 20:
        advice.append("Include at least 20–30 minutes of physical activity daily.")
    if row['caffeine_cups'] >= 2:
        advice.append("Avoid caffeine late in the day; limit to 1 cup earlier in the day.")
    if row['bedtime_variability_mins'] > 60:
        advice.append("Keep a consistent sleep schedule (go to bed & wake up at similar times).")
    if row['has_sleep_disorder'] == 1:
        advice.append("Consult a sleep specialist — there are treatable conditions like sleep apnea or insomnia.")
    if row['stress_level'] == 'High':
        advice.append("Practice relaxation: breathing exercises, meditation, or journaling before bed.")

    if len(advice) == 0:
        advice = ["Your habits look pretty good — keep them consistent!"]

    return advice
