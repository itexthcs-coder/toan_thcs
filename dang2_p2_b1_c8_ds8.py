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


def bt_dang2_p2_b1_c8_ds8(self):
    # Dạng 2: Xác định kết quả có thể và kết quả thuận lợi trên vòng quay số tự nhiên từ 1 đến N
    N = random.choice([8, 10, 12])
    primes = [i for i in range(1, N + 1) if i > 1 and all(i % d != 0 for d in range(2, int(i**0.5) + 1))]
    divisors = [i for i in range(1, N + 1) if N % i == 0]
    str_primes = "; ".join(map(str, primes))
    str_divisors = "; ".join(map(str, divisors))
    str_divisors_sai = "; ".join(map(str, divisors[:-1]))

    noidungcauhoi = (f"Vòng quay may mắn của một siêu thị được chia thành ${N}$ phần bằng nhau, ghi các số tự nhiên từ $1$ đến ${N}$. Khách hàng quay kim một lần và quan sát số ở phần kim chỉ vào (nếu kim chỉ vào vạch phân chia thì quay lại).")

    # Nhận biết
    nb_da_1_d = f"\\True Có ${N}$ kết quả có thể của thực nghiệm này."
    nb_da_1_s = f"Có ${N - 1}$ kết quả có thể của thực nghiệm này."
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (f"Kim có thể chỉ vào một trong ${N}$ phần ghi các số từ $1$ đến ${N}$ nên có ${N}$ kết quả có thể.")

    # Thông hiểu
    th_da_1_d = f"\\True Biến cố \\textit{{``Kim chỉ vào phần ghi số nguyên tố''}} có ${len(primes)}$ kết quả thuận lợi là ${str_primes}$."
    th_da_1_s = f"Biến cố \\textit{{``Kim chỉ vào phần ghi số nguyên tố''}} có ${len(primes) + 1}$ kết quả thuận lợi là $1; {str_primes}$."
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (f"Từ $1$ đến ${N}$, các số nguyên tố là ${str_primes}$ (lưu ý số $1$ không phải số nguyên tố). Vậy có ${len(primes)}$ kết quả thuận lợi.")

    # Vận dụng 1
    vd_da_1_d = f"\\True Các kết quả thuận lợi cho biến cố \\textit{{``Kim chỉ vào phần ghi số là ước của ${N}$''}} là ${str_divisors}$."
    vd_da_1_s = f"Các kết quả thuận lợi cho biến cố \\textit{{``Kim chỉ vào phần ghi số là ước của ${N}$''}} là ${str_divisors_sai}$."
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (f"Trong các số từ $1$ đến ${N}$, các ước của ${N}$ là ${str_divisors}$. Vậy có ${len(divisors)}$ kết quả thuận lợi.")

    # Vận dụng 2 (biến cố không thể)
    vdc_da_1_d = f"\\True Biến cố \\textit{{``Kim chỉ vào phần ghi số lớn hơn ${N}$''}} không có kết quả thuận lợi nào."
    vdc_da_1_s = f"Biến cố \\textit{{``Kim chỉ vào phần ghi số lớn hơn ${N}$''}} có $1$ kết quả thuận lợi là ${N}$."
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (f"Vòng quay chỉ ghi các số từ $1$ đến ${N}$ nên không thể xảy ra trường hợp kim chỉ vào số lớn hơn ${N}$. Vậy biến cố này có $0$ kết quả thuận lợi.")

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
