import unittest
from fct_to_tests import  parse_event

class TestFct(unittest.TestCase):

    def test_validate_event_as_dict(self):
        event = {}
        validate, evt = parse_event(event,"event",["purpose"])
        assert validate == True
        assert "Please ensure you have purpose in the event" in str(evt)
    
    def test_validate_event_as_str(self):
        event = ""
        validate, evt = parse_event(event,"event",["purpose"])
        assert validate == True
        assert "Please ensure you have purpose in the event" in str(evt)

if __name__ == "__main__":
    unittest.main()