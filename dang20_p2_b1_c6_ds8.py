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


def bt_dang20_p2_b1_c6_ds8(self):
    # Dạng 20: Mô hình hóa bài toán kinh tế - chi phí trung bình trên một sản phẩm
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        scenarios = [
            ('15\\,000\\,000', '80\\,000', 300, '130\\,000', '50\\,000'),
            ('12\\,000\\,000', '60\\,000', 400, '90\\,000', '30\\,000'),
            ('20\\,000\\,000', '100\\,000', 500, '140\\,000', '40\\,000')
        ]
        cp_cd, cp_sp, x0, cp_tb, cp_cd_tb = random.choice(scenarios)
        
        noidungcauhoi = ('Một cơ sở sản xuất thủ công mỹ nghệ có chi phí cố định hằng tháng (tiền thuê mặt bằng, điện nước, khấu hao máy móc) là $%s$ đồng và chi phí nguyên vật liệu, nhân công trực tiếp cho mỗi sản phẩm là $%s$ đồng. Gọi $x$ là số sản phẩm cơ sở sản xuất được trong một tháng ($x \\in \\mathbb{N}^*$). Xét tính đúng sai của các khẳng định sau:'
                         % (cp_cd, cp_sp))
        
        nb_da_1_d = '\\True Tổng chi phí để sản xuất $x$ sản phẩm trong một tháng là $%s + %sx$ (đồng)' % (cp_cd, cp_sp)
        nb_da_1_s = 'Tổng chi phí để sản xuất $x$ sản phẩm trong một tháng là $%sx + %s$ (đồng)' % (cp_cd, cp_sp)
        list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
        loigiai_nb_d = 'Đúng. Tổng chi phí gồm chi phí cố định $%s$ đồng cộng với chi phí biến đổi cho $x$ sản phẩm là $%sx$ đồng.' % (cp_cd, cp_sp)
        loigiai_nb_s = 'Sai. Chi phí cố định $%s$ đồng không nhân với $x$, chỉ có chi phí mỗi sản phẩm $%s$ đồng mới nhân với $x$.' % (cp_cd, cp_sp)
        
        th_da_1_d = '\\True Phân thức biểu thị chi phí trung bình để sản xuất một sản phẩm là $\\dfrac{%s + %sx}{x}$ (đồng)' % (cp_cd, cp_sp)
        th_da_1_s = 'Phân thức biểu thị chi phí trung bình để sản xuất một sản phẩm là $\\dfrac{x}{%s + %sx}$ (đồng)' % (cp_cd, cp_sp)
        list_th_da_1 = [th_da_1_d, th_da_1_s]
        loigiai_th_d = 'Đúng. Chi phí trung bình cho một sản phẩm bằng tổng chi phí chia cho tổng số sản phẩm $x$: $\\dfrac{%s + %sx}{x}$ (đồng).' % (cp_cd, cp_sp)
        loigiai_th_s = 'Sai. Phải lấy tổng chi phí chia cho số sản phẩm $x$, tức là $\\dfrac{%s + %sx}{x}$ (đồng).' % (cp_cd, cp_sp)
        
        vd_da_1_d = '\\True Khi sản xuất $%s$ sản phẩm trong một tháng, chi phí trung bình cho mỗi sản phẩm là $%s$ đồng' % (x0, cp_tb)
        vd_da_1_s = 'Khi sản xuất $%s$ sản phẩm trong một tháng, chi phí trung bình cho mỗi sản phẩm là $%s$ đồng' % (x0, cp_cd_tb)
        list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
        loigiai_vd_d = 'Đúng. Thay $x = %s$ vào phân thức chi phí trung bình: $\\dfrac{%s + %s \\cdot %s}{%s} = %s + %s = %s$ (đồng).' % (x0, cp_cd, cp_sp, x0, x0, cp_cd_tb, cp_sp, cp_tb)
        loigiai_vd_s = 'Sai. $%s$ đồng mới chỉ là phần chi phí cố định phân bổ cho một sản phẩm; phải cộng thêm $%s$ đồng chi phí trực tiếp để được $%s$ đồng.' % (cp_cd_tb, cp_sp, cp_tb)
        
        vdc_da_1_d = '\\True Khi số lượng sản phẩm $x$ càng tăng thì chi phí trung bình cho mỗi sản phẩm càng giảm'
        vdc_da_1_s = 'Khi số lượng sản phẩm $x$ càng tăng thì chi phí trung bình cho mỗi sản phẩm càng tăng lên'
        list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
        loigiai_vdc_d = 'Đúng. Ta có $\\dfrac{%s + %sx}{x} = \\dfrac{%s}{x} + %s$. Khi $x$ tăng thì $\\dfrac{%s}{x}$ giảm nên chi phí trung bình giảm.' % (cp_cd, cp_sp, cp_cd, cp_sp, cp_cd)
        loigiai_vdc_s = 'Sai. Vì chi phí cố định $%s$ đồng được chia đều cho nhiều sản phẩm hơn khi $x$ tăng nên chi phí trung bình trên mỗi sản phẩm sẽ giảm dần.' % cp_cd
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

    sol_nb = loigiai_nb_d if '\\True' in nb_da_1 else loigiai_nb_s
    sol_th = loigiai_th_d if '\\True' in th_da_1 else loigiai_th_s
    sol_vd = loigiai_vd_d if '\\True' in vd_da_1 else loigiai_vd_s
    sol_vdc = loigiai_vdc_d if '\\True' in vdc_da_1 else loigiai_vdc_s

    combined = [
        (nb_da_1, sol_nb),
        (th_da_1, sol_th),
        (vd_da_1, sol_vd),
        (vdc_da_1, sol_vdc)
    ]
    random.shuffle(combined)
    shuffled_answers, shuffled_solutions = zip(*combined)

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\choiceTFn \n' +
               '{' + str(shuffled_answers[0]) + '}\n' +
               '{' + str(shuffled_answers[1]) + '}\n' +
               '{' + str(shuffled_answers[2]) + '}\n' +
               '{' + str(shuffled_answers[3]) + '}\n' +
               '\\loigiai{ \n' +
               '\\begin{enumEX}[a)]{1} \n' +
               '\\item ' + str(shuffled_solutions[0]) + '\n' +
               '\\item ' + str(shuffled_solutions[1]) + '\n' +
               '\\item ' + str(shuffled_solutions[2]) + '\n' +
               '\\item ' + str(shuffled_solutions[3]) + '\n' +
               '\\end{enumEX}} \n' +
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
