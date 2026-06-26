from service import TaskService


def run():
    service = TaskService()
    service.seed_sample_data()

    # Intentional bug: email is passed, but service expects numeric user_id.
    user_tasks = service.get_tasks_by_user("alice@example.com")

    # Intentional bug: NameError (task is undefined).
    print("Task count:", len(task))

    rate = service.completion_rate("alice@example.com")
    print(f"Completion rate: {rate:.0%}")
    print("Tasks:")
    for item in user_tasks:
        print("-", item["title"])


if __name__ == "__main__":
    run()
