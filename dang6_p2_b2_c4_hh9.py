import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang6_p2_b2_c4_hh9(self):
    v = random.choice([450, 500, 600])
    phut = 1.2 if v == 500 else (1.6 if v == 450 else 1.0)
    phut_str = str(phut).replace('.', ',')
    s_km = int(round(v * (phut / 60.0)))
    h_km = Rational(s_km, 2)
    hc_sym = Rational(s_km, 2) * sqrt(3)
    hc_str = str(Decimal(str(s_km * math.cos(math.radians(30)))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ',')
    phut2_str = str(2 * phut).replace('.', ',')

    noidungcauhoi = ('''Một chiếc máy bay bay lên với vận tốc $%s\\text{ km/h}$. Đường bay lên tạo với phương nằm ngang một góc $30^\\circ$. Xét tính đúng sai của các khẳng định sau:'''
                     % (v))

    # a)
    nb_da_1_d = '\\True Sau $%s\\text{ phút}$, quãng đường máy bay đi được theo đường bay là $%s\\text{ km}$' % (phut_str, s_km)
    nb_da_1_s = 'Sau $%s\\text{ phút}$, quãng đường máy bay đi được theo đường bay là $%s\\text{ km}$' % (phut_str, s_km + 5)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Đổi $%s\\text{ phút} = \\dfrac{%s}{60}\\text{ giờ}$. Quãng đường máy bay đi được theo đường bay là $AB = %s \\cdot \\dfrac{%s}{60} = %s\\text{ (km)}$.''' % (phut_str, phut_str, v, phut_str, s_km))
    list_nb_2 = [loigiai_nb_1]

    # b)
    th_da_1_d = '\\True Độ cao của máy bay so với mặt đất sau $%s\\text{ phút}$ là $%s\\text{ km}$' % (phut_str, latex(h_km))
    th_da_1_s = 'Độ cao của máy bay so với mặt đất sau $%s\\text{ phút}$ là $%s\\text{ km}$' % (phut_str, latex(hc_sym))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Độ cao của máy bay đạt được sau $%s\\text{ phút}$ là $BH = AB \\cdot \\sin 30^\\circ = %s \\cdot \\dfrac{1}{2} = %s\\text{ (km)}$.''' % (phut_str, s_km, latex(h_km)))
    list_th_2 = [loigiai_th_1]

    # c)
    vd_da_1_d = '\\True Hình chiếu của đường bay trên phương nằm ngang sau $%s\\text{ phút}$ dài khoảng $%s\\text{ km}$' % (phut_str, hc_str)
    vd_da_1_s = 'Hình chiếu của đường bay trên phương nằm ngang sau $%s\\text{ phút}$ dài khoảng $%s\\text{ km}$' % (phut_str, str(Decimal(str(s_km * math.cos(math.radians(30)) + 1.5)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)).replace('.', ','))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Hình chiếu trên phương nằm ngang là $AH = AB \\cdot \\cos 30^\\circ = %s \\cdot \\dfrac{\\sqrt{3}}{2} = %s \\approx %s\\text{ (km)}$.''' % (s_km, latex(hc_sym), hc_str))
    list_vd_2 = [loigiai_vd_1]

    # d)
    vdc_da_1_d = '\\True Để máy bay đạt độ cao $%s\\text{ km}$ thì thời gian bay kể từ lúc cất cánh là $%s\\text{ phút}$' % (s_km, phut2_str)
    vdc_da_1_s = 'Để máy bay đạt độ cao $%s\\text{ km}$ thì thời gian bay kể từ lúc cất cánh là $%s\\text{ phút}$' % (s_km, str(3 * phut).replace('.', ','))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Để đạt độ cao $%s\\text{ km}$, quãng đường bay cần thiết là $\\dfrac{%s}{\\sin 30^\\circ} = %s\\text{ (km)}$, gấp đôi quãng đường trong $%s\\text{ phút}$ nên thời gian cần là $2 \\cdot %s = %s\\text{ (phút)}$.''' % (s_km, s_km, 2 * s_km, phut_str, phut_str, phut2_str))
    list_vdc_2 = [loigiai_vdc_1]

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)
        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        if 1 <= count_true_answers(answers) <= 3:
            break

    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))

    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)

    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\choiceTFn \n' +
               '{' + str(shuffled_answers_nb[0]) + '}\n' +
               '{' + str(shuffled_answers_th[0]) + '}\n' +
               '{' + str(shuffled_answers_vd[0]) + '}\n' +
               '{' + str(shuffled_answers_vdc[0]) + '}\n' +
               '\\loigiai{ \n' +
               '\\begin{enumEX}[a)]{1} \n' +
               '\\item ' + str(shuffled_solutions_nb[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_th[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_vd[0]) + '\n' +
               '\\item ' + str(shuffled_solutions_vdc[0]) + '\n' +
               '\\end{enumEX}} \n' +
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
