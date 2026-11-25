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


def bt_dang16_p2_b2_c5_ds8(self):
    # Dạng 16 (Vận dụng - Thực tế): Cơ cấu chi tiêu hộ gia đình và ngân sách
    thu_nhap = random.choice([20, 24, 30])
    tien_hoc = thu_nhap * 25 // 100
    tien_tk_moi = thu_nhap * 20 // 100
    s_tn = f"{thu_nhap}\\,000\\,000"
    s_th = f"{tien_hoc}\\,000\\,000"
    s_tk = f"{tien_tk_moi}\\,000\\,000"
    
    tikz_code = ("""\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\draw[line width=1pt] (0,0) circle (1.5);
    \\draw[line width=1pt] (0,0) -- (0:1.5) (0,0) -- (144:1.5) (0,0) -- (234:1.5) (0,0) -- (306:1.5);
    \\node at (72:0.9) {$40\\%%$};
    \\node at (189:0.9) {$25\\%%$};
    \\node at (270:0.9) {$20\\%%$};
    \\node at (333:0.95) {$15\\%%$};
    \\node[right] at (1.9, 0.8) {Tiền ăn uống: $40\\%%$};
    \\node[right] at (1.9, 0.25) {Học tập của con: $25\\%%$};
    \\node[right] at (1.9, -0.3) {Sinh hoạt phí: $20\\%%$};
    \\node[right] at (1.9, -0.85) {Tiết kiệm: $15\\%%$};
    \\end{tikzpicture}
    \\end{center}""" )
    
    noidungcauhoi = ("""Biểu đồ hình quạt tròn dưới đây biểu diễn cơ cấu chi tiêu tháng $10/2026$ của gia đình bác Hùng với tổng thu nhập $%s$ đồng:%sXét tính đúng sai của các khẳng định sau:"""
                     % (s_tn, tikz_code))
    
    nb_da_1_d = '\\True Biểu đồ hình quạt tròn được lựa chọn ở đây là hợp lý vì mục đích là thể hiện tỉ trọng từng khoản chi trong tổng thu nhập'
    nb_da_1_s = 'Nên thay bằng biểu đồ đoạn thẳng để thể hiện tỉ trọng từng khoản chi trong tháng $10/2026$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ("""Biểu đồ hình quạt tròn dùng để biểu diễn tỉ lệ phần trăm các thành phần trong một tổng thể ($100\\%%$) nên lựa chọn này là hoàn toàn hợp lý.""")
    list_nb_2 = [loigiai_nb_1]
    
    th_da_1_d = '\\True Số tiền gia đình bác Hùng dành cho việc học tập của con trong tháng là $%s$ đồng' % s_th
    th_da_1_s = 'Số tiền gia đình bác Hùng dành cho việc học tập của con trong tháng là $%s$ đồng' % f"{thu_nhap * 20 // 100}\\,000\\,000"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ("""Số tiền dành cho việc học tập của con chiếm $25\\%%$ tổng thu nhập, bằng: $%s \\cdot 25\\%% = %s$ (đồng).""" % (s_tn, s_th))
    list_th_2 = [loigiai_th_1]
    
    vd_da_1_d = '\\True Nếu chuyển dữ liệu này sang biểu đồ cột đơn thì cột ``Tiền ăn uống cao gấp đôi cột ``Sinh hoạt phí'
    vd_da_1_s = 'Nếu chuyển dữ liệu này sang biểu đồ cột đơn thì cột ``Tiền ăn uống cao gấp ba lần cột ``Sinh hoạt phí'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ("""Tiền ăn uống chiếm $40\\%%$ và sinh hoạt phí chiếm $20\\%%$ của cùng một tổng thu nhập nên khi vẽ biểu đồ cột đơn, cột Tiền ăn uống cao gấp $\\dfrac{40\\%%}{20\\%%} = 2$ lần cột Sinh hoạt phí.""")
    list_vd_2 = [loigiai_vd_1]
    
    vdc_da_1_s = '\\True Trong tháng $11/2026$, nếu tổng thu nhập không đổi và gia đình tăng khoản Tiết kiệm lên $%s$ đồng thì tỉ trọng khoản Tiết kiệm trên biểu đồ hình quạt tròn sẽ chiếm $25\\%%$' % s_tk
    vdc_da_1_d = 'Trong tháng $11/2026$, nếu tổng thu nhập không đổi và gia đình tăng khoản Tiết kiệm lên $%s$ đồng thì tỉ trọng khoản Tiết kiệm trên biểu đồ hình quạt tròn sẽ chiếm $20\\%%$' % s_tk
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ("""Tỉ trọng mới của khoản Tiết kiệm là: $\\dfrac{%s}{%s} \\cdot 100\\%% = 20\\%%$ (không phải $25\\%%$).""" % (s_tk, s_tn))
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
