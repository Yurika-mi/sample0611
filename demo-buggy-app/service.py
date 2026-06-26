class TaskService:
    def __init__(self):
        self.users = {}
        self.tasks = []

    def seed_sample_data(self):
        self.users = {
            1: "alice@example.com",
            2: "bob@example.com",
        }
        self.tasks = [
            {"id": 1, "user_id": 1, "title": "Create login page", "done": True},
            {"id": 2, "user_id": 1, "title": "Add input validation", "done": False},
            {"id": 3, "user_id": 2, "title": "Prepare release note", "done": True},
        ]

    def get_tasks_by_user(self, user_id):
        # Intentional bug: wrong key "user" causes KeyError.
        return [task for task in self.tasks if task["user"] == user_id]

    def completion_rate(self, user_id):
        user_tasks = self.get_tasks_by_user(user_id)
        done_count = len([task for task in user_tasks if task["done"]])
        return done_count / len(user_tasks)
