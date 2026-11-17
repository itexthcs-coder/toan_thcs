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

def bt_dang14_p2_b2_c5_hh9(self):
    R = random.choice([20, 25, 30])
    dk = 2 * R
    goc_mo = random.choice([130, 140, 150, 160])
    goc_giam = random.choice([30, 40, 50])
    goc_moi = goc_mo - goc_giam
    cung_lon_moi = 360 - goc_moi

    noidungcauhoi = ('''Một chiếc quạt giấy khi mở hết cỡ tạo thành một phần hình tròn tâm $O$, bán kính $R = %s\\text{ cm}$, với hai nan quạt ngoài cùng $OA$ và $OB$ tạo với nhau một góc ở tâm $\\widehat{AOB} = %s^\\circ$ (như hình vẽ).
    \\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (O) at (0,0);
    \\coordinate (A) at (15:1.8);
    \\coordinate (B) at (165:1.8);
    \\draw[line width=1pt] (A) arc (15:165:1.8);
    \\draw[line width=1pt] (A) arc (15:165:0.6);
    \\draw[line width=1pt] (A)--(O)--(B);
    \\fill (O) circle (1pt) node[below] {$O$};
    \\fill (A) circle (1pt) node[right] {$A$};
    \\fill (B) circle (1pt) node[left] {$B$};
    \\end{tikzpicture}
    \\end{center}''' % (R, goc_mo))

    nb_da_1_d = '\\True Phần mép giấy ngoài cùng của quạt là một cung nhỏ có số đo bằng $%s^\\circ$' % (goc_mo)
    nb_da_1_s = 'Phần mép giấy ngoài cùng của quạt là một cung lớn có số đo bằng $%s^\\circ$' % (goc_mo)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ('''Vì góc ở tâm $\\widehat{AOB} = %s^\\circ < 180^\\circ$ nên cung bị chắn $\\overparen{AB}$ là cung nhỏ có số đo bằng $%s^\\circ$.''' % (goc_mo, goc_mo))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Khoảng cách thẳng nối hai đầu mút $A$ và $B$ của hai nan quạt ngoài cùng luôn nhỏ hơn $%s\\text{ cm}$' % (dk)
    th_da_1_s = 'Khoảng cách thẳng nối hai đầu mút $A$ và $B$ của hai nan quạt ngoài cùng có thể bằng $%s\\text{ cm}$' % (dk)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = ('''Khi $\\widehat{AOB} = %s^\\circ < 180^\\circ$ thì $AB$ là dây cung không đi qua tâm của đường tròn $(O; %s\\text{ cm})$ nên $AB < 2R = %s\\text{ cm}$.''' % (goc_mo, R, dk))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Nếu khép bớt quạt lại để góc $\\widehat{AOB}$ giảm đi $%s^\\circ$ thì cung lớn $\\overparen{AB}$ của đường tròn $(O; %s\\text{ cm})$ có số đo bằng $%s^\\circ$' % (goc_giam, R, cung_lon_moi)
    vd_da_1_s = 'Nếu khép bớt quạt lại để góc $\\widehat{AOB}$ giảm đi $%s^\\circ$ thì cung lớn $\\overparen{AB}$ của đường tròn $(O; %s\\text{ cm})$ có số đo bằng $%s^\\circ$' % (goc_giam, R, goc_moi)
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ('''Khi góc $\\widehat{AOB}$ giảm đi $%s^\\circ$, góc ở tâm mới bằng $%s^\\circ - %s^\\circ = %s^\\circ$. \\\\ Khi đó cung lớn $\\overparen{AB}$ có số đo bằng $360^\\circ - %s^\\circ = %s^\\circ$.''' % (goc_giam, goc_mo, goc_giam, goc_moi, goc_moi, cung_lon_moi))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Khi mở quạt tạo góc $\\widehat{AOB} = 180^\\circ$ thì phần mép quạt tạo thành một nửa đường tròn có số đo $180^\\circ$'
    vdc_da_1_s = 'Khi mở quạt tạo góc $\\widehat{AOB} = 180^\\circ$ thì phần mép quạt tạo thành một cung lớn có số đo $180^\\circ$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = ('''Khi góc ở tâm $\\widehat{AOB}$ là góc bẹt ($180^\\circ$) thì mỗi cung $AB$ được gọi là một nửa đường tròn và có số đo bằng $180^\\circ$.''')
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
