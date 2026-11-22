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

def bt_dang20_p2_b3_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        bo_pyth = random.choice([(6, 8, 10), (9, 12, 15)])
        ab, ac, bc = bo_pyth
        ah_rat = Rational(ab * ac, bc)
        str_ah = str(int(ah_rat)) if ah_rat.q == 1 else str(float(ah_rat)).replace('.', ',')
        nua_bc = Rational(bc, 2)
        str_nua_bc = str(int(nua_bc)) if nua_bc.q == 1 else str(float(nua_bc)).replace('.', ',')
        
        hinh_ve = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,2.4);
\\coordinate (B) at (0,0);
\\coordinate (C) at (3.6,0);
\\coordinate (M) at (1.5,1.4);
\\coordinate (D) at (0,1.4);
\\coordinate (E) at (1.5,0);
\\draw[line width=1pt] (A)--(B)--(C)--cycle (M)--(D) (M)--(E) (D)--(E) (A)--(M);
\\draw[line width=1pt] (0,0.25)--(0.25,0.25)--(0.25,0);
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (M) circle (1pt) node[above right] {$M$};
\\fill (D) circle (1pt) node[left] {$D$};
\\fill (E) circle (1pt) node[below] {$E$};
\\end{tikzpicture}
\\end{center}'''
        
        noidungcauhoi = ('''Cho tam giác $ABC$ có $AB = %s$ cm, $AC = %s$ cm, $BC = %s$ cm. Lấy điểm $M$ di động trên cạnh $BC$. Kẻ $MD // AC$ ($D \\in AB$) và $ME // AB$ ($E \\in AC$) (như hình vẽ).
%s''' % (ab, ac, bc, hinh_ve))
        
        nb_da_1_d = '\\True Tứ giác $ADME$ là hình bình hành với mọi vị trí của điểm $M$ trên cạnh $BC$'
        nb_da_1_s = 'Tứ giác $ADME$ chỉ là hình bình hành khi $M$ là trung điểm của cạnh $BC$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1_d = ('''Tứ giác $ADME$ có $AD // ME$ (do $AB // ME$) và $AE // MD$ (do $AC // MD$) nên theo định nghĩa, tứ giác $ADME$ luôn là hình bình hành.''')
        loigiai_nb_1_s = ('''Mệnh đề sai vì tứ giác $ADME$ luôn có các cạnh đối song song với mọi vị trí của $M$ trên $BC$.''')
        
        th_da_1_d = '\\True Tam giác $ABC$ vuông tại $A$'
        th_da_1_s = 'Tam giác $ABC$ không phải là tam giác vuông'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1_d = ('''Ta có $AB^2 + AC^2 = %s^2 + %s^2 = %s = %s^2 = BC^2$. Theo định lí Pythagore đảo, tam giác $ABC$ vuông tại $A$.''' % (ab, ac, ab**2 + ac**2, bc))
        loigiai_th_1_s = ('''Mệnh đề sai vì $AB^2 + AC^2 = %s = BC^2$ nên $\\Delta ABC$ vuông tại $A$.''' % (bc**2))
        
        vd_da_1_d = '\\True Độ dài hai đường chéo của hình bình hành $ADME$ luôn bằng nhau ($DE = AM$)'
        vd_da_1_s = 'Chu vi hình bình hành $ADME$ luôn không đổi khi điểm $M$ di chuyển trên cạnh $BC$'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1_d = ('''Vì $MD // AC$ và $\\widehat{BAC} = 90^\\circ$ nên $\\widehat{MDB} = 90^\\circ$, suy ra $\\widehat{MDA} = 90^\\circ$. Hai tam giác vuông $DAE$ và $EDA$ có $AD$ chung, $\\widehat{DAE} = \\widehat{EDA} = 90^\\circ$ và $AE = DM$, nên $\\Delta DAE = \\Delta EDA$ (c.g.c), suy ra $DE = EA$ hay hai đường chéo của hình bình hành $ADME$ bằng nhau ($DE = AM$).''')
        loigiai_vd_1_s = ('''Mệnh đề sai vì chu vi hình bình hành $ADME$ bằng $2(AD + AE) = 2(AD + MD)$; do $AB \\ne AC$ nên $MD \\ne BD$, tổng này thay đổi khi $M$ di chuyển trên $BC$.''')
        
        vdc_da_1_d = '\\True Độ dài đoạn thẳng $DE$ đạt giá trị nhỏ nhất bằng $%s$ cm khi $M$ là chân đường cao kẻ từ $A$ xuống $BC$' % (str_ah)
        vdc_da_1_s = 'Độ dài đoạn thẳng $DE$ đạt giá trị nhỏ nhất bằng $%s$ cm khi $M$ là trung điểm của $BC$' % (str_nua_bc)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1_d = ('''Kẻ đường cao $AH \\perp BC$ ($H \\in BC$). Ta có $DE = AM \\ge AH$. Dấu bằng xảy ra khi $M \\equiv H$. Tính $AH = \\frac{AB \\cdot AC}{BC} = \\frac{%s \\cdot %s}{%s} = %s$ (cm). Vậy $DE$ nhỏ nhất bằng $%s$ cm.''' % (ab, ac, bc, str_ah, str_ah))
        loigiai_vdc_1_s = ('''Mệnh đề sai vì $DE = AM$ nhỏ nhất khi $AM$ vuông góc với $BC$ (tức $M$ là chân đường cao hạ từ $A$ xuống $BC$), khi đó $DE_{\\min} = AH = \\frac{%s \\cdot %s}{%s} = %s$ cm.''' % (ab, ac, bc, str_ah))
        
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
