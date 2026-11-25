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

def bt_dang12_p2_b3_c5_ds8(self):
    # Dạng 12: Quy đổi số liệu tuyệt đối từ biểu đồ cột sang tỉ lệ phần trăm để đối chiếu với biểu đồ hình quạt tròn
    mult = random.choice([1, 2])
    e1, e2, e3, e4 = 420 * mult, 300 * mult, 180 * mult, 100 * mult
    tong = e1 + e2 + e3 + e4
    
    def fmt_int(n):
        return f"{n:,}".replace(",", "\\,")
        
    hs = [round(v / (125.0 * mult), 2) for v in [e1, e2, e3, e4]]
    
    tikz_code = (
        '\\begin{center}\n' +
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
        '\\draw[line width=1pt, ->] (0,0) -- (7.6,0) node[below] {Lĩnh vực};\n' +
        '\\draw[line width=1pt, ->] (0,0) -- (0,4.5) node[left] {Điện năng (triệu $\\text{kWh}$)};\n' +
        '\\node[below left] at (0,0) {$0$};\n' +
        '\\draw[line width=1pt, fill=black!20] (0.5,0) rectangle (1.5,%s); \\node[above] at (1.0,%s) {$%s$}; \\node[below] at (1.0,0) {Cơ khí};\n' % (hs[0], hs[0], e1) +
        '\\draw[line width=1pt, fill=black!20] (2.2,0) rectangle (3.2,%s); \\node[above] at (2.7,%s) {$%s$}; \\node[below] at (2.7,0) {Thực phẩm};\n' % (hs[1], hs[1], e2) +
        '\\draw[line width=1pt, fill=black!20] (3.9,0) rectangle (4.9,%s); \\node[above] at (4.4,%s) {$%s$}; \\node[below] at (4.4,0) {Dệt may};\n' % (hs[2], hs[2], e3) +
        '\\draw[line width=1pt, fill=black!20] (5.6,0) rectangle (6.6,%s); \\node[above] at (6.1,%s) {$%s$}; \\node[below] at (6.1,0) {Dịch vụ};\n' % (hs[3], hs[3], e4) +
        '\\end{tikzpicture}\n' +
        '\\end{center}'
    )
    
    noidungcauhoi = ('Biểu đồ cột dưới đây thống kê lượng điện năng tiêu thụ (đơn vị: triệu $\\text{kWh}$) của một khu công nghiệp trong năm $2025$ theo bốn lĩnh vực:\n' +
                     tikz_code + '\n' +
                     'Một kĩ sư muốn vẽ biểu đồ hình quạt tròn thể hiện cơ cấu tiêu thụ điện của khu công nghiệp này. Xét tính đúng, sai của các khẳng định sau:')
    
    # a (Đúng)
    nb_da_1_d = '\\True Tổng lượng điện năng tiêu thụ của toàn khu công nghiệp trong năm $2025$ là $%s$ triệu $\\text{kWh}$' % fmt_int(tong)
    nb_da_1_s = 'Tổng lượng điện năng tiêu thụ của toàn khu công nghiệp trong năm $2025$ là $%s$ triệu $\\text{kWh}$' % fmt_int(tong - 100)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Tổng lượng điện năng tiêu thụ là $%s + %s + %s + %s = %s$ (triệu $\\text{kWh}$).' % (e1, e2, e3, e4, fmt_int(tong)))
    list_nb_2 = [loigiai_nb_1]
    
    # b (Đúng)
    th_da_1_d = '\\True Lĩnh vực Sản xuất cơ khí chiếm $42\\%%$ tổng lượng điện năng tiêu thụ'
    th_da_1_s = 'Lĩnh vực Sản xuất cơ khí chiếm $45\\%%$ tổng lượng lượng điện năng tiêu thụ'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Tỉ trọng tiêu thụ điện của ngành Cơ khí là $\\dfrac{%s}{%s} \\cdot 100\\%% = 42\\%%$.' % (e1, fmt_int(tong)))
    list_th_2 = [loigiai_th_1]
    
    # c (Đúng)
    vd_da_1_d = '\\True Tổng tỉ trọng tiêu thụ điện của hai ngành Dệt may và Dịch vụ nhỏ hơn ngành Chế biến thực phẩm'
    vd_da_1_s = 'Tổng tỉ trọng tiêu thụ điện của hai ngành Dệt may và Dịch vụ lớn hơn ngành Chế biến thực phẩm'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Tỉ trọng Dệt may là $18\\%%$, Dịch vụ là $10\\%%$, tổng hai ngành là $28\\%% < 30\\%%$ (ngành Chế biến thực phẩm).' )
    list_vd_2 = [loigiai_vd_1]
    
    # d (Sai)
    vdc_da_1_d = '\\True Trên biểu đồ hình quạt tròn, góc ở tâm ứng với ngành Chế biến thực phẩm lớn hơn góc ở tâm ứng với ngành Dệt may là $43,2^\\circ$'
    vdc_da_1_s = 'Trên biểu đồ hình quạt tròn, góc ở tâm ứng với ngành Chế biến thực phẩm lớn hơn góc ở tâm ứng với ngành Dệt may là $45^\\circ$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Chênh lệch tỉ trọng giữa Chế biến thực phẩm ($30\\%%$) và Dệt may ($18\\%%$) là $12\\%%$, ứng với góc ở tâm chênh lệch là $360^\\circ \\cdot 12\\%% = 43,2^\\circ$.' )
    list_vdc_2 = [loigiai_vdc_1]

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    # Lặp đến khi đáp án có từ 1 đến 3 đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)

        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
            break

    # Gán lại vào list
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

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
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
