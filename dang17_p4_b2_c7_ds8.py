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
    QApplication, QPushButton, QMainWindow, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D


def bt_dang17_p4_b2_c7_ds8(self):
    # Dạng 17: Ứng dụng - Bài toán năng suất lao động và sản xuất
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        ns_kh = random.choice([25, 30, 35, 40])
        tang_ns = random.choice([5, 10, 15])
        ns_tt = ns_kh + tang_ns
        som_ngay = random.choice([2, 3, 4])
        them_sp = random.choice([10, 15, 20, 25])
        
        # x/ns_kh - (x + them_sp)/ns_tt = som_ngay
        # Quy đồng bcnn(ns_kh, ns_tt): m1*x - m2*(x + them_sp) = som_ngay * bcnn
        # (m1 - m2)x = som_ngay * bcnn + m2 * them_sp
        bcnn = math.lcm(ns_kh, ns_tt)
        m1 = bcnn // ns_kh
        m2 = bcnn // ns_tt
        rhs = som_ngay * bcnn + m2 * them_sp
        while rhs % (m1 - m2) != 0:
            them_sp += 5
            rhs = som_ngay * bcnn + m2 * them_sp
            
        x_val = rhs // (m1 - m2)
        
        noidungcauhoi = ('''Một tổ sản xuất theo kế hoạch mỗi ngày phải lắp ráp $%s$ bộ linh kiện điện tử. Do cải tiến kỹ thuật nên mỗi ngày tổ đã lắp ráp vượt mức $%s$ bộ linh kiện so với kế hoạch. Vì vậy, tổ không những đã hoàn thành công việc sớm hơn dự định $%s$ ngày mà còn làm thêm được $%s$ bộ linh kiện nữa. Tính số bộ linh kiện điện tử mà tổ sản xuất phải lắp ráp theo kế hoạch.'''
                         % (ns_kh, tang_ns, som_ngay, them_sp))
        
        loigiai = ('''Gọi số bộ linh kiện điện tử mà tổ sản xuất phải lắp ráp theo kế hoạch là $x$ (bộ) (điều kiện: $x \\in \\mathbb{N}^*$). \\\\
- Thời gian hoàn thành công việc theo kế hoạch là: $\\frac{x}{%s}$ (ngày). \\\\
- Thực tế mỗi ngày tổ lắp ráp được: $%s + %s = %s$ (bộ). \\\\
- Tổng số bộ linh kiện thực tế tổ đã lắp ráp được là: $x + %s$ (bộ). \\\\
- Thời gian thực tế tổ hoàn thành công việc là: $\\frac{x + %s}{%s}$ (ngày). \\\\
Vì thực tế tổ hoàn thành sớm hơn kế hoạch $%s$ ngày nên ta có phương trình: \\\\
$\\frac{x}{%s} - \\frac{x + %s}{%s} = %s$. \\\\
Quy đồng mẫu thức hai vế với mẫu chung là $%s$, ta được: \\\\
$%sx - %s(x + %s) = %s$ \\\\
$\\Leftrightarrow %sx - %sx - %s = %s$ \\\\
$\\Leftrightarrow %sx = %s \\Leftrightarrow x = %s$ (thỏa mãn điều kiện). \\\\
Vậy theo kế hoạch, tổ sản xuất phải lắp ráp $%s$ bộ linh kiện điện tử.'''
                   % (ns_kh,
                      ns_kh, tang_ns, ns_tt,
                      them_sp,
                      them_sp, ns_tt,
                      som_ngay,
                      ns_kh, them_sp, ns_tt, som_ngay,
                      bcnn,
                      m1, m2, them_sp, som_ngay * bcnn,
                      m1, m2, m2 * them_sp, som_ngay * bcnn,
                      m1 - m2, rhs, x_val,
                      x_val))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
