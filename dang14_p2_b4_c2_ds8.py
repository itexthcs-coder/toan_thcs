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


def bt_dang14_p2_b4_c2_ds8(self):
    a = random.choice([1, 2, 3])
    c_val = 4 * (a**4)
    b_val = 4 * (a**2)
    da_thuc = x**4 + c_val
    
    noidungcauhoi = ('''Cho đa thức $L = %s$.''' % (latex(da_thuc)))
    
    nb_da_1_d = '\\True Ta có thể thêm và bớt $%sx^2$ để viết $L = (x^4 + %sx^2 + %s) - %sx^2$' % (b_val, b_val, c_val, b_val)
    nb_da_1_s = 'Ta có thể thêm và bớt $%sx^2$ để viết $L = (x^4 + %sx^2 + %s) + %sx^2$' % (b_val, b_val, c_val, b_val)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    list_nb_2 = ['''Thêm và bớt cùng một lượng $%sx^2$ không làm thay đổi giá trị đa thức: $L = (x^4 + %sx^2 + %s) - %sx^2$.'''
                 % (b_val, b_val, c_val, b_val)]
    
    th_da_1_d = '\\True Đa thức $L$ được đưa về hiệu hai bình phương là $(x^2 + %s)^2 - (%sx)^2$' % (2*(a**2), 2*a)
    th_da_1_s = 'Đa thức $L$ được đưa về hiệu hai bình phương là $(x^2 + %s)^2 - (%sx)^2$' % (2*(a**2), 4*(a**2))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    list_th_2 = ['''Ta có $x^4 + %sx^2 + %s = (x^2 + %s)^2$ và $%sx^2 = (%sx)^2$, nên $L = (x^2 + %s)^2 - (%sx)^2$.'''
                 % (b_val, c_val, 2*(a**2), b_val, 2*a, 2*(a**2), 2*a)]
    
    nt1 = x**2 - 2*a*x + 2*(a**2)
    nt2 = x**2 + 2*a*x + 2*(a**2)
    vd_da_1_d = '\\True Kết quả phân tích $L$ thành nhân tử là $(%s)(%s)$' % (latex(nt1), latex(nt2))
    vd_da_1_s = 'Kết quả phân tích $L$ thành nhân tử là $(x^2 - %s)(x^2 + %s)$' % (2*(a**2), 2*(a**2))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    list_vd_2 = ['''Áp dụng hiệu hai bình phương: $L = (x^2 + %s - %sx)(x^2 + %s + %sx) = (%s)(%s)$.'''
                 % (2*(a**2), 2*a, 2*(a**2), 2*a, latex(nt1), latex(nt2))]
    
    x_test = a + 1
    val_L = x_test**4 + c_val
    f1 = x_test**2 - 2*a*x_test + 2*(a**2)
    f2 = x_test**2 + 2*a*x_test + 2*(a**2)
    vdc_da_1_d = '\\True Với $x = %s$, giá trị $L = %s$ là một hợp số' % (x_test, val_L)
    vdc_da_1_s = 'Với $x = %s$, giá trị $L = %s$ là một số nguyên tố' % (x_test, val_L)
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    list_vdc_2 = ['''Tại $x = %s$, ta có $L = %s \\cdot %s = %s$ (với cả hai thừa số đều lớn hơn $1$), nên $%s$ là hợp số.'''
                  % (x_test, f1, f2, val_L, val_L)]

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
