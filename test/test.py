import unittest
import learnflask

class MyTestCase(unittest.TestCase):
    def setUp(self):
        learnflask.app.config['TESTING'] = True
        self.app = learnflask.app.test_client()

    def tearDown(self):
        print self._testMethodName + ' ok'

    def test_index(self):
        rv = self.app.get('/')
        assert 'hello' in rv.data

    def test_post(self):
        rv = self.app.post('/post/', data={'name':'value'}, follow_redirects=True)
        assert 'value' in rv.data



if __name__ == '__main__':
    unittest.main()
