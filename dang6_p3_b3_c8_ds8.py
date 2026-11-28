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


def bt_dang6_p3_b3_c8_ds8(self):
    # Dạng 6: Tính gần đúng hằng số pi thông qua thí nghiệm ném vật thể (Mô hình Buffon)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        h = random.choice([2, 3, 4])
        d = 2 * h
        k_cat = random.choice([500, 600, 800, 1000])
        n_nem = random.choice([1570, 1571, 1885, 2513, 3142])
        # Tính pi_approx = (2 * h * n_nem) / (k_cat * d) = n_nem / k_cat
        pi_raw = Decimal(n_nem) / Decimal(k_cat)
        kq = pi_raw.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')
        pi_raw_str = str(pi_raw.quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)).replace('.', ',')

        noidungcauhoi = ('''Trên sân gạch kẻ các đường thẳng song song cách đều nhau một khoảng $d = %s\\text{ cm}$, một nhóm học sinh thực hiện ném ngẫu nhiên một chiếc que thẳng có độ dài $h = %s\\text{ cm}$ tổng cộng $%s$ lần và đếm được $%s$ lần chiếc que cắt một trong các đường thẳng kẻ trên sân.\\
\begin{center}
\begin{tikzpicture}[scale=1, font=\footnotesize, line join=round, line cap=round, >=stealth]
\draw[line width=1pt] (0,0) -- (6,0);
\draw[line width=1pt] (0,1.5) -- (6,1.5);
\draw[line width=1pt] (0,3) -- (6,3);
\draw[line width=1pt] (1.2,1.1) -- (1.8,1.8);
\fill (1.2,1.1) circle (1pt);
\fill (1.8,1.8) circle (1pt);
\draw[line width=1pt] (3.5,0.3) -- (4.3,0.7);
\fill (3.5,0.3) circle (1pt);
\fill (4.3,0.7) circle (1pt);
\draw[line width=1pt, <->] (5.3,1.5) -- (5.3,3) node[midway, right] {$d$};
\end{tikzpicture}
\end{center}
Biết xác suất lý thuyết để chiếc que cắt đường thẳng là $P(E) = \\dfrac{2h}{\\pi d}$, hãy tính giá trị gần đúng của số $\\pi$ thu được từ thí nghiệm trên (làm tròn kết quả đến hàng phần trăm).'''
                         % (d, h, n_nem, k_cat))

        loigiai = ('''Xác suất thực nghiệm của biến cố $E$: ``Chiếc que cắt một trong các đường thẳng kẻ trên sân'' là $\\dfrac{%s}{%s}$.\\
Theo mối liên hệ giữa xác suất thực nghiệm và xác suất, ta có $P(E) \\approx \\dfrac{%s}{%s}$, suy ra $\\dfrac{2h}{\\pi d} \\approx \\dfrac{%s}{%s}$.\\
Thay $h = %s$ và $d = %s$ vào hệ thức trên, ta được: $\\dfrac{2 \\cdot %s}{\\pi \\cdot %s} \\approx \\dfrac{%s}{%s} \\Leftrightarrow \\dfrac{1}{\\pi} \\approx \\dfrac{%s}{%s}$.\\
Từ đó suy ra $\\pi \\approx \\dfrac{%s}{%s} = %s \\approx %s$.'''
                   % (k_cat, n_nem, k_cat, n_nem, k_cat, n_nem, h, d, h, d, k_cat, n_nem, k_cat, n_nem, n_nem, k_cat, pi_raw_str, kq_str))

        dapan = '\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\begin{minipage}{\textwidth} \n' +
               '\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\loigiai{ \n' + str(loigiai) + '}\n' +
               '\end{ex}\n \end{minipage} \n\n')
    return content
