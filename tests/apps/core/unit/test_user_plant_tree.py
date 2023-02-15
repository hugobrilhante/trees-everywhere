from decimal import Decimal

from django.test import TestCase
from model_bakery import baker

from src.apps.core.models import PlantedTree


class UserPlantTreeTestCase(TestCase):
    def setUp(self) -> None:
        self.user = baker.make("core.User", first_name="The Tester")
        self.tree = baker.make("core.Tree", name="The Tree")
        self.account = baker.make("core.Account", name="The Account")
        self.location = (Decimal("14.235004"), Decimal("51.925282"))

    def test_when_user_plant_tree_successful(self):
        self.user.plant_tree(account=self.account, tree=self.tree, location=self.location)
        self.assertEqual(PlantedTree.objects.filter(user=self.user).count(), 1)

    def test_when_user_plant_trees_successful(self):
        self.user.plant_trees([(self.account, self.tree, self.location)])
        self.assertEqual(PlantedTree.objects.filter(user=self.user).count(), 1)
