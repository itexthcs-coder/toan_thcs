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


def bt_dang9_p2_b1_c8_ds8(self):
    # Dạng 9: Phép thử có đánh số kết hợp điều kiện kép (loại vật phẩm và tính chẵn/lẻ)
    cau_hinh = [
        (8, [1, 4, 7], [2, 5], [3, 6, 8]),
        (9, [1, 4, 7], [2, 5, 8], [3, 6, 9]),
        (10, [1, 4, 7, 10], [2, 5, 8], [3, 6, 9])
    ]
    N, vang, trang_bi, trong = random.choice(cau_hinh)
    str_vang = "; ".join(map(str, vang))
    str_tb = "; ".join(map(str, trang_bi))
    str_trong = "; ".join(map(str, trong))
    trong_chan = [x for x in trong if x % 2 == 0]
    vang_le = [x for x in vang if x % 2 == 1]
    str_trong_chan = "; ".join(map(str, trong_chan))
    str_vang_le = "; ".join(map(str, vang_le))
    so_vp = len(vang) + len(trang_bi)

    noidungcauhoi = (f"Trong một trò chơi điện tử, người chơi mở ngẫu nhiên $1$ rương báu từ ${N}$ rương đóng kín được đánh số từ $1$ đến ${N}$. Biết rương số ${str_vang}$ chứa vàng; rương số ${str_tb}$ chứa trang bị; rương số ${str_trong}$ là rương trống.")

    # Nhận biết
    nb_da_1_d = f"\\True Có ${N}$ kết quả có thể khi mở rương."
    nb_da_1_s = f"Có $3$ kết quả có thể khi mở rương."
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (f"Người chơi chọn $1$ trong ${N}$ rương đánh số từ $1$ đến ${N}$ nên có ${N}$ kết quả có thể.")

    # Thông hiểu
    th_da_1_d = f"\\True Số kết quả thuận lợi cho biến cố \\textit{{``Người chơi mở được rương có vật phẩm (vàng hoặc trang bị)''}} là ${so_vp}$."
    th_da_1_s = f"Số kết quả thuận lợi cho biến cố \\textit{{``Người chơi mở được rương có vật phẩm (vàng hoặc trang bị)''}} là ${len(trong)}$."
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (f"Có ${len(vang)}$ rương chứa vàng và ${len(trang_bi)}$ rương chứa trang bị nên có ${len(vang)} + {len(trang_bi)} = {so_vp}$ kết quả thuận lợi.")

    # Vận dụng 1
    vd_da_1_d = f"\\True Biến cố \\textit{{``Người chơi mở được rương trống mang số chẵn''}} có ${len(trong_chan)}$ kết quả thuận lợi."
    vd_da_1_s = f"Biến cố \\textit{{``Người chơi mở được rương trống mang số chẵn''}} có ${len(trong)}$ kết quả thuận lợi."
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (f"Trong các rương trống (${str_trong}$), các rương mang số chẵn là ${str_trong_chan}$. Vậy có ${len(trong_chan)}$ kết quả thuận lợi.")

    # Vận dụng 2
    vdc_da_1_d = f"\\True Các kết quả thuận lợi cho biến cố \\textit{{``Người chơi mở được rương chứa vàng mang số lẻ''}} là rương số ${str_vang_le}$."
    vdc_da_1_s = f"Các kết quả thuận lợi cho biến cố \\textit{{``Người chơi mở được rương chứa vàng mang số lẻ''}} là rương số ${str_vang}$."
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (f"Trong các rương chứa vàng (${str_vang}$), các rương mang số lẻ là ${str_vang_le}$. Vậy có ${len(vang_le)}$ kết quả thuận lợi.")

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
