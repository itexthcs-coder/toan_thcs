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

def bt_dang4_p2_b3_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        gM = randint(105, 130)
        gN = 180 - gM
        mn = randint(5, 10)
        
        hinh_ve = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (M) at (1.2,2.2);
\\coordinate (N) at (4.6,2.2);
\\coordinate (Q) at (0,0);
\\coordinate (P) at (3.4,0);
\\draw[line width=1pt] (M)--(N)--(P)--(Q)--cycle;
\\fill (M) circle (1pt) node[above left] {$M$};
\\fill (N) circle (1pt) node[above right] {$N$};
\\fill (P) circle (1pt) node[below right] {$P$};
\\fill (Q) circle (1pt) node[below left] {$Q$};
\\end{tikzpicture}
\\end{center}'''
        
        noidungcauhoi = ('''Cho tứ giác $MNPQ$ có $\\widehat{M} = %s^\\circ$, $\\widehat{N} = %s^\\circ$ và $MN = %s$ cm (như hình vẽ).
%s''' % (gM, gN, mn, hinh_ve))
        
        nb_da_1_d = '\\True Hai cạnh $MQ$ và $NP$ song song với nhau'
        nb_da_1_s = 'Hai cạnh $MN$ và $PQ$ song song với nhau'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1_d = ('''Ta có $\\widehat{M} + \\widehat{N} = %s^\\circ + %s^\\circ = 180^\\circ$. Mà hai góc này ở vị trí trong cùng phía nên $MQ // NP$.''' % (gM, gN))
        loigiai_nb_1_s = ('''Mệnh đề sai vì $\\widehat{M} + \\widehat{N} = 180^\\circ$ nên $MQ // NP$.''')
        
        th_da_1_d = '\\True Nếu biết thêm $\\widehat{P} = %s^\\circ$ thì tứ giác $MNPQ$ là hình bình hành' % (gM)
        th_da_1_s = 'Nếu biết thêm $\\widehat{P} = %s^\\circ$ thì tứ giác $MNPQ$ là hình bình hành' % (gN)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1_d = ('''Khi $\\widehat{P} = %s^\\circ$, ta tính được $\\widehat{Q} = 360^\\circ - (%s^\\circ + %s^\\circ + %s^\\circ) = %s^\\circ = \\widehat{N}$. Tứ giác $MNPQ$ có các góc đối bằng nhau ($\\widehat{M} = \\widehat{P}$, $\\widehat{N} = \\widehat{Q}$) nên là hình bình hành.''' % (gM, gM, gN, gM, gN))
        loigiai_th_1_s = ('''Mệnh đề sai vì nếu $\\widehat{P} = %s^\\circ$ thì $\\widehat{Q} = %s^\\circ$, hai góc đối không bằng nhau nên $MNPQ$ không phải là hình bình hành.''' % (gN, gM))
        
        vd_da_1_d = '\\True Nếu biết thêm $MQ = NP$ thì tứ giác $MNPQ$ là hình bình hành'
        vd_da_1_s = 'Nếu biết thêm $PQ = %s$ cm thì tứ giác $MNPQ$ chắc chắn là hình bình hành' % (mn)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1_d = ('''Tứ giác $MNPQ$ có một cặp cạnh đối song song và bằng nhau ($MQ // NP$ và $MQ = NP$) nên theo Định lí 2b, $MNPQ$ là hình bình hành.''')
        loigiai_vd_1_s = ('''Mệnh đề sai vì nếu $PQ = %s$ cm thì tứ giác $MNPQ$ có thể là hình thang cân có hai đáy $MQ, NP$ và hai cạnh bên $MN = PQ = %s$ cm.''' % (mn, mn))
        
        vdc_da_1_d = '\\True Nếu biết thêm $MN // PQ$ thì $PQ = %s$ cm' % (mn)
        vdc_da_1_s = 'Nếu biết thêm $MN // PQ$ thì chưa đủ điều kiện để tính độ dài $PQ$'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1_d = ('''Khi $MN // PQ$, kết hợp với $MQ // NP$ ta suy ra tứ giác $MNPQ$ là hình bình hành theo định nghĩa. Do đó $PQ = MN = %s$ cm.''' % (mn))
        loigiai_vdc_1_s = ('''Mệnh đề sai vì khi $MN // PQ$ và $MQ // NP$ thì $MNPQ$ là hình bình hành nên $PQ = MN = %s$ cm.''' % (mn))
        
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
