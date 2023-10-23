import unittest, sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from classes.bible import Bible

class TestBible(unittest.TestCase):

    def test_http_status(self):
        bible = Bible()
        bible.get_verse()
        want = 200
        got = bible.status()

        self.assertEqual(got, want)


    def test_check_book(self):
        bible = Bible()
        want = 'JHN.3.16'
        got = bible.check_book('John 3:16')
        
        self.assertEqual(got, want)

    def test_failing_check_book(self):
        bible = Bible()
        want = 'Not found'
        got = bible.check_book('Erro')

        self.assertEqual(got, want)
        

    # TODO
    def test_get_verse_text(self):
        bible = Bible()
        want = '¶ For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life.'
        got = bible.get_verse()

        #self.assertEqual(got, want)

if __name__ == '__main__':
    unittest.main()