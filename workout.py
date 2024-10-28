class Workout:
    def __init__(self, name):
        self.name = name
        self.exercises = []

    def add_exercise(self, exercise, sets, reps, rest_time):
        self.exercises.append({
            'exercise': exercise,
            'sets': sets,
            'reps': reps,
            'rest_time': rest_time
        })

    def remove_exercise(self, exercise_name):
        self.exercises = [
            ex for ex in self.exercises if ex['exercise'].name != exercise_name
        ]

    def view_workout(self):
        workout_info = f"Workout: {self.name}\n"
        for ex in self.exercises:
            workout_info += (f"{ex['exercise'].name}: {ex['sets']} sets, {ex['reps']} reps, "
                             f"{ex['rest_time']} seconds rest\n")
        return workout_info