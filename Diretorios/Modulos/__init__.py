# -*- coding: utf-8 -*-

from subprocess import call as shell
from Modulos.shell import Rodar
from tkinter import *
from tkinter import filedialog
from tkinter.scrolledtext import *
from PIL import Image, ImageTk
from re import sub as Substituir
import os

# Simplificações
Rodar_shell = Rodar.Rodar