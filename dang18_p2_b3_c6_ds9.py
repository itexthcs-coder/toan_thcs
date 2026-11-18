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

def bt_dang18_p2_b3_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        plus_pt = 5
        minus_pt = 2
        total_q = 25
        while True:
            x_ans = random.randint(12, 16)
            y_ans = random.randint(2, 5)
            score = plus_pt * x_ans - minus_pt * y_ans
            if (score + 2 * total_q) % 7 != 0:
                break
        skip_q = total_q - x_ans - y_ans

        # Nội dung câu hỏi
        noidungcauhoi = ('''Trong một cuộc thi Rung chuông vàng gồm $%s$ câu hỏi, mỗi câu trả lời đúng được cộng $%s$ điểm, mỗi câu trả lời sai bị trừ $%s$ điểm, câu bỏ qua không tính điểm. Một thí sinh trả lời đúng $x$ câu, sai $y$ câu và đạt được $%s$ điểm ($x, y \\in \\mathbb{N}, x + y \\le %s$).'''
                         % (total_q, plus_pt, minus_pt, score, total_q))

        # Nhận biết
        nb_da_1_d = '\\True Phương trình bậc nhất hai ẩn biểu thị số điểm thí sinh đạt được là $%sx - %sy = %s$' % (plus_pt, minus_pt, score)
        nb_da_1_s = 'Phương trình bậc nhất hai ẩn biểu thị số điểm thí sinh đạt được là $%sx + %sy = %s$' % (plus_pt, minus_pt, score)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Số điểm được cộng từ $x$ câu đúng là $%sx$ điểm, số điểm bị trừ từ $y$ câu sai là $%sy$ điểm. Vậy phương trình biểu thị tổng số điểm là $%sx - %sy = %s$.'''
                        % (plus_pt, minus_pt, plus_pt, minus_pt, score))
        list_nb_2 = [loigiai_nb_1]

        # Thông hiểu
        th_da_1_d = '\\True Cặp số $(%s; %s)$ là một nghiệm thỏa mãn các điều kiện thực tế của thí sinh trên' % (x_ans, y_ans)
        th_da_1_s = 'Cặp số $(%s; %s)$ là một nghiệm của phương trình điểm số trên' % (x_ans + 1, y_ans + 1)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Thay $x = %s$ và $y = %s$ vào phương trình ta được $%s \\cdot %s - %s \\cdot %s = %s$, đồng thời thỏa mãn $%s + %s = %s \\le %s$.'''
                        % (x_ans, y_ans, plus_pt, x_ans, minus_pt, y_ans, score, x_ans, y_ans, x_ans + y_ans, total_q))
        list_th_2 = [loigiai_th_1]

        # Vận dụng
        vd_da_1_d = '\\True Nếu thí sinh đó trả lời sai $%s$ câu thì số câu thí sinh đã bỏ qua là $%s$ câu' % (y_ans, skip_q)
        vd_da_1_s = 'Nếu thí sinh đó trả lời sai $%s$ câu thì thí sinh đã trả lời hết tất cả $%s$ câu hỏi' % (y_ans, total_q)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Khi $y = %s$, thay vào phương trình $%sx - %sy = %s$ tìm được $x = %s$. Vậy số câu thí sinh đã bỏ qua là $%s - (%s + %s) = %s$ (câu).'''
                        % (y_ans, plus_pt, minus_pt, score, x_ans, total_q, x_ans, y_ans, skip_q))
        list_vd_2 = [loigiai_vd_1]

        # Vận dụng cao
        vdc_da_1_d = '\\True Trong trường hợp thí sinh không bỏ qua câu nào ($x + y = %s$), số điểm $%s$ là không thể xảy ra' % (total_q, score)
        vdc_da_1_s = 'Trong trường hợp thí sinh không bỏ qua câu nào ($x + y = %s$), thí sinh vẫn có thể đạt được $%s$ điểm' % (total_q, score)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Nếu $x + y = %s$ thì $y = %s - x$. Thay vào phương trình điểm số ta được $%sx - %s(%s - x) = %s \\Leftrightarrow 7x = %s$. Vì $%s$ không chia hết cho $7$ nên không tồn tại số câu đúng $x \\in \\mathbb{N}$.'''
                         % (total_q, total_q, plus_pt, minus_pt, total_q, score, score + 2 * total_q, score + 2 * total_q))
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
