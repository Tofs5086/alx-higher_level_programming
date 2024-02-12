import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_base_init(self):
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_to_json_string(self):
        list_dicts = [{'id': 1, 'name': 'example'}, {'id': 2, 'name': 'sample'}]
        json_string = Base.to_json_string(list_dicts)
        self.assertEqual(json_string, '[{"id": 1, "name": "example"}, {"id": 2, "name": "sample"}]')

    def test_save_to_file(self):
        class MockCls:
            @staticmethod
            def to_dictionary():
                return {'id': 1, 'name': 'example'}

        list_objs = [MockCls(), MockCls()]
        Base.save_to_file(list_objs)

        with open('Base.json', 'r') as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 1, "name": "example"}, {"id": 1, "name": "example"}]')

    def test_from_json_string(self):
        json_string = '[{"id": 1, "name": "example"}, {"id": 2, "name": "sample"}]'
        list_dicts = Base.from_json_string(json_string)
        self.assertEqual(list_dicts, [{'id': 1, 'name': 'example'}, {'id': 2, 'name': 'sample'}])

    def test_create(self):
        instance = Base.create(id=1, name='example')
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.name, 'example')

    def test_load_from_file(self):
        with open('Base.json', 'w') as file:
            file.write('[{"id": 1, "name": "example"}, {"id": 2, "name": "sample"}]')

        instances = Base.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[1].name, 'sample')


if __name__ == '__main__':
    unittest.main()

