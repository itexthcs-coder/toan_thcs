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
from mpl_toolkits.mplot3d import Axes3D

def bt_dang1_p2_b3_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a = random.choice([2, 3, 4, 5])
        b = random.choice([-1, 1])
        x0 = random.randint(-3, 3)
        y0 = random.randint(-4, 4)
        c = a * x0 + b * y0

        dau_b = '+' if b > 0 else '-'
        pt_str = '%sx %s y = %s' % (a, dau_b, c)
        k = -a // b
        m_val = c // b
        dau_m = '+' if m_val > 0 else ('-' if m_val < 0 else '')
        abs_m = str(abs(m_val)) if m_val != 0 else ''
        y_expr_str = '%sx %s %s' % (k, dau_m, abs_m) if m_val != 0 else '%sx' % k
        y_expr_sai = '%sx %s %s' % (-k, dau_m, abs_m) if m_val != 0 else '%sx' % (-k)

        x_sub = x0 + 2
        y_sub = k * x_sub + m_val
        y_sub_sai = y_sub + 2

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho phương trình bậc nhất hai ẩn $%s$ có đường thẳng biểu diễn tập nghiệm là $(d)$.'''
                         % (pt_str))

        # Nhận biết
        nb_da_1_d = '\\True Công thức nghiệm tổng quát của phương trình là $(x; %s)$ với $x \\in \\mathbb{R}$' % (y_expr_str)
        nb_da_1_s = 'Công thức nghiệm tổng quát của phương trình là $(x; %s)$ với $x \\in \\mathbb{R}$' % (y_expr_sai)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Ta có $%s \\Leftrightarrow y = %s$. Vậy công thức nghiệm tổng quát của phương trình là $(x; %s)$ với $x \\in \\mathbb{R}$.'''
                        % (pt_str, y_expr_str, y_expr_str))
        list_nb_2 = [loigiai_nb_1]

        # Thông hiểu
        th_da_1_d = '\\True Cặp số $(%s; %s)$ là một nghiệm của phương trình đã cho' % (x0, y0)
        th_da_1_s = 'Cặp số $(%s; %s)$ là một nghiệm của phương trình đã cho' % (x0, y0 + 1)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Thay $x = %s$ và $y = %s$ vào vế trái của phương trình ta được $%s \\cdot (%s) %s (%s) = %s$ (bằng vế phải). Vậy cặp số $(%s; %s)$ là một nghiệm của phương trình đã cho.'''
                        % (x0, y0, a, x0, dau_b, y0, c, x0, y0))
        list_th_2 = [loigiai_th_1]

        # Vận dụng
        vd_da_1_d = '\\True Đường thẳng $(d)$ đi qua điểm $M(%s; %s)$' % (x_sub, y_sub)
        vd_da_1_s = 'Đường thẳng $(d)$ đi qua điểm $M(%s; %s)$' % (x_sub, y_sub_sai)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Thay $x = %s$ vào công thức $y = %s$ ta được $y = %s \\cdot (%s) %s %s = %s$. Suy ra điểm $M(%s; %s)$ thuộc đường thẳng $(d)$.'''
                        % (x_sub, y_expr_str, k, x_sub, dau_m, abs_m, y_sub, x_sub, y_sub))
        list_vd_2 = [loigiai_vd_1]

        # Vận dụng cao
        vdc_da_1_d = '\\True Phương trình đã cho có vô số nghiệm'
        vdc_da_1_s = 'Phương trình đã cho chỉ có duy nhất một nghiệm là $(%s; %s)$' % (x0, y0)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Phương trình bậc nhất hai ẩn $%s$ luôn có vô số nghiệm dạng $(x; %s)$ với $x \\in \\mathbb{R}$.'''
                         % (pt_str, y_expr_str))
        list_vdc_2 = [loigiai_vdc_1]

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
