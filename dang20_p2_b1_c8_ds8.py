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


def bt_dang20_p2_b1_c8_ds8(self):
    # Dạng 20: Chọn ngẫu nhiên thành viên theo số thứ tự quy ước chẵn/lẻ kết hợp điều kiện chia hết/so sánh
    N = random.choice([12, 14, 16])
    nu = [i for i in range(1, N + 1) if i % 2 == 0]
    nam = [i for i in range(1, N + 1) if i % 2 == 1]
    moc = N - 5
    nam_lon = [i for i in nam if i > moc]
    nu_sai = [i for i in nu if i > moc]
    nu_div3 = [i for i in nu if i % 3 == 0]

    str_nam_lon = "; ".join(map(str, nam_lon))
    str_nu_sai = "; ".join(map(str, nu_sai))
    str_nu_div3 = "; ".join(map(str, nu_div3))

    noidungcauhoi = (f"Bảng điểm thi đua của lớp 8B có ${N}$ tổ viên của Tổ $1$ được đánh số thứ tự từ $1$ đến ${N}$. Giáo viên chủ nhiệm chọn ngẫu nhiên $1$ bạn trong tổ để kiểm tra vở bài tập. Biết các bạn có số thứ tự là số lẻ là nam, các bạn có số thứ tự là số chẵn là nữ.")

    # Nhận biết
    nb_da_1_d = f"\\True Có ${N}$ kết quả có thể của hành động chọn này."
    nb_da_1_s = f"Có ${N - 1}$ kết quả có thể của hành động chọn này."
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (f"Có ${N}$ tổ viên được đánh số thứ tự từ $1$ đến ${N}$ nên có ${N}$ kết quả có thể.")

    # Thông hiểu
    th_da_1_d = f"\\True Biến cố \\textit{{``Giáo viên chọn được một bạn nữ''}} có ${len(nu)}$ kết quả thuận lợi."
    th_da_1_s = f"Biến cố \\textit{{``Giáo viên chọn được một bạn nữ''}} có ${len(nu) - 1}$ kết quả thuận lợi."
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (f"Từ $1$ đến ${N}$ có ${len(nu)}$ số chẵn nên có ${len(nu)}$ bạn nữ. Vậy có ${len(nu)}$ kết quả thuận lợi.")

    # Vận dụng 1
    vd_da_1_d = f"\\True Biến cố \\textit{{``Giáo viên chọn được một bạn nam có số thứ tự lớn hơn ${moc}$''}} có ${len(nam_lon)}$ kết quả thuận lợi là ${str_nam_lon}$."
    vd_da_1_s = f"Biến cố \\textit{{``Giáo viên chọn được một bạn nam có số thứ tự lớn hơn ${moc}$''}} có ${len(nu_sai)}$ kết quả thuận lợi là ${str_nu_sai}$."
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (f"Bạn nam có số thứ tự là số lẻ, kết hợp điều kiện lớn hơn ${moc}$ ta được các số ${str_nam_lon}$ (các số ${str_nu_sai}$ là số chẵn nên là bạn nữ). Có ${len(nam_lon)}$ kết quả thuận lợi.")

    # Vận dụng 2
    vdc_da_1_d = f"\\True Số kết quả thuận lợi cho biến cố \\textit{{``Giáo viên chọn được một bạn nữ có số thứ tự chia hết cho $3$''}} là ${len(nu_div3)}$."
    vdc_da_1_s = f"Số kết quả thuận lợi cho biến cố \\textit{{``Giáo viên chọn được một bạn nữ có số thứ tự chia hết cho $3$''}} là ${len(nu_div3) + 1}$."
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (f"Bạn nữ có số thứ tự chẵn và chia hết cho $3$ tức là số thứ tự chia hết cho $6$. Từ $1$ đến ${N}$ có ${len(nu_div3)}$ số là ${str_nu_div3}$. Vậy có ${len(nu_div3)}$ kết quả thuận lợi.")

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

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\choiceTFn \n'
               '{' + str(nb_da_1) + '}\n'
               '{' + str(th_da_1) + '}\n'
               '{' + str(vd_da_1) + '}\n'
               '{' + str(vdc_da_1) + '}\n'
               '\\loigiai{ \n'
               '\\begin{enumEX}[a)]{1} \n'
               '\\item ' + str(loigiai_nb_1) + '\n'
               '\\item ' + str(loigiai_th_1) + '\n'
               '\\item ' + str(loigiai_vd_1) + '\n'
               '\\item ' + str(loigiai_vdc_1) + '\n'
               '\\end{enumEX}} \n'
               '\\end{ex}\n \\end{minipage}\n\n')
    return content
