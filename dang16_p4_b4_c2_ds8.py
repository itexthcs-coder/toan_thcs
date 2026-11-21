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


def bt_dang16_p4_b4_c2_ds8(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        r_nho = Decimal(str(random.choice([2.5, 3.5, 4.5])))
        r_lon = r_nho + Decimal(str(random.choice([2.0, 3.0, 4.0])))
        r_nho_str = str(r_nho).replace('.', ',')
        r_lon_str = str(r_lon).replace('.', ',')
        
        hieu_r = r_lon - r_nho
        tong_r = r_lon + r_nho
        dt_chinh_xac = Decimal('3.14') * hieu_r * tong_r
        dt_lam_tron = dt_chinh_xac.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        dt_lam_tron_str = str(dt_lam_tron).replace('.', ',')
        dt_chinh_xac_str = str(dt_chinh_xac.normalize()).replace('.', ',')
        
        tikz_hinh = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (O) at (0,0);
    \\draw[line width=1pt] (O) circle (1.9);
    \\draw[line width=1pt] (O) circle (0.95);
    \\fill (O) circle (1pt) node[below left] {$O$};
    \\draw[line width=1pt, ->] (O) -- (35:1.9) node[midway, above left] {$R$};
    \\draw[line width=1pt, ->] (O) -- (-40:0.95) node[midway, below left] {$r$};
\\end{tikzpicture}
\\end{center}'''
        
        noidungcauhoi = ('''Tại quảng trường trung tâm, người ta thiết kế một bồn hoa hình tròn có bán kính ngoài $R\\text{ (m)}$, ở chính giữa là một đài phun nước hình tròn đồng tâm có bán kính $r\\text{ (m)}$ ($R > r > 0$). Phần diện tích hình vành khuyên giữa bồn hoa và đài phun nước được dùng để trồng hoa hồng. \\
a) Viết biểu thức biểu thị diện tích $S$ của phần đất trồng hoa hồng theo $R$ và $r$, sau đó phân tích biểu thức $S$ thành nhân tử. \\\\
b) Tính diện tích phần đất trồng hoa hồng khi $R = %s\\text{ m}$ và $r = %s\\text{ m}$ (lấy $\\pi \\approx 3,14$ và làm tròn kết quả đến hàng phần mười).'''
                         % (r_lon_str, r_nho_str) + tikz_hinh)
        
        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Diện tích phần đất trồng hoa hồng bằng hiệu diện tích bồn hoa ngoài và đài phun nước bên trong:
\\begin{align*}
S = \\pi R^2 - \\pi r^2 = \\pi(R^2 - r^2) = \\pi(R - r)(R + r)\\text{ (m}^2\\text{)}.
\\end{align*}
\\item Thay $R = %s\\text{ m}$, $r = %s\\text{ m}$ và $\\pi \\approx 3,14$ vào biểu thức trên, ta được:
\\begin{align*}
S \\approx 3,14 \\cdot (%s - %s)(%s + %s) = 3,14 \\cdot %s \\cdot %s = %s \\approx %s\\text{ (m}^2\\text{)}.
\\end{align*}
\\end{enumEX}''' % (r_lon_str, r_nho_str, r_lon_str, r_nho_str, r_lon_str, r_nho_str,
                      str(hieu_r).replace('.', ','), str(tong_r).replace('.', ','),
                      dt_chinh_xac_str, dt_lam_tron_str))

    # Xuất câu hỏi và lời giải tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' + str(noidungcauhoi) +
               '\\loigiai{ \n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
