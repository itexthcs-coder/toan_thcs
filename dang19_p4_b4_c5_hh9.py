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


def bt_dang19_p4_b4_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        ih = randint(6, 15)
        canh = 2 * ih
        r_lon = ih + randint(2, 5)
        he = sqrt(r_lon ** 2 - ih ** 2)
        ef = 2 * he
        ef_dec = Decimal(str(float(ef))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        ef_str = str(ef_dec).replace('.', ',')

        # Nội dung câu hỏi
        noidungcauhoi = ('''Một khu vườn hình vuông $ABCD$ có cạnh bằng $%s\\text{ m}$ và hai đường chéo cắt nhau tại $I$. Người nông dân lắp một béc tưới xoay tròn tự động tại tâm $I$ có bán kính phun nước điều chỉnh được là $R$. \\\\
        a) Cần chỉnh bán kính $R$ bằng bao nhiêu mét để vùng nước phun tới sát mép cả bốn bờ rào của khu vườn mà không bắn ra ngoài? \\\\
        b) Nếu chỉnh $R = %s\\text{ m}$ thì trên mỗi cạnh bờ rào của khu vườn có một đoạn thẳng dài bao nhiêu mét bị nước phun ướt (làm tròn kết quả đến chữ số thập phân thứ hai)? \\\\
        \\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
            \\coordinate (A) at (-1.8,1.8);
            \\coordinate (B) at (1.8,1.8);
            \\coordinate (C) at (1.8,-1.8);
            \\coordinate (D) at (-1.8,-1.8);
            \\coordinate (I) at (0,0);
            \\coordinate (H) at (0,-1.8);
            \\coordinate (E) at (-1.2, -1.8);
            \\coordinate (F) at (1.2, -1.8);
            \\draw[line width=1pt] (A)--(B)--(C)--(D)--cycle;
            \\draw[line width=1pt] (I) circle (2.163);
            \\draw[line width=1pt, dashed] (I)--(H) (I)--(E) (I)--(F);
            \\fill (A) circle (1pt) node[above left] {$A$};
            \\fill (B) circle (1pt) node[above right] {$B$};
            \\fill (C) circle (1pt) node[below right] {$C$};
            \\fill (D) circle (1pt) node[below left] {$D$};
            \\fill (I) circle (1pt) node[above] {$I$};
            \\fill (H) circle (1pt) node[below] {$H$};
            \\fill (E) circle (1pt) node[below left] {$E$};
            \\fill (F) circle (1pt) node[below right] {$F$};
        \\end{tikzpicture}
        \\end{center}'''
        %(latex(canh), latex(r_lon)))

        # Nội dung lời giải
        loigiai = ('''\\begin{enumEX}[a)]{1} \n
        \\item Kẻ $IH \\perp CD$ tại $H$. Vì $I$ là giao điểm hai đường chéo của hình vuông $ABCD$ cạnh $%s\\text{ m}$ nên khoảng cách từ tâm $I$ đến mỗi cạnh của hình vuông đều bằng nửa độ dài cạnh hình vuông: \\\\
        $d = IH = \\dfrac{%s}{2} = %s\\text{ (m)}$. \\\\
        Để vùng nước phun tới sát mép bốn bờ rào mà không bắn ra ngoài thì đường tròn $(I; R)$ phải tiếp xúc với cả bốn cạnh của hình vuông, tức là $R = d = %s\\text{ m}$. \n
        \\item Khi chỉnh $R = %s\\text{ m} > %s\\text{ m}$, đường tròn $(I; %s)$ cắt cạnh $CD$ tại hai điểm phân biệt $E$ và $F$. \\\\
        Xét tam giác $IHE$ vuông tại $H$ ($IE = R = %s\\text{ m}$, $IH = %s\\text{ m}$), áp dụng định lí Pythagore ta có: \\\\
        $HE = \\sqrt{IE^2 - IH^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ (m)}$. \\\\
        Vì $IH \\perp EF$ nên $H$ là trung điểm của đoạn thẳng $EF$. Vậy độ dài đoạn bờ rào bị nước phun ướt trên mỗi cạnh là: \\\\
        $EF = 2HE = 2 \\cdot %s \\approx %s\\text{ (m)}$. \n
        \\end{enumEX} \n'''
        %(latex(canh), latex(canh), latex(ih), latex(ih), latex(r_lon), latex(ih), latex(r_lon), latex(r_lon), latex(ih), latex(r_lon), latex(ih), latex(he), latex(he), ef_str))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
