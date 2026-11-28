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


def bt_dang14_p3_b3_c8_ds8(self):
    # Dạng 14: So sánh xác suất lý thuyết và xác suất thực nghiệm (Độ lệch tần suất)
    lisdang = ['1']
    dang = random.choice(lisdang)
    if dang == '1':
        n_gieo = random.choice([120, 150, 180, 240, 300])
        k_lt = n_gieo // 6
        chenh = random.choice([6, 9, 12, 15, 18])
        k_tn = k_lt + chenh
        mat_cham = random.randint(1, 6)

        hieu_raw = Decimal(chenh) / Decimal(n_gieo)
        kq = hieu_raw.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        kq_str = str(kq).replace('.', ',')
        hieu_raw_str = str(hieu_raw.quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP)).rstrip('0').rstrip('.').replace('.', ',')

        noidungcauhoi = ('''Gieo một con xúc xắc cân đối $6$ mặt đồng chất $%s$ lần, người ta thấy mặt $%s$ chấm xuất hiện $%s$ lần.\\
\begin{center}
\begin{tikzpicture}[scale=1, font=\footnotesize, line join=round, line cap=round, >=stealth]
\draw[line width=1pt] (0,0) rectangle (1.4,1.4);
\draw[line width=1pt] (0,1.4) -- (0.5,1.8) -- (1.9,1.8) -- (1.4,1.4);
\draw[line width=1pt] (1.4,0) -- (1.9,0.4) -- (1.9,1.8);
\fill (0.4,0.4) circle (1pt);
\fill (1.0,1.0) circle (1pt);
\fill (0.7,0.7) circle (1pt);
\fill (0.4,1.0) circle (1pt);
\fill (1.0,0.4) circle (1pt);
\end{tikzpicture}
\end{center}
Hỏi xác suất thực nghiệm xuất hiện mặt $%s$ chấm lớn hơn xác suất lý thuyết của biến cố đó bao nhiêu (viết kết quả dưới dạng số thập phân làm tròn đến hàng phần trăm)?'''
                         % (n_gieo, mat_cham, k_tn, mat_cham))

        loigiai = ('''Vì con xúc xắc cân đối và đồng chất nên $6$ mặt có khả năng xuất hiện như nhau.\\
Xác suất lý thuyết của biến cố $E$: ``Xuất hiện mặt $%s$ chấm'' là $P(E) = \\dfrac{1}{6}$.\\
Trong $%s$ lần gieo, mặt $%s$ chấm xuất hiện $%s$ lần nên xác suất thực nghiệm của biến cố $E$ là $\\dfrac{%s}{%s}$.\\
Xác suất thực nghiệm lớn hơn xác suất lý thuyết là: $\\dfrac{%s}{%s} - \\dfrac{1}{6} = \\dfrac{%s}{%s} = %s \\approx %s$.'''
                   % (mat_cham, n_gieo, mat_cham, k_tn, k_tn, n_gieo, k_tn, n_gieo, chenh, n_gieo, hieu_raw_str, kq_str))

        dapan = '\shortans[0]{$%s$}\n' % (str(kq_str))

    content = ('\begin{minipage}{\textwidth} \n' +
               '\begin{ex}\n' +
               str(noidungcauhoi) + str(dapan) +
               '\loigiai{ \n' + str(loigiai) + '}\n' +
               '\end{ex}\n \end{minipage} \n\n')
    return content
