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


def bt_dang4_p3_b3_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.choice([4, 5, 6, 7, 8, 9, 10, 11, 12])
        OM = 2 * R
        sq_frac = Rational(R ** 2, 3)
        val = (R ** 2) * (math.sqrt(3) - 3.14 / 3)
        number = Decimal(str(val))
        kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Từ điểm $M$ nằm ngoài đường tròn $(O; %d\\text{ cm})$ sao cho $OM = %d\\text{ cm}$, kẻ hai tiếp tuyến $MA, MB$ tới đường tròn ($A, B$ là các tiếp điểm). Tính diện tích phần hình phẳng giới hạn bởi hai đoạn thẳng $MA, MB$ và cung nhỏ $AB$ theo đơn vị $\\text{cm}^2$ (lấy $\\pi \\approx 3,14$, làm tròn kết quả đến hàng phần mười).
\\begin{center}
\\begin{tikzpicture}[scale=0.8]
\\fill[purple!18] (3,0) -- (60:1.5) arc (60:-60:1.5) -- cycle;
\\draw (0,0) circle (1.5);
\\draw[thick] (3,0) -- (60:1.5);
\\draw[thick] (3,0) -- (-60:1.5);
\\draw[dashed] (0,0) -- (3,0);
\\draw (0,0) -- (60:1.5);
\\draw (0,0) -- (-60:1.5);
\\fill (0,0) circle (1.5pt) node[left] {$O$};
\\fill (3,0) circle (1.5pt) node[right] {$M$};
\\node[above] at (60:1.5) {$A$};
\\node[below] at (-60:1.5) {$B$};
\\end{tikzpicture}
\\end{center}''' % (R, OM))

        # Nội dung lời giải
        loigiai = ('''Xét tam giác $OAM$ vuông tại $A$, ta có $\\cos\\widehat{AOM} = \\dfrac{OA}{OM} = \\dfrac{%d}{%d} = \\dfrac{1}{2} \\Rightarrow \\widehat{AOM} = 60^\\circ$. \\\\
Theo tính chất hai tiếp tuyến cắt nhau, suy ra $\\widehat{AOB} = 2\\widehat{AOM} = 120^\\circ$ và $MA = MB = \\sqrt{OM^2 - OA^2} = \\sqrt{%d^2 - %d^2} = %d\\sqrt{3}\\text{ (cm)}$. \\\\
Diện tích tứ giác $OAMB$ là:
$$S_{OAMB} = 2 \\cdot \\dfrac{1}{2}OA \\cdot MA = %d \\cdot %d\\sqrt{3} = %d\\sqrt{3}\\text{ (cm}^2\\text{)}.$$
Diện tích hình quạt tròn $OAB$ ứng với cung nhỏ $AB$ ($120^\\circ$) là:
$$S_q = \\dfrac{120}{360}\\pi \\cdot %d^2 = %s\\pi\\text{ (cm}^2\\text{)}.$$
Diện tích phần hình phẳng cần tìm là:
$$S = S_{OAMB} - S_q = %d\\sqrt{3} - %s\\pi \\approx %d\\sqrt{3} - %s \\cdot 3,14 \\approx %s\\text{ (cm}^2\\text{)}.$$''' % (
            R, OM, OM, R, R, R, R, R ** 2, R, latex(sq_frac), R ** 2, latex(sq_frac), R ** 2, latex(sq_frac), kq_str))

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
