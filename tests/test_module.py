import unittest
from email_sender_automation import EmailAutomation

class TestEmailAutomation(unittest.TestCase):
    def setUp(self):
        self.automation = EmailAutomation()

    def test_template_generation(self):
        company = "Test Co"
        image = "http://test.com/img.png"
        content = "Hello World"
        html = self.automation.generate_html_template(company, image, content)
        
        self.assertIn(company, html)
        self.assertIn(image, html)
        self.assertIn(content, html)
        self.assertIn("<!DOCTYPE html>", html)

if __name__ == "__main__":
    unittest.main()
