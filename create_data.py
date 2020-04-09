#import os
#import django

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto.settings")
#django.setup()

#import string
#import timeit
#from random import choice, random, randint
#from projeto.produto.models import Produto

#class Utils:
#    @staticmethod
#    def gen_difits(max_length):
#        return str(''.join(choice(string.digits) for i in range(max_length)))