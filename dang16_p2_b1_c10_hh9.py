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


def bt_dang16_p2_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        r_val = random.randint(3, 5)
        h_val = random.randint(8, 12)
        sxq_pi = 2 * r_val * h_val
        sday_pi = r_val ** 2
        stong_pi = sxq_pi + sday_pi
        v_pi = sday_pi * h_val
        v_thuc = (Decimal(str(v_pi)) * Decimal('3.14')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        v_thuc_str = str(v_thuc).replace('.', ',')
        v_rot = int(v_thuc) - random.randint(25, 45)

        noidungcauhoi = ('''Một chiếc cốc thủy tinh dạng hình trụ (không có nắp) có bán kính đáy trong lòng cốc là $r = %s\\text{ cm}$ và chiều cao trong lòng cốc là $h = %s\\text{ cm}$ (như hình vẽ). Lấy $\\pi \\approx 3,14$. Xét tính đúng sai của các khẳng định sau:
\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (0,2.4) ellipse (1.2 and 0.3);
\\draw[line width=1pt] (-1.2,0) arc (180:360:1.2 and 0.3);
\\draw[line width=1pt, dashed] (1.2,0) arc (0:180:1.2 and 0.3);
\\draw[line width=1pt] (-1.2,0)--(-1.2,2.4) (1.2,0)--(1.2,2.4);
\\draw[line width=1pt, dashed] (0,0)--(1.2,0);
\\node[below] at (0.6,0) {$r$};
\\node[right] at (1.2,1.2) {$h$};
\\end{tikzpicture}
\\end{center}'''
                         % (r_val, h_val))

        nb_da_1_d = '\\True Diện tích mặt xung quanh bên trong của cốc là $%s\\pi\\text{ cm}^2$' % (sxq_pi)
        nb_da_1_s = 'Diện tích mặt xung quanh bên trong của cốc là $%s\\pi\\text{ cm}^2$' % (r_val * h_val)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        loigiai_nb_1 = ('''Diện tích mặt xung quanh bên trong của cốc là: $S_{xq} = 2\\pi r h = 2\\pi \\cdot %s \\cdot %s = %s\\pi\\text{ (cm}^2\\text{)}$.''' % (r_val, h_val, sxq_pi))
        list_nb_2 = [loigiai_nb_1]

        th_da_1_d = '\\True Tổng diện tích mặt xung quanh và mặt đáy bên trong của cốc là $%s\\pi\\text{ cm}^2$' % (stong_pi)
        th_da_1_s = 'Tổng diện tích mặt xung quanh và mặt đáy bên trong của cốc là $%s\\pi\\text{ cm}^2$' % (sxq_pi + 2 * sday_pi)
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        loigiai_th_1 = ('''Vì cốc không có nắp nên tổng diện tích mặt xung quanh và mặt đáy bên trong là: $S = S_{xq} + S_{\\text{đáy}} = %s\\pi + \\pi \\cdot %s^2 = %s\\pi\\text{ (cm}^2\\text{)}$.''' % (sxq_pi, r_val, stong_pi))
        list_th_2 = [loigiai_th_1]

        vd_da_1_d = '\\True Thể tích tối đa lượng nước cốc có thể chứa được là $%s\\pi\\text{ cm}^3$' % (v_pi)
        vd_da_1_s = 'Thể tích tối đa lượng nước cốc có thể chứa được là $%s\\pi\\text{ cm}^3$' % (sxq_pi)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        loigiai_vd_1 = ('''Thể tích tối đa lượng nước cốc có thể chứa là: $V = \\pi r^2 h = \\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}$.''' % (r_val, h_val, v_pi))
        list_vd_2 = [loigiai_vd_1]

        vdc_da_1_d = '\\True Nếu rót vào cốc $%s\\text{ ml}$ nước (biết $1\\text{ ml} = 1\\text{ cm}^3$) thì nước không bị tràn ra ngoài' % (v_rot)
        vdc_da_1_s = 'Nếu rót vào cốc $%s\\text{ ml}$ nước (biết $1\\text{ ml} = 1\\text{ cm}^3$) thì nước sẽ bị tràn ra ngoài' % (v_rot)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_vdc_1 = ('''Thể tích tối đa của cốc là $V \\approx %s \\cdot 3,14 = %s\\text{ cm}^3 = %s\\text{ ml}$. Vì $%s < %s$ nên nước không bị tràn ra ngoài.''' % (v_pi, v_thuc_str, v_thuc_str, v_rot, v_thuc_str))
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
