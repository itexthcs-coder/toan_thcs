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

def bt_dang18_p2_b3_c3_hh8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        k = randint(2, 6)
        s_hbh = 8 * k
        s_abm = 2 * k
        s_cmn = k
        s_amn = 3 * k
        
        hinh_ve = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (1.2,2.4);
\\coordinate (B) at (5.2,2.4);
\\coordinate (D) at (0,0);
\\coordinate (C) at (4,0);
\\coordinate (M) at ($(B)!0.5!(C)$);
\\coordinate (N) at ($(C)!0.5!(D)$);
\\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle (A)--(M)--(N)--cycle;
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[below left] {$D$};
\\fill (M) circle (1pt) node[right] {$M$};
\\fill (N) circle (1pt) node[below] {$N$};
\\end{tikzpicture}
\\end{center}'''
        
        noidungcauhoi = ('''Cho hình bình hành $ABCD$ có diện tích bằng $%s\\text{ cm}^2$. Gọi $M$ là trung điểm của cạnh $BC$, $N$ là trung điểm của cạnh $CD$ (như hình vẽ).
%s''' % (s_hbh, hinh_ve))
        
        nb_da_1_d = '\\True Diện tích tam giác $ABM$ bằng $%s\\text{ cm}^2$' % (s_abm)
        nb_da_1_s = 'Diện tích tam giác $ABM$ bằng $%s\\text{ cm}^2$' % (4 * k)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1_d = ('''Đường chéo $AC$ chia hình bình hành thành hai tam giác bằng nhau nên $S_{ABC} = \\frac{1}{2}S_{ABCD} = %s$ ($\\text{cm}^2$). Vì $M$ là trung điểm của $BC$ nên $S_{ABM} = \\frac{1}{2}S_{ABC} = %s$ ($\\text{cm}^2$).''' % (4 * k, s_abm))
        loigiai_nb_1_s = ('''Mệnh đề sai vì $S_{ABM} = \\frac{1}{2}S_{ABC} = \\frac{1}{4}S_{ABCD} = %s$ ($\\text{cm}^2$).''' % (s_abm))
        
        th_da_1_d = '\\True Diện tích tam giác $AND$ bằng diện tích tam giác $ABM$'
        th_da_1_s = 'Diện tích tam giác $AND$ lớn hơn diện tích tam giác $ABM$'
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1_d = ('''Tương tự câu a, vì $N$ là trung điểm của $CD$ nên $S_{AND} = \\frac{1}{2}S_{ACD} = \\frac{1}{4}S_{ABCD} = %s$ ($\\text{cm}^2$), do đó $S_{AND} = S_{ABM}$.''' % (s_abm))
        loigiai_th_1_s = ('''Mệnh đề sai vì $S_{AND} = S_{ABM} = \\frac{1}{4}S_{ABCD} = %s$ ($\\text{cm}^2$).''' % (s_abm))
        
        vd_da_1_d = '\\True Diện tích tam giác $CMN$ bằng $%s\\text{ cm}^2$' % (s_cmn)
        vd_da_1_s = 'Diện tích tam giác $CMN$ bằng $%s\\text{ cm}^2$' % (s_abm)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1_d = ('''Ta có $S_{BMN} = \\frac{1}{2}S_{BCD}$ (do $M$ là trung điểm $BC$) và $S_{CMN} = \\frac{1}{2}S_{BCM}$ (do $N$ là trung điểm $CD$). Suy ra $S_{CMN} = \\frac{1}{4}S_{BCD} = \\frac{1}{8}S_{ABCD} = \\frac{%s}{8} = %s$ ($\\text{cm}^2$).''' % (s_hbh, s_cmn))
        loigiai_vd_1_s = ('''Mệnh đề sai vì $S_{CMN} = \\frac{1}{8}S_{ABCD} = %s$ ($\\text{cm}^2$).''' % (s_cmn))
        
        vdc_da_1_d = '\\True Diện tích tam giác $AMN$ bằng $%s\\text{ cm}^2$' % (s_amn)
        vdc_da_1_s = 'Diện tích tam giác $AMN$ bằng $%s\\text{ cm}^2$' % (4 * k)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1_d = ('''Ta có $S_{AMN} = S_{ABCD} - (S_{ABM} + S_{AND} + S_{CMN}) = %s - (%s + %s + %s) = %s$ ($\\text{cm}^2$).''' % (s_hbh, s_abm, s_abm, s_cmn, s_amn))
        loigiai_vdc_1_s = ('''Mệnh đề sai vì $S_{AMN} = S_{ABCD} - (%s + %s + %s) = %s$ ($\\text{cm}^2$).''' % (s_abm, s_abm, s_cmn, s_amn))
        
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
