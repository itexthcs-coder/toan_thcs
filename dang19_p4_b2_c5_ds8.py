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


def bt_dang19_p4_b2_c5_ds8(self):
    # Dạng 19 (Tự luận - Vận dụng thực tế): Thống kê bán hàng, vẽ biểu đồ tranh có nửa biểu tượng và tính doanh thu
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        g1, g2, g3, g4 = 1250, 1750, 1500, 1000
        p1, p2, p3, p4 = 36, 24, 22, 28
        dt_nghin = g1 * p1 + g2 * p2 + g3 * p3 + g4 * p4
        dt_trieu = dt_nghin // 1000
        
        tikz_a = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt] (-1.6, 0.2) rectangle (4.8, 3.4);
        \\draw[line width=1pt] (0.6, 0.2) -- (0.6, 3.4);
        \\draw[line width=1pt] (-1.6, 2.6) -- (4.8, 2.6);
        \\draw[line width=1pt] (-1.6, 1.8) -- (4.8, 1.8);
        \\draw[line width=1pt] (-1.6, 1.0) -- (4.8, 1.0);
        \\node at (-0.5, 3.0) {ST25};
        \\node at (-0.5, 2.2) {Nàng Hương};
        \\node at (-0.5, 1.4) {Tám Xoan};
        \\node at (-0.5, 0.6) {Nếp cái};
        \\draw[line width=1pt] (1.1,2.8) rectangle (1.5,3.2) (1.8,2.8) rectangle (2.2,3.2) (2.5,2.8) rectangle (2.7,3.2);
        \\draw[line width=1pt] (1.1,2.0) rectangle (1.5,2.4) (1.8,2.0) rectangle (2.2,2.4) (2.5,2.0) rectangle (2.9,2.4) (3.2,2.0) rectangle (3.4,2.4);
        \\draw[line width=1pt] (1.1,1.2) rectangle (1.5,1.6) (1.8,1.2) rectangle (2.2,1.6) (2.5,1.2) rectangle (2.9,1.6);
        \\draw[line width=1pt] (1.1,0.4) rectangle (1.5,0.8) (1.8,0.4) rectangle (2.2,0.8);
        \\draw[line width=1pt] (0.2,-0.45) rectangle (0.6,-0.05);
        \\node[right] at (0.7,-0.25) {$= 500\\text{ kg}$;};
        \\draw[line width=1pt] (2.6,-0.45) rectangle (2.8,-0.05);
        \\node[right] at (2.9,-0.25) {$= 250\\text{ kg}$};
        \\end{tikzpicture}
        \\end{center}""" )
        
        noidungcauhoi = ("""Một đại lý phân phối gạo thống kê khối lượng gạo bán được trong quý III gồm: Gạo ST25 bán được $1\\,250\\text{ kg}$, Gạo Nàng Hương bán được $1\\,750\\text{ kg}$, Gạo Tám Xoan bán được $1\\,500\\text{ kg}$ và Gạo Nếp cái hoa vàng bán được $1\\,000\\text{ kg}$.\\\\
        a) Nếu biểu diễn bảng số liệu trên bằng biểu đồ tranh sao cho mỗi biểu tượng nguyên ứng với $500\\text{ kg}$ và mỗi nửa biểu tượng ứng với $250\\text{ kg}$, hãy tính số biểu tượng cần vẽ cho từng loại gạo và vẽ biểu đồ tranh đó.\\\\
        b) Tính tổng doanh thu của đại lý trong quý III (đơn vị: triệu đồng), biết giá bán mỗi ki-lô-gam gạo ST25 là $%s\\,000$ đồng, gạo Nàng Hương là $%s\\,000$ đồng, gạo Tám Xoan là $%s\\,000$ đồng và gạo Nếp cái hoa vàng là $%s\\,000$ đồng."""
                         % (p1, p2, p3, p4))
        
        loigiai = ("""\\begin{enumEX}[a)]{1}
        \\item Quy đổi số biểu tượng cho từng loại gạo:\\\\
        - Gạo ST25: $1\\,250 = 2 \\cdot 500 + 250$ ($2$ biểu tượng nguyên và $1$ nửa biểu tượng).\\\\
        - Gạo Nàng Hương: $1\\,750 = 3 \\cdot 500 + 250$ ($3$ biểu tượng nguyên và $1$ nửa biểu tượng).\\\\
        - Gạo Tám Xoan: $1\\,500 = 3 \\cdot 500$ ($3$ biểu tượng nguyên).\\\\
        - Gạo Nếp cái hoa vàng: $1\\,000 = 2 \\cdot 500$ ($2$ biểu tượng nguyên).%s
        \\item Tổng doanh thu của đại lý trong quý III là:
        $$1\\,250 \\cdot %s + 1\\,750 \\cdot %s + 1\\,500 \\cdot %s + 1\\,000 \\cdot %s = %s\\,000 \\text{ (nghìn đồng)} = %s \\text{ (triệu đồng)}.$$
        \\end{enumEX}""" % (tikz_a, p1, p2, p3, p4, dt_nghin // 1000, dt_trieu))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
