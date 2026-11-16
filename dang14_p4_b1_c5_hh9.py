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


def bt_dang14_p4_b1_c5_hh9(self):
    # Khai báo biến
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        R = random.randint(3, 6)
        oa = R + random.randint(4, 9)
        am_min = oa - R
        am_max = oa + R
        m1m2 = 2 * R
        tich = am_min * am_max

        tikz_code = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (M2) at (-1.4,0);
\\coordinate (M1) at (1.4,0);
\\coordinate (M) at (60:1.4);
\\coordinate (A) at (3.2,0);
\\draw[line width=1pt] (O) circle (1.4);
\\draw[line width=1pt] (M2)--(A);
\\draw[line width=1pt, dashed] (O)--(M)--(A);
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (M2) circle (1pt) node[below left] {$M_2$};
\\fill (M1) circle (1pt) node[below right] {$M_1$};
\\fill (M) circle (1pt) node[above] {$M$};
\\fill (A) circle (1pt) node[below] {$A$};
\\end{tikzpicture}
\\end{center}''')

        noidungcauhoi = ('''Cho đường tròn $(O; R)$ và một điểm $A$ cố định nằm ngoài đường tròn ($OA > R$). Với mỗi điểm $M$ di động trên đường tròn $(O)$ (minh họa như hình vẽ): \\\\
a) Chứng minh rằng $OA - R \\le AM \\le OA + R$. Chỉ rõ vị trí của điểm $M$ trên đường tròn $(O)$ để $AM$ đạt giá trị nhỏ nhất và giá trị lớn nhất. \\\\
b) Cho $R = %s\\text{ cm}$ và $OA = %s\\text{ cm}$. Gọi $M_1, M_2$ lần lượt là vị trí của $M$ để $AM$ nhỏ nhất và lớn nhất. Tính độ dài đoạn thẳng $M_1M_2$ và tích $AM_1 \\cdot AM_2$.
%s''' % (R, oa, tikz_code))

        loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Với ba điểm $O, A, M$, áp dụng bất đẳng thức tam giác (và trường hợp ba điểm thẳng hàng), ta luôn có:\\\\
$OA - OM \\le AM \\le OA + OM$.\\\\
Vì $M \\in (O; R)$ nên $OM = R$, do đó $OA - R \\le AM \\le OA + R$.\\\\
- Dấu bằng $AM = OA - R$ xảy ra khi điểm $M$ nằm giữa hai điểm $O$ và $A$, tức là $M$ là giao điểm $M_1$ của tia $OA$ với đường tròn $(O)$.\\\\
- Dấu bằng $AM = OA + R$ xảy ra khi điểm $O$ nằm giữa hai điểm $A$ và $M$, tức là $M$ là giao điểm $M_2$ của tia đối của tia $OA$ với đường tròn $(O)$.
\\item Khi $R = %s\\text{ cm}$ và $OA = %s\\text{ cm}$:\\\\
- Hai điểm $M_1, M_2$ đối xứng với nhau qua tâm $O$ nên $M_1M_2$ là đường kính của $(O)$, suy ra $M_1M_2 = 2R = 2 \\cdot %s = %s\\text{ cm}$.\\\\
- Ta có $AM_1 = OA - R = %s - %s = %s\\text{ cm}$ và $AM_2 = OA + R = %s + %s = %s\\text{ cm}$.\\\\
Vậy tích $AM_1 \\cdot AM_2 = %s \\cdot %s = %s\\text{ cm}^2$.
\\end{enumEX}''' % (R, oa, R, m1m2, oa, R, am_min, oa, R, am_max, am_min, am_max, tich))

    # Xuất câu hỏi với đáp án và lời giải
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
