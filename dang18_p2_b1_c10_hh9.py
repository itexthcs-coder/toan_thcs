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


def bt_dang18_p2_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        cau_hinh = [
            (Decimal('0.8'), Decimal('0.1'), Decimal('1.5')),
            (Decimal('1.0'), Decimal('0.1'), Decimal('2.0')),
            (Decimal('1.2'), Decimal('0.2'), Decimal('1.5'))
        ]
        d_ngoai, day_thanh, h_ong = random.choice(cau_hinh)
        r_ngoai = d_ngoai / Decimal('2')
        r_trong = r_ngoai - day_thanh
        sxq_ngoai = Decimal('2') * r_ngoai * h_ong
        v_betong = (r_ngoai ** 2 - r_trong ** 2) * h_ong
        v_sai = (day_thanh ** 2) * h_ong

        def fmt(val):
            s = f"{val:f}".rstrip('0').rstrip('.')
            return s.replace('.', ',')

        d_ngoai_s = fmt(d_ngoai)
        day_thanh_s = fmt(day_thanh)
        h_ong_s = fmt(h_ong)
        r_ngoai_s = fmt(r_ngoai)
        r_trong_s = fmt(r_trong)
        sxq_ngoai_s = fmt(sxq_ngoai)
        v_betong_s = fmt(v_betong)
        v_sai_s = fmt(v_sai)

        noidungcauhoi = ('''Một ống cống thoát nước bằng bê tông có dạng hình trụ rỗng với chiều dài $%s\\text{ m}$, đường kính ngoài là $%s\\text{ m}$ và bề dày thành ống là $%s\\text{ m}$ (như hình vẽ). Xét tính đúng sai của các khẳng định sau:
\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (0,2.4) ellipse (1.6 and 0.4);
\\draw[line width=1pt] (0,2.4) ellipse (1.1 and 0.25);
\\draw[line width=1pt] (-1.6,0) arc (180:360:1.6 and 0.4);
\\draw[line width=1pt, dashed] (1.6,0) arc (0:180:1.6 and 0.4);
\\draw[line width=1pt, dashed] (0,0) ellipse (1.1 and 0.25);
\\draw[line width=1pt] (-1.6,0)--(-1.6,2.4) (1.6,0)--(1.6,2.4);
\\draw[line width=1pt, dashed] (-1.1,0)--(-1.1,2.4) (1.1,0)--(1.1,2.4);
\\end{tikzpicture}
\\end{center}'''
                         % (h_ong_s, d_ngoai_s, day_thanh_s))

        nb_da_1_d = '\\True Bán kính vòng tròn ngoài của ống cống là $R = %s\\text{ m}$' % (r_ngoai_s)
        nb_da_1_s = 'Bán kính vòng tròn ngoài của ống cống là $R = %s\\text{ m}$' % (d_ngoai_s)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        loigiai_nb_1 = ('''Bán kính vòng tròn ngoài của ống cống là: $R = \\frac{%s}{2} = %s\\text{ (m)}$.''' % (d_ngoai_s, r_ngoai_s))
        list_nb_2 = [loigiai_nb_1]

        th_da_1_d = '\\True Bán kính vòng tròn trong lòng ống cống là $r = %s\\text{ m}$' % (r_trong_s)
        th_da_1_s = 'Bán kính vòng tròn trong lòng ống cống là $r = %s\\text{ m}$' % (fmt(d_ngoai - day_thanh))
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        loigiai_th_1 = ('''Bán kính vòng tròn trong lòng ống cống là: $r = R - %s = %s - %s = %s\\text{ (m)}$.''' % (day_thanh_s, r_ngoai_s, day_thanh_s, r_trong_s))
        list_th_2 = [loigiai_th_1]

        vd_da_1_d = '\\True Diện tích mặt xung quanh phía bên ngoài của ống cống bằng $%s\\pi\\text{ m}^2$' % (sxq_ngoai_s)
        vd_da_1_s = 'Diện tích mặt xung quanh phía bên ngoài của ống cống bằng $%s\\pi\\text{ m}^2$' % (fmt(d_ngoai * h_ong))
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        loigiai_vd_1 = ('''Diện tích mặt xung quanh phía bên ngoài của ống cống là: $S_{xq} = 2\\pi R h = 2\\pi \\cdot %s \\cdot %s = %s\\pi\\text{ (m}^2\\text{)}$.''' % (r_ngoai_s, h_ong_s, sxq_ngoai_s))
        list_vd_2 = [loigiai_vd_1]

        vdc_da_1_d = '\\True Thể tích phần bê tông dùng để đúc một ống cống đó bằng $%s\\pi\\text{ m}^3$' % (v_betong_s)
        vdc_da_1_s = 'Thể tích phần bê tông dùng để đúc một ống cống đó bằng $%s\\pi\\text{ m}^3$' % (v_sai_s)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_vdc_1 = ('''Thể tích phần bê tông bằng hiệu thể tích hình trụ ngoài và hình trụ rỗng bên trong: $V = \\pi (R^2 - r^2) h = \\pi (%s^2 - %s^2) \\cdot %s = %s\\pi\\text{ (m}^3\\text{)}$.''' % (r_ngoai_s, r_trong_s, h_ong_s, v_betong_s))
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
