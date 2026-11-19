# -*- coding: utf-8 -*-
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


def bt_dang18_p4_b4_c9_hh9(self):
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        bo_du_lieu = [
            (10, 15, 2),
            (12, 18, 2),
            (12, 20, 3),
            (15, 24, 3),
            (18, 30, 4)
        ]
        so_cabin, r_vong, khoang_cach_dinh = random.choice(bo_du_lieu)
        goc_moi_khoang = 360 // so_cabin
        nua_vong_khoang = so_cabin // 2
        so_khoang_quay = nua_vong_khoang - khoang_cach_dinh
        goc_quay = so_khoang_quay * goc_moi_khoang
        val_cung = (3.14 * r_vong * goc_quay) / 180.0
        number = Decimal(str(val_cung))
        kq = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')

        hinh_tikz = '''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\draw[line width=1pt] (O) circle (1.7);
\\foreach \\i in {0,36,...,324} {
    \\draw[line width=1pt] (O)--(\\i:1.7);
    \\fill (\\i:1.7) circle (1pt);
}
\\draw[line width=1pt] (-0.8,-2.1)--(O)--(0.8,-2.1);
\\fill (O) circle (1pt) node[below left] {$O$};
\\node[above] at (90:1.7) {Cao nhất};
\\node[below] at (270:1.7) {Thấp nhất};
\\end{tikzpicture}
\\end{center}'''

        noidungcauhoi = ('''Một vòng quay mặt trời trong khu vui chơi có $%s$ cabin gắn cách đều nhau trên vành tròn tâm $O$ bán kính $%s\\text{ m}$, tạo thành các đỉnh của một đa giác đều $%s$ cạnh (như hình vẽ). \\
a) Hỏi vòng quay phải quay thuận chiều kim đồng hồ quanh tâm $O$ ít nhất bao nhiêu độ để cabin đang ở vị trí thấp nhất di chuyển đến vị trí cách vị trí cao nhất đúng $%s$ khoảng cabin (tính theo chiều ngược kim đồng hồ so với vị trí cao nhất)? \\
b) Tính độ dài cung tròn mà cabin đó đã di chuyển được trong quá trình trên (lấy $\\pi \\approx 3,14$). %s'''
                         % (so_cabin, r_vong, so_cabin, khoang_cach_dinh, hinh_tikz))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\item Vì $%s$ cabin gắn cách đều nhau trên đường tròn $(O)$ nên hai cabin liên tiếp bất kì tạo với tâm $O$ một góc ở tâm bằng $\\frac{360^\\circ}{%s} = %s^\\circ$. \\
Vị trí thấp nhất và vị trí cao nhất đối xứng nhau qua tâm $O$ nên cách nhau $\\frac{%s}{2} = %s$ khoảng cabin. \\
Khi cabin đi thuận chiều kim đồng hồ từ vị trí thấp nhất đến vị trí cách vị trí cao nhất $%s$ khoảng cabin (chưa vượt qua vị trí cao nhất), số khoảng cabin mà nó đã di chuyển là $%s - %s = %s$ khoảng. \\
Vậy góc quay thuận chiều kim đồng hồ nhỏ nhất cần tìm là:
$$\\alpha = %s \\cdot %s^\\circ = %s^\\circ.$$
\item Độ dài cung tròn bán kính $R = %s\\text{ m}$ có số đo $%s^\\circ$ mà cabin đã di chuyển được là:
$$l = \\frac{\\pi R \\alpha}{180} \\approx \\frac{3,14 \\cdot %s \\cdot %s}{180} = %s\\text{ (m)}.$$
\end{enumEX}'''
                   % (so_cabin, so_cabin, goc_moi_khoang, so_cabin, nua_vong_khoang, khoang_cach_dinh, nua_vong_khoang, khoang_cach_dinh, so_khoang_quay, so_khoang_quay, goc_moi_khoang, goc_quay, r_vong, goc_quay, r_vong, goc_quay, kq_str))

    content = ('\\begin{minipage}{\\textwidth} \n'
               '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
               '\\loigiai{ \n' + str(loigiai) + '}\n'
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
