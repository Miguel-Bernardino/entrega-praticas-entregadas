import unittest
from app.app import app

class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_print_health_check(self):
        response = self.app.get('/health-check')
        self.assertEqual(200, response.status_code, "Erro no test_http_code!")
        self.assertEqual("<h1>Hello, I'm Alive!</h1>", response.get_data(as_text=True)
                          , "Erro no test_print_health_check!")
    
    def  test_print_hello_fail(self):
        response = self.app.get('/hello')
        self.assertEqual(400, response.status_code, "Erro ao informar as informacoes do usuário")

    def test_print_hello_sucess(self):
            name_teste = "Joao"
            response = self.app.get('/hello', query_string={'name': name_teste})
            self.assertEqual(200, response.status_code, "O status code deveria ser 200")
            expected_message = f"Hello, {name_teste}!"
            self.assertEqual(expected_message, response.get_data(as_text=True), "A mensagem de saudação está incorreta")
