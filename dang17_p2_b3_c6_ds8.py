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
def bt_dang17_p2_b3_c6_ds8(self):
    # Dạng 17: Thực tế chi phí mua sắm theo nhóm
    bo = [
        (180, 5, 225, 20, 9),
        (160, 4, 200, 16, 10),
        (240, 6, 300, 24, 10),
        (150, 5, 180, 25, 6)
    ]
    tien_dau, them_vo, tien_sau, x_val, don_gia = random.choice(bo)
    
    noidungcauhoi = ('Một câu lạc bộ học sinh mua $x$ quyển vở giống nhau hết $%s$ nghìn đồng (với $x > 0$). Nếu mua thêm $%s$ quyển vở nữa thì tổng tiền vở là $%s$ nghìn đồng. Xét tính đúng, sai của các khẳng định sau:' % (tien_dau, them_vo, tien_sau))
    
    list_nb_da_1 = [
        '\\True Giá tiền mỗi quyển vở ban đầu là $\\dfrac{%s}{x}$ (nghìn đồng)' % tien_dau,
        'Giá tiền mỗi quyển vở ban đầu là $\\dfrac{x}{%s}$ (nghìn đồng)' % tien_dau
    ]
    loigiai_nb_1 = ('Chia tổng số tiền cho số quyển vở ban đầu, giá tiền mỗi quyển vở lúc đầu là $\\dfrac{%s}{x}$ (nghìn đồng).' % tien_dau)
    
    list_th_da_1 = [
        '\\True Giá tiền mỗi quyển vở lúc sau là $\\dfrac{%s}{x + %s}$ (nghìn đồng)' % (tien_sau, them_vo),
        'Giá tiền mỗi quyển vở lúc sau là $\\dfrac{%s}{x - %s}$ (nghìn đồng)' % (tien_sau, them_vo)
    ]
    loigiai_th_1 = ('Tổng số quyển vở lúc sau là $x + %s$, nên giá tiền mỗi quyển vở lúc sau là $\\dfrac{%s}{x + %s}$ (nghìn đồng).' % (them_vo, tien_sau, them_vo))
    
    list_vd_da_1 = [
        '\\True Hiệu giá tiền một quyển vở lúc đầu và lúc sau được biểu diễn bởi phân thức $\\dfrac{%s}{x} - \\dfrac{%s}{x + %s}$' % (tien_dau, tien_sau, them_vo),
        'Hiệu giá tiền một quyển vở lúc đầu và lúc sau được biểu diễn bởi phân thức $\\dfrac{%s - %s}{x + %s}$' % (tien_dau, tien_sau, them_vo)
    ]
    loigiai_vd_1 = ('Hiệu giá tiền một quyển vở lúc đầu và lúc sau là $\\dfrac{%s}{x} - \\dfrac{%s}{x + %s}$ (nghìn đồng).' % (tien_dau, tien_sau, them_vo))
    
    list_vdc_da_1 = [
        'Khi $x = %s$, giá tiền mỗi quyển vở lúc đầu rẻ hơn lúc sau' % x_val,
        '\\True Khi $x = %s$, giá tiền mỗi quyển vở lúc đầu và lúc sau bằng nhau (đều là $%s$ nghìn đồng)' % (x_val, don_gia)
    ]
    loigiai_vdc_1 = ('Khi $x = %s$, giá tiền mỗi quyển lúc đầu là $\\dfrac{%s}{%s} = %s$ nghìn đồng; lúc sau là $\\dfrac{%s}{%s} = %s$ nghìn đồng nên bằng nhau.' % (x_val, tien_dau, x_val, don_gia, tien_sau, x_val + them_vo, don_gia))
    
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
            
    combined = list(zip(answers, [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]))
    random.shuffle(combined)
    shuffled_answers, shuffled_solutions = zip(*combined)
    
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\choiceTFn \n' +
               '{' + str(shuffled_answers[0]) + '}\n' +
               '{' + str(shuffled_answers[1]) + '}\n' +
               '{' + str(shuffled_answers[2]) + '}\n' +
               '{' + str(shuffled_answers[3]) + '}\n' +
               '\\loigiai{ \n' +
               '\\begin{enumEX}[a)]{1} \n' +
               '\\item ' + str(shuffled_solutions[0]) + '\n' +
               '\\item ' + str(shuffled_solutions[1]) + '\n' +
               '\\item ' + str(shuffled_solutions[2]) + '\n' +
               '\\item ' + str(shuffled_solutions[3]) + '\n' +
               '\\end{enumEX}} \n' +
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
