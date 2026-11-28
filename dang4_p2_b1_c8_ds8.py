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


def bt_dang4_p2_b1_c8_ds8(self):
    # Dạng 4: Chọn ngẫu nhiên 1 học sinh từ nhóm gồm 4 lớp khác nhau
    while True:
        c1, c2, c3, c4 = random.randint(3, 6), random.randint(3, 6), random.randint(5, 8), random.randint(2, 4)
        if c3 > max(c1, c2, c4):
            break
    tong = c1 + c2 + c3 + c4
    noidungcauhoi = (f"Một nhóm tình nguyện viên bảo vệ môi trường gồm ${tong}$ bạn học sinh: ${c1}$ bạn lớp 8A1, ${c2}$ bạn lớp 8A2, ${c3}$ bạn lớp 8A3 và ${c4}$ bạn lớp 8A4. Ban tổ chức chọn ngẫu nhiên $1$ bạn làm nhóm trưởng.")

    # Nhận biết
    nb_da_1_d = f"\\True Nếu kí hiệu các bạn theo từng lớp, ta liệt kê được ${tong}$ kết quả có thể."
    nb_da_1_s = f"Vì chỉ có $4$ lớp tham gia nên có $4$ kết quả có thể xảy ra."
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (f"Mỗi bạn học sinh trong nhóm được chọn là một kết quả riêng biệt. Tổng có ${c1} + {c2} + {c3} + {c4} = {tong}$ bạn nên có ${tong}$ kết quả có thể.")

    # Thông hiểu (biến cố hợp)
    hop = c2 + c4
    th_da_1_d = f"\\True Biến cố \\textit{{``Bạn được chọn học lớp 8A2 hoặc 8A4''}} có ${hop}$ kết quả thuận lợi."
    th_da_1_s = f"Biến cố \\textit{{``Bạn được chọn học lớp 8A2 hoặc 8A4''}} có ${abs(c2 - c4) + 1}$ kết quả thuận lợi."
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (f"Tổng số học sinh lớp 8A2 và 8A4 là ${c2} + {c4} = {hop}$ bạn nên có ${hop}$ kết quả thuận lợi.")

    # Vận dụng 1 (biến cố phủ định)
    not_8a3 = tong - c3
    vd_da_1_d = f"\\True Số kết quả thuận lợi cho biến cố \\textit{{``Bạn được chọn không học lớp 8A3''}} là ${not_8a3}$."
    vd_da_1_s = f"Số kết quả thuận lợi cho biến cố \\textit{{``Bạn được chọn không học lớp 8A3''}} là ${c3}$."
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (f"Số học sinh không học lớp 8A3 là ${tong} - {c3} = {not_8a3}$ bạn nên có ${not_8a3}$ kết quả thuận lợi.")

    # Vận dụng 2 (so sánh số lượng)
    vdc_da_1_d = f"\\True Biến cố \\textit{{``Bạn được chọn thuộc lớp có nhiều tình nguyện viên nhất''}} có ${c3}$ kết quả thuận lợi."
    vdc_da_1_s = f"Biến cố \\textit{{``Bạn được chọn thuộc lớp có nhiều tình nguyện viên nhất''}} có ${c1}$ kết quả thuận lợi."
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (f"Lớp có nhiều tình nguyện viên nhất là lớp 8A3 với ${c3}$ bạn nên có ${c3}$ kết quả thuận lợi.")

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
