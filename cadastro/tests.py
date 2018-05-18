from django.test import TestCase
from .models import Cadastro


class CadastroTesteViews(TestCase):
    """
        Teste função a urls
    """

    def test_request200(self):
        response = self.client.get('/employee/')
        self.assertEqual(response.status_code, 200)


class CadastroTesteModel(TestCase):

    """
        Testes funções models
    """
    def setUp(self):
        self.arnaldo = Cadastro.objects.create(
            active=True, name='Arnaldo Pereira',
            email='arnaldo@gmail.com', department='Developer'
        )

    def teste_funcionario_name(self):
        self.assertEqual(self.arnaldo.name, 'Arnaldo Pereira')

    def teste_funcionario_email(self):
        self.assertEqual(self.arnaldo.email, 'arnaldo@gmail.com')

    def teste_funcionario_department(self):
        self.assertEqual(self.arnaldo.department, 'Developer')







#python manage.py test
