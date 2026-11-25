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

def bt_dang4_p2_b3_c5_ds8(self):
    # Dạng 4: Kiểm tra tính hợp lí của biểu đồ hình quạt tròn trong thống kê hoạt động ngoại khóa
    n_hs = random.choice([40, 50])
    if n_hs == 40:
        c1, c2, c3 = 30, 24, 26
    else:
        c1, c2, c3 = 35, 30, 35
    tong_luot = c1 + c2 + c3
    p1 = int(c1 * 100 // n_hs)
    p2 = int(c2 * 100 // n_hs)
    p3 = int(c3 * 100 // n_hs)
    tong_p = p1 + p2 + p3
    
    noidungcauhoi = ('Giáo viên chủ nhiệm lớp $8\\text{C}$ ($%s$ học sinh) thực hiện khảo sát đăng kí tham gia ba chuyên đề kĩ năng sống: An toàn giao thông, Phòng chống đuối nước, Kĩ năng giao tiếp (mỗi học sinh có thể đăng kí nhiều chuyên đề). Kết quả thu được $%s$ lượt chọn An toàn giao thông, $%s$ lượt chọn Phòng chống đuối nước và $%s$ lượt chọn Kĩ năng giao tiếp. Xét tính đúng, sai của các khẳng định sau:'
                     % (n_hs, c1, c2, c3))
    
    # a (Đúng)
    nb_da_1_d = '\\True Tổng số lượt đăng kí là $%s$ lượt, gấp đôi sĩ số học sinh của lớp' % tong_luot
    nb_da_1_s = 'Tổng số lượt đăng kí bằng đúng $%s$ lượt, bằng sĩ số học sinh của lớp' % n_hs
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('Tổng số lượt đăng kí của cả lớp là $%s + %s + %s = %s$ (lượt), gấp đôi sĩ số $%s$ học sinh của lớp.' % (c1, c2, c3, tong_luot, n_hs))
    list_nb_2 = [loigiai_nb_1]
    
    # b (Đúng)
    th_da_1_d = '\\True Tỉ lệ học sinh lớp $8\\text{C}$ đăng kí chuyên đề An toàn giao thông là $%s\\%%$' % p1
    th_da_1_s = 'Tỉ lệ học sinh lớp $8\\text{C}$ đăng kí chuyên đề An toàn giao thông là $%s\\%%$' % (p1 - 15)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('Tỉ lệ học sinh của lớp đăng kí chuyên đề An toàn giao thông là $\\dfrac{%s}{%s} \\cdot 100\\%% = %s\\%%$.' % (c1, n_hs, p1))
    list_th_2 = [loigiai_th_1]
    
    # c (Sai)
    vd_da_1_d = '\\True Không thể dùng một biểu đồ hình quạt tròn gồm $3$ hình quạt ghi các số liệu $%s\\%%$, $%s\\%%$, $%s\\%%$ để biểu diễn dữ liệu trên' % (p1, p2, p3)
    vd_da_1_s = 'Có thể dùng một biểu đồ hình quạt tròn gồm $3$ hình quạt ghi các số liệu $%s\\%%$, $%s\\%%$, $%s\\%%$ để biểu diễn tỉ lệ học sinh tham gia từng chuyên đề' % (p1, p2, p3)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('Biểu đồ hình quạt tròn biểu diễn tỉ lệ các phần trong một tổng thể duy nhất (tổng tỉ lệ bằng $100\\%%$). Ở đây tổng các tỉ lệ bằng $%s\\%% + %s\\%% + %s\\%% = %s\\%% \\neq 100\\%%$ nên không thể dùng biểu đồ hình quạt tròn.' % (p1, p2, p3, tong_p))
    list_vd_2 = [loigiai_vd_1]
    
    # d (Đúng)
    vdc_da_1_d = '\\True Biểu đồ cột đơn là lựa chọn thích hợp để biểu diễn tỉ lệ học sinh lớp $8\\text{C}$ lựa chọn từng chuyên đề trên'
    vdc_da_1_s = 'Biểu đồ đoạn thẳng là lựa chọn duy nhất để biểu diễn số lượt chọn từng chuyên đề trên'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('Khi dữ liệu khảo sát cho phép mỗi đối tượng chọn nhiều phương án cùng lúc, ta dùng biểu đồ cột để so sánh tỉ lệ (hoặc số lượt) lựa chọn từng phương án.' )
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
