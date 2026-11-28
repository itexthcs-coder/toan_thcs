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


def bt_dang8_p2_b1_c8_ds8(self):
    # Dạng 8: Xét tập kết quả thuận lợi trùng nhau và tính bất biến khi thay đổi nhóm khác
    t = random.randint(3, 5)
    x_ao = random.randint(4, 6)
    d = random.randint(2, 4)
    tong = t + x_ao + d
    str_t = ", ".join([f"T_{i}" for i in range(1, t + 1)])
    str_x = ", ".join([f"X_{i}" for i in range(1, x_ao + 1)])
    str_d = ", ".join([f"D_{i}" for i in range(1, d + 1)])

    noidungcauhoi = (f"Một cửa hàng thời trang treo ${tong}$ chiếc áo sơ mi cùng kiểu trên một giá: ${t}$ chiếc màu trắng (kí hiệu ${str_t}$), ${x_ao}$ chiếc màu xanh (kí hiệu ${str_x}$) và ${d}$ chiếc màu đen (kí hiệu ${str_d}$). Khách hàng lấy ngẫu nhiên một chiếc áo.")

    # Nhận biết
    nb_da_1_d = f"\\True Có ${tong}$ kết quả có thể của hành động trên."
    nb_da_1_s = f"Có $3$ kết quả có thể của hành động trên."
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (f"Có ${t} + {x_ao} + {d} = {tong}$ chiếc áo phân biệt được kí hiệu nên có ${tong}$ kết quả có thể.")

    # Thông hiểu
    hop_td = t + d
    th_da_1_d = f"\\True Biến cố \\textit{{``Khách lấy được áo màu trắng hoặc màu đen''}} có ${hop_td}$ kết quả thuận lợi."
    th_da_1_s = f"Biến cố \\textit{{``Khách lấy được áo màu trắng hoặc màu đen''}} có ${abs(t - d) + 1}$ kết quả thuận lợi."
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (f"Các kết quả thuận lợi là ${str_t}, {str_d}$. Tổng cộng có ${t} + {d} = {hop_td}$ kết quả thuận lợi.")

    # Vận dụng 1
    vd_da_1_d = "\\True Tập hợp các kết quả thuận lợi cho biến cố \\textit{``Khách không lấy được áo màu xanh''} trùng với tập hợp các kết quả thuận lợi cho biến cố \\textit{``Khách lấy được áo màu trắng hoặc màu đen''}."
    vd_da_1_s = "Tập hợp các kết quả thuận lợi cho biến cố \\textit{``Khách không lấy được áo màu xanh''} chỉ gồm các chiếc áo màu trắng."
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (f"Áo không phải màu xanh thì phải là áo màu trắng hoặc màu đen. Vì vậy hai biến cố có cùng tập hợp kết quả thuận lợi là $\\{{{str_t}, {str_d}\\}}$ gồm ${hop_td}$ phần tử.")

    # Vận dụng 2
    ban_bot = random.randint(1, 2)
    vdc_da_1_d = f"\\True Nếu cửa hàng bán bớt ${ban_bot}$ chiếc áo màu xanh thì số kết quả thuận lợi cho biến cố \\textit{{``Khách lấy được áo màu trắng''}} vẫn là ${t}$."
    vdc_da_1_s = f"Nếu cửa hàng bán bớt ${ban_bot}$ chiếc áo màu xanh thì số kết quả thuận lợi cho biến cố \\textit{{``Khách lấy được áo màu trắng''}} giảm đi ${ban_bot}$."
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (f"Việc bán bớt áo màu xanh chỉ làm giảm tổng số áo trên giá (tổng số kết quả có thể) chứ không làm thay đổi số áo màu trắng. Do đó số kết quả thuận lợi cho biến cố lấy được áo trắng vẫn là ${t}$.")

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
