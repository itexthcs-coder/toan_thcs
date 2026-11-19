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


def bt_dang20_p2_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        k = random.choice([1, 2])
        r_val = Decimal('2') * k
        h2_val = Decimal('1.5') * k
        l_val = Decimal('2.5') * k
        h1_val = Decimal('3') * k + random.choice([Decimal('2'), Decimal('3')])

        v_tru = (r_val ** 2) * h1_val
        v_non = ((r_val ** 2) * h2_val) / Decimal('3')
        v_tong = v_tru + v_non
        sxq_tru = Decimal('2') * r_val * h1_val
        sxq_non = r_val * l_val
        s_ngoai = sxq_tru + sxq_non

        def fmt(val):
            s = f"{val:f}".rstrip('0').rstrip('.')
            return s.replace('.', ',')

        r_s = fmt(r_val)
        h1_s = fmt(h1_val)
        h2_s = fmt(h2_val)
        l_s = fmt(l_val)
        v_tru_s = fmt(v_tru)
        v_non_s = fmt(v_non)
        v_tong_s = fmt(v_tong)
        s_ngoai_s = fmt(s_ngoai)
        s_sai_s = fmt(s_ngoai + r_val ** 2)

        noidungcauhoi = ('''Một tháp chứa ngũ cốc có cấu tạo gồm phần thân dưới dạng hình trụ có bán kính đáy $R = %s\\text{ m}$, chiều cao $h_1 = %s\\text{ m}$ và phần mái che phía trên dạng hình nón có cùng bán kính đáy $R = %s\\text{ m}$, chiều cao $h_2 = %s\\text{ m}$ (như hình vẽ). Xét tính đúng sai của các khẳng định sau:
\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (S) at (0,3.6);
\\coordinate (O1) at (0,2.2);
\\coordinate (O) at (0,0);
\\coordinate (A1) at (-1.4,2.2);
\\coordinate (B1) at (1.4,2.2);
\\coordinate (A) at (-1.4,0);
\\coordinate (B) at (1.4,0);
\\draw[line width=1pt] (S)--(A1) (S)--(B1);
\\draw[line width=1pt] (-1.4,2.2) arc (180:360:1.4 and 0.3);
\\draw[line width=1pt, dashed] (1.4,2.2) arc (0:180:1.4 and 0.3);
\\draw[line width=1pt] (-1.4,0) arc (180:360:1.4 and 0.3);
\\draw[line width=1pt, dashed] (1.4,0) arc (0:180:1.4 and 0.3);
\\draw[line width=1pt] (A1)--(A) (B1)--(B);
\\draw[line width=1pt, dashed] (S)--(O) (O)--(B);
\\node[below] at (0.7,0) {$R$};
\\node[right] at (1.4,1.1) {$h_1$};
\\node[left] at (0,2.9) {$h_2$};
\\end{tikzpicture}
\\end{center}'''
                         % (r_s, h1_s, r_s, h2_s))

        nb_da_1_d = '\\True Độ dài đường sinh của phần mái hình nón bằng $%s\\text{ m}$' % (l_s)
        nb_da_1_s = 'Độ dài đường sinh của phần mái hình nón bằng $%s\\text{ m}$' % (fmt(r_val + h2_val))
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        loigiai_nb_1 = ('''Độ dài đường sinh của phần mái hình nón là: $l = \\sqrt{R^2 + h_2^2} = \\sqrt{%s^2 + %s^2} = %s\\text{ (m)}$.''' % (r_s, h2_s, l_s))
        list_nb_2 = [loigiai_nb_1]

        th_da_1_d = '\\True Thể tích của phần thân hình trụ bằng $%s\\pi\\text{ m}^3$' % (v_tru_s)
        th_da_1_s = 'Thể tích của phần thân hình trụ bằng $%s\\pi\\text{ m}^3$' % (fmt(sxq_tru))
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        loigiai_th_1 = ('''Thể tích của phần thân hình trụ là: $V_{\\text{trụ}} = \\pi R^2 h_1 = \\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (m}^3\\text{)}$.''' % (r_s, h1_s, v_tru_s))
        list_th_2 = [loigiai_th_1]

        vd_da_1_d = '\\True Tổng sức chứa (thể tích) của cả tháp chứa ngũ cốc bằng $%s\\pi\\text{ m}^3$' % (v_tong_s)
        vd_da_1_s = 'Tổng sức chứa (thể tích) của cả tháp chứa ngũ cốc bằng $%s\\pi\\text{ m}^3$' % (fmt(v_tru + v_non * Decimal('3')))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        loigiai_vd_1 = ('''Thể tích phần mái hình nón là $V_{\\text{nón}} = \\frac{1}{3}\\pi R^2 h_2 = \\frac{1}{3}\\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (m}^3\\text{)}$. Tổng thể tích của tháp là: $V = V_{\\text{trụ}} + V_{\\text{nón}} = %s\\pi + %s\\pi = %s\\pi\\text{ (m}^3\\text{)}$.''' % (r_s, h2_s, v_non_s, v_tru_s, v_non_s, v_tong_s))
        list_vd_2 = [loigiai_vd_1]

        vdc_da_1_d = '\\True Diện tích toàn bộ mặt ngoài của tháp (không tính đáy dưới) bằng $%s\\pi\\text{ m}^2$' % (s_ngoai_s)
        vdc_da_1_s = 'Diện tích toàn bộ mặt ngoài của tháp (không tính đáy dưới) bằng $%s\\pi\\text{ m}^2$' % (s_sai_s)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_vdc_1 = ('''Diện tích mặt ngoài cần tính gồm diện tích xung quanh hình trụ và diện tích xung quanh hình nón: $S_{\\text{ngoài}} = 2\\pi R h_1 + \\pi R l = 2\\pi \\cdot %s \\cdot %s + \\pi \\cdot %s \\cdot %s = %s\\pi\\text{ (m}^2\\text{)}$.''' % (r_s, h1_s, r_s, l_s, s_ngoai_s))
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
