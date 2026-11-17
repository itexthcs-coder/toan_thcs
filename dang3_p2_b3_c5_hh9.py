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
from PyQt5.QtGui import QTextCursor, QFont
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








def bt_dang3_p2_b3_c5_hh9(self):
    R_val = random.choice([4, 6, 8, 12])
    n_val = random.choice([90, 120, 135, 150])
    l_val = Rational(n_val, 180) * R_val * pi
    Sq_val = Rational(n_val, 360) * (R_val**2) * pi
    ti_so = Rational(n_val, 360)

    noidungcauhoi = ('''Cho hình quạt tròn $OAB$ có bán kính $R = %d\\text{ cm}$ và độ dài cung $\\overparen{AB}$ bằng $%s\\text{ cm}$. Xét tính đúng sai của các khẳng định sau:''' % (R_val, latex(l_val)))

    nb_da_1_d = '\\True Diện tích của hình quạt tròn $OAB$ bằng $%s\\text{ cm}^2$' % latex(Sq_val)
    nb_da_1_s = 'Diện tích của hình quạt tròn $OAB$ bằng $%s\\text{ cm}^2$' % latex(2 * Sq_val)
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    list_nb_1 = [nb_da_1]
    loigiai_nb_1 = ('''Diện tích hình quạt tròn $OAB$ là $S_q = \\dfrac{l \\cdot R}{2} = \\dfrac{%s \\cdot %d}{2} = %s\\text{ (cm}^2\\text{)}$.''' % (latex(l_val), R_val, latex(Sq_val)))
    list_nb_2 = [loigiai_nb_1]

    th_da_1_d = '\\True Số đo của cung $\\overparen{AB}$ là $%d^\\circ$' % n_val
    th_da_1_s = 'Số đo của cung $\\overparen{AB}$ là $%d^\\circ$' % (n_val // 2)
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    list_th_1 = [th_da_1]
    loigiai_th_1 = ('''Từ công thức $l = \\dfrac{n}{180}\\pi R$, suy ra $n = \\dfrac{180 \\cdot %s}{\\pi \\cdot %d} = %d$. Vậy cung $\\overparen{AB}$ có số đo $%d^\\circ$.''' % (latex(l_val), R_val, n_val, n_val))
    list_th_2 = [loigiai_th_1]

    vd_da_1_d = '\\True Tỉ số giữa diện tích hình quạt tròn $OAB$ và diện tích hình tròn $(O; %d\\text{ cm})$ bằng $%s$' % (R_val, latex(ti_so))
    vd_da_1_s = 'Tỉ số giữa diện tích hình quạt tròn $OAB$ và diện tích hình tròn $(O; %d\\text{ cm})$ bằng $%s$' % (R_val, latex(ti_so * 2))
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    list_vd_1 = [vd_da_1]
    loigiai_vd_1 = ('''Tỉ số giữa diện tích hình quạt tròn $OAB$ và diện tích hình tròn cùng bán kính là $\\dfrac{S_q}{S} = \\dfrac{n}{360} = \\dfrac{%d}{360} = %s$.''' % (n_val, latex(ti_so)))
    list_vd_2 = [loigiai_vd_1]

    vdc_da_1_d = '\\True Nếu tăng bán kính lên gấp đôi và giữ nguyên số đo cung thì diện tích hình quạt tròn mới gấp $4$ lần diện tích hình quạt tròn $OAB$'
    vdc_da_1_s = 'Nếu tăng bán kính lên gấp đôi và giữ nguyên số đo cung thì diện tích hình quạt tròn mới gấp đôi diện tích hình quạt tròn $OAB$'
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    list_vdc_1 = [vdc_da_1]
    loigiai_vdc_1 = ('''Khi tăng bán kính lên $2R$ và giữ nguyên số đo cung $n^\\circ$, diện tích hình quạt mới là $S'_q = \\dfrac{n}{360}\\pi (2R)^2 = 4 \\cdot \\dfrac{n}{360}\\pi R^2 = 4S_q$. Vậy diện tích gấp $4$ lần.''')
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
