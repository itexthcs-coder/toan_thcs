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


def bt_dang19_p2_b1_c6_ds8(self):
    # Dạng 19: Mô hình hóa bài toán hóa học - nồng độ dung dịch nước muối
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        scenarios = [
            (200, 15, 30, 100, 10, 200, '7,5'),   # 30/(200+100)=10%; 30/(200+200)=7,5%
            (300, 20, 60, 100, 15, 200, '12'),    # 60/400=15%; 60/500=12%
            (400, 10, 40, 100, 8, 400, '5')       # 40/500=8%; 40/800=5%
        ]
        m_dd, c_dau, m_muoi, x1, c1, x2, c2_str = random.choice(scenarios)
        c2_sai = '8' if c2_str != '8' else '6'
        
        noidungcauhoi = ('Trong phòng thí nghiệm, một bình đang chứa $%s\\text{ g}$ dung dịch nước muối có nồng độ $%s\\%%$ (tức là có $%s\\text{ g}$ muối nguyên chất). Người ta pha thêm vào bình $x\\text{ (g)}$ nước tinh khiết ($x > 0$) để làm loãng dung dịch. Xét tính đúng sai của các khẳng định sau:'
                         % (m_dd, c_dau, m_muoi))
        
        nb_da_1_d = '\\True Khối lượng dung dịch nước muối sau khi pha thêm $x\\text{ (g)}$ nước là $%s + x\\text{ (g)}$' % m_dd
        nb_da_1_s = 'Khối lượng dung dịch nước muối sau khi pha thêm $x\\text{ (g)}$ nước là $%s + x\\text{ (g)}$' % m_muoi
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_d = 'Đúng. Ban đầu có $%s\\text{ g}$ dung dịch, pha thêm $x\\text{ g}$ nước thì khối lượng dung dịch mới là $%s + x\\text{ (g)}$.' % (m_dd, m_dd)
        loigiai_nb_s = 'Sai. Khối lượng dung dịch mới bằng khối lượng dung dịch ban đầu cộng thêm lượng nước pha vào: $%s + x\\text{ (g)}$.' % m_dd
        
        th_da_1_d = '\\True Phân thức biểu thị nồng độ phần trăm của dung dịch sau khi pha thêm nước là $\\dfrac{%s}{%s + x} \\cdot 100\\text{ (\\%%)}$' % (m_muoi, m_dd)
        th_da_1_s = 'Phân thức biểu thị nồng độ phần trăm của dung dịch sau khi pha thêm nước là $\\dfrac{%s + x}{%s + x} \\cdot 100\\text{ (\\%%)}$' % (m_muoi, m_dd)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_d = 'Đúng. Vì pha thêm nước tinh khiết nên khối lượng chất tan (muối) vẫn giữ nguyên là $%s\\text{ g}$, do đó nồng độ dung dịch mới là $\\dfrac{%s}{%s + x} \\cdot 100\\text{ (\\%%)}$.' % (m_muoi, m_muoi, m_dd)
        loigiai_th_s = 'Sai. Nước tinh khiết không làm tăng lượng muối, nên tử thức vẫn là $%s$ chứ không phải $%s + x$.' % (m_muoi, m_muoi)
        
        vd_da_1_d = '\\True Nếu pha thêm $%s\\text{ g}$ nước tinh khiết thì nồng độ dung dịch mới là $%s\\%%$' % (x1, c1)
        vd_da_1_s = 'Nếu pha thêm $%s\\text{ g}$ nước tinh khiết thì nồng độ dung dịch mới là $%s\\%%$' % (x1, c1 + 2)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_d = 'Đúng. Thay $x = %s$, nồng độ dung dịch mới là $\\dfrac{%s}{%s + %s} \\cdot 100\\%% = \\dfrac{%s}{%s} \\cdot 100\\%% = %s\\%%$.' % (x1, m_muoi, m_dd, x1, m_muoi, m_dd + x1, c1)
        loigiai_vd_s = 'Sai. Thay $x = %s$ vào công thức ta được $\\dfrac{%s}{%s} \\cdot 100\\%% = %s\\%%$.' % (x1, m_muoi, m_dd + x1, c1)
        
        vdc_da_1_d = '\\True Nếu pha thêm $%s\\text{ g}$ nước tinh khiết thì nồng độ dung dịch mới là $%s\\%%$' % (x2, c2_str)
        vdc_da_1_s = 'Nếu pha thêm $%s\\text{ g}$ nước tinh khiết thì nồng độ dung dịch mới là $%s\\%%$' % (x2, c2_sai)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_d = 'Đúng. Thay $x = %s$, nồng độ dung dịch mới là $\\dfrac{%s}{%s + %s} \\cdot 100\\%% = \\dfrac{%s}{%s} \\cdot 100\\%% = %s\\%%$.' % (x2, m_muoi, m_dd, x2, m_muoi, m_dd + x2, c2_str)
        loigiai_vdc_s = 'Sai. Thay $x = %s$ vào công thức ta được nồng độ dung dịch mới là $\\dfrac{%s}{%s} \\cdot 100\\%% = %s\\%%$.' % (x2, m_muoi, m_dd + x2, c2_str)
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
