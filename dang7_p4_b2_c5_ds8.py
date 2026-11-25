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


def bt_dang7_p4_b2_c5_ds8(self):
    # Dạng 7 (Tự luận - Vận dụng): Thiết kế biểu đồ cột kép từ bảng hai chiều theo hai mục đích đối lập
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        k = random.choice([0, 2, 4])
        bm22, bm26 = 14 + k, 20 + k
        rd22, rd26 = 18 + k, 16 + k
        
        tikz_a = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt, ->] (0,0) -- (0,2.5) node[above] {Số HCV};
        \\draw[line width=1pt, ->] (0,0) -- (5.0,0) node[right] {Trường};
        \\draw[line width=1pt, fill=black!35] (0.7,0) rectangle (1.3,1.4) (2.7,0) rectangle (3.3,1.8);
        \\draw[line width=1pt, fill=white] (1.3,0) rectangle (1.9,2.0) (3.3,0) rectangle (3.9,1.6);
        \\node[above] at (1.0,1.4) {$%s$}; \\node[above] at (1.6,2.0) {$%s$};
        \\node[above] at (3.0,1.8) {$%s$}; \\node[above] at (3.6,1.6) {$%s$};
        \\node[below] at (1.3,0) {Bình Minh}; \\node[below] at (3.3,0) {Rạng Đông};
        \\draw[line width=1pt, fill=black!35] (4.8,1.7) rectangle (5.1,2.0); \\node[right] at (5.1,1.85) {Năm $2022$};
        \\draw[line width=1pt, fill=white] (4.8,1.2) rectangle (5.1,1.5); \\node[right] at (5.1,1.35) {Năm $2026$};
        \\end{tikzpicture}
        \\end{center}""" % (bm22, bm26, rd22, rd26))
        
        tikz_b = ("""\\begin{center}
        \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\draw[line width=1pt, ->] (0,0) -- (0,2.5) node[above] {Số HCV};
        \\draw[line width=1pt, ->] (0,0) -- (5.0,0) node[right] {Năm};
        \\draw[line width=1pt, fill=black!35] (0.7,0) rectangle (1.3,1.4) (2.7,0) rectangle (3.3,2.0);
        \\draw[line width=1pt, fill=white] (1.3,0) rectangle (1.9,1.8) (3.3,0) rectangle (3.9,1.6);
        \\node[above] at (1.0,1.4) {$%s$}; \\node[above] at (1.6,1.8) {$%s$};
        \\node[above] at (3.0,2.0) {$%s$}; \\node[above] at (3.6,1.6) {$%s$};
        \\node[below] at (1.3,0) {Năm $2022$}; \\node[below] at (3.3,0) {Năm $2026$};
        \\draw[line width=1pt, fill=black!35] (4.8,1.7) rectangle (5.1,2.0); \\node[right] at (5.1,1.85) {Bình Minh};
        \\draw[line width=1pt, fill=white] (4.8,1.2) rectangle (5.1,1.5); \\node[right] at (5.1,1.35) {Rạng Đông};
        \\end{tikzpicture}
        \\end{center}""" % (bm22, rd22, bm26, rd26))
        
        noidungcauhoi = ("""Bảng thống kê dưới đây ghi lại số lượng huy chương Vàng (HCV) của hai trường THCS Bình Minh và Rạng Đông trong hai kì Hội khỏe Phù Đổng năm $2022$ và năm $2026$:\\\\
        \\begin{center}
        \\begin{tabular}{|c|c|c|}
        \\hline
        \\textbf{Trường / Năm} & \textbf{Năm $2022$} & \textbf{Năm $2026$} \\\\
        \\hline
        \\textbf{Trường Bình Minh} & $%s$ & $%s$ \\\\
        \\hline
        \\textbf{Trường Rạng Đông} & $%s$ & $%s$ \\\\
        \\hline
        \\end{tabular}
        \\end{center}
        a) Muốn biết sự thay đổi số huy chương Vàng của \textbf{mỗi trường} qua hai kì Hội khỏe Phù Đổng, ta nên vẽ biểu đồ cột kép với cách chia nhóm trên trục ngang như thế nào? Vẽ biểu đồ đó.\\\\
        b) Muốn so sánh thành tích giữa \textbf{hai trường trong cùng một kì} Hội khỏe Phù Đổng, ta phải vẽ biểu đồ cột kép như thế nào? Vẽ biểu đồ đó."""
                         % (bm22, bm26, rd22, rd26))
        
        loigiai = ("""\\begin{enumEX}[a)]{1}
        \\item Để thấy rõ sự thay đổi số huy chương Vàng của mỗi trường qua hai kì, trên trục ngang ta chia thành $2$ nhóm là ``Trường Bình Minh'' và ``Trường Rạng Đông'', mỗi nhóm gồm $2$ cột ứng với Năm $2022$ và Năm $2026$:%s
        \\item Để so sánh thành tích giữa hai trường trong cùng một kì, trên trục ngang ta chia thành $2$ nhóm là ``Năm $2022$'' và ``Năm $2026$'', mỗi nhóm gồm $2$ cột ứng với Trường Bình Minh và Trường Rạng Đông:%s
        \\end{enumEX}""" % (tikz_a, tikz_b))

    # Xuất câu tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) + '\n\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
