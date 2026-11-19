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


def bt_dang8_p2_b1_c9_hh9(self):
    bo_diem = [
        ('A', 'B', 'S', 'M', 'N', 'H', 'O'),
        ('A', 'B', 'S', 'M', 'N', 'P', 'O')
    ]
    A, B, S, M, N, H, O = random.choice(bo_diem)

    hinh_ve = (
        '\\begin{center}\n'
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
        '\\coordinate (%s) at (0,0);\n'
        '\\coordinate (%s) at (0,2);\n'
        '\\coordinate (%s) at (0,-2);\n'
        '\\coordinate (%s) at (3.6,0.5);\n'
        '\\coordinate (%s) at (65:2);\n'
        '\\coordinate (%s) at (-35:2);\n'
        '\\coordinate (%s) at (intersection of %s--%s and %s--%s);\n'
        '\\draw[line width=1pt] (%s) circle (2cm);\n'
        '\\draw[line width=1pt] (%s)--(%s) (%s)--(%s) (%s)--(%s) (%s)--(%s) (%s)--(%s) (%s)--(%s);\n'
        '\\fill (%s) circle (1pt) node[left] {$%s$};\n'
        '\\fill (%s) circle (1pt) node[above] {$%s$};\n'
        '\\fill (%s) circle (1pt) node[below] {$%s$};\n'
        '\\fill (%s) circle (1pt) node[right] {$%s$};\n'
        '\\fill (%s) circle (1pt) node[above right] {$%s$};\n'
        '\\fill (%s) circle (1pt) node[below right] {$%s$};\n'
        '\\fill (%s) circle (1pt) node[left] {$%s$};\n'
        '\\end{tikzpicture}\n'
        '\\end{center}'
        % (O, A, B, S, M, N, H, B, M, A, N, O, A, B, S, A, S, B, B, M, A, N, S, H, O, O, A, A, B, B, S, S, M, M, N, N, H, H)
    )

    noidungcauhoi = (
        'Cho đường tròn $(%s)$ đường kính $%s%s$ và điểm $%s$ nằm bên ngoài đường tròn. Các đường thẳng $%s%s, %s%s$ lần lượt cắt $(%s)$ tại $%s$ (khác $%s$) và $%s$ (khác $%s$). Gọi $%s$ là giao điểm của $%s%s$ và $%s%s$ như hình vẽ.\n%s'
        % (O, A, B, S, S, A, S, B, O, M, A, N, B, H, B, M, A, N, hinh_ve)
    )

    nb_da_1_d = '\\True Góc $\\widehat{%s%s%s}$ và góc $\\widehat{%s%s%s}$ đều là góc vuông' % (A, M, B, A, N, B)
    nb_da_1_s = 'Góc $\\widehat{%s%s%s}$ và góc $\\widehat{%s%s%s}$ đều bằng $60^\\circ$' % (A, M, B, A, N, B)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = 'Vì $%s%s$ là đường kính của đường tròn $(%s)$ nên $\\widehat{%s%s%s}$ và $\\widehat{%s%s%s}$ là các góc nội tiếp chắn nửa đường tròn, suy ra $\\widehat{%s%s%s} = \\widehat{%s%s%s} = 90^\\circ$.' % (A, B, O, A, M, B, A, N, B, A, M, B, A, N, B)
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Điểm $%s$ là trực tâm của tam giác $%s%s%s$' % (H, S, A, B)
    th_da_1_s = 'Điểm $%s$ là trọng tâm của tam giác $%s%s%s$' % (H, S, A, B)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = 'Xét $\\triangle %s%s%s$ có $%s%s \\perp %s%s$ (do $\\widehat{%s%s%s} = 90^\\circ$) và $%s%s \\perp %s%s$ (do $\\widehat{%s%s%s} = 90^\\circ$). Hai đường cao $%s%s$ và $%s%s$ cắt nhau tại $%s$ nên $%s$ là trực tâm của $\\triangle %s%s%s$.' % (S, A, B, B, M, S, A, A, M, B, A, N, S, B, A, N, B, B, M, A, N, H, H, S, A, B)
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Đường thẳng $%s%s$ vuông góc với đường thẳng $%s%s$' % (S, H, A, B)
    vd_da_1_s = 'Đường thẳng $%s%s$ song song với đường thẳng $%s%s$' % (S, H, A, B)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = 'Vì $%s$ là trực tâm của $\\triangle %s%s%s$ nên $%s%s$ là đường cao thứ ba của $\\triangle %s%s%s$, suy ra $%s%s \\perp %s%s$.' % (H, S, A, B, S, H, S, A, B, S, H, A, B)
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Bốn điểm $%s, %s, %s, %s$ cùng nằm trên một đường tròn đường kính $%s%s$' % (S, M, H, N, S, H)
    vdc_da_1_s = 'Bốn điểm $%s, %s, %s, %s$ không cùng nằm trên một đường tròn' % (S, M, H, N)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = 'Vì $\\widehat{%s%s%s} = 90^\\circ$ và $\\widehat{%s%s%s} = 90^\\circ$ nên hai điểm $%s, %s$ cùng nằm trên đường tròn đường kính $%s%s$. Vậy bốn điểm $%s, %s, %s, %s$ cùng thuộc đường tròn đường kính $%s%s$.' % (S, M, H, S, N, H, M, N, S, H, S, M, H, N, S, H)
    list_vdc_2 = [loigiai_vdc_1]

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)

        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
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
