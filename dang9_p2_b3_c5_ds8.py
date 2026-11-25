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

def bt_dang9_p2_b3_c5_ds8(self):
    # Dạng 9: Phân tích cấu trúc doanh thu theo kênh bán hàng qua biểu đồ hình quạt tròn
    p_store, p_ecom, p_web, p_school = random.choice([
        (46, 32, 14, 8),
        (44, 30, 16, 10),
        (48, 30, 14, 8),
        (45, 31, 14, 10)
    ])
    p_online = p_ecom + p_web
    diff_on = p_ecom - p_web
    angle_school = Decimal(str(p_school)) * Decimal('3.6')
    angle_str = str(angle_school).rstrip('0').rstrip('.').replace('.', ',')
    
    a1 = round(p_store * 3.6, 1)
    a2 = round((p_store + p_ecom) * 3.6, 1)
    a3 = round((p_store + p_ecom + p_web) * 3.6, 1)
    m0 = round(a1 / 2.0, 1)
    m1 = round((a1 + a2) / 2.0, 1)
    m2 = round((a2 + a3) / 2.0, 1)
    m3 = round((a3 + 360.0) / 2.0, 1)
    
    tikz_code = (
        '\\begin{center}\n' +
        '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n' +
        '\\draw[line width=1pt, fill=black!10] (0,0) -- (0:2) arc (0:%s:2) -- cycle;\n' % a1 +
        '\\draw[line width=1pt, fill=black!25] (0,0) -- (%s:2) arc (%s:%s:2) -- cycle;\n' % (a1, a1, a2) +
        '\\draw[line width=1pt, fill=black!40] (0,0) -- (%s:2) arc (%s:%s:2) -- cycle;\n' % (a2, a2, a3) +
        '\\draw[line width=1pt, fill=white] (0,0) -- (%s:2) arc (%s:360:2) -- cycle;\n' % (a3, a3) +
        '\\node at (%s:1.2) {$%s\\%%$};\n' % (m0, p_store) +
        '\\node at (%s:1.3) {$%s\\%%$};\n' % (m1, p_ecom) +
        '\\node at (%s:1.35) {$%s\\%%$};\n' % (m2, p_web) +
        '\\node at (%s:1.45) {$%s\\%%$};\n' % (m3, p_school) +
        '\\draw[line width=1pt, fill=black!10] (2.7,1.2) rectangle (3.1,1.5) node[right, yshift=-4pt] {Cửa hàng trực tiếp};\n' +
        '\\draw[line width=1pt, fill=black!25] (2.7,0.4) rectangle (3.1,0.7) node[right, yshift=-4pt] {Sàn TMĐT};\n' +
        '\\draw[line width=1pt, fill=black!40] (2.7,-0.4) rectangle (3.1,-0.1) node[right, yshift=-4pt] {Website riêng};\n' +
        '\\draw[line width=1pt, fill=white] (2.7,-1.2) rectangle (3.1,-0.9) node[right, yshift=-4pt] {Bán buôn trường học};\n' +
        '\\end{tikzpicture}\n' +
        '\\end{center}'
    )
    
    noidungcauhoi = ('Biểu đồ hình quạt tròn dưới đây biểu diễn cơ cấu doanh thu của một chuỗi nhà sách trong năm $2025$ qua $4$ kênh bán hàng:\n' +
                     tikz_code + '\n' +
                     'Xét tính đúng, sai của các khẳng định sau:')
    
    # a (Đúng)
    nb_da_1_d = '\\True Doanh thu từ các kênh bán hàng trực tuyến (Sàn TMĐT và Website riêng) chiếm tổng cộng $%s\\%%$ doanh thu toàn chuỗi' % p_online
    nb_da_1_s = 'Doanh thu từ các kênh bán hàng trực tuyến chiếm chưa tới $40\\%%$ doanh thu toàn chuỗi'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Tổng tỉ trọng của hai kênh trực tuyến là $%s\\%% + %s\\%% = %s\\%%$.' % (p_ecom, p_web, p_online))
    list_nb_2 = [loigiai_nb_1]
    
    # b (Sai)
    th_da_1_d = '\\True Kênh bán trực tiếp tại cửa hàng chiếm tỉ trọng lớn nhất nhưng chưa gấp đôi kênh Sàn TMĐT'
    th_da_1_s = 'Kênh bán trực tiếp tại cửa hàng mang lại doanh thu cao gấp đôi kênh bán qua Sàn TMĐT'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Kênh cửa hàng trực tiếp chiếm $%s\\%%$, trong khi gấp đôi kênh Sàn TMĐT là $2 \\cdot %s\\%% = %s\\%% > %s\\%%$.' % (p_store, p_ecom, 2 * p_ecom, p_store))
    list_th_2 = [loigiai_th_1]
    
    # c (Đúng)
    vd_da_1_d = '\\True Doanh thu từ kênh Website riêng ít hơn kênh Sàn TMĐT là $%s\\%%$ tổng doanh thu' % diff_on
    vd_da_1_s = 'Doanh thu từ kênh Website riêng ít hơn kênh Sàn TMĐT là $10\\%%$ tổng doanh thu'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Chênh lệch tỉ trọng doanh thu giữa Sàn TMĐT và Website riêng là $%s\\%% - %s\\%% = %s\\%%$.' % (p_ecom, p_web, diff_on))
    list_vd_2 = [loigiai_vd_1]
    
    # d (Đúng)
    vdc_da_1_d = '\\True Trên biểu đồ hình quạt tròn, góc ở tâm của hình quạt biểu diễn kênh Bán buôn trường học có số đo bằng $%s^\\circ$' % angle_str
    vdc_da_1_s = 'Trên biểu đồ hình quạt tròn, góc ở tâm của hình quạt biểu diễn kênh Bán buôn trường học có số đo bằng $%s^\\circ$' % (p_school * 3)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Số đo góc ở tâm của hình quạt ứng với $%s\\%%$ là $360^\\circ \\cdot %s\\%% = %s^\\circ$.' % (p_school, p_school, angle_str))
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
