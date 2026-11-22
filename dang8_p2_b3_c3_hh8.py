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

def bt_dang8_p2_b3_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_pythagore = random.choice([(3, 4, 5), (6, 8, 10)])
        dh, ah, ad = bo_pythagore
        ab = randint(ad + 2, 14)
        s_hbh = ab * ah
        ak_rat = Rational(s_hbh, ad)
        str_ak = str(int(ak_rat)) if ak_rat.q == 1 else str(float(ak_rat)).replace('.', ',')
        nua_s = Rational(s_hbh, 2)
        str_nua_s = str(int(nua_s)) if nua_s.q == 1 else str(float(nua_s)).replace('.', ',')
        
        hinh_ve = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.5,2.4);
\\coordinate (B) at (5.5,2.4);
\\coordinate (D) at (0,0);
\\coordinate (C) at (4.0,0);
\\coordinate (H) at (1.5,0);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (A)--(H);
\\draw[line width=1pt] (1.5,0.25)--(1.75,0.25)--(1.75,0);
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below left] {$D$};
\\fill (H) circle (1pt) node[below] {$H$};
\\end{tikzpicture}
\\end{center}'''
        
        noidungcauhoi = ('''Cho hình bình hành $ABCD$ có $AB = %s$ cm, $AD = %s$ cm. Kẻ đường cao $AH \\perp CD$ ($H \\in CD$), biết $AH = %s$ cm (như hình vẽ).
%s''' % (ab, ad, ah, hinh_ve))
        
        nb_da_1_d = '\\True Độ dài cạnh $CD$ bằng $%s$ cm' % (ab)
        nb_da_1_s = 'Độ dài cạnh $CD$ bằng $%s$ cm' % (ad)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1_d = ('''Vì $ABCD$ là hình bình hành nên các cạnh đối bằng nhau, suy ra $CD = AB = %s$ cm.''' % (ab))
        loigiai_nb_1_s = ('''Mệnh đề sai vì $CD = AB = %s$ cm.''' % (ab))
        
        th_da_1_d = '\\True Diện tích hình bình hành $ABCD$ bằng $%s\\text{ cm}^2$' % (s_hbh)
        th_da_1_s = 'Diện tích hình bình hành $ABCD$ bằng $%s\\text{ cm}^2$' % (str_nua_s)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1_d = ('''Diện tích hình bình hành $ABCD$ là: $S_{ABCD} = CD \\cdot AH = %s \\cdot %s = %s$ ($\\text{cm}^2$).''' % (ab, ah, s_hbh))
        loigiai_th_1_s = ('''Mệnh đề sai vì diện tích hình bình hành bằng tích độ dài một cạnh với chiều cao tương ứng: $S_{ABCD} = CD \\cdot AH = %s \\cdot %s = %s$ ($\\text{cm}^2$).''' % (ab, ah, s_hbh))
        
        vd_da_1_d = '\\True Độ dài đoạn thẳng $DH$ bằng $%s$ cm' % (dh)
        vd_da_1_s = 'Độ dài đoạn thẳng $DH$ bằng $%s$ cm' % (dh + 1)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1_d = ('''Áp dụng định lí Pythagore trong tam giác vuông $AHD$ vuông tại $H$, ta có: $DH = \\sqrt{AD^2 - AH^2} = \\sqrt{%s^2 - %s^2} = %s$ (cm).''' % (ad, ah, dh))
        loigiai_vd_1_s = ('''Mệnh đề sai vì theo định lí Pythagore trong $\\Delta AHD$ vuông tại $H$, ta tính được $DH = \\sqrt{%s^2 - %s^2} = %s$ (cm).''' % (ad, ah, dh))
        
        vdc_da_1_d = '\\True Nếu kẻ đường cao $AK \\perp BC$ ($K \\in BC$) thì độ dài $AK$ bằng $%s$ cm' % (str_ak)
        vdc_da_1_s = 'Nếu kẻ đường cao $AK \\perp BC$ ($K \\in BC$) thì độ dài $AK$ bằng $%s$ cm' % (ah)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1_d = ('''Ta có $BC = AD = %s$ cm và $S_{ABCD} = BC \\cdot AK$. Suy ra $AK = \\frac{S_{ABCD}}{BC} = \\frac{%s}{%s} = %s$ (cm).''' % (ad, s_hbh, ad, str_ak))
        loigiai_vdc_1_s = ('''Mệnh đề sai vì $AK = \\frac{S_{ABCD}}{BC} = \\frac{%s}{%s} = %s$ (cm).''' % (s_hbh, ad, str_ak))
        
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
