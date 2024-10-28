class ProgressTracker:
    def __init__(self, user):
        self.user = user

    def log_workout(self, workout):
        self.user.log_workout(workout)

    def generate_report(self):
        total_workouts = len(self.user.workout_history)
        report = f"{self.user.name} has completed {total_workouts} workouts.\n"
        for workout in self.user.workout_history:
            report += f"- {workout.name}\n"
        return report