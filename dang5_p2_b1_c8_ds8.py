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


def bt_dang5_p2_b1_c8_ds8(self):
    # Dạng 5: Gieo đồng thời hai đồng xu cân đối và đồng chất
    mat_chon = random.choice([('ngửa', 'N', 'SN; NS; NN'), ('sấp', 'S', 'SS; SN; NS')])
    ten_mat, ki_hieu, kq_it_nhat = mat_chon
    mat_thu_nhat = random.choice([('sấp', 'SS và SN'), ('ngửa', 'NN và NS')])
    ten_m1, kq_m1 = mat_thu_nhat

    noidungcauhoi = ("Gieo đồng thời hai đồng xu cân đối và đồng chất (mỗi đồng xu có một mặt sấp kí hiệu là $S$ và một mặt ngửa kí hiệu là $N$). Quan sát mặt xuất hiện của cả hai đồng xu.")

    # Nhận biết
    nb_da_1_d = "\\True Các kết quả có thể của thực nghiệm này là $SS; SN; NS; NN$."
    nb_da_1_s = "Các kết quả có thể của thực nghiệm này là $SS; SN; NN$."
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    loigiai_nb_1 = ("Khi gieo hai đồng xu, có $4$ kết quả có thể phân biệt theo thứ tự đồng xu thứ nhất và thứ hai là: $SS; SN; NS; NN$.")

    # Thông hiểu
    th_da_1_d = f"\\True Có $3$ kết quả thuận lợi cho biến cố \\textit{{``Có ít nhất một đồng xu xuất hiện mặt {ten_mat}''}}."
    th_da_1_s = f"Có $2$ kết quả thuận lợi cho biến cố \\textit{{``Có ít nhất một đồng xu xuất hiện mặt {ten_mat}''}}."
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    loigiai_th_1 = (f"Các kết quả có ít nhất một mặt {ten_mat} là ${kq_it_nhat}$. Vậy có $3$ kết quả thuận lợi.")

    # Vận dụng 1
    vd_da_1_d = "\\True Biến cố \\textit{``Hai đồng xu xuất hiện hai mặt giống nhau''} có $2$ kết quả thuận lợi."
    vd_da_1_s = "Biến cố \\textit{``Hai đồng xu xuất hiện hai mặt giống nhau''} có $1$ kết quả thuận lợi."
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    loigiai_vd_1 = ("Hai đồng xu xuất hiện hai mặt giống nhau gồm $2$ kết quả thuận lợi là $SS$ và $NN$.")

    # Vận dụng 2
    vdc_da_1_d = f"\\True Số kết quả thuận lợi cho biến cố \\textit{{``Đồng xu thứ nhất xuất hiện mặt {ten_m1}''}} là $2$."
    vdc_da_1_s = f"Số kết quả thuận lợi cho biến cố \\textit{{``Đồng xu thứ nhất xuất hiện mặt {ten_m1}''}} là $1$."
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    loigiai_vdc_1 = (f"Đồng xu thứ nhất xuất hiện mặt {ten_m1} gồm $2$ kết quả thuận lợi là ${kq_m1}$.")

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
