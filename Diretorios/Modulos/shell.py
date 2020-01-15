# -*- coding: utf-8 -*-

import subprocess
import shlex


class Rodar():
	def __init__(self):
		pass
	def Rodar(paramentro):
		subprocess.call(shlex.split(paramentro), shell=True)