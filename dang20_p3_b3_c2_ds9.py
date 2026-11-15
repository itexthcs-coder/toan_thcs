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


def bt_dang20_p3_b3_c2_ds9(self):
    x = symbols('x')
    tong_sp = randint(300, 600)
    so_ngay_dau = randint(3, 6)
    ns_dau = randint(25, 45)
    so_ngay_con_lai = randint(4, 8)
    
    sp_da_lam = so_ngay_dau * ns_dau
    sp_con_lai = tong_sp - sp_da_lam
    x_min_val = Rational(sp_con_lai, so_ngay_con_lai)
    ans = math.ceil(float(x_min_val))
    kq_str = str(ans)
    
    noidungcauhoi = ('''Một phân xưởng nhận đơn hàng may $%s$ bộ quần áo. Trong $%s$ ngày đầu, phân xưởng may được trung bình mỗi ngày $%s$ bộ. Để hoàn thành đơn hàng đúng hạn trong $%s$ ngày làm việc tiếp theo, trung bình mỗi ngày còn lại phân xưởng phải may ít nhất bao nhiêu bộ quần áo?'''
                     % (tong_sp, so_ngay_dau, ns_dau, so_ngay_con_lai))
    
    loigiai = ('''Gọi $x$ ($x \\in \\mathbb{N}^*$) là số bộ quần áo trung bình mỗi ngày còn lại phân xưởng cần may. \\
               Trong $%s$ ngày đầu, phân xưởng đã may được $%s \\cdot %s = %s$ (bộ). \\
               Tổng số bộ quần áo may được sau cả hai giai đoạn là $%s + %sx$ (bộ). \\
               Để hoàn thành đơn hàng (may được ít nhất $%s$ bộ), ta có bất phương trình: \\
               $%s + %sx \\ge %s \\Leftrightarrow %sx \\ge %s \\Leftrightarrow x \\ge %s \\approx %.2f$. \\
               Vì $x \\in \\mathbb{N}^*$ nên mỗi ngày còn lại phân xưởng phải may ít nhất $%s$ bộ quần áo.'''
               % (so_ngay_dau, so_ngay_dau, ns_dau, sp_da_lam,
                  sp_da_lam, so_ngay_con_lai,
                  tong_sp,
                  sp_da_lam, so_ngay_con_lai, tong_sp, so_ngay_con_lai, sp_con_lai, latex(x_min_val), float(x_min_val),
                  kq_str))
    
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan) +
        '\\loigiai{ \n' + str(loigiai) + '}\n'
        '\\end{ex}\n \\end{minipage}\n\n')
    return content
