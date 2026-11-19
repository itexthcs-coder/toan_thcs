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


def bt_dang14_p2_b1_c10_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        canh_sym = random.choice(['a', 'x', 'm'])

        noidungcauhoi = ('''Quay hình vuông $ABCD$ có cạnh bằng $%s\\text{ (cm)}$ ($%s > 0$) một vòng quanh cạnh $AB$ cố định để được một hình trụ (như hình vẽ). Xét tính đúng sai của các khẳng định sau:
\\begin{center}
\\begin{tikzpicture}[scale=0.9, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,2.2);
\\coordinate (B) at (0,0);
\\coordinate (C) at (2.2,0);
\\coordinate (D) at (2.2,2.2);
\\draw[line width=1pt] (0,2.2) ellipse (2.2 and 0.45);
\\draw[line width=1pt] (-2.2,0) arc (180:360:2.2 and 0.45);
\\draw[line width=1pt, dashed] (2.2,0) arc (0:180:2.2 and 0.45);
\\draw[line width=1pt] (-2.2,0)--(-2.2,2.2) (2.2,0)--(2.2,2.2);
\\draw[line width=1pt, dashed] (A)--(B)--(C) (A)--(D);
\\draw[line width=1pt] (D)--(C);
\\fill (A) circle (1pt) node[above] {$A$};
\\fill (B) circle (1pt) node[below] {$B$};
\\fill (C) circle (1pt) node[right] {$C$};
\\fill (D) circle (1pt) node[right] {$D$};
\\end{tikzpicture}
\\end{center}'''
                         % (canh_sym, canh_sym))

        nb_da_1_d = '\\True Hình trụ tạo thành có bán kính đáy và chiều cao đều bằng $%s\\text{ (cm)}$' % (canh_sym)
        nb_da_1_s = 'Hình trụ tạo thành có đường kính đáy bằng $%s\\text{ (cm)}$' % (canh_sym)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

        loigiai_nb_1 = ('''Vì $ABCD$ là hình vuông cạnh $%s$ nên khi quay quanh cạnh $AB$, hình trụ tạo thành có bán kính đáy $R = BC = %s\\text{ (cm)}$ và chiều cao $h = AB = %s\\text{ (cm)}$.''' % (canh_sym, canh_sym, canh_sym))
        list_nb_2 = [loigiai_nb_1]

        th_da_1_d = '\\True Diện tích xung quanh của hình trụ bằng $2\\pi %s^2\\text{ (cm}^2\\text{)}$' % (canh_sym)
        th_da_1_s = 'Diện tích xung quanh của hình trụ bằng $\\pi %s^2\\text{ (cm}^2\\text{)}$' % (canh_sym)
        list_th_da_1 = [th_da_1_d, th_da_1_s]

        loigiai_th_1 = ('''Diện tích xung quanh của hình trụ là: $S_{xq} = 2\\pi R h = 2\\pi \\cdot %s \\cdot %s = 2\\pi %s^2\\text{ (cm}^2\\text{)}$.''' % (canh_sym, canh_sym, canh_sym))
        list_th_2 = [loigiai_th_1]

        vd_da_1_d = '\\True Diện tích xung quanh của hình trụ gấp đôi diện tích một mặt đáy của nó'
        vd_da_1_s = 'Diện tích xung quanh của hình trụ bằng diện tích một mặt đáy của nó'
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

        loigiai_vd_1 = ('''Diện tích một mặt đáy là $S_{\\text{đáy}} = \\pi %s^2$. Ta thấy $S_{xq} = 2\\pi %s^2 = 2 S_{\\text{đáy}}$, nên diện tích xung quanh gấp đôi diện tích một mặt đáy.''' % (canh_sym, canh_sym))
        list_vd_2 = [loigiai_vd_1]

        vdc_da_1_d = '\\True Thể tích của hình trụ bằng $\\pi %s^3\\text{ (cm}^3\\text{)}$' % (canh_sym)
        vdc_da_1_s = 'Thể tích của hình trụ bằng $2\\pi %s^3\\text{ (cm}^3\\text{)}$' % (canh_sym)
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

        loigiai_vdc_1 = ('''Thể tích của hình trụ là: $V = \\pi R^2 h = \\pi \\cdot %s^2 \\cdot %s = \\pi %s^3\\text{ (cm}^3\\text{)}$.''' % (canh_sym, canh_sym, canh_sym))
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
