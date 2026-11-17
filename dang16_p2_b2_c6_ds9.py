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


def bt_dang16_p2_b2_c6_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        v = symbols('v')
        v1 = random.choice([40, 60, 80])
        d1 = 0.005 * (v1**2) + 0.2 * v1
        d1_str = str(int(d1)) if d1 == int(d1) else str(d1).replace('.', ',')

        v2 = random.choice([100, 120])
        d2 = int(0.005 * (v2**2) + 0.2 * v2)
        d1_double = int(0.005 * ((2*v1)**2) + 0.2 * (2*v1))

        noidungcauhoi = ('Trong an toàn giao thông, quãng đường phanh $d$ (tính bằng mét) của một chiếc ô tô chạy trên đường nhựa khô ráo được mô hình hóa bởi công thức $d = 0,005v^2 + 0,2v$, trong đó $v \\text{ (km/h)}$ là vận tốc của xe tại thời điểm bắt đầu đạp phanh ($v > 0$). Xét tính đúng sai của các khẳng định sau:')

        nb_da_1_d = '\\True Để tìm vận tốc của xe khi biết quãng đường phanh là $%s \\text{ m}$, ta cần giải phương trình bậc hai $0,005v^2 + 0,2v - %s = 0$' % (d2, d2)
        nb_da_1_s = 'Để tìm vận tốc của xe khi biết quãng đường phanh là $%s \\text{ m}$, ta cần giải phương trình bậc hai $0,005v^2 + 0,2v + %s = 0$' % (d2, d2)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('Thay $d = %s$ vào công thức $d = 0,005v^2 + 0,2v$, ta được phương trình $0,005v^2 + 0,2v = %s \\Leftrightarrow 0,005v^2 + 0,2v - %s = 0$.' % (d2, d2, d2))

        th_da_1_d = '\\True Nếu xe đang chạy với vận tốc $%s \\text{ km/h}$ thì quãng đường phanh của xe là $%s \\text{ m}$' % (v1, d1_str)
        th_da_1_s = 'Nếu xe đang chạy với vận tốc $%s \\text{ km/h}$ thì quãng đường phanh của xe là $%s \\text{ m}$' % (v1, int(d1) + 10)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('Thay $v = %s$ vào công thức ta được: $d = 0,005 \\cdot %s^2 + 0,2 \\cdot %s = %s \\text{ (m)}$.' % (v1, v1, v1, d1_str))

        vd_da_1_d = '\\True Nếu vết phanh để lại trên mặt đường dài $%s \\text{ m}$ thì vận tốc của xe lúc bắt đầu phanh là $%s \\text{ km/h}$' % (d2, v2)
        vd_da_1_s = 'Nếu vết phanh để lại trên mặt đường dài $%s \\text{ m}$ thì vận tốc của xe lúc bắt đầu phanh là $%s \\text{ km/h}$' % (d2, v2 + 20)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('Giải phương trình $0,005v^2 + 0,2v - %s = 0 \\Leftrightarrow v^2 + 40v - %s = 0$. \\\\ Có $\\Delta\\prime = 20^2 - 1 \\cdot (-%s) = %s \\Rightarrow \\sqrt{\\Delta\\prime} = %s$. \\\\ Vì $v > 0$ nên $v = -20 + %s = %s \\text{ (km/h)}$.' % (d2, 200*d2, 200*d2, 400 + 200*d2, v2 + 20, v2 + 20, v2))

        vdc_da_1_d = '\\True Khi vận tốc của xe tăng gấp đôi từ $%s \\text{ km/h}$ lên $%s \\text{ km/h}$ thì quãng đường phanh tăng hơn gấp ba lần' % (v1, 2*v1)
        vdc_da_1_s = 'Khi vận tốc của xe tăng gấp đôi thì quãng đường phanh cũng tăng đúng gấp đôi'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('Khi $v = %s \\text{ km/h}$ thì $d = %s \\text{ m}$. Khi vận tốc tăng gấp đôi lên $v = %s \\text{ km/h}$ thì quãng đường phanh là $d\\prime = 0,005 \\cdot %s^2 + 0,2 \\cdot %s = %s \\text{ m} > 3 \\cdot %s \\text{ m}$.' % (v1, d1_str, 2*v1, 2*v1, 2*v1, d1_double, d1_str))

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
