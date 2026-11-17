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


def bt_dang2_p4_b1_c6_ds9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        mau_a = random.choice([2, 4])
        x_m = mau_a // 2
        y_m = -Rational(1, mau_a) * (x_m**2)
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Trên mặt phẳng tọa độ $Oxy$, cho parabol $(P): y = -\\frac{1}{%s}x^2$. Điểm $M$ có hoành độ dương thuộc $(P)$ sao cho khoảng cách từ $M$ đến trục tung gấp đôi khoảng cách từ $M$ đến trục hoành. Tìm tọa độ điểm $M$ và điểm $M'$ đối xứng với $M$ qua trục tung $Oy$.'''
                         %(latex(mau_a)
                         ))
        
        # Nội dung lời giải
        loigiai = ('''Gọi tọa độ điểm $M$ là $(x_0; y_0)$. Vì $M$ thuộc parabol $(P): y = -\\frac{1}{%s}x^2$ và có hoành độ dương nên $x_0 > 0$ và $y_0 = -\\frac{1}{%s}x_0^2 < 0$. \\\\
Khoảng cách từ điểm $M(x_0; y_0)$ đến trục tung $Oy$ là $|x_0| = x_0$ (do $x_0 > 0$). \\\\
Khoảng cách từ điểm $M(x_0; y_0)$ đến trục hoành $Ox$ là $|y_0| = -y_0$ (do $y_0 < 0$). \\\\
Theo giả thiết, khoảng cách từ $M$ đến trục tung gấp đôi khoảng cách từ $M$ đến trục hoành nên ta có: \\\\
$x_0 = 2(-y_0)$ \\\\
Thay $y_0 = -\\frac{1}{%s}x_0^2$ vào hệ thức trên, ta được: \\\\
$x_0 = 2 \\cdot \\left(\\frac{1}{%s}x_0^2\\right)$ \\\\
$x_0 = \\frac{2}{%s}x_0^2$ \\\\
Vì $x_0 > 0$, chia cả hai vế cho $x_0$ ta được: \\\\
$1 = \\frac{2}{%s}x_0 \\Rightarrow x_0 = %s$. \\\\
Khi đó tung độ điểm $M$ là $y_0 = -\\frac{1}{%s} \\cdot %s^2 = %s$. \\\\
Vậy tọa độ điểm $M$ là $\\left(%s; %s\\right)$. \\\\
Vì điểm $M'$ đối xứng với điểm $M\\left(%s; %s\\right)$ qua trục tung $Oy$ nên hai điểm có tung độ bằng nhau và hoành độ đối nhau. \\\\
Vậy tọa độ điểm $M'$ là $\\left(-%s; %s\\right)$.'''
                   %(latex(mau_a), latex(mau_a),
                     latex(mau_a),
                     latex(mau_a),
                     latex(mau_a),
                     latex(mau_a), latex(x_m),
                     latex(mau_a), latex(x_m), latex(y_m),
                     latex(x_m), latex(y_m),
                     latex(x_m), latex(y_m),
                     latex(x_m), latex(y_m)
                   ))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' + str(loigiai) + '\n}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
