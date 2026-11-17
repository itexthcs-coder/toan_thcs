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


def bt_dang13_p4_b4_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ma = randint(15, 45)
        r_exact = ma * sqrt(3)
        r_dec = Decimal(str(float(r_exact))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        r_str = str(r_dec).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một đoạn đường dẫn lên cầu vượt gồm hai đoạn đường thẳng $Mx$ và $My$ giao nhau tại $M$ tạo thành góc $\\widehat{xMy} = 120^\\circ$. Kỹ sư cần thiết kế một khúc cua hình cung tròn tâm $O$ tiếp xúc với cả hai mép đường thẳng $Mx$ và $My$ lần lượt tại $A$ và $B$ sao cho khoảng cách từ điểm giao $M$ đến điểm bắt đầu vào cua $A$ là $%s\\text{ m}$. Tính bán kính $R$ của cung tròn khúc cua này (làm tròn kết quả đến chữ số thập phân thứ hai). \\\\
        \\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (M) at (0,0);
            \\coordinate (A) at (-1.5,0);
            \\coordinate (B) at (0.75,-1.299);
            \\coordinate (O) at (-1.5,-2.598);
            \\draw[line width=1pt] (M)--(-3.5,0) node[above] {$x$};
            \\draw[line width=1pt] (M)--(1.75,-3.031) node[right] {$y$};
            \\draw[line width=1pt] (A) arc (90:30:2.598);
            \\draw[line width=1pt, dashed] (O)--(A) (O)--(B) (O)--(M);
            \\fill (M) circle (1pt) node[above right] {$M$};
            \\fill (A) circle (1pt) node[above] {$A$};
            \\fill (B) circle (1pt) node[right] {$B$};
            \\fill (O) circle (1pt) node[below left] {$O$};
        \\end{tikzpicture}
        \\end{center}'''
        %(latex(ma)))

        # Nội dung lời giải
        loigiai = ('''Vì cung tròn tâm $O$ tiếp xúc với hai đường thẳng $Mx$ và $My$ lần lượt tại $A$ và $B$ nên $MA$ và $MB$ là hai tiếp tuyến cắt nhau của đường tròn $(O)$. \\\\
        Theo tính chất của hai tiếp tuyến cắt nhau, $MO$ là tia phân giác của góc $\\widehat{xMy}$, suy ra: \\\\
        $\\widehat{AMO} = \\dfrac{\\widehat{xMy}}{2} = \\dfrac{120^\\circ}{2} = 60^\\circ$. \\\\
        Vì $MA$ là tiếp tuyến của $(O)$ tại $A$ nên $OA \\perp MA$ tại $A$, hay $\\widehat{OAM} = 90^\\circ$. \\\\
        Xét tam giác $OAM$ vuông tại $A$, bán kính $R = OA$ của cung tròn khúc cua là: \\\\
        $R = OA = MA \\cdot \\tan \\widehat{AMO} = %s \\cdot \\tan 60^\\circ = %s\\sqrt{3} \\approx %s\\text{ (m)}$.'''
        %(latex(ma), latex(ma), r_str))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
