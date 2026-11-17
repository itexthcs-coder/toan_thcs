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


def bt_dang5_p4_b1_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        a_abs = randint(2, 5)
        a_val = -a_abs
        x_left = -randint(2, 4)
        x_right = randint(1, abs(x_left) - 1)
        y_left = a_val * (x_left**2)
        y_right = a_val * (x_right**2)

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hàm số $y = %sx^2$. Khi biến số $x$ nhận các giá trị thỏa mãn điều kiện $%s \\le x \\le %s$, hãy tìm giá trị lớn nhất và giá trị nhỏ nhất của hàm số. Giải thích lập luận dựa trên tính chất và hình dáng đồ thị của hàm số.'''
                         %(latex(a_val), latex(x_left), latex(x_right)
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Hàm số $y = %sx^2$ có hệ số $a = %s < 0$ nên đồ thị của hàm số là một đường parabol nằm hoàn toàn phía dưới trục hoành và nhận gốc tọa độ $O(0; 0)$ làm điểm cao nhất. \\\\
Do đó $y = %sx^2 \\le 0$ với mọi $x \\in \\mathbb{R}$, dấu bằng xảy ra khi $x = 0$. \\\\
Vì $x = 0$ thuộc đoạn $[%s; %s]$ nên giá trị lớn nhất của hàm số trên đoạn này là $0$, đạt được tại $x = 0$. \\\\
Mặt khác, với $a < 0$, điểm càng nằm xa trục tung $Oy$ (tức là $|x|$ càng lớn) thì tung độ $y$ càng nhỏ. \\\\
Trên đoạn $[%s; %s]$, giá trị $x$ có giá trị tuyệt đối lớn nhất là $x = %s$ (vì $|%s| = %s > |%s| = %s$). \\\\
Khi $x = %s$, giá trị của hàm số là $y = %s \\cdot (%s)^2 = %s$. \\\\
Lập bảng một số giá trị tiêu biểu trên đoạn $[%s; %s]$:
\\begin{center}
\\begin{tabular}{|c|c|c|c|}
\\hline
$x$ & $%s$ & $0$ & $%s$ \\\\
\\hline
$y = %sx^2$ & $%s$ & $0$ & $%s$ \\\\
\\hline
\\end{tabular}
\\end{center}
Vậy trên đoạn $[%s; %s]$, giá trị lớn nhất của hàm số là $0$ (khi $x = 0$) và giá trị nhỏ nhất của hàm số là $%s$ (khi $x = %s$).'''
                   %(latex(a_val), latex(a_val),
                     latex(a_val),
                     latex(x_left), latex(x_right),
                     latex(x_left), latex(x_right), latex(x_left), latex(x_left), latex(abs(x_left)), latex(x_right), latex(abs(x_right)),
                     latex(x_left), latex(a_val), latex(x_left), latex(y_left),
                     latex(x_left), latex(x_right),
                     latex(x_left), latex(x_right),
                     latex(a_val), latex(y_left), latex(y_right),
                     latex(x_left), latex(x_right), latex(y_left), latex(x_left)
                   ))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' + str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
