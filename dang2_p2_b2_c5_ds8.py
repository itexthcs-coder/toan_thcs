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


def bt_dang2_p2_b2_c5_ds8(self):
    # Dạng 2 (Thông hiểu - Thuần túy toán học): Tìm quy ước đơn vị tối ưu cho biểu đồ tranh bằng ước chung
    gcd_val = random.choice([40, 60, 80])
    m1, m2, m3, m4 = 3, 4, 5, 7
    v1, v2, v3, v4 = gcd_val * m1, gcd_val * m2, gcd_val * m3, gcd_val * m4
    half_gcd = gcd_val // 2
    tong_bt_half = (v1 + v2 + v3 + v4) // half_gcd
    bad_unit = gcd_val - 20 if gcd_val == 60 else gcd_val + 20
    
    noidungcauhoi = ("""Cho bảng số liệu thống kê bốn đối tượng $M_1, M_2, M_3, M_4$:\\\\
    \\begin{center}
    \\begin{tabular}{|c|c|c|c|c|}
    \\hline
    \\textbf{Đối tượng} & $M_1$ & $M_2$ & $M_3$ & $M_4$ \\\\
    \\hline
    \\textbf{Số lượng} & $%s$ & $%s$ & $%s$ & $%s$ \\\\
    \\hline
    \\end{tabular}
    \\end{center}
    Người ta muốn biểu diễn bảng số liệu này bằng biểu đồ tranh sao cho không phải chia nhỏ bất kì biểu tượng nào. Xét tính đúng sai của các khẳng định sau:"""
                     % (v1, v2, v3, v4))
    
    nb_da_1_d = '\\True Giá trị quy ước $k$ của mỗi biểu tượng phải là một ước chung của $%s, %s, %s, %s$' % (v1, v2, v3, v4)
    nb_da_1_s = 'Giá trị quy ước $k$ của mỗi biểu tượng phải là một bội chung của $%s, %s, %s, %s$' % (v1, v2, v3, v4)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ("""Để không phải chia nhỏ bất kì biểu tượng nào thì số lượng của cả bốn đối tượng đều phải chia hết cho $k$, tức là $k$ phải là ước chung của $%s, %s, %s, %s$.""" % (v1, v2, v3, v4))
    list_nb_2 = [loigiai_nb_1]
    
    th_da_1_d = '\\True Nếu chọn mỗi biểu tượng ứng với $%s$ đơn vị thì tổng số biểu tượng cần vẽ cho cả bốn đối tượng là $%s$ biểu tượng' % (half_gcd, tong_bt_half)
    th_da_1_s = 'Nếu chọn mỗi biểu tượng ứng với $%s$ đơn vị thì tổng số biểu tượng cần vẽ cho cả bốn đối tượng là $%s$ biểu tượng' % (half_gcd, tong_bt_half + 4)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ("""Nếu chọn mỗi biểu tượng ứng với $%s$ đơn vị thì tổng số biểu tượng cần vẽ là: $\\frac{%s + %s + %s + %s}{%s} = \\frac{%s}{%s} = %s$ (biểu tượng)."""
                    % (half_gcd, v1, v2, v3, v4, half_gcd, v1 + v2 + v3 + v4, half_gcd, tong_bt_half))
    list_th_2 = [loigiai_th_1]
    
    vd_da_1_d = '\\True Để số lượng biểu tượng phải vẽ là ít nhất, ta cần chọn mỗi biểu tượng ứng với $%s$ đơn vị' % gcd_val
    vd_da_1_s = 'Để số lượng biểu tượng phải vẽ là ít nhất, ta cần chọn mỗi biểu tượng ứng với $%s$ đơn vị' % half_gcd
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ("""Để số biểu tượng vẽ ra là ít nhất, giá trị quy ước $k$ phải lớn nhất có thể, tức là $k = \\text{ƯCLN}(%s, %s, %s, %s) = %s$."""
                    % (v1, v2, v3, v4, gcd_val))
    list_vd_2 = [loigiai_vd_1]
    
    vdc_da_1_s = '\\True Nếu chọn mỗi biểu tượng ứng với $%s$ đơn vị thì vẫn vẽ được trọn vẹn các biểu tượng nguyên cho cả bốn đối tượng' % bad_unit
    vdc_da_1_d = 'Nếu chọn mỗi biểu tượng ứng với $%s$ đơn vị thì không thể vẽ trọn vẹn các biểu tượng nguyên cho cả bốn đối tượng' % bad_unit
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ("""Vì $%s$ không chia hết cho $%s$ nên nếu chọn quy ước $%s$ đơn vị thì sẽ phải chia nhỏ biểu tượng, không vẽ được trọn vẹn các biểu tượng nguyên."""
                     % (v1, bad_unit, bad_unit))
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
