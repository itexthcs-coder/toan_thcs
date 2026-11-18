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

def bt_dang10_p2_b3_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a = random.choice([3, 4, 5])
        b = random.choice([1, 2])
        val_eq = random.choice([1, 2, 3])
        c = (a + b) * val_eq
        x_opp = Rational(c, a - b)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho phương trình bậc nhất hai ẩn $%sx + %sy = %s$.'''
                         % (a, b, c))

        # Nhận biết
        nb_da_1_d = '\\True Nghiệm $(x_0; y_0)$ của phương trình thỏa mãn $x_0 = y_0$ là $(%s; %s)$' % (val_eq, val_eq)
        nb_da_1_s = 'Không tồn tại nghiệm $(x_0; y_0)$ nào của phương trình thỏa mãn $x_0 = y_0$'
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_1 = ('''Thay $y_0 = x_0$ vào phương trình ta được $%sx_0 + %sx_0 = %s \\Leftrightarrow %sx_0 = %s \\Leftrightarrow x_0 = %s$. Vậy nghiệm cần tìm là $(%s; %s)$.'''
                        % (a, b, c, a + b, c, val_eq, val_eq, val_eq))
        list_nb_2 = [loigiai_nb_1]

        # Thông hiểu
        th_da_1_d = '\\True Nghiệm $(x_0; y_0)$ của phương trình có hoành độ và tung độ đối nhau là $\\left(%s; %s\\right)$' % (latex(x_opp), latex(-x_opp))
        th_da_1_s = 'Nghiệm $(x_0; y_0)$ của phương trình có hoành độ và tung độ đối nhau là $(%s; -%s)$' % (val_eq, val_eq)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_1 = ('''Vì hoành độ và tung độ đối nhau nên $y_0 = -x_0$. Thay vào phương trình ta được $%sx_0 - %sx_0 = %s \\Leftrightarrow %sx_0 = %s \\Leftrightarrow x_0 = %s$, suy ra $y_0 = %s$.'''
                        % (a, b, c, a - b, c, latex(x_opp), latex(-x_opp)))
        list_th_2 = [loigiai_th_1]

        # Vận dụng
        vd_da_1_d = '\\True Đường thẳng biểu diễn tập nghiệm của phương trình cắt đường phân giác $y = x$ tại điểm $M(%s; %s)$' % (val_eq, val_eq)
        vd_da_1_s = 'Đường thẳng biểu diễn tập nghiệm của phương trình song song với đường thẳng $y = x$'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_1 = ('''Giao điểm của đường thẳng $%sx + %sy = %s$ và đường thẳng $y = x$ có tọa độ là nghiệm thỏa mãn $x = y$, đó chính là điểm $M(%s; %s)$.'''
                        % (a, b, c, val_eq, val_eq))
        list_vd_2 = [loigiai_vd_1]

        # Vận dụng cao
        vdc_da_1_d = '\\True Nếu nghiệm $(x_0; y_0)$ thỏa mãn $x_0 > %s$ thì $y_0 < %s$' % (val_eq, val_eq)
        vdc_da_1_s = 'Nếu nghiệm $(x_0; y_0)$ thỏa mãn $x_0 > %s$ thì $y_0 > %s$' % (val_eq, val_eq)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_1 = ('''Ta có $%sx_0 + %sy_0 = %s = %s \\cdot %s + %s \\cdot %s$. Khi $x_0 > %s$ thì $%sx_0 > %s \\cdot %s$, suy ra $%sy_0 < %s \\cdot %s \\Leftrightarrow y_0 < %s$.'''
                         % (a, b, c, a, val_eq, b, val_eq, val_eq, a, a, val_eq, b, b, val_eq, val_eq))
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
