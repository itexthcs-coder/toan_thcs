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
def bt_dang18_p4_b3_c6_ds8(self):
    # Dạng 18: Bài toán năng suất lao động – So sánh thời gian hoàn thành công việc của hai phân xưởng
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo = [
            (1200, 10, 50, 24, 20, 4),
            (1500, 15, 60, 25, 20, 5),
            (1800, 15, 45, 40, 30, 10),
            (2000, 10, 40, 50, 40, 10)
        ]
        chi_tieu, chenh_ns, x_val, tg1, tg2, som_hon = random.choice(bo)
        tu_so = chi_tieu * chenh_ns
        
        noidungcauhoi = ('Hai phân xưởng cùng được giao chỉ tiêu sản xuất $%s$ sản phẩm. Mỗi ngày phân xưởng I sản xuất được $x$ sản phẩm ($x > 0$), phân xưởng II sản xuất nhiều hơn phân xưởng I là $%s$ sản phẩm.\\'
                         'a) Viết các phân thức biểu thị thời gian để phân xưởng I và phân xưởng II hoàn thành chỉ tiêu.\\'
                         'b) Viết phân thức biểu thị số ngày phân xưởng II hoàn thành chỉ tiêu sớm hơn phân xưởng I và tính giá trị đó khi $x = %s$.'
                         % (chi_tieu, chenh_ns, x_val))
        
        loigiai = ('\\begin{enumEX}[a)]{1} \n'
                   '\\item Thời gian để phân xưởng I hoàn thành chỉ tiêu là $\\dfrac{%s}{x}$ (ngày).\\'
                   'Mỗi ngày phân xưởng II sản xuất được $x + %s$ sản phẩm nên thời gian để phân xưởng II hoàn thành chỉ tiêu là $\\dfrac{%s}{x + %s}$ (ngày).\n'
                   '\\item Phân thức biểu thị số ngày phân xưởng II hoàn thành chỉ tiêu sớm hơn phân xưởng I là:\\'
                   '$$T = \\dfrac{%s}{x} - \\dfrac{%s}{x + %s} = \\dfrac{%s(x + %s) - %sx}{x(x + %s)} = \\dfrac{%s}{x(x + %s)}\\text{ (ngày)}.$$\\'
                   'Khi $x = %s$, phân xưởng II hoàn thành chỉ tiêu sớm hơn phân xưởng I số ngày là:\\'
                   '$$T = \\dfrac{%s}{%s} - \\dfrac{%s}{%s + %s} = %s - %s = %s\\text{ (ngày)}.$$\n'
                   '\\end{enumEX} \n'
                   % (chi_tieu, chenh_ns, chi_tieu, chenh_ns, chi_tieu, chi_tieu, chenh_ns, chi_tieu, chenh_ns, chi_tieu, chenh_ns, tu_so, chenh_ns,
                      x_val, chi_tieu, x_val, chi_tieu, x_val, chenh_ns, tg1, tg2, som_hon))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
