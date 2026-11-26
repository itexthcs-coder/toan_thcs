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
    QApplication, QPushButton, QMainWindow, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D


def bt_dang20_p4_b2_c7_ds8(self):
    # Dạng 20: Ứng dụng - Bài toán hình học thực tế mảnh đất hình thang vuông
    lisdang = ['1']
    dang = random.choice(lisdang)
    
    if dang == '1':
        ab = random.randint(14, 24)
        dc = ab + random.randint(6, 16)
        ad = random.choice([10, 12, 14, 16])
        ce = random.randint(4, 10)
        de = dc + ce
        dien_tich_moi = ((ab + de) * ad) // 2
        
        hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (D) at (0,0);
\\coordinate (A) at (0,2.2);
\\coordinate (B) at (2.8,2.2);
\\coordinate (C) at (4.2,0);
\\coordinate (E) at (5.4,0);
\\draw[line width=1pt] (D)--(A)--(B)--(C)--cycle;
\\draw[line width=1pt, dashed] (C)--(E)--(B);
\\draw[line width=1pt] (0,0.25)--(0.25,0.25)--(0.25,0);
\\draw[line width=1pt] (0,1.95)--(0.25,1.95)--(0.25,2.2);
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[above right] {$B$};
\\fill (C) circle (1pt) node[below] {$C$};
\\fill (D) circle (1pt) node[below left] {$D$};
\\fill (E) circle (1pt) node[below right] {$E$};
\\end{tikzpicture}
\\end{center}''')
        
        noidungcauhoi = ('''Một mảnh đất hình thang vuông $ABCD$ ($\\widehat{A} = \\widehat{D} = 90^\\circ$) có đáy nhỏ $AB = %s\\text{ m}$ và chiều cao $AD = %s\\text{ m}$. Người ta mở rộng mảnh đất bằng cách kéo dài đáy lớn $DC$ về phía $C$ thêm một đoạn $CE = %s\\text{ m}$ để được mảnh đất hình thang vuông mới $ABED$ có diện tích bằng $%s\\text{ m}^2$. Tính độ dài đáy lớn $DC$ ban đầu của mảnh đất.'''
                         % (ab, ad, ce, dien_tich_moi))
        
        loigiai = ('''%s \\\\
Gọi độ dài đáy lớn $DC$ ban đầu của mảnh đất là $x\\text{ (m)}$ (điều kiện: $x > %s$). \\\\
Sau khi kéo dài đáy lớn $DC$ về phía $C$ thêm $%s\\text{ m}$, độ dài đáy lớn mới $DE$ của mảnh đất là $x + %s\\text{ (m)}$. \\\\
Mảnh đất mới $ABED$ là hình thang vuông có hai đáy $AB = %s\\text{ m}$, $DE = x + %s\\text{ m}$, chiều cao $AD = %s\\text{ m}$ và diện tích bằng $%s\\text{ m}^2$ nên ta có phương trình: \\\\
$\\frac{[%s + (x + %s)] \\cdot %s}{2} = %s$ \\\\
$\\Leftrightarrow (x + %s) \\cdot %s = %s$ \\\\
$\\Leftrightarrow x + %s = %s \\Leftrightarrow x = %s$ (thỏa mãn điều kiện). \\\\
Vậy độ dài đáy lớn $DC$ ban đầu của mảnh đất là $%s\\text{ m}$.'''
                   % (hinh_ve, ab, ce, ce,
                      ab, ce, ad, dien_tich_moi,
                      ab, ce, ad, dien_tich_moi,
                      ab + ce, ad // 2, dien_tich_moi,
                      ab + ce, dien_tich_moi // (ad // 2), dc,
                      dc))
        
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n' +
               '\\loigiai{\n' + str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
