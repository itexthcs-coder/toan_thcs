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


def bt_dang5_p2_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        k_val = random.choice([2, 3, 4])
        k2_val = k_val ** 2

        noidungcauhoi = ('''Xét hai hình trụ $(T_1)$ và $(T_2)$: Hình trụ $(T_1)$ có bán kính đáy $R$ và chiều cao $h$; hình trụ $(T_2)$ được tạo ra bằng cách tăng gấp $%s$ lần bán kính đáy của $(T_1)$ và giữ nguyên chiều cao $h$ (như hình vẽ). Xét tính đúng sai của các khẳng định sau:
\\begin{center}
\\begin{tikzpicture}[scale=0.85, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt] (0,2.2) ellipse (0.8 and 0.22);
\\draw[line width=1pt] (-0.8,0) arc (180:360:0.8 and 0.22);
\\draw[line width=1pt, dashed] (0.8,0) arc (0:180:0.8 and 0.22);
\\draw[line width=1pt] (-0.8,0)--(-0.8,2.2) (0.8,0)--(0.8,2.2);
\\draw[line width=1pt, dashed] (0,0)--(0.8,0);
\\node[below] at (0.4,0) {$R$};
\\node[left] at (-0.8,1.1) {$h$};
\\draw[line width=1pt] (4.2,2.2) ellipse (1.6 and 0.35);
\\draw[line width=1pt] (2.6,0) arc (180:360:1.6 and 0.35);
\\draw[line width=1pt, dashed] (5.8,0) arc (0:180:1.6 and 0.35);
\\draw[line width=1pt] (2.6,0)--(2.6,2.2) (5.8,0)--(5.8,2.2);
\\draw[line width=1pt, dashed] (4.2,0)--(5.8,0);
\\node[below] at (5,0) {$%sR$};
\\node[right] at (5.8,1.1) {$h$};
\\end{tikzpicture}
\\end{center}'''
                         % (k_val, k_val))

        nb_da_1_d = '\\True Chu vi đáy của hình trụ $(T_2)$ gấp $%s$ lần chu vi đáy của hình trụ $(T_1)$' % (k_val)
        nb_da_1_s = 'Chu vi đáy của hình trụ $(T_2)$ gấp $%s$ lần chu vi đáy của hình trụ $(T_1)$' % (k2_val)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        loigiai_nb_1 = ('''Chu vi đáy của $(T_2)$ là $C_2 = 2\\pi (%sR) = %s \\cdot (2\\pi R) = %s C_1$, nên gấp $%s$ lần chu vi đáy của $(T_1)$.''' % (k_val, k_val, k_val, k_val))
        list_nb_2 = [loigiai_nb_1]

        th_da_1_d = '\\True Diện tích xung quanh của hình trụ $(T_2)$ gấp $%s$ lần diện tích xung quanh của hình trụ $(T_1)$' % (k_val)
        th_da_1_s = 'Diện tích xung quanh của hình trụ $(T_2)$ gấp $%s$ lần diện tích xung quanh của hình trụ $(T_1)$' % (k2_val)
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        loigiai_th_1 = ('''Diện tích xung quanh của $(T_2)$ là $S_{xq2} = 2\\pi (%sR) h = %s \\cdot (2\\pi Rh) = %s S_{xq1}$, nên gấp $%s$ lần diện tích xung quanh của $(T_1)$.''' % (k_val, k_val, k_val, k_val))
        list_th_2 = [loigiai_th_1]

        vd_da_1_d = '\\True Diện tích đáy của hình trụ $(T_2)$ gấp $%s$ lần diện tích đáy của hình trụ $(T_1)$' % (k2_val)
        vd_da_1_s = 'Diện tích đáy của hình trụ $(T_2)$ gấp $%s$ lần diện tích đáy của hình trụ $(T_1)$' % (k_val)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        loigiai_vd_1 = ('''Diện tích đáy của $(T_2)$ là $S_2 = \\pi (%sR)^2 = %s\\pi R^2 = %s S_1$, nên gấp $%s$ lần diện tích đáy của $(T_1)$.''' % (k_val, k2_val, k2_val, k2_val))
        list_vd_2 = [loigiai_vd_1]

        vdc_da_1_d = '\\True Thể tích của hình trụ $(T_2)$ gấp $%s$ lần thể tích của hình trụ $(T_1)$' % (k2_val)
        vdc_da_1_s = 'Thể tích của hình trụ $(T_2)$ gấp $%s$ lần thể tích của hình trụ $(T_1)$' % (k_val ** 3)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_vdc_1 = ('''Thể tích của $(T_2)$ là $V_2 = \\pi (%sR)^2 h = %s\\pi R^2 h = %s V_1$, nên gấp $%s$ lần thể tích của $(T_1)$.''' % (k_val, k2_val, k2_val, k2_val))
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
