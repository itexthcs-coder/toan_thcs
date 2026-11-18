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


def bt_dang8_p2_b1_c7_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        f1 = random.choice([20, 24, 28])
        f2 = random.choice([32, 36, 40])
        f3 = 80 - f1 - f2 - 5
        f4 = 5
        tu_hl = f1 + f2
        noidungcauhoi = ('''Khảo sát mức độ hài lòng của khách hàng tại một siêu thị theo $4$ mức, thu được bảng tần số:
\\begin{center}
\\begin{tabular}{|c|c|c|c|c|}
\\hline
Mức độ & Rất hài lòng & Hài lòng & Bình thường & Không hài lòng \\\\
\\hline
Tần số & $%s$ & $%s$ & $%s$ & $%s$ \\\\
\\hline
\\end{tabular}
\\end{center}''' % (f1, f2, f3, f4))
        
        ######################################################################## Mệnh đề a ############################################################################
        nb_da_1_d = '\\True ' + ('Mẫu dữ liệu trên có $80$ khách hàng tham gia đánh giá')
        nb_da_1_s = ('Mẫu dữ liệu trên có $75$ khách hàng tham gia đánh giá')
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        
        ######################################################################## Mệnh đề b ############################################################################
        th_da_1_d = '\\True ' + ('Giá trị ``Hài lòng'' có tần số lớn nhất')
        th_da_1_s = ('Giá trị ``Rất hài lòng'' có tần số lớn nhất')
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        
        ######################################################################## Mệnh đề c ############################################################################
        vd_da_1_d = '\\True ' + ('Tỉ lệ khách hàng đánh giá ``Không hài lòng'' chiếm $6,25\\%%$ tổng số khách hàng')
        vd_da_1_s = ('Tỉ lệ khách hàng đánh giá ``Không hài lòng'' chiếm $5\\%%$ tổng số khách hàng')
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        
        ######################################################################## Mệnh đề d ############################################################################
        vdc_da_1_d = '\\True ' + ('Có $%s$ khách hàng đánh giá từ mức ``Hài lòng'' trở lên' % tu_hl)
        vdc_da_1_s = ('Có $%s$ khách hàng đánh giá từ mức ``Hài lòng'' trở lên' % f2)
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
        
        loigiai_nb_1 = ('Đúng. Cỡ mẫu bằng $%s + %s + %s + %s = 80$ (khách hàng).' % (f1, f2, f3, f4)) if '\\True' in nb_da_1 else ('Sai. Tổng số khách hàng tham gia đánh giá là $%s + %s + %s + %s = 80$.' % (f1, f2, f3, f4))
        loigiai_th_1 = ('Đúng. Mức ``Hài lòng'' có tần số bằng $%s$, lớn nhất trong $4$ mức.' % f2) if '\\True' in th_da_1 else ('Sai. Mức ``Hài lòng'' có tần số $%s$ lớn hơn ``Rất hài lòng'' ($%s$).' % (f2, f1))
        loigiai_vd_1 = ('Đúng. Tỉ lệ khách hàng không hài lòng là $\\dfrac{5}{80} \\cdot 100\\%% = 6,25\\%%$.') if '\\True' in vd_da_1 else ('Sai. Có $5$ trên $80$ khách hàng không hài lòng, chiếm $\\dfrac{5}{80} \\cdot 100\\%% = 6,25\\%%$, không phải $5\\%%$.')
        loigiai_vdc_1 = ('Đúng. Số khách hàng đánh giá ``Hài lòng'' hoặc ``Rất hài lòng'' là $%s + %s = %s$.' % (f1, f2, tu_hl)) if '\\True' in vdc_da_1 else ('Sai. Cần cộng cả hai mức ``Hài lòng'' và ``Rất hài lòng'': $%s + %s = %s$ (khách hàng).' % (f1, f2, tu_hl))
        
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
