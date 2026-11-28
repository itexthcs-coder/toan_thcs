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


def bt_dang11_p2_b1_c8_ds8(self):
    # Dạng 11: Rút vật phẩm từ tập hợp dãy số cho trước
    day_list = [
        [2, 3, 5, 7, 8, 9, 11, 13, 15],
        [2, 4, 5, 7, 9, 11, 13, 15, 17, 21],
        [2, 3, 6, 7, 9, 11, 15, 17, 19, 25]
    ]
    day = random.choice(day_list)
    N = len(day)
    str_day = "; ".join(map(str, day))
    primes = [x for x in day if x > 1 and all(x % d != 0 for d in range(2, int(x**0.5) + 1))]
    le_ko_nt = [x for x in day if x % 2 == 1 and x not in primes]
    chans = [x for x in day if x % 2 == 0]
    str_primes = "; ".join(map(str, primes))
    str_le_ko_nt = "; ".join(map(str, le_ko_nt))
    str_chans = "; ".join(map(str, chans))

    noidungcauhoi = (f"Một túi đựng ${N}$ quả bóng bàn có kích thước như nhau được đánh số: ${str_day}$. Rút ngẫu nhiên một quả bóng từ túi.")

    # Nhận biết
    nb_da_1_d = f"\\True Có ${N}$ kết quả có thể xảy ra."
    nb_da_1_s = f"Có ${N - 1}$ kết quả có thể xảy ra."
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = (f"Trong túi có ${N}$ quả bóng được đánh số phân biệt nên có ${N}$ kết quả có thể.")

    # Thông hiểu
    th_da_1_d = f"\\True Số kết quả thuận lợi cho biến cố \\textit{{``Rút được quả bóng ghi số nguyên tố''}} là ${len(primes)}$."
    th_da_1_s = f"Số kết quả thuận lợi cho biến cố \\textit{{``Rút được quả bóng ghi số nguyên tố''}} là ${len(primes) + 1}$."
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (f"Trong dãy số đã cho, các số nguyên tố là ${str_primes}$. Vậy có ${len(primes)}$ kết quả thuận lợi.")

    # Vận dụng 1
    vd_da_1_d = f"\\True Các kết quả thuận lợi cho biến cố \\textit{{``Rút được quả bóng ghi số lẻ nhưng không phải số nguyên tố''}} là ${str_le_ko_nt}$."
    vd_da_1_s = f"Các kết quả thuận lợi cho biến cố \\textit{{``Rút được quả bóng ghi số lẻ nhưng không phải số nguyên tố''}} chỉ có số $9$."
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = (f"Các số lẻ trong dãy nhưng là hợp số (không phải số nguyên tố) gồm ${str_le_ko_nt}$. Có ${len(le_ko_nt)}$ kết quả thuận lợi.")

    # Vận dụng 2
    vdc_da_1_d = f"\\True Biến cố \\textit{{``Rút được quả bóng ghi số chẵn''}} có ${len(chans)}$ kết quả thuận lợi."
    vdc_da_1_s = f"Biến cố \\textit{{``Rút được quả bóng ghi số chẵn''}} có ${len(chans) + 1}$ kết quả thuận lợi."
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (f"Trong dãy số trên, các số chẵn là ${str_chans}$. Vậy có ${len(chans)}$ kết quả thuận lợi.")

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
