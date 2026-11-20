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


def bt_dang19_p4_b3_c1_ds8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x, y, z = symbols('x y z')
        a1, b1, c1, d1 = randint(3, 5), randint(2, 4), randint(1, 3), randint(10, 14)
        a2, b2, c2, d2 = randint(4, 6), randint(2, 3), randint(2, 4), randint(12, 16)
        a3, b3, c3, d3 = randint(4, 6), randint(2, 4), randint(1, 3), randint(10, 15)
        
        T1 = a1*x + b1*y + c1*z + d1
        T2 = a2*x + b2*y + c2*z + d2
        T3 = a3*x + b3*y + c3*z + d3
        T = simplify(T1 + T2 + T3)
        
        x0 = 2
        y0 = Rational(3, 2)
        z0 = 1
        gt = T3.subs({x: x0, y: y0, z: z0})
        gt_str = str(float(gt)).replace('.', ',') if gt != int(gt) else str(int(gt))
        
        noidungcauhoi = ('''Tổng chi tiêu (tính theo triệu đồng) của một gia đình trong Quý I và Quý II lần lượt được biểu thị bởi các đa thức:
                         $$T_1 = %s; \\qquad T_2 = %s.$$
                         Biết tổng ngân sách dự kiến cho cả $3$ quý đầu năm là $T = %s$ (triệu đồng). \\\\
                         a) Tìm đa thức $T_3$ biểu thị số tiền còn lại dành cho chi tiêu trong Quý III. \\\\
                         b) Tính số tiền chi tiêu của Quý III nếu $x = 2$, $y = 1,5$, $z = 1$.'''
                         % (latex(T1), latex(T2), latex(T)))
        
        loigiai = ('''\\begin{enumEX}[a)]{1} \n
                        \\item Đa thức $T_3$ biểu thị số tiền chi tiêu của Quý III là:
                        \\begin{align*}
                        T_3 &= T - (T_1 + T_2) \\\\
                        &= (%s) - [(%s) + (%s)] \\\\
                        &= (%s) - (%s) \\\\
                        &= %s \\text{ (triệu đồng)}.
                        \\end{align*} \n
                        \\item Thay $x = 2$, $y = 1,5$, $z = 1$ vào đa thức $T_3$, ta được số tiền chi tiêu của Quý III là:
                        $$T_3 = %s \\cdot 2 + %s \\cdot 1,5 + %s \\cdot 1 + %s = %s \\text{ (triệu đồng)}.$$ \n
                        \\end{enumEX} \n'''
                   % (latex(T), latex(T1), latex(T2), latex(T), latex(simplify(T1 + T2)), latex(T3),
                      a3, b3, c3, d3, gt_str))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
