import unittest, sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from classes.ping_pong import PingPong

class TestPingPong(unittest.TestCase): 

    def test_pong(self):
        pong = PingPong()
        got = pong.pong()
        want = 'pong!'
        self.assertEqual(got, want)

if __name__ == '__main__':
    unittest.main()
