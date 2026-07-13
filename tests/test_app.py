import unittest

from app import create_app


class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hola Flask", response.data)

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"ok", response.data)

    def test_user_registration(self):
        response = self.client.post(
            "/register",
            data={
                "name": "Ana",
                "email": "ana@example.com",
                "password": "secret123",
            },
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Registro exitoso", response.data)


if __name__ == "__main__":
    unittest.main()
