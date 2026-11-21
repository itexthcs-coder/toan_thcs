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


def bt_dang18_p4_b3_c2_ds8(self):
    # Dạng 18 (Thực tế): Bài toán tài chính – So sánh hai phương án gửi tiết kiệm lãi kép kỳ hạn 3 năm
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        P = random.choice([100, 200])
        S_A = Decimal(str(P)) * (Decimal('1.055')**3)
        S_B = Decimal(str(P)) * (Decimal('1.06')**3)
        chenh_lech = S_B - S_A

        SA_str = str(S_A.normalize()).replace('.', ',')
        SB_str = str(S_B.normalize()).replace('.', ',')
        cl_str = str(chenh_lech.normalize()).replace('.', ',')

        noidungcauhoi = ('''Cô Hương có $%s$ triệu đồng dự định gửi tiết kiệm vào ngân hàng theo thể thức lãi kép kì hạn $3$ năm với lãi suất không đổi $x$ mỗi năm (số tiền nhận được sau $3$ năm là $S = %s(1 + x)^3$ triệu đồng).\\\\
                         a) Khai triển $S$ thành đa thức theo biến $x$, xác định bậc của đa thức và viết biểu thức biểu thị số tiền lãi $L$ cô Hương nhận được sau $3$ năm.\\\\
                         b) Nếu ngân hàng A áp dụng lãi suất $x = 5,5\\%%$/năm và ngân hàng B áp dụng lãi suất $x = 6\\%%$/năm, hỏi sau $3$ năm gửi ở ngân hàng B thì cô Hương nhận được nhiều hơn ngân hàng A bao nhiêu triệu đồng?'''
                         % (P, P))

        loigiai = ('''\\begin{enumEX}[a)]{1}
                    \\item Ta có
                    $$S = %s(1 + x)^3 = %s(1 + 3x + 3x^2 + x^3) = %sx^3 + %sx^2 + %sx + %s.$$
                    Đây là đa thức bậc $3$ theo biến $x$.\\\\
                    Biểu thức biểu thị số tiền lãi cô Hương nhận được sau $3$ năm là
                    $$L = S - %s = %sx^3 + %sx^2 + %sx\\text{ (triệu đồng)}.$$
                    \\item Với lãi suất ở ngân hàng A là $x = 5,5\\%% = 0,055$, số tiền cô Hương nhận được sau $3$ năm là
                    $$S_A = %s \\cdot (1 + 0,055)^3 = %s \\cdot 1,055^3 = %s\\text{ (triệu đồng)}.$$
                    Với lãi suất ở ngân hàng B là $x = 6\\%% = 0,06$, số tiền cô Hương nhận được sau $3$ năm là
                    $$S_B = %s \\cdot (1 + 0,06)^3 = %s \\cdot 1,06^3 = %s\\text{ (triệu đồng)}.$$
                    Vậy gửi ở ngân hàng B cô Hương nhận được nhiều hơn ngân hàng A số tiền là
                    $$%s - %s = %s\\text{ (triệu đồng)}.$$
                    \\end{enumEX}'''
                   % (P, P, P, 3*P, 3*P, P,
                      P, P, 3*P, 3*P,
                      P, P, SA_str,
                      P, P, SB_str,
                      SB_str, SA_str, cl_str))

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
