import unittest
import json
from models.base import Base

class TestBase(unittest.TestCase):
    def test_init(self):
        # Test the constructor (__init__) of Base
        b = Base()
        self.assertEqual(b.id, 1)

        b2 = Base(10)
        self.assertEqual(b2.id, 10)

    def test_to_json_string(self):
        # Test the to_json_string method
        d = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        json_str = Base.to_json_string(d)
        self.assertEqual(json_str, json.dumps(d))

    def test_from_json_string(self):
        # Test the from_json_string method
        json_str = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        d = Base.from_json_string(json_str)
        expected = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        self.assertEqual(d, expected)

    def test_create(self):
        # Test the create method
        d = {'id': 1, 'name': 'Alice'}
        instance = Base.create(**d)
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.name, 'Alice')

    def test_save_to_file(self):
        # Test the save_to_file method
        obj_list = [Base(1), Base(2)]
        Base.save_to_file(obj_list)
        with open('Base.json', 'r') as file:
            json_data = file.read()
            d = json.loads(json_data)
            self.assertEqual(len(d), 2)

    def test_load_from_file(self):
        # Test the load_from_file method
        with open('Base.json', 'w') as file:
            json_data = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
            file.write(json_data)

        instance_list = Base.load_from_file()
        self.assertEqual(len(instance_list), 2)
        self.assertEqual(instance_list[0].name, 'Alice')
        self.assertEqual(instance_list[1].name, 'Bob')

if __name__ == '__main__':
    unittest.main()
