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

def fmt_dec(val, places=2):
    d = Decimal(str(val)).quantize(Decimal('1.' + '0'*places) if places > 0 else Decimal('1'), rounding=ROUND_HALF_UP)
    s = format(d, 'f')
    if '.' in s:
        s = s.rstrip('0').rstrip('.')
    return s.replace('.', ',')

def fmt_frac(num, den):
    f = Fraction(num, den)
    if f.denominator == 1:
        return str(f.numerator)
    return '\\dfrac{%s}{%s}' % (f.numerator, f.denominator)

def count_true_answers(answers):
    return sum('\\True' in ans for ans in answers)

def bt_dang14_p2_b3_c8_ds8(self):
    # Dạng 14: So sánh xác suất lí thuyết và thực nghiệm gieo xúc xắc
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n = 150
        while True:
            f1 = random.randint(20, 25)
            f2 = random.randint(25, 30)
            f3 = random.randint(22, 26)
            f4 = random.randint(24, 28)
            f5 = random.randint(18, 22)
            f6 = n - (f1 + f2 + f3 + f4 + f5)
            if 24 <= f6 <= 33 and (f3 + f6) != 50 and (f2 + f4 + f6) != 75 and (f2 + f3 + f5) % 3 == 0:
                break

        p_tn_chia3 = fmt_dec(Fraction(f3 + f6, n), 2)
        p_tn_chan = Fraction(f2 + f4 + f6, n)
        chenh_chan = fmt_dec(abs(p_tn_chan - Fraction(1, 2)), 2)
        chenh_chan_sai = fmt_dec(abs(p_tn_chan - Fraction(1, 2)) + Fraction(1, 50), 2)
        du_bao_6 = f6 * 2
        du_bao_6_sai = du_bao_6 - 10
        pct_snt = ((f2 + f3 + f5) * 100) // n
        pct_snt_sai = pct_snt + 4

        bang_tex = (
            '\\begin{center}\n'
            '\\begin{tabular}{|l|c|c|c|c|c|c|}\n'
            '\\hline\n'
            '\\textbf{Mặt xuất hiện} & $1$ & $2$ & $3$ & $4$ & $5$ & $6$ \\\\ \n'
            '\\hline\n'
            '\\textbf{Số lần} & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
            '\\hline\n'
            '\\end{tabular}\n'
            '\\end{center}'
            % (f1, f2, f3, f4, f5, f6)
        )

        noidungcauhoi = (
            'Bạn Hùng gieo một con xúc xắc cân đối $150$ lần và thu được bảng tần số sau:%s'
            'Xét tính đúng sai của các mệnh đề sau:'
            % bang_tex
        )

        nb_da_1_d = '\\True Xác suất lí thuyết của biến cố "Xuất hiện mặt có số chấm chia hết cho $3$" khác với xác suất thực nghiệm của biến cố đó trong $150$ lần gieo'
        nb_da_1_s = 'Xác suất lí thuyết của biến cố "Xuất hiện mặt có số chấm chia hết cho $3$" bằng xác suất thực nghiệm của biến cố đó trong $150$ lần gieo'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        th_da_1_d = '\\True Xác suất thực nghiệm xuất hiện mặt chẵn chênh lệch so với xác suất lí thuyết một lượng là $%s$' % chenh_chan
        th_da_1_s = 'Xác suất thực nghiệm xuất hiện mặt chẵn chênh lệch so với xác suất lí thuyết một lượng là $%s$' % chenh_chan_sai
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        vd_da_1_d = '\\True Nếu Hùng tiếp tục gieo thêm $300$ lần nữa, dựa trên kết quả thực nghiệm đã có, dự đoán số lần xuất hiện mặt $6$ chấm là $%s$ lần' % du_bao_6
        vd_da_1_s = 'Nếu Hùng tiếp tục gieo thêm $300$ lần nữa, dựa trên kết quả thực nghiệm đã có, dự đoán số lần xuất hiện mặt $6$ chấm là $%s$ lần' % du_bao_6_sai
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        vdc_da_1_d = '\\True Xác suất thực nghiệm xuất hiện mặt có số chấm là số nguyên tố bằng $%s\\%%$' % pct_snt
        vdc_da_1_s = 'Xác suất thực nghiệm xuất hiện mặt có số chấm là số nguyên tố bằng $%s\\%%$' % pct_snt_sai
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_nb_1 = (
            'Xác suất lí thuyết xuất hiện mặt chia hết cho $3$ (mặt $3$ và $6$) là $\\dfrac{2}{6} = \\dfrac{1}{3}$.\\'
            'Xác suất thực nghiệm tương ứng là $\\dfrac{%s + %s}{150} = %s \\neq \\dfrac{1}{3}$.'
            % (f3, f6, p_tn_chia3)
        )
        loigiai_th_1 = (
            'Xác suất thực nghiệm xuất hiện mặt chẵn là $\\dfrac{%s + %s + %s}{150} = %s$. Xác suất lí thuyết là $0,5$.\\'
            'Độ chênh lệch giữa hai xác suất là $|%s - 0,5| = %s$.'
            % (f2, f4, f6, fmt_dec(p_tn_chan, 2), fmt_dec(p_tn_chan, 2), chenh_chan)
        )
        loigiai_vd_1 = (
            'Xác suất thực nghiệm xuất hiện mặt $6$ chấm là $\\dfrac{%s}{150}$.\\'
            'Trong $300$ lần gieo tiếp theo, số lần xuất hiện mặt $6$ chấm dự đoán là $300 \\cdot \\dfrac{%s}{150} = %s$ (lần).'
            % (f6, f6, du_bao_6)
        )
        loigiai_vdc_1 = (
            'Các mặt có số chấm nguyên tố là $2; 3; 5$, xuất hiện tổng cộng $%s + %s + %s = %s$ (lần).\\'
            'Xác suất thực nghiệm tương ứng là $\\dfrac{%s}{150} = %s\\%%$.'
            % (f2, f3, f5, f2 + f3 + f5, f2 + f3 + f5, pct_snt)
        )

        while True:
            nb_da_1 = random.choice(list_nb_da_1)
            th_da_1 = random.choice(list_th_da_1)
            vd_da_1 = random.choice(list_vd_da_1)
            vdc_da_1 = random.choice(list_vdc_da_1)
            answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
            if 1 <= count_true_answers(answers) <= 3:
                break

        combined_nb = list(zip([nb_da_1], [loigiai_nb_1]))
        combined_th = list(zip([th_da_1], [loigiai_th_1]))
        combined_vd = list(zip([vd_da_1], [loigiai_vd_1]))
        combined_vdc = list(zip([vdc_da_1], [loigiai_vdc_1]))
        random.shuffle(combined_nb)
        random.shuffle(combined_th)
        random.shuffle(combined_vd)
        random.shuffle(combined_vdc)
        shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
        shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
        shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
        shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
               '{' + str(shuffled_answers_nb[0]) + '}\n'
               '{' + str(shuffled_answers_th[0]) + '}\n'
               '{' + str(shuffled_answers_vd[0]) + '}\n'
               '{' + str(shuffled_answers_vdc[0]) + '}\n'
               '\\loigiai{ \n'
               '\\begin{enumEX}[a)]{1} \n'
               '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
               '\\item ' + str(shuffled_solutions_th[0]) + '\n'
               '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
               '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
               '\\end{enumEX}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
