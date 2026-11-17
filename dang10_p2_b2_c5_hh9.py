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

def bt_dang10_p2_b2_c5_hh9(self):
    goc_cod = random.choice([40, 50, 70, 80, 100, 110])
    goc_day = (180 - goc_cod) // 2
    cung_lon_cd = 360 - goc_cod

    noidungcauhoi = ('''Cho đường tròn $(O)$ có đường kính $AB$ và dây $CD$ không đi qua tâm sao cho $CD // AB$ và $\\text{sđ}\\overparen{CD}_{\\text{nhỏ}} = %s^\\circ$ (như hình vẽ).
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (O) at (0,0);
    \\coordinate (A) at (-1.8,0);
    \\coordinate (B) at (1.8,0);
    \\coordinate (C) at (130:1.8);
    \\coordinate (D) at (50:1.8);
    \\draw[line width=1pt] (O) circle (1.8);
    \\draw[line width=1pt] (A)--(B) (C)--(D) (O)--(C) (O)--(D);
    \\fill (O) circle (1pt) node[below] {$O$};
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[right] {$B$};
    \\fill (C) circle (1pt) node[above left] {$C$};
    \\fill (D) circle (1pt) node[above right] {$D$};
    \\end{tikzpicture}
    \\end{center}''' % (goc_cod))

    nb_da_1_d = '\\True Góc ở tâm $\\widehat{COD}$ có số đo bằng $%s^\\circ$' % (goc_cod)
    nb_da_1_s = 'Góc ở tâm $\\widehat{COD}$ có số đo bằng $%s^\\circ$' % (180 - goc_cod)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Vì góc ở tâm $\\widehat{COD}$ chắn cung nhỏ $\\overparen{CD}$ có số đo bằng $%s^\\circ$ nên $\\widehat{COD} = %s^\\circ$.''' % (goc_cod, goc_cod))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Hai góc ở tâm $\\widehat{AOC}$ và $\\widehat{BOD}$ có số đo bằng nhau và cùng bằng $%s^\\circ$' % (goc_day)
    th_da_1_s = 'Hai góc ở tâm $\\widehat{AOC}$ và $\\widehat{BOD}$ có số đo bằng nhau và cùng bằng $%s^\\circ$' % (goc_cod)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Tam giác $OCD$ cân tại $O$ có $\\widehat{COD} = %s^\\circ$ nên $\\widehat{OCD} = \\widehat{ODC} = \\dfrac{180^\\circ - %s^\\circ}{2} = %s^\\circ$. \\\\ Vì $CD // AB$ nên $\\widehat{AOC} = \\widehat{OCD} = %s^\\circ$ và $\\widehat{BOD} = \\widehat{ODC} = %s^\\circ$ (so le trong).''' % (goc_cod, goc_cod, goc_day, goc_day, goc_day))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Hai cung nhỏ $\\overparen{AC}$ và $\\overparen{BD}$ bằng nhau'
    vd_da_1_s = 'Số đo cung nhỏ $\\overparen{AC}$ gấp đôi số đo cung nhỏ $\\overparen{BD}$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Ta có $\\text{sđ}\\overparen{AC} = \\widehat{AOC} = %s^\\circ$ và $\\text{sđ}\\overparen{BD} = \\widehat{BOD} = %s^\\circ$. \\\\ Trên cùng đường tròn $(O)$, hai cung nhỏ $\\overparen{AC}$ và $\\overparen{BD}$ có cùng số đo nên bằng nhau.''' % (goc_day, goc_day))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Số đo của cung lớn $\\overparen{CD}$ bằng $%s^\\circ$' % (cung_lon_cd)
    vdc_da_1_s = 'Số đo của cung lớn $\\overparen{CD}$ bằng $%s^\\circ$' % (180 + goc_cod)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Số đo cung lớn $\\overparen{CD}$ là $\\text{sđ}\\overparen{CD}_{\\text{lớn}} = 360^\\circ - \\text{sđ}\\overparen{CD}_{\\text{nhỏ}} = 360^\\circ - %s^\\circ = %s^\\circ$.''' % (goc_cod, cung_lon_cd))
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
