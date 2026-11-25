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


def bt_dang16_p2_b1_c6_ds8(self):
    # Dạng 16: Mô hình hóa bài toán chuyển động đường thủy (xuôi dòng, ngược dòng) bằng phân thức
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        v_nuoc = random.choice([2, 3, 4])
        # Chọn vận tốc riêng của ca nô v_cano sao cho S chia hết cho (v_cano + v_nuoc) và 2*S chia hết cho (v_cano - v_nuoc)
        if v_nuoc == 2:
            S = 48
            v_cano = 14 # xuôi: 48/16 = 3; ngược: 48/12 = 4 -> tổng 7
        elif v_nuoc == 3:
            S = 60
            v_cano = 27 # xuôi: 60/30 = 2; ngược: 60/24 = 2,5 -> tổng 4,5
        else:
            S = 72
            v_cano = 20 # xuôi: 72/24 = 3; ngược: 72/16 = 4,5 -> tổng 7,5
            
        t_xuoi = Fraction(S, v_cano + v_nuoc)
        t_nguoc = Fraction(S, v_cano - v_nuoc)
        t_tong = t_xuoi + t_nguoc
        
        def fmt_num(fr):
            if fr.denominator == 1:
                return str(fr.numerator)
            val = float(fr)
            return str(val).replace('.', ',')
            
        str_tx = fmt_num(t_xuoi)
        str_tn = fmt_num(t_nguoc)
        str_tt = fmt_num(t_tong)
        str_sai_tt = fmt_num(t_tong + Fraction(1, 2))
        
        noidungcauhoi = ('Một ca nô đi xuôi dòng trên một khúc sông dài $%s\\text{ km}$, sau đó quay ngược dòng trở về điểm xuất phát. Biết vận tốc dòng nước là $%s\\text{ km/h}$ và vận tốc riêng của ca nô khi nước yên lặng là $x\\text{ (km/h)}$ ($x > %s$). Xét tính đúng sai của các khẳng định sau:'
                         % (S, v_nuoc, v_nuoc))
        
        nb_da_1_d = '\\True Vận tốc của ca nô khi xuôi dòng là $x + %s\\text{ (km/h)}$ và khi ngược dòng là $x - %s\\text{ (km/h)}$' % (v_nuoc, v_nuoc)
        nb_da_1_s = 'Vận tốc của ca nô khi xuôi dòng là $x - %s\\text{ (km/h)}$ và khi ngược dòng là $x + %s\\text{ (km/h)}$' % (v_nuoc, v_nuoc)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_d = 'Đúng. Khi xuôi dòng, ca nô được dòng nước đẩy thêm nên vận tốc là $x + %s\\text{ (km/h)}$; khi ngược dòng, ca nô bị nước cản lại nên vận tốc là $x - %s\\text{ (km/h)}$.' % (v_nuoc, v_nuoc)
        loigiai_nb_s = 'Sai. Xuôi dòng thì cộng thêm vận tốc dòng nước ($x + %s$), ngược dòng thì trừ đi vận tốc dòng nước ($x - %s$).' % (v_nuoc, v_nuoc)
        
        th_da_1_d = '\\True Phân thức biểu thị thời gian ca nô đi xuôi dòng hết $%s\\text{ km}$ là $\\dfrac{%s}{x + %s}$ (giờ)' % (S, S, v_nuoc)
        th_da_1_s = 'Phân thức biểu thị thời gian ca nô đi xuôi dòng hết $%s\\text{ km}$ là $\\dfrac{%s}{x - %s}$ (giờ)' % (S, S, v_nuoc)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_d = 'Đúng. Áp dụng công thức $t = \\dfrac{s}{v}$, thời gian ca nô đi xuôi dòng là $\\dfrac{%s}{x + %s}$ (giờ).' % (S, v_nuoc)
        loigiai_th_s = 'Sai. Vận tốc xuôi dòng là $x + %s$ nên thời gian đi xuôi dòng phải là $\\dfrac{%s}{x + %s}$ (giờ).' % (v_nuoc, S, v_nuoc)
        
        vd_da_1_d = '\\True Phân thức biểu thị thời gian ca nô đi ngược dòng hết $%s\\text{ km}$ là $\\dfrac{%s}{x - %s}$ (giờ)' % (S, S, v_nuoc)
        vd_da_1_s = 'Phân thức biểu thị thời gian ca nô đi ngược dòng hết $%s\\text{ km}$ là $\\dfrac{x - %s}{%s}$ (giờ)' % (S, v_nuoc, S)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_d = 'Đúng. Thời gian ca nô đi ngược dòng hết quãng đường $%s\\text{ km}$ với vận tốc $x - %s\\text{ (km/h)}$ là $\\dfrac{%s}{x - %s}$ (giờ).' % (S, v_nuoc, S, v_nuoc)
        loigiai_vd_s = 'Sai. Thời gian bằng quãng đường chia cho vận tốc ($\\dfrac{%s}{x - %s}$), không phải vận tốc chia quãng đường.' % (S, v_nuoc)
        
        vdc_da_1_d = '\\True Nếu vận tốc riêng của ca nô là $%s\\text{ km/h}$ thì tổng thời gian cả đi lẫn về của ca nô là $%s$ giờ' % (v_cano, str_tt)
        vdc_da_1_s = 'Nếu vận tốc riêng của ca nô là $%s\\text{ km/h}$ thì tổng thời gian cả đi lẫn về của ca nô là $%s$ giờ' % (v_cano, str_sai_tt)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_d = 'Đúng. Thay $x = %s$: thời gian xuôi dòng là $\\dfrac{%s}{%s + %s} = %s$ giờ; thời gian ngược dòng là $\\dfrac{%s}{%s - %s} = %s$ giờ. Tổng thời gian là $%s + %s = %s$ giờ.' % (v_cano, S, v_cano, v_nuoc, str_tx, S, v_cano, v_nuoc, str_tn, str_tx, str_tn, str_tt)
        loigiai_vdc_s = 'Sai. Tổng thời gian cả đi lẫn về là $\\dfrac{%s}{%s} + \\dfrac{%s}{%s} = %s + %s = %s$ giờ.' % (S, v_cano + v_nuoc, S, v_cano - v_nuoc, str_tx, str_tn, str_tt)
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

    sol_nb = loigiai_nb_d if '\\True' in nb_da_1 else loigiai_nb_s
    sol_th = loigiai_th_d if '\\True' in th_da_1 else loigiai_th_s
    sol_vd = loigiai_vd_d if '\\True' in vd_da_1 else loigiai_vd_s
    sol_vdc = loigiai_vdc_d if '\\True' in vdc_da_1 else loigiai_vdc_s

    combined = [
        (nb_da_1, sol_nb),
        (th_da_1, sol_th),
        (vd_da_1, sol_vd),
        (vdc_da_1, sol_vdc)
    ]
    random.shuffle(combined)
    shuffled_answers, shuffled_solutions = zip(*combined)

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\choiceTFn \n' +
               '{' + str(shuffled_answers[0]) + '}\n' +
               '{' + str(shuffled_answers[1]) + '}\n' +
               '{' + str(shuffled_answers[2]) + '}\n' +
               '{' + str(shuffled_answers[3]) + '}\n' +
               '\\loigiai{ \n' +
               '\\begin{enumEX}[a)]{1} \n' +
               '\\item ' + str(shuffled_solutions[0]) + '\n' +
               '\\item ' + str(shuffled_solutions[1]) + '\n' +
               '\\item ' + str(shuffled_solutions[2]) + '\n' +
               '\\item ' + str(shuffled_solutions[3]) + '\n' +
               '\\end{enumEX}} \n' +
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
