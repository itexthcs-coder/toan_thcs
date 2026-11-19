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
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea
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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang5_p2_b4_c9_hh9(self):
    bo_goc = [
        (110, 50, 80),
        (120, 40, 80),
        (100, 60, 80),
        (130, 50, 70)
    ]
    aob, boc, cod = random.choice(bo_goc)
    doa = 360 - (aob + boc + cod)
    adb = aob // 2
    bad = (boc + cod) // 2
    bcd = 180 - bad

    hinh_tikz = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (A) at (130:1.8);
\\coordinate (B) at (20:1.8);
\\coordinate (C) at (-30:1.8);
\\coordinate (D) at (-110:1.8);
\\draw[line width=1pt] (O) circle (1.8);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
\\draw[line width=1pt, dashed] (O)--(A) (O)--(B) (O)--(C) (O)--(D) (A)--(C) (B)--(D);
\\fill (O) circle (1pt) node[left] {$O$};
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below left] {$D$};
\\end{tikzpicture}
\\end{center}'''

    noidungcauhoi = ('''Cho tứ giác $ABCD$ nội tiếp đường tròn $(O)$ sao cho các điểm $A, B, C, D$ nằm trên đường tròn theo thứ tự thuận chiều kim đồng hồ, biết $\\widehat{AOB} = %s^\\circ$, $\\widehat{BOC} = %s^\\circ$, $\\widehat{COD} = %s^\\circ$ (như hình vẽ). Xét tính đúng sai của các khẳng định sau: %s''' % (aob, boc, cod, hinh_tikz))

    nb_da_1_d = '\\True Số đo góc ở tâm $\\widehat{DOA}$ bằng $%s^\\circ$' % (doa)
    nb_da_1_s = 'Số đo góc ở tâm $\\widehat{DOA}$ bằng $%s^\\circ$' % (doa + 20)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Ta có $\\widehat{DOA} = 360^\\circ - (\\widehat{AOB} + \\widehat{BOC} + \\widehat{COD}) = 360^\\circ - (%s^\\circ + %s^\\circ + %s^\\circ) = %s^\\circ$.''' % (aob, boc, cod, doa))

    th_da_1_d = '\\True Số đo góc nội tiếp $\\widehat{ADB}$ bằng $%s^\\circ$' % (adb)
    th_da_1_s = 'Số đo góc nội tiếp $\\widehat{ADB}$ bằng $%s^\\circ$' % (aob)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Xét đường tròn $(O)$, góc nội tiếp $\\widehat{ADB}$ và góc ở tâm $\\widehat{AOB}$ cùng chắn cung nhỏ $AB$ nên $\\widehat{ADB} = \\frac{1}{2}\\widehat{AOB} = \\frac{1}{2} \\cdot %s^\\circ = %s^\\circ$.''' % (aob, adb))

    vd_da_1_d = '\\True Số đo góc $\\widehat{BAD}$ của tứ giác $ABCD$ bằng $%s^\\circ$' % (bad)
    vd_da_1_s = 'Số đo góc $\\widehat{BAD}$ của tứ giác $ABCD$ bằng $%s^\\circ$' % (bad + 15)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Ta có $\\widehat{BAC} = \\frac{1}{2}\\widehat{BOC} = %s^\\circ$ và $\\widehat{CAD} = \\frac{1}{2}\\widehat{COD} = %s^\\circ$. Suy ra $\\widehat{BAD} = \\widehat{BAC} + \\widehat{CAD} = %s^\\circ + %s^\\circ = %s^\\circ$.''' % (boc // 2, cod // 2, boc // 2, cod // 2, bad))

    vdc_da_1_d = '\\True Số đo góc $\\widehat{BCD}$ của tứ giác $ABCD$ bằng $%s^\\circ$' % (bcd)
    vdc_da_1_s = 'Số đo góc $\\widehat{BCD}$ của tứ giác $ABCD$ bằng $%s^\\circ$' % (bad)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Vì tứ giác $ABCD$ nội tiếp đường tròn $(O)$ nên hai góc đối diện có tổng bằng $180^\\circ$, do đó $\\widehat{BCD} = 180^\\circ - \\widehat{BAD} = 180^\\circ - %s^\\circ = %s^\\circ$.''' % (bad, bcd))

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

    list_nb_1, list_nb_2 = [nb_da_1], [loigiai_nb_1]
    list_th_1, list_th_2 = [th_da_1], [loigiai_th_1]
    list_vd_1, list_vd_2 = [vd_da_1], [loigiai_vd_1]
    list_vdc_1, list_vdc_2 = [vdc_da_1], [loigiai_vdc_1]

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
