from user import User
from exercise import Exercise
from workout import Workout
from progress import ProgressTracker

def main_menu():
    print("\n=== Fitness Training App ===")
    print("1. View Profile")
    print("2. Edit Profile")
    print("3. View Exercises")
    print("4. Create/Modify Workouts")
    print("5. Track Progress")
    print("6. Exit")

def profile_menu(user):
    print("\n=== Profile Menu ===")
    print("1. Display Info")
    print("2. Update Weight")
    print("3. Update Goal")
    choice = input("Choose an option: ")

    if choice == "1":
        print(user.display_info())
    elif choice == "2":
        new_weight = float(input("Enter new weight (kg): "))
        user.update_weight(new_weight)
        print("Weight updated.")
    elif choice == "3":
        new_goal = input("Enter new fitness goal: ")
        user.update_goal(new_goal)
        print("Goal updated.")

def view_exercises(exercises):
    print("\n=== Exercise Library ===")
    for exercise in exercises:
        print(exercise.display_exercise())

def workout_menu(workout):
    print("\n=== Workout Menu ===")
    print("1. Add Exercise")
    print("2. Remove Exercise")
    print("3. View Workout")
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Exercise Name: ")
        sets = int(input("Sets: "))
        reps = int(input("Reps: "))
        rest = int(input("Rest time (seconds): "))
        workout.add_exercise(name, sets, reps, rest)
        print("Exercise added to workout.")
    elif choice == "2":
        name = input("Enter the name of the exercise to remove: ")
        workout.remove_exercise(name)
        print("Exercise removed from workout.")
    elif choice == "3":
        print(workout.view_workout())

def progress_menu(progress_tracker):
    print("\n=== Progress Tracker ===")
    print("1. Log Workout")
    print("2. Generate Report")
    choice = input("Choose an option: ")

    if choice == "1":
        workout_name = input("Workout Name to Log: ")
        workout = Workout(workout_name)
        progress_tracker.log_workout(workout)
        print("Workout logged.")
    elif choice == "2":
        print(progress_tracker.generate_report())

def main():
    user = User("John Doe", 25, 70, 175, "Lose weight")
    exercises = [
        Exercise("Push-Up", "Push-up exercise to strengthen chest and arms", "Moderate"),
        Exercise("Squat", "Squat exercise for leg strength", "Easy"),
        Exercise("Lunge", "Lunge exercise for leg and glute strength", "Hard")
    ]
    workout = Workout("Full Body Workout")
    progress_tracker = ProgressTracker(user)

    while True:
        main_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            profile_menu(user)
        elif choice == "2":
            profile_menu(user)
        elif choice == "3":
            view_exercises(exercises)
        elif choice == "4":
            workout_menu(workout)
        elif choice == "5":
            progress_menu(progress_tracker)
        elif choice == "6":
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()