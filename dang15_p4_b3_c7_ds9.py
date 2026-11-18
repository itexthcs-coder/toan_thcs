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


def bt_dang15_p4_b3_c7_ds9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n = 150
        m2, m4 = 54, 21
        hieu = random.choice([15, 21, 27])
        tong_xy = n - (m2 + m4)
        x_val = (tong_xy - hieu) // 2
        y_val = (tong_xy + hieu) // 2

        f1 = (x_val * 100) // n
        f2 = (m2 * 100) // n
        f3 = (y_val * 100) // n
        f4 = (m4 * 100) // n
        f_tu_200 = f3 + f4

        noidungcauhoi = ('''Khảo sát mức chi tiêu hằng tháng cho việc mua sách và tài liệu học tập (đơn vị: nghìn đồng) của $%s$ sinh viên thu được bảng tần số ghép nhóm sau:
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Mức chi tiêu (nghìn đồng) & $[0; 100)$ & $[100; 200)$ & $[200; 300)$ & $[300; 400)$ \\\\
\\hline
Số sinh viên & $x$ & $%s$ & $y$ & $%s$ \\\\
\\hline
\\end{tabular}
\\end{center}
Biết rằng số sinh viên thuộc nhóm $[200; 300)$ nhiều hơn số sinh viên thuộc nhóm $[0; 100)$ là $%s$ người.\\
a) Tìm $x$ và $y$, từ đó lập bảng tần số tương đối ghép nhóm.\\
b) Tính tỉ lệ phần trăm sinh viên chi tiêu từ $200$ nghìn đồng trở lên mỗi tháng.''' % (n, m2, m4, hieu))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Vì tổng số sinh viên là $%s$ nên ta có: $x + %s + y + %s = %s \\Leftrightarrow x + y = %s$.\\
Mặt khác, theo đề bài ta có: $y - x = %s$.\\
Giải hệ hai phương trình trên, ta được: $y = \\dfrac{%s + %s}{2} = %s$ và $x = %s - %s = %s$.\\
Ta có bảng tần số tương đối ghép nhóm:
\\begin{center}
\\begin{tabular}{|l|c|c|c|c|}
\\hline
Mức chi tiêu (nghìn đồng) & $[0; 100)$ & $[100; 200)$ & $[200; 300)$ & $[300; 400)$ \\\\
\\hline
Tần số tương đối & $%s\\%%$ & $%s\\%%$ & $%s\\%%$ & $%s\\%%$ \\\\
\\hline
\\end{tabular}
\\end{center}
\\item Tỉ lệ phần trăm sinh viên chi tiêu từ $200$ nghìn đồng trở lên mỗi tháng là: $%s\\%% + %s\\%% = %s\\%%$.
\\end{enumEX}''' % (n, m2, m4, n, tong_xy, hieu, tong_xy, hieu, y_val, tong_xy, y_val, x_val, f1, f2, f3, f4, f3, f4, f_tu_200))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
