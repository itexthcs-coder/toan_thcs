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


def bt_dang13_p2_b2_c4_hh9(self):
    di = random.choice([40, 50, 60, 80])
    goc = 40
    rad = math.radians(goc)
    d_val = di * math.tan(rad)
    chim_val = di / math.cos(rad)
    d50_val = di * math.tan(math.radians(50))

    d_str = str(Decimal(str(d_val)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
    chim_str = str(Decimal(str(chim_val)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
    d50_str = str(Decimal(str(d50_val)).quantize(Decimal('1'), rounding=ROUND_HALF_UP))

    noidungcauhoi = ('''Để đo chiều rộng $d$ của một khúc sông có hai bờ song song, người ta chọn một điểm mốc bên bờ kia, đứng từ bờ này ngắm vuông góc với bờ sông rồi di chuyển dọc theo bờ sông một đoạn $%s\\text{ m}$ và đo được góc ngắm tới điểm mốc đó bằng $%s^\\circ$. Xét tính đúng sai của các khẳng định sau (làm tròn đến mét):'''
                     % (di, goc))

    # a)
    nb_da_1_d = '\\True Chiều rộng $d$ của dòng sông được tính bằng công thức $d = %s \\cdot \\tan %s^\\circ$' % (di, goc)
    nb_da_1_s = 'Chiều rộng $d$ của dòng sông được tính bằng công thức $d = %s \\cdot \\sin %s^\\circ$' % (di, goc)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Chiều rộng $d$ của dòng sông là cạnh góc vuông đối diện với góc $%s^\\circ$ và đoạn di chuyển $%s\\text{ m}$ là cạnh góc vuông kề nên $d = %s \\cdot \\tan %s^\\circ$.''' % (goc, di, di, goc))
    list_nb_2 = [loigiai_nb_1]

    # b)
    th_da_1_d = '\\True Chiều rộng của dòng sông xấp xỉ bằng $%s\\text{ m}$' % d_str
    th_da_1_s = 'Chiều rộng của dòng sông xấp xỉ bằng $%s\\text{ m}$' % (int(d_str) + 8)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Ta có $d = %s \\cdot \\tan %s^\\circ \\approx %s\\text{ (m)}$.''' % (di, goc, d_str))
    list_th_2 = [loigiai_th_1]

    # c)
    vd_da_1_d = '\\True Khoảng cách đường chim bay từ vị trí ngắm sau đến điểm mốc bên kia sông xấp xỉ bằng $%s\\text{ m}$' % chim_str
    vd_da_1_s = 'Khoảng cách đường chim bay từ vị trí ngắm sau đến điểm mốc bên kia sông xấp xỉ bằng $%s\\text{ m}$' % (int(chim_str) - 9)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Khoảng cách đường chim bay chính là cạnh huyền của tam giác vuông: $c = \\dfrac{%s}{\\cos %s^\\circ} \\approx %s\\text{ (m)}$.''' % (di, goc, chim_str))
    list_vd_2 = [loigiai_vd_1]

    # d)
    vdc_da_1_d = '\\True Nếu góc ngắm đo được là $50^\\circ$ thì chiều rộng dòng sông xấp xỉ bằng $%s\\text{ m}$' % d50_str
    vdc_da_1_s = 'Nếu góc ngắm đo được là $50^\\circ$ thì chiều rộng dòng sông vẫn xấp xỉ bằng $%s\\text{ m}$' % d_str
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Nếu góc ngắm là $50^\\circ$ thì chiều rộng dòng sông là $%s \\cdot \\tan 50^\\circ \\approx %s\\text{ (m)}$.''' % (di, d50_str))
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
