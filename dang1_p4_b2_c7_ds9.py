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
from mpl_toolkits.mplot3d import Axes3D


def bt_dang1_p4_b2_c7_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_so = random.choice([(11, 6, 5, 3, 44, 24, 20, 12), (10, 7, 5, 3, 40, 28, 20, 12)])
        m1, m2, m3, m4, f1, f2, f3, f4 = bo_so
        ds = ['CK']*m1 + ['TM']*m2 + ['VT']*m3 + ['QT']*m4
        random.shuffle(ds)
        chuoi_ds = ', '.join(ds)

        noidungcauhoi = (
            'Khảo sát phương thức thanh toán của $25$ khách hàng đầu tiên trong ngày tại một cửa hàng tiện lợi, nhân viên thu ngân ghi lại kết quả như sau (CK: Chuyển khoản; TM: Tiền mặt; VT: Ví điện tử; QT: Quẹt thẻ):\\\\ '
            '\\textit{%s}.\\\\ '
            'a) Lập bảng tần số và bảng tần số tương đối cho dãy dữ liệu trên.\\\\ '
            'b) Phương thức thanh toán nào được khách hàng sử dụng phổ biến nhất? Giải thích.'
        ) % (chuoi_ds)

        loigiai = (
            '\\begin{enumEX}[a)]{1}\n'
            '\\item Tổng số khách hàng được khảo sát là $n = 25$. Đếm trong dãy dữ liệu trên ta được tần số của CK, TM, VT, QT lần lượt là $%s; %s; %s; %s$.\\\\ '
            'Các tần số tương đối tương ứng lần lượt là:\\\\ '
            '$f_1 = \\frac{%s}{25} \\cdot 100\\%% = %s\\%%$; $f_2 = \\frac{%s}{25} \\cdot 100\\%% = %s\\%%$; $f_3 = \\frac{%s}{25} \\cdot 100\\%% = %s\\%%$; $f_4 = \\frac{%s}{25} \\cdot 100\\%% = %s\\%%$.\\\\ '
            'Ta có bảng tần số và bảng tần số tương đối sau:\\\\ '
            '\\begin{center}\n'
            '\\begin{tabular}{|l|c|c|c|c|}\n'
            '\\hline\n'
            'Phương thức & CK & TM & VT & QT \\\\ \n'
            '\\hline\n'
            'Tần số & $%s$ & $%s$ & $%s$ & $%s$ \\\\ \n'
            '\\hline\n'
            'Tần số tương đối & $%s\\%%$ & $%s\\%%$ & $%s\\%%$ & $%s\\%%$ \\\\ \n'
            '\\hline\n'
            '\\end{tabular}\n'
            '\\end{center}\n'
            '\\item Phương thức \\textbf{Chuyển khoản (CK)} được khách hàng sử dụng phổ biến nhất vì có tần số tương đối cao nhất ($%s\\%%$).\n'
            '\\end{enumEX}'
        ) % (m1, m2, m3, m4, m1, f1, m2, f2, m3, f3, m4, f4, m1, m2, m3, m4, f1, f2, f3, f4, f1)
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
