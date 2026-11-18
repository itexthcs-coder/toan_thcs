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


def bt_dang13_p2_b1_c7_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        fS = 12
        fM = 35
        fL = 28
        fXL = 15
        fXXL = 10
        yS, yM, yL, yXL, yXXL = 1.2, 3.5, 2.8, 1.5, 1.0
        noidungcauhoi = ('''Một cửa hàng kinh doanh áo phông thống kê số lượng áo bán ra trong tuần qua theo các cỡ và biểu diễn bằng biểu đồ tần số dạng cột:
\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\draw[line width=1pt, ->] (0,0) -- (6.5,0) node[below] {Cỡ áo};
\\draw[line width=1pt, ->] (0,0) -- (0,4.2) node[left] {Số áo (chiếc)};
\\foreach \\y/\\lbl in {1/10, 2/20, 3/30, 4/40}{
    \\draw[line width=1pt, dashed] (0,\\y) -- (6.0,\\y);
    \\draw[line width=1pt] (-0.08,\\y) -- (0.08,\\y) node[left=2pt] {$\\lbl$};
}
\\node[below left] at (0,0) {$0$};
\\draw[line width=1pt] (0.7,0) rectangle (1.3,%s);
\\node[above] at (1,%s) {$%s$};
\\node[below] at (1,0) {$S$};
\\draw[line width=1pt] (1.8,0) rectangle (2.4,%s);
\\node[above] at (2.1,%s) {$%s$};
\\node[below] at (2.1,0) {$M$};
\\draw[line width=1pt] (2.9,0) rectangle (3.5,%s);
\\node[above] at (3.2,%s) {$%s$};
\\node[below] at (3.2,0) {$L$};
\\draw[line width=1pt] (4.0,0) rectangle (4.6,%s);
\\node[above] at (4.3,%s) {$%s$};
\\node[below] at (4.3,0) {$XL$};
\\draw[line width=1pt] (5.1,0) rectangle (5.7,%s);
\\node[above] at (5.4,%s) {$%s$};
\\node[below] at (5.4,0) {$XXL$};
\\end{tikzpicture}
\\end{center}''' % (yS, yS, fS, yM, yM, fM, yL, yL, fL, yXL, yXL, fXL, yXXL, yXXL, fXXL))
        
        ######################################################################## Mệnh đề a ############################################################################
        nb_da_1_d = '\\True ' + ('Tổng số áo cửa hàng bán được trong tuần là $100$ chiếc')
        nb_da_1_s = ('Tổng số áo cửa hàng bán được trong tuần là $90$ chiếc')
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        
        ######################################################################## Mệnh đề b ############################################################################
        th_da_1_d = '\\True ' + ('Hai cỡ áo bán chạy nhất chiếm $63\\%%$ tổng số áo bán ra')
        th_da_1_s = ('Hai cỡ áo bán chạy nhất chiếm $50\\%%$ tổng số áo bán ra')
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        
        ######################################################################## Mệnh đề c ############################################################################
        vd_da_1_d = '\\True ' + ('Nếu tuần tới cửa hàng nhập về $300$ chiếc áo theo đúng tỉ lệ tần số của tuần này thì cần nhập $84$ chiếc cỡ $L$')
        vd_da_1_s = ('Nếu tuần tới cửa hàng nhập về $300$ chiếc áo theo đúng tỉ lệ tần số của tuần này thì cần nhập $90$ chiếc cỡ $L$')
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        
        ######################################################################## Mệnh đề d ############################################################################
        vdc_da_1_d = '\\True ' + ('Cỡ $XXL$ có tần số thấp nhất nên cửa hàng nên nhập với số lượng ít nhất để phục vụ nhóm khách hàng đặc thù')
        vdc_da_1_s = ('Cỡ $XXL$ có tần số thấp nhất nên cửa hàng cần ngừng kinh doanh hoàn toàn cỡ áo này')
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
        
        loigiai_nb_1 = ('Đúng. Tổng số áo bán ra là $12 + 35 + 28 + 15 + 10 = 100$ (chiếc).') if '\\True' in nb_da_1 else ('Sai. Cộng tần số của cả $5$ cỡ áo ta được $12 + 35 + 28 + 15 + 10 = 100$ (chiếc).')
        loigiai_th_1 = ('Đúng. Hai cỡ bán chạy nhất là $M$ ($35$) và $L$ ($28$), tổng là $35 + 28 = 63$ chiếc, chiếm $63\\%%$.') if '\\True' in th_da_1 else ('Sai. Hai cỡ có tần số lớn nhất là $M$ và $L$ có tổng là $63$ trên $100$ chiếc, chiếm $63\\%%$.')
        loigiai_vd_1 = ('Đúng. Tỉ lệ cỡ $L$ là $28\\%%$, nên trong $300$ chiếc cần nhập $300 \\cdot 28\\%% = 84$ (chiếc).') if '\\True' in vd_da_1 else ('Sai. Cỡ $L$ chiếm $28\\%%$ nên cần nhập $300 \\cdot 28\\%% = 84$ chiếc, không phải $90$ chiếc.')
        loigiai_vdc_1 = ('Đúng. Cỡ $XXL$ vẫn có nhu cầu ($10\\%%$), nên giải pháp hợp lý là nhập số lượng ít nhất thay vì ngừng bán.') if '\\True' in vdc_da_1 else ('Sai. Tần số bằng $10$ cho thấy vẫn có khách hàng mua cỡ $XXL$, không nên loại bỏ hoàn toàn.')
        
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
