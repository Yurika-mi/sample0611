import unittest

from service import TaskService


class TaskServiceTest(unittest.TestCase):
    def setUp(self):
        self.service = TaskService()
        self.service.seed_sample_data()

    def test_get_tasks_by_user_with_email(self):
        tasks = self.service.get_tasks_by_user("alice@example.com")
        self.assertEqual([task["title"] for task in tasks], ["Create login page", "Add input validation"])

    def test_completion_rate_with_email(self):
        self.assertEqual(self.service.completion_rate("alice@example.com"), 0.5)


if __name__ == "__main__":
    unittest.main()
