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


def bt_dang9_p4_b2_c10_hh9(self):
    # Hình nón có r_day = 6k, h_non = 8k, l_non = 10k => hình cầu nội tiếp có R = 3k.
    k = random.choice([1, 2])
    r_day = 6 * k
    h_non = 8 * k
    l_non = 10 * k
    R_cau = 3 * k
    V_non = (r_day**2 * h_non) // 3
    V_cau = Rational(4, 3) * R_cau**3

    noidungcauhoi = ('''Cho một hình nón có bán kính đáy $r = %s\\text{ cm}$ và chiều cao $h = %s\\text{ cm}$. Bên trong hình nón đặt một hình cầu tiếp xúc với mặt đáy và tiếp xúc với tất cả các đường sinh của hình nón.\\\na) Tính diện tích xung quanh và thể tích của hình nón.\\\nb) Chứng minh rằng bán kính $R$ của hình cầu nội tiếp hình nón bằng $%s\\text{ cm}$.\\\nc) Tính tỉ số giữa thể tích khối cầu và thể tích hình nón.'''
                     % (r_day, h_non, R_cau))

    ti_so = Rational(V_cau, V_non)

    loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Độ dài đường sinh của hình nón là: $l = \\sqrt{r^2 + h^2} = \\sqrt{%s^2 + %s^2} = %s\\text{ (cm)}$.\\\nDiện tích xung quanh hình nón là: $S_{\\text{xq}} = \\pi r l = \\pi \\cdot %s \\cdot %s = %s\\pi\\text{ (cm}^2\\text{)}$.\\\nThể tích hình nón là: $V_{\\text{nón}} = \\dfrac{1}{3}\\pi r^2 h = \\dfrac{1}{3}\\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}$.
\\item Xét thiết diện qua trục hình nón là tam giác cân $SAB$ có đáy $AB = 2r = %s\\text{ cm}$, đường cao $SH = h = %s\\text{ cm}$, nội tiếp đường tròn tâm $O$ bán kính $R$ tiếp xúc với $AB$ tại $H$ và $SB$ tại $T$.\\\nTa có $BT = BH = r = %s\\text{ cm} \\Rightarrow ST = SB - BT = %s - %s = %s\\text{ (cm)}$.\\\nVì $\\triangle STO \\backsim \\triangle SHB$ (g.g) nên:
$$\\dfrac{OT}{HB} = \\dfrac{ST}{SH} \\Rightarrow \\dfrac{R}{%s} = \\dfrac{%s}{%s} \\Rightarrow R = %s\\text{ (cm)}.$$
\\item Thể tích của khối cầu là: $V_{\\text{cầu}} = \\dfrac{4}{3}\\pi R^3 = \\dfrac{4}{3}\\pi \\cdot %s^3 = %s\\pi\\text{ (cm}^3\\text{)}$.\\\nTỉ số thể tích giữa khối cầu và hình nón là: $\\dfrac{V_{\\text{cầu}}}{V_{\\text{nón}}} = \\dfrac{%s\\pi}{%s\\pi} = %s$.
\\end{enumEX}'''
               % (r_day, h_non, l_non, r_day, l_non, r_day * l_non, r_day, h_non, V_non, 2 * r_day, h_non, r_day, l_non, r_day, l_non - r_day, r_day, l_non - r_day, h_non, R_cau, R_cau, latex(V_cau), latex(V_cau), V_non, latex(ti_so)))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
