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


def bt_dang17_p2_b1_c7_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        f1, f2, f3, f4, f5 = 42, 28, 35, 65, 50
        noidungcauhoi = ('''Một phòng khám nha khoa thống kê số lượt bệnh nhân đến khám theo từng khung giờ trong $10$ ngày làm việc và lập được bảng tần số:
\\begin{center}
\\begin{tabular}{|c|c|c|c|c|c|}
\\hline
Khung giờ & $8\\text{h}$–$10\\text{h}$ & $10\\text{h}$–$12\\text{h}$ & $14\\text{h}$–$16\\text{h}$ & $16\\text{h}$–$18\\text{h}$ & $18\\text{h}$–$20\\text{h}$ \\\\
\\hline
Số lượt bệnh nhân & $42$ & $28$ & $35$ & $65$ & $50$ \\\\
\\hline
\\end{tabular}
\\end{center}''')
        
        ######################################################################## Mệnh đề a ############################################################################
        nb_da_1_d = '\\True ' + ('Cỡ mẫu của cuộc thống kê này là $220$ lượt bệnh nhân')
        nb_da_1_s = ('Cỡ mẫu của cuộc thống kê này là $210$ lượt bệnh nhân')
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        
        ######################################################################## Mệnh đề b ############################################################################
        th_da_1_d = '\\True ' + ('Khung giờ cao điểm nhất là $16\\text{h}$–$18\\text{h}$ với tần số chiếm gần $30\\%$ tổng số lượt khám')
        th_da_1_s = ('Khung giờ cao điểm nhất là $18\\text{h}$–$20\\text{h}$ với tần số chiếm $25\\%$ tổng số lượt khám')
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        
        ######################################################################## Mệnh đề c ############################################################################
        vd_da_1_d = '\\True ' + ('Tổng số lượt bệnh nhân khám vào buổi sáng ($8\\text{h}$–$12\\text{h}$) nhiều hơn buổi tối ($18\\text{h}$–$20\\text{h}$) là $20$ lượt')
        vd_da_1_s = ('Tổng số lượt bệnh nhân khám vào buổi sáng ($8\\text{h}$–$12\\text{h}$) nhiều hơn buổi tối ($18\\text{h}$–$20\\text{h}$) là $15$ lượt')
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        
        ######################################################################## Mệnh đề d ############################################################################
        vdc_da_1_d = '\\True ' + ('Để giảm tải ùn ứ, phòng khám cần tăng cường thêm bác sĩ trực vào khung giờ $16\\text{h}$–$18\\text{h}$ và $18\\text{h}$–$20\\text{h}$')
        vdc_da_1_s = ('Phòng khám cần tập trung toàn bộ bác sĩ vào khung giờ $10\\text{h}$–$12\\text{h}$ vì đây là lúc đông nhất')
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
        
        loigiai_nb_1 = ('Đúng. Tổng số lượt bệnh nhân là $42 + 28 + 35 + 65 + 50 = 220$ (lượt).') if '\\True' in nb_da_1 else ('Sai. Cộng tần số của cả $5$ khung giờ ta được $42 + 28 + 35 + 65 + 50 = 220$ (lượt).')
        loigiai_th_1 = ('Đúng. Khung giờ $16\\text{h}$–$18\\text{h}$ có tần số cao nhất ($65$ lượt), chiếm $\\dfrac{65}{220} \\cdot 100\\% \\approx 29,5\\%$.') if '\\True' in th_da_1 else ('Sai. Khung giờ $16\\text{h}$–$18\\text{h}$ mới có tần số cao nhất ($65$ lượt), chiếm khoảng $29,5\\%$.')
        loigiai_vd_1 = ('Đúng. Buổi sáng có $42 + 28 = 70$ lượt, nhiều hơn buổi tối ($50$ lượt) là $70 - 50 = 20$ (lượt).') if '\\True' in vd_da_1 else ('Sai. Tổng số lượt khám buổi sáng là $42 + 28 = 70$ lượt, nhiều hơn buổi tối $70 - 50 = 20$ lượt.')
        loigiai_vdc_1 = ('Đúng. Hai khung giờ $16\\text{h}$–$18\\text{h}$ ($65$ lượt) và $18\\text{h}$–$20\\text{h}$ ($50$ lượt) có tần số cao nhất nên cần tăng cường nhân lực.') if '\\True' in vdc_da_1 else ('Sai. Khung giờ $10\\text{h}$–$12\\text{h}$ có tần số thấp nhất ($28$ lượt), đông nhất là từ $16\\text{h}$ đến $20\\text{h}$.')
        
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
