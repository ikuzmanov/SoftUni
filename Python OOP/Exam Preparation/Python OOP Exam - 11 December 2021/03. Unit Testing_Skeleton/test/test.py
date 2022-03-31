from unittest import TestCase, main

from project.team import Team


class TeamTest(TestCase):

    def setUp(self) -> None:
        self.team1 = Team("Edno")
        self.team1.members = {"Gosho": 21, "Pesho": 21}
        self.team2 = Team("Dve")

    def test_name_init(self):
        with self.assertRaises(ValueError) as ex:
            team = Team("123")

        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

        team = Team("Peshovci")
        self.assertEqual("Peshovci", team.name)

    def test_team_init(self):
        name = "Edno"
        self.assertEqual(name, self.team1.name)
        self.assertEqual({"Gosho": 21, "Pesho": 21}, self.team1.members)
        self.team1.members.clear()
        self.assertEqual({}, self.team1.members)

    def test_add_member_member_not_in_list(self):
        result = self.team2.add_member(Neno={"Neno": 25})
        self.assertEqual({'Neno': {'Neno': 25}}, self.team2.members)
        self.assertEqual("Successfully added: Neno", result)

    def test_remove_member_if_member_in_list(self):
        result = self.team1.remove_member("Gosho")
        self.assertEqual({"Pesho": 21}, self.team1.members)
        self.assertEqual(f"Member Gosho removed", result)

    def test_remove_member_if_member_not_in_list(self):
        result = self.team1.remove_member("Ivo")
        self.assertEqual("Member with name Ivo does not exist", result)
        self.assertEqual({"Gosho": 21, "Pesho": 21}, self.team1.members)

    def test_gt(self):
        self.assertTrue(self.team1 > self.team2)
        self.assertFalse(self.team2 > self.team1)

    def test_len(self):
        self.assertTrue(2, len(self.team1))

    def test_str_repr(self):
        expected = f"Team name: Edno\nMember: Gosho - 21-years old\nMember: Pesho - 21-years old"
        self.assertEqual(expected, str(self.team1))

    def test_add(self):
        new_team = self.team1 + self.team2
        self.assertEqual(self.team1.name + self.team2.name, new_team.name)
        self.assertEqual({**self.team1.members, **self.team2.members}, new_team.members)

if __name__ == '__main__':
    main()
