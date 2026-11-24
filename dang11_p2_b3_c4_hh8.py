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

def fmt_num(val):
    if isinstance(val, (int, float)):
        if val == int(val):
            return str(int(val))
        return str(round(val, 4)).replace('.', ',')
    return str(val).replace('.', ',')

def bt_dang11_p2_b3_c4_hh8(self):
    # Dạng 11: Khai thác giả thiết tam giác cân có phân giác góc đáy cắt cạnh bên
    bo_so = [
        (15, 10, 9, 6, 28),
        (12, 8, 7.2, 4.8, 22.4),
        (20, 5, 16, 4, 17),
        (18, 12, 10.8, 7.2, 33.6)
    ]
    ab, bc, ad, be, cv_bcde = random.choice(bo_so)
    s_ad = fmt_num(ad)
    s_be = fmt_num(be)
    s_cv = fmt_num(cv_bcde)

    hinh_ve = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\coordinate (A) at (1.8,3.6);\n'
        '\\coordinate (B) at (0,0);\n'
        '\\coordinate (C) at (3.6,0);\n'
        '\\coordinate (D) at (2.88,1.44);\n'
        '\\coordinate (E) at (0.72,1.44);\n'
        '\\draw[line width=1pt] (A)--(B)--(C)--cycle (B)--(D) (D)--(E);\n'
        '\\fill (A) circle (1pt) node[above] {$A$};\n'
        '\\fill (B) circle (1pt) node[below left] {$B$};\n'
        '\\fill (C) circle (1pt) node[below right] {$C$};\n'
        '\\fill (D) circle (1pt) node[right] {$D$};\n'
        '\\fill (E) circle (1pt) node[left] {$E$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
    )

    noidungcauhoi = (
        'Cho tam giác $ABC$ cân tại $A$ có $AB = %s\\text{ cm}$, $BC = %s\\text{ cm}$. Đường phân giác của góc $B$ cắt cạnh $AC$ tại $D$. Kẻ $DE // BC$ ($E \\in AB$).\n%s'
        % (ab, bc, hinh_ve)
    )

    nb_da_1_d = '\\True Độ dài đoạn thẳng $AD = %s\\text{ cm}$' % s_ad
    nb_da_1_s = 'Độ dài đoạn thẳng $AD = %s\\text{ cm}$' % s_be
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_d = 'Đúng. Vì tam giác $ABC$ cân tại $A$ nên $AC = AB = %s\\text{ cm}$. Áp dụng tính chất đường phân giác $BD$, ta có $\\frac{DA}{DC} = \\frac{BA}{BC} = \\frac{%s}{%s}$, suy ra $AD = \\frac{%s}{%s} \\cdot %s = %s\\text{ cm}$.' % (ab, ab, bc, ab, ab + bc, ab, s_ad)
    loigiai_nb_s = 'Sai. Ta tính được $AD = \\frac{%s}{%s} \\cdot %s = %s\\text{ cm}$.' % (ab, ab + bc, ab, s_ad)

    th_da_1_d = '\\True Tam giác $EBD$ là tam giác cân tại $E$'
    th_da_1_s = 'Tam giác $EBD$ là tam giác vuông tại $E$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_d = 'Đúng. Vì $DE // BC$ nên $\\widehat{EDB} = \\widehat{DBC}$ (so le trong). Mà $\\widehat{DBC} = \\widehat{EBD}$ (do $BD$ là phân giác góc $B$) nên $\\widehat{EDB} = \\widehat{EBD}$, suy ra tam giác $EBD$ cân tại $E$.'
    loigiai_th_s = 'Sai. Ta có $\\widehat{EDB} = \\widehat{DBC} = \\widehat{EBD}$ nên tam giác $EBD$ cân tại $E$.'

    vd_da_1_d = '\\True Độ dài đoạn thẳng $BE = %s\\text{ cm}$' % s_be
    vd_da_1_s = 'Độ dài đoạn thẳng $BE = %s\\text{ cm}$' % s_ad
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_d = 'Đúng. Vì $DE // BC$ nên $\\frac{BE}{AB} = \\frac{CD}{AC} = \\frac{%s}{%s}$, suy ra $BE = %s\\text{ cm}$.' % (s_be, ab, s_be)
    loigiai_vd_s = 'Sai. Ta tính được $BE = CD = AC - AD = %s - %s = %s\\text{ cm}$.' % (ab, s_ad, s_be)

    vdc_da_1_d = '\\True Chu vi tứ giác $BCDE$ bằng $%s\\text{ cm}$' % s_cv
    vdc_da_1_s = 'Chu vi tứ giác $BCDE$ bằng $%s\\text{ cm}$' % fmt_num(cv_bcde + 4)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_d = 'Đúng. Vì tam giác $EBD$ cân tại $E$ nên $ED = BE = %s\\text{ cm}$. Chu vi tứ giác $BCDE$ là $BC + CD + DE + EB = %s + %s + %s + %s = %s\\text{ cm}$.' % (s_be, bc, s_be, s_be, s_be, s_cv)
    loigiai_vdc_s = 'Sai. Chu vi tứ giác $BCDE$ bằng $%s + %s + %s + %s = %s\\text{ cm}$.' % (bc, s_be, s_be, s_be, s_cv)

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

    loigiai_nb_1 = loigiai_nb_d if '\\True' in nb_da_1 else loigiai_nb_s
    loigiai_th_1 = loigiai_th_d if '\\True' in th_da_1 else loigiai_th_s
    loigiai_vd_1 = loigiai_vd_d if '\\True' in vd_da_1 else loigiai_vd_s
    loigiai_vdc_1 = loigiai_vdc_d if '\\True' in vdc_da_1 else loigiai_vdc_s

    list_nb_1 = [nb_da_1]
    list_nb_2 = [loigiai_nb_1]
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    list_th_1 = [th_da_1]
    list_th_2 = [loigiai_th_1]
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    list_vd_1 = [vd_da_1]
    list_vd_2 = [loigiai_vd_1]
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    list_vdc_1 = [vdc_da_1]
    list_vdc_2 = [loigiai_vdc_1]
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
               '{' + str(shuffled_answers_nb[0]) + '}\n'
               '{' + str(shuffled_answers_th[0]) + '}\n'
               '{' + str(shuffled_answers_vd[0]) + '}\n'
               '{' + str(shuffled_answers_vdc[0]) + '}\n'
               '\\loigiai{ \n'
               '\\begin{enumEX}[a)]{1} \n'
               '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
               '\\item ' + str(shuffled_solutions_th[0]) + '\n'
               '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
               '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
               '\\end{enumEX}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
