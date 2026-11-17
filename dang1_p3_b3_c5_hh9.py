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


def bt_dang1_p3_b3_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        cap_so = [(36, 3), (36, 4), (45, 2), (45, 3), (45, 4), (60, 2), (60, 3), (60, 4), (72, 2), (72, 3), (72, 4), (90, 2), (90, 3)]
        n, k = random.choice(cap_so)
        tu_so = 360
        mau_so = 360 - k * n
        g = math.gcd(tu_so, mau_so)
        tu_rg = tu_so // g
        mau_rg = mau_so // g
        val = math.sqrt(tu_rg / mau_rg)
        number = Decimal(str(val))
        kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hai đường tròn đồng tâm $(O; R)$ và $(O; r)$ với $R > r$. Một góc ở tâm $\\widehat{AOB} = %d^\\circ$ cắt đường tròn lớn tại $A, B$ và cắt đường tròn nhỏ tại $C, D$. Biết diện tích hình vành khuyên giới hạn bởi hai đường tròn gấp $%d$ lần diện tích hình quạt tròn $OAB$ (thuộc đường tròn lớn). Tính tỉ số $\\dfrac{R}{r}$ (làm tròn kết quả đến hàng phần trăm).
\\begin{center}
\\begin{tikzpicture}[scale=0.85]
\\fill[blue!10] (0,0) circle (2.2);
\\fill[white] (0,0) circle (1.3);
\\fill[blue!25] (0,0) -- (2.2,0) arc (0:%d:2.2) -- cycle;
\\draw (0,0) circle (2.2);
\\draw (0,0) circle (1.3);
\\draw (0,0) -- (2.2,0);
\\draw (0,0) -- (%d:2.2);
\\fill (0,0) circle (1.5pt) node[below left] {$O$};
\\node[right] at (2.2,0) {$A$};
\\node[above right] at (%d:2.2) {$B$};
\\node[below right] at (1.3,0) {$C$};
\\node[above left] at (%d:1.3) {$D$};
\\draw (0.45,0) arc (0:%d:0.45);
\\node at (%d:0.85) {$%d^\\circ$};
\\end{tikzpicture}
\\end{center}''' % (n, k, n, n, n, n, n, n // 2, n))

        # Nội dung lời giải
        loigiai = ('''Diện tích hình quạt tròn $OAB$ thuộc đường tròn lớn là $S_q = \\dfrac{%d}{360}\\pi R^2$. \\\\
Diện tích hình vành khuyên giới hạn bởi hai đường tròn đồng tâm là $S_v = \\pi(R^2 - r^2)$. \\\\
Theo giả thiết, ta có:
$$\\pi(R^2 - r^2) = %d \\cdot \\dfrac{%d}{360}\\pi R^2 \\Leftrightarrow R^2 - r^2 = \\dfrac{%d}{360}R^2 \\Leftrightarrow r^2 = \\dfrac{%d}{%d}R^2.$$
Suy ra $\\dfrac{R^2}{r^2} = \\dfrac{%d}{%d} \\Rightarrow \\dfrac{R}{r} = \\sqrt{\\dfrac{%d}{%d}} \\approx %s$.''' % (
            n, k, n, k * n, mau_rg, tu_rg, tu_rg, mau_rg, tu_rg, mau_rg, kq_str))

        # Đáp án
        dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
