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


def bt_dang17_p4_b3_c1_ds8(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        x, y = symbols('x y')
        h1 = random.choice([1, 2])
        h2 = random.choice([2, 3])
        cf = randint(12, 18)
        
        x0 = random.choice([15, 20])
        y0 = random.choice([10, 15])
        gt = h1 * x0 + h2 * y0 - cf
        
        c1_str = '1,2'
        r1_str = str(h1 + 1) + ',2'
        c2_str = '2,5'
        r2_str = str(h2 + 2) + ',5'
        
        noidungcauhoi = ('''Một cơ sở sản xuất đèn lồng thủ công có chi phí cố định và chi phí nguyên vật liệu (tính theo trăm nghìn đồng) để làm ra $x$ chiếc đèn cỡ nhỏ và $y$ chiếc đèn cỡ vừa được biểu thị bởi đa thức $C = %sx + %sy + 0,04xy + %s$. Tổng doanh thu (tính theo trăm nghìn đồng) khi bán hết số đèn đó được biểu thị bởi đa thức $R = %sx + %sy + 0,04xy$. \\\\
                         a) Lập đa thức $L$ biểu thị lợi nhuận của cơ sở sản xuất đó. \\\\
                         b) Nếu cơ sở bán được $%s$ chiếc đèn cỡ nhỏ và $%s$ chiếc đèn cỡ vừa thì cơ sở lãi bao nhiêu tiền?'''
                         % (c1_str, c2_str, cf, r1_str, r2_str, x0, y0))
        
        loigiai = ('''\\begin{enumEX}[a)]{1} \n
                        \\item Đa thức $L$ biểu thị lợi nhuận của cơ sở sản xuất là:
                        \\begin{align*}
                        L &= R - C \\\\
                        &= (%sx + %sy + 0,04xy) - (%sx + %sy + 0,04xy + %s) \\\\
                        &= %sx + %sy - %s \\text{ (trăm nghìn đồng)}.
                        \\end{align*} \n
                        \\item Thay $x = %s$ và $y = %s$ vào đa thức $L$, ta được:
                        $$L = %s \\cdot %s + %s \\cdot %s - %s = %s \\text{ (trăm nghìn đồng)}.$$
                        Vậy cơ sở đó lãi $%s$ trăm nghìn đồng (tức là $%s$ triệu đồng). \n
                        \\end{enumEX} \n'''
                   % (r1_str, r2_str, c1_str, c2_str, cf, h1, h2, cf,
                      x0, y0, h1, x0, h2, y0, cf, gt, gt, str(gt / 10).replace('.', ',')))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
