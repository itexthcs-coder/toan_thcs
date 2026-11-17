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


def bt_dang5_p3_b3_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n = random.choice([90, 120])
        S = random.choice([5, 8, 10, 12, 15, 18, 20, 25])
        if n == 90:
            val = math.sqrt(S / (3.14 / 4 - 0.5))
        else:
            val = math.sqrt(S / (3.14 / 3 - math.sqrt(3) / 4))
        number = Decimal(str(val))
        kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một hình viên phân giới hạn bởi dây cung $AB$ và cung nhỏ $AB$ có số đo $%d^\\circ$ của đường tròn $(O; R)$ có diện tích bằng $%d\\text{ cm}^2$. Tính bán kính $R$ của đường tròn đó theo đơn vị $\\text{cm}$ (lấy $\\pi \\approx 3,14$, làm tròn kết quả đến hàng phần trăm).
\\begin{center}
\\begin{tikzpicture}[scale=0.85]
\\fill[cyan!25] (30:1.8) arc (30:150:1.8) -- cycle;
\\draw (0,0) circle (1.8);
\\draw (0,0) -- (30:1.8);
\\draw (0,0) -- (150:1.8);
\\draw[thick] (30:1.8) -- (150:1.8);
\\fill (0,0) circle (1.5pt) node[below] {$O$};
\\node[right] at (30:1.8) {$B$};
\\node[left] at (150:1.8) {$A$};
\\node at (0,0.45) {$%d^\\circ$};
\\end{tikzpicture}
\\end{center}''' % (n, S, n))

        # Nội dung lời giải
        if n == 90:
            loigiai = ('''Diện tích hình quạt tròn $OAB$ ứng với cung $90^\\circ$ là $S_q = \\dfrac{90}{360}\\pi R^2 = \\dfrac{\\pi}{4}R^2$. \\\\
Diện tích tam giác $OAB$ vuông cân tại $O$ là $S_{\\triangle OAB} = \\dfrac{1}{2}OA \\cdot OB = \\dfrac{1}{2}R^2$. \\\\
Diện tích hình viên phân là $S = S_q - S_{\\triangle OAB} = R^2\\left(\\dfrac{\\pi}{4} - \\dfrac{1}{2}\\right) = %d$. \\\\
Thay $\\pi \\approx 3,14$, ta được:
$$R^2 \\approx \\dfrac{%d}{\\dfrac{3,14}{4} - \\dfrac{1}{2}} = \\dfrac{%d}{0,285} \\Rightarrow R \\approx \\sqrt{\\dfrac{%d}{0,285}} \\approx %s\\text{ (cm)}.$$''' % (
                S, S, S, S, kq_str))
        else:
            loigiai = ('''Diện tích hình quạt tròn $OAB$ ứng với cung $120^\\circ$ là $S_q = \\dfrac{120}{360}\\pi R^2 = \\dfrac{\\pi}{3}R^2$. \\\\
Kẻ đường cao $OH$ của tam giác cân $OAB$ ($\\widehat{AOB} = 120^\\circ$), ta có $OH = R\\cos 60^\\circ = \\dfrac{R}{2}$ và $AB = 2R\\sin 60^\\circ = R\\sqrt{3}$. \\\\
Diện tích tam giác $OAB$ là $S_{\\triangle OAB} = \\dfrac{1}{2}OH \\cdot AB = \\dfrac{\\sqrt{3}}{4}R^2$. \\\\
Diện tích hình viên phân là $S = S_q - S_{\\triangle OAB} = R^2\\left(\\dfrac{\\pi}{3} - \\dfrac{\\sqrt{3}}{4}\\right) = %d$. \\\\
Thay $\\pi \\approx 3,14$, ta được:
$$R^2 \\approx \\dfrac{%d}{\\dfrac{3,14}{3} - \\dfrac{\\sqrt{3}}{4}} \\Rightarrow R \\approx %s\\text{ (cm)}.$$''' % (
                S, S, kq_str))

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
