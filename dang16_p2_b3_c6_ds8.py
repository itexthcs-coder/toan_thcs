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
def bt_dang16_p2_b3_c6_ds8(self):
    # Dạng 16: Thực tế năng suất / khối lượng công việc mỗi ngày
    bo = [
        (120, 5, 24, 10),
        (150, 5, 30, 10),
        (180, 6, 30, 12),
        (200, 10, 20, 20),
        (240, 8, 30, 16)
    ]
    tong_kl, vuot_muc, x_val, thuc_te = random.choice(bo)
    
    noidungcauhoi = ('Một đội công nhân dự định đào xong $%s\\text{ m}^3$ đất trong $x$ ngày (với $x > 0$). Thực tế, mỗi ngày đội làm vượt mức $%s\\text{ m}^3$ đất. Xét tính đúng, sai của các khẳng định sau:' % (tong_kl, vuot_muc))
    
    list_nb_da_1 = [
        '\\True Khối lượng đất đội dự định làm mỗi ngày là $\\dfrac{%s}{x}\\text{ (m}^3\\text{)}$' % tong_kl,
        'Khối lượng đất đội dự định làm mỗi ngày là $\\dfrac{x}{%s}\\text{ (m}^3\\text{)}$' % tong_kl
    ]
    loigiai_nb_1 = ('Mỗi ngày theo dự định đội làm được số mét khối đất là $\\dfrac{%s}{x}\\text{ (m}^3\\text{)}$.' % tong_kl)
    
    list_th_da_1 = [
        '\\True Khối lượng đất đội thực tế làm mỗi ngày là $\\dfrac{%s + %sx}{x}\\text{ (m}^3\\text{)}$' % (tong_kl, vuot_muc),
        'Khối lượng đất đội thực tế làm mỗi ngày là $\\dfrac{%s - %sx}{x}\\text{ (m}^3\\text{)}$' % (tong_kl, vuot_muc)
    ]
    loigiai_th_1 = ('Thực tế mỗi ngày đội làm vượt mức $%s\\text{ m}^3$ nên làm được $\\dfrac{%s}{x} + %s = \\dfrac{%s + %sx}{x}\\text{ (m}^3\\text{)}$.' % (vuot_muc, tong_kl, vuot_muc, tong_kl, vuot_muc))
    
    list_vd_da_1 = [
        '\\True Hiệu khối lượng đất làm mỗi ngày giữa thực tế và dự định là $%s\\text{ (m}^3\\text{)}$' % vuot_muc,
        'Hiệu khối lượng đất làm mỗi ngày giữa thực tế và dự định là $\\dfrac{%s}{x}\\text{ (m}^3\\text{)}$' % vuot_muc
    ]
    loigiai_vd_1 = ('Ta có: $\\dfrac{%s + %sx}{x} - \\dfrac{%s}{x} = \\dfrac{%sx}{x} = %s\\text{ (m}^3\\text{)}$.' % (tong_kl, vuot_muc, tong_kl, vuot_muc, vuot_muc))
    
    list_vdc_da_1 = [
        '\\True Nếu dự định làm trong $%s$ ngày thì khối lượng đất làm mỗi ngày theo thực tế là $%s\\text{ m}^3$' % (x_val, thuc_te),
        'Nếu dự định làm trong $%s$ ngày thì khối lượng đất làm mỗi ngày theo thực tế là $%s\\text{ m}^3$' % (x_val, thuc_te + vuot_muc)
    ]
    loigiai_vdc_1 = ('Thay $x = %s$ vào biểu thức thực tế mỗi ngày, ta được $\\dfrac{%s}{%s} + %s = %s + %s = %s\\text{ (m}^3\\text{)}$.' % (x_val, tong_kl, x_val, vuot_muc, tong_kl // x_val, vuot_muc, thuc_te))
    
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
