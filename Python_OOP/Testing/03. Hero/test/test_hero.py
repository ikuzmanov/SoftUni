from unittest import main, TestCase

from project.hero import Hero


class HeroTest(TestCase):
    def test_initialize(self):
        hero = Hero("Gosho", 10, 100, 1500)
        self.assertEqual("Gosho", hero.username)
        self.assertEqual(10, hero.level)
        self.assertEqual(100, hero.health)
        self.assertEqual(1500, hero.damage)

    def test_battle_yourself(self):
        hero = Hero("Gosho", 10, 100, 1500)

        with self.assertRaises(Exception) as ex:
            hero.battle(hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_when_health_is_zero_or_less(self):
        hero2 = Hero("Pesho", 12, 200, 1000)
        hero = Hero("Gosho", 10, 0, 1500)
        with self.assertRaises(Exception) as ex:
            hero.battle(hero2)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

        hero = Hero("Gosho", 10, -5, 1500)

        with self.assertRaises(ValueError) as ex:
            hero.battle(hero2)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_with_health_less_or_eq_than_zero(self):
        hero2 = Hero("Pesho", 12, 0, 1000)
        hero = Hero("Gosho", 10, 200, 1500)

        with self.assertRaises(ValueError) as ex:
            hero.battle(hero2)
        self.assertEqual("You cannot fight Pesho. He needs to rest", str(ex.exception))

        hero2 = Hero("Pesho", 12, -5, 1000)

        with self.assertRaises(ValueError) as ex:
            hero.battle(hero2)
        self.assertEqual("You cannot fight Pesho. He needs to rest", str(ex.exception))

    def test_battle_draw(self):
        #health eq to 0
        hero = Hero("Gosho", 10, 200, 20)
        hero2 = Hero("Pesho", 10, 200, 20)
        result = hero.battle(hero2)

        self.assertEqual("Draw", result)

        #health less than 02
        hero = Hero("Gosho", 12, 200, 20)
        hero2 = Hero("Pesho", 12, 200, 20)
        result = hero.battle(hero2)

        self.assertEqual("Draw", result)

    def test_battle_win(self):
        hero = Hero("Gosho", 10, 1000, 20)
        hero2 = Hero("Pesho", 10, 200, 20)

        result = hero.battle(hero2)
        self.assertEqual("You win", result)

        hero = Hero("Gosho", 10, 1000, 20)
        hero2 = Hero("Pesho", 10, 150, 20)

        result = hero.battle(hero2)
        self.assertEqual("You win", result)

        self.assertEqual(11, hero.level)
        self.assertEqual(805, hero.health)
        self.assertEqual(25, hero.damage)


    def test_battle_lose(self):
        hero = Hero("Gosho", 10, 100, 10)
        hero2 = Hero("Pesho", 10, 200, 20)

        result = hero.battle(hero2)
        self.assertEqual("You lose", result)
        self.assertEqual(11, hero2.level)
        self.assertEqual(105, hero2.health)
        self.assertEqual(25, hero2.damage)

    def test_hero_str_repr(self):
        hero = Hero("Gosho", 10, 100, 10)
        expected = f"Hero Gosho: 10 lvl\n" \
                   f"Health: 100\n" \
                   f"Damage: 10\n"

        result = str(hero)

        self.assertEqual(expected, result)

if __name__ == "__main__":
    main()
