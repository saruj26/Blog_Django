from blog.models import Category
from django.core.management.base import BaseCommand
from typing import Any


class Command(BaseCommand):
    help = "This Command inserts post data"  
  
    def handle(self, *args: Any, **options: Any):
        

        #deleting existing data
        Category.objects.all().delete()

        Categories = ['sports','Technology','Science','Art','Food']




        for Category_name in Categories:
            Category.objects.create(name=Category_name)


        self.stdout.write(self.style.SUCCESS("Completed inserting Data"))