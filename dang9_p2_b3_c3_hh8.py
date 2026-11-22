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

def bt_dang9_p2_b3_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bc = randint(4, 8)
        hieu = randint(2, 5)
        ab = bc + hieu
        nua_cv = ab + bc
        cv = 2 * nua_cv
        
        hinh_ve = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.2,2.4);
\\coordinate (B) at (5.2,2.4);
\\coordinate (D) at (0,0);
\\coordinate (C) at (4,0);
\\coordinate (O) at ($(A)!0.5!(C)$);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (A)--(C) (B)--(D);
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below left] {$D$};
\\fill (O) circle (1pt) node[above] {$O$};
\\end{tikzpicture}
\\end{center}'''
        
        noidungcauhoi = ('''Cho hình bình hành $ABCD$ có giao điểm hai đường chéo là $O$. Biết chu vi tam giác $AOB$ lớn hơn chu vi tam giác $BOC$ là $%s$ cm và chu vi hình bình hành $ABCD$ bằng $%s$ cm (như hình vẽ).
%s''' % (hieu, cv, hinh_ve))
        
        nb_da_1_d = '\\True Tổng độ dài hai cạnh $AB + BC$ bằng $%s$ cm' % (nua_cv)
        nb_da_1_s = 'Tổng độ dài hai cạnh $AB + BC$ bằng $%s$ cm' % (cv)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1_d = ('''Nửa chu vi hình bình hành $ABCD$ là $AB + BC = \\frac{%s}{2} = %s$ (cm).''' % (cv, nua_cv))
        loigiai_nb_1_s = ('''Mệnh đề sai vì chu vi bằng $2(AB + BC) = %s$ cm nên $AB + BC = %s$ cm.''' % (cv, nua_cv))
        
        th_da_1_d = '\\True Hiệu độ dài hai cạnh $AB - BC$ bằng $%s$ cm' % (hieu)
        th_da_1_s = 'Hiệu độ dài hai cạnh $AB - BC$ bằng $%s$ cm' % (2 * hieu)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1_d = ('''Vì $O$ là giao điểm hai đường chéo của hình bình hành $ABCD$ nên $OA = OC$. Ta có $C_{\\Delta AOB} - C_{\\Delta BOC} = (OA + OB + AB) - (OB + OC + BC) = AB - BC = %s$ (cm).''' % (hieu))
        loigiai_th_1_s = ('''Mệnh đề sai vì $OA = OC$ nên hiệu chu vi hai tam giác $AOB$ và $BOC$ đúng bằng $AB - BC = %s$ cm.''' % (hieu))
        
        vd_da_1_d = '\\True Độ dài cạnh $CD$ bằng $%s$ cm' % (ab)
        vd_da_1_s = 'Độ dài cạnh $CD$ bằng $%s$ cm' % (bc)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1_d = ('''Từ $AB + BC = %s$ cm và $AB - BC = %s$ cm, suy ra $AB = \\frac{%s + %s}{2} = %s$ (cm). Do đó $CD = AB = %s$ cm.''' % (nua_cv, hieu, nua_cv, hieu, ab, ab))
        loigiai_vd_1_s = ('''Mệnh đề sai vì $CD = AB = \\frac{%s + %s}{2} = %s$ cm.''' % (nua_cv, hieu, ab))
        
        vdc_da_1_d = '\\True Độ dài cạnh $AD$ bằng $%s$ cm' % (bc)
        vdc_da_1_s = 'Độ dài cạnh $AD$ bằng $%s$ cm' % (bc + 1)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1_d = ('''Ta có $BC = %s - %s = %s$ (cm). Vì $ABCD$ là hình bình hành nên $AD = BC = %s$ cm.''' % (nua_cv, ab, bc, bc))
        loigiai_vdc_1_s = ('''Mệnh đề sai vì $AD = BC = %s - %s = %s$ cm.''' % (nua_cv, ab, bc))
        
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
        
        loigiai_nb_1 = loigiai_nb_1_d if '\\True' in nb_da_1 else loigiai_nb_1_s
        loigiai_th_1 = loigiai_th_1_d if '\\True' in th_da_1 else loigiai_th_1_s
        loigiai_vd_1 = loigiai_vd_1_d if '\\True' in vd_da_1 else loigiai_vd_1_s
        loigiai_vdc_1 = loigiai_vdc_1_d if '\\True' in vdc_da_1 else loigiai_vdc_1_s
        
        shuffled_answers_nb = [nb_da_1]
        shuffled_solutions_nb = [loigiai_nb_1]
        shuffled_answers_th = [th_da_1]
        shuffled_solutions_th = [loigiai_th_1]
        shuffled_answers_vd = [vd_da_1]
        shuffled_solutions_vd = [loigiai_vd_1]
        shuffled_answers_vdc = [vdc_da_1]
        shuffled_solutions_vdc = [loigiai_vdc_1]
    
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
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
