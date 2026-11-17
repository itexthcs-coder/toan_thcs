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
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
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
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
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
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang15_p3_b5_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R1 = randint(6, 10)
        R2 = randint(3, R1 - 1)
        d1 = 2 * R1
        d2 = 2 * R2
        L_val = R1 + R2 + 2 * math.sqrt(R1 * R2)
        number = Decimal(L_val)
        kq = number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        hinhve = ('''\\begin{center}
\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (1.5, 1.5);
\\coordinate (Op) at (3.95, 1.0);
\\coordinate (H) at (1.5, 1.0);
\\draw[line width=1pt] (0,0) rectangle (4.95, 3.0);
\\draw[line width=1pt] (O) circle (1.5cm);
\\draw[line width=1pt] (Op) circle (1.0cm);
\\draw[line width=1pt] (O)--(Op);
\\draw[line width=1pt, dashed] (0, 1.5)--(O)--(H)--(Op)--(4.95, 1.0);
\\fill (O) circle (1pt) node[above] {$O$};
\\fill (Op) circle (1pt) node[above] {$O'$};
\\fill (H) circle (1pt) node[below left] {$H$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Một người thợ cắt hai tấm thép hình tròn có đường kính lần lượt là $%s\\text{ cm}$ và $%s\\text{ cm}$ từ một tấm thép hình chữ nhật có chiều rộng $%s\\text{ cm}$ sao cho hai hình tròn tiếp xúc ngoài với nhau và cùng chạm vào hai cạnh đối diện của chiều rộng tấm thép. Chiều dài tối thiểu của tấm thép hình chữ nhật cần dùng là bao nhiêu $\\text{cm}$? (Làm tròn kết quả đến hàng phần mười).\\\\
%s''' % (d1, d2, d1, hinhve))

        loigiai = ('''Bán kính của hai tấm thép hình tròn lần lượt là $R_1 = %s\\text{ cm}$ và $R_2 = %s\\text{ cm}$. \\\\
Vì hai đường tròn $(O; R_1)$ và $(O'; R_2)$ tiếp xúc ngoài với nhau nên độ dài đoạn nối tâm là: \\\\
$OO' = R_1 + R_2 = %s + %s = %s\\text{ (cm)}$. \\\\
Vì hai đường tròn lần lượt tiếp xúc với hai cạnh chiều dài đối diện của hình chữ nhật có chiều rộng $%s\\text{ cm}$ nên khoảng cách theo phương thẳng đứng giữa hai tâm là: \\\\
$OH = %s - R_1 - R_2 = %s - %s - %s = %s\\text{ (cm)}$. \\\\
Áp dụng định lí Pythagore vào tam giác vuông $OHO'$, khoảng cách theo phương ngang giữa hai tâm là: \\\\
$O'H = \\sqrt{OO'^2 - OH^2} = \\sqrt{%s^2 - %s^2} = \\sqrt{%s}\\text{ (cm)}$. \\\\
Vậy chiều dài tối thiểu của tấm thép hình chữ nhật cần dùng là: \\\\
$L = R_1 + O'H + R_2 = %s + \\sqrt{%s} + %s \\approx %s\\text{ (cm)}$.'''
                   % (R1, R2, R1, R2, R1 + R2, d1, d1, d1, R1, R2, R1 - R2,
                      R1 + R2, R1 - R2, 4 * R1 * R2, R1, 4 * R1 * R2, R2, kq_str))

        dapan = '\\shortans[0]{$%s$}\n' % (kq_str)

    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
