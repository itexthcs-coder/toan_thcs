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


def bt_dang20_p2_b1_c7_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        f1, f2, f3, f4, f5 = 5, 11, 14, 7, 3
        noidungcauhoi = ('''Biểu đồ tần số dạng đoạn thẳng dưới đây thống kê quãng đường đi học từ nhà đến trường (đơn vị: $\\text{km}$, làm tròn đến hàng đơn vị) của toàn bộ học sinh lớp $9E$. Nhà trường dự kiến hỗ trợ vé xe buýt tháng cho những học sinh có nhà cách trường từ $4\\text{ km}$ trở lên:
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt, ->] (0,0) -- (6.2,0) node[below] {Quãng đường ($\\text{km}$)};
\\draw[line width=1pt, ->] (0,0) -- (0,3.6) node[left] {Số học sinh};
\\foreach \\y/\\lbl in {1/5, 2/10, 3/15}{
    \\draw[line width=1pt, dashed] (0,\\y) -- (5.8,\\y);
    \\draw[line width=1pt] (-0.08,\\y) -- (0.08,\\y) node[left=2pt] {$\\lbl$};
}
\\node[below left] at (0,0) {$0$};
\\coordinate (P1) at (1,1.0);
\\coordinate (P2) at (2,2.2);
\\coordinate (P3) at (3,2.8);
\\coordinate (P4) at (4,1.4);
\\coordinate (P5) at (5,0.6);
\\draw[line width=1pt] (P1) -- (P2) -- (P3) -- (P4) -- (P5);
\\fill (P1) circle (1pt) node[above] {$5$};
\\fill (P2) circle (1pt) node[above] {$11$};
\\fill (P3) circle (1pt) node[above] {$14$};
\\fill (P4) circle (1pt) node[above] {$7$};
\\fill (P5) circle (1pt) node[above] {$3$};
\\node[below] at (1,0) {$1$};
\\node[below] at (2,0) {$2$};
\\node[below] at (3,0) {$3$};
\\node[below] at (4,0) {$4$};
\\node[below] at (5,0) {$5$};
\\end{tikzpicture}
\\end{center}''')
        
        ######################################################################## Mệnh đề a ############################################################################
        nb_da_1_d = '\\True ' + ('Sĩ số của lớp $9E$ là $40$ học sinh')
        nb_da_1_s = ('Sĩ số của lớp $9E$ là $38$ học sinh')
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        
        ######################################################################## Mệnh đề b ############################################################################
        th_da_1_d = '\\True ' + ('Quãng đường đi học phổ biến nhất của học sinh lớp $9E$ là $3\\text{ km}$')
        th_da_1_s = ('Quãng đường đi học phổ biến nhất của học sinh lớp $9E$ là $2\\text{ km}$')
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        
        ######################################################################## Mệnh đề c ############################################################################
        vd_da_1_d = '\\True ' + ('Có $10$ học sinh của lớp $9E$ thuộc diện được nhà trường hỗ trợ vé xe buýt tháng')
        vd_da_1_s = ('Có $7$ học sinh của lớp $9E$ thuộc diện được nhà trường hỗ trợ vé xe buýt tháng')
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        
        ######################################################################## Mệnh đề d ############################################################################
        vdc_da_1_d = '\\True ' + ('Số học sinh có nhà cách trường dưới $3\\text{ km}$ chiếm $40\\%$ sĩ số cả lớp')
        vdc_da_1_s = ('Số học sinh có nhà cách trường dưới $3\\text{ km}$ chiếm $35\\%$ sĩ số cả lớp')
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        
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
        
        loigiai_nb_1 = ('Đúng. Sĩ số lớp $9E$ bằng cỡ mẫu: $5 + 11 + 14 + 7 + 3 = 40$ (học sinh).') if '\\True' in nb_da_1 else ('Sai. Cộng tần số tại $5$ mốc quãng đường ta được $5 + 11 + 14 + 7 + 3 = 40$ (học sinh).')
        loigiai_th_1 = ('Đúng. Giá trị $3\\text{ km}$ có tần số lớn nhất ($14$ học sinh) nên phổ biến nhất.') if '\\True' in th_da_1 else ('Sai. Đỉnh cao nhất của đa giác tần số nằm tại hoành độ $3\\text{ km}$ với tần số là $14$.')
        loigiai_vd_1 = ('Đúng. Học sinh có nhà cách trường từ $4\\text{ km}$ trở lên gồm mức $4\\text{ km}$ ($7$ học sinh) và $5\\text{ km}$ ($3$ học sinh), tổng là $7 + 3 = 10$ (học sinh).') if '\\True' in vd_da_1 else ('Sai. Cần tính cả học sinh cách trường $4\\text{ km}$ và $5\\text{ km}$: $7 + 3 = 10$ (học sinh).')
        loigiai_vdc_1 = ('Đúng. Số học sinh có nhà cách trường dưới $3\\text{ km}$ gồm mức $1\\text{ km}$ ($5$) và $2\\text{ km}$ ($11$), tổng là $16$ học sinh, chiếm $\\dfrac{16}{40} \\cdot 100\\% = 40\\%$.') if '\\True' in vdc_da_1 else ('Sai. Có $5 + 11 = 16$ học sinh có nhà cách trường dưới $3\\text{ km}$, chiếm $\\dfrac{16}{40} \\cdot 100\\% = 40\\%$.')
        
        list_nb_1 = [nb_da_1]
        list_nb_2 = [loigiai_nb_1]
        combined_nb = list(zip(list_nb_1, list_nb_2))
        random.shuffle(combined_nb)
        shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
        
        list_th_1 = [th_da_1]
        list_th_2 = [loigiai_th_1]
        combined_th = list(zip(list_th_1, list_th_2))
        random.shuffle(combined_th)
        shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
        
        list_vd_1 = [vd_da_1]
        list_vd_2 = [loigiai_vd_1]
        combined_vd = list(zip(list_vd_1, list_vd_2))
        random.shuffle(combined_vd)
        shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
        
        list_vdc_1 = [vdc_da_1]
        list_vdc_2 = [loigiai_vdc_1]
        combined_vdc = list(zip(list_vdc_1, list_vdc_2))
        random.shuffle(combined_vdc)
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
