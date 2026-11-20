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


def bt_dang18_p4_b3_c1_ds8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x, y = symbols('x y')
        a1, b1, c1 = randint(3, 5), randint(3, 6), randint(-4, -2)
        a2, b2, c2 = randint(1, 2), randint(-2, -1), randint(3, 6)
        a3, b3, c3 = randint(3, 5), randint(2, 4), randint(5, 8)
        
        S1 = a1*x**2 + b1*x*y + c1
        S2 = a2*x**2 + b2*x*y + c2
        S3 = a3*x**2 + b3*x*y + c3
        
        S_tong = simplify(S1 + S2 + S3)
        S_chenh = simplify(S1 + S3 - S2)
        
        x0 = randint(2, 4)
        y0 = randint(2, 3)
        gt = int(S_chenh.subs({x: x0, y: y0}))
        
        noidungcauhoi = ('''Một tàu thủy chở hàng di chuyển trên một tuyến sông gồm ba chặng: chặng xuôi dòng dài $S_1 = %s$ ($\\text{km}$), chặng nước lặng dài $S_2 = %s$ ($\\text{km}$) và chặng ngược dòng dài $S_3 = %s$ ($\\text{km}$). \\\\
                         a) Tìm đa thức biểu thị tổng chiều dài toàn bộ tuyến đường mà tàu đã đi. \\\\
                         b) Biết tổng chiều dài chặng xuôi dòng và chặng ngược dòng dài hơn chặng nước lặng bao nhiêu ki-lô-mét (biểu thị dưới dạng đa thức)? Tính giá trị đó khi $x = %s$ và $y = %s$.'''
                         % (latex(S1), latex(S2), latex(S3), x0, y0))
        
        loigiai = ('''\\begin{enumEX}[a)]{1} \n
                        \\item Đa thức biểu thị tổng chiều dài toàn bộ tuyến đường là:
                        \\begin{align*}
                        S &= S_1 + S_2 + S_3 \\\\
                        &= (%s) + (%s) + (%s) \\\\
                        &= %s \\text{ (km)}.
                        \\end{align*} \n
                        \\item Đa thức biểu thị phần chênh lệch chiều dài là:
                        \\begin{align*}
                        D &= (S_1 + S_3) - S_2 \\\\
                        &= (%s) + (%s) - (%s) \\\\
                        &= %s \\text{ (km)}.
                        \\end{align*}
                        Thay $x = %s$ và $y = %s$ vào đa thức $D$, ta được giá trị bằng $%s\\text{ km}$. \n
                        \\end{enumEX} \n'''
                   % (latex(S1), latex(S2), latex(S3), latex(S_tong),
                      latex(S1), latex(S3), latex(S2), latex(S_chenh),
                      x0, y0, gt))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
