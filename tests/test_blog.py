from django.test import Client, TestCase


class IndexPageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.response = self.client.get("/")

    def test_view_works(self):
        self.assertEqual(self.response.status_code, 200)

    def test_view_has_link(self):
        self.assertContains(self.response, "/add_post")


class AddPostPageTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_view_works(self):
        r = self.client.get("/add_post")
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, "<form")
        self.assertContains(r, "<input")

    def test_adding_works(self):
        r = self.client.post(
            "/add_post",
            {"body": "some text", "title": "some title", "submit": "Submit"},
        )
        r = self.client.get("/")
        self.assertContains(r, "some text")
