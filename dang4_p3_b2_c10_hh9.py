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


def bt_dang4_p3_b2_c10_hh9(self):
    k = random.choice([1, 2, 3])
    R = 5 * k
    half_h = 3 * k
    h_tru = 2 * half_h
    r_day = 4 * k
    V_tru_heso = (r_day**2) * h_tru
    kq_str = str(V_tru_heso)

    hinh_ve = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (O) at (0,0);
\\coordinate (O1) at (0,1.2);
\\coordinate (O2) at (0,-1.2);
\\coordinate (B) at (1.6,1.2);
\\draw[line width=1pt] (O) circle (2cm);
\\draw[line width=1pt] (0,1.2) ellipse (1.6cm and 0.35cm);
\\draw[line width=1pt] (-1.6,-1.2) arc (180:360:1.6cm and 0.35cm);
\\draw[line width=1pt, dashed] (1.6,-1.2) arc (0:180:1.6cm and 0.35cm);
\\draw[line width=1pt] (-1.6,-1.2)--(-1.6,1.2) (1.6,-1.2)--(1.6,1.2);
\\draw[line width=1pt, dashed] (O1)--(O2) (O1)--(B) (O)--(B);
\\fill (O) circle (1pt) node[left] {$O$};
\\fill (O1) circle (1pt) node[above] {$O_1$};
\\fill (B) circle (1pt) node[right] {$B$};
\\end{tikzpicture}
\\end{center}''')

    noidungcauhoi = ('''Một hình trụ có chiều cao $h = %s\\text{ cm}$ và hai đường tròn đáy cùng nằm trên một mặt cầu tâm $O$ bán kính $R = %s\\text{ cm}$. Thể tích của hình trụ đó bằng $a\\pi\\text{ cm}^3$. Tìm giá trị của $a$.%s'''
                     % (h_tru, R, hinh_ve))

    loigiai = ('''Gọi $O_1$ là tâm của một đáy hình trụ và $B$ là một điểm thuộc đường tròn đáy đó.\\\nDo tính đối xứng, tâm $O$ của mặt cầu là trung điểm của đoạn nối tâm hai đáy hình trụ nên $OO_1 = \\dfrac{h}{2} = \\dfrac{%s}{2} = %s\\text{ (cm)}$.\\\nTam giác $OO_1B$ vuông tại $O_1$ có $OB = R = %s\\text{ cm}$, suy ra bán kính đáy hình trụ là:
$$r = O_1B = \\sqrt{OB^2 - OO_1^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ (cm)}.$$
Thể tích của hình trụ là:
$$V = \\pi r^2 h = \\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}.$$
Vậy $a = %s$.'''
               % (h_tru, half_h, R, R, half_h, r_day, r_day, h_tru, V_tru_heso, V_tru_heso))

    # Đáp án
    dapan = '\\shortans[0]{$%s$}\n' % (str(kq_str))

    # Xuất câu hỏi
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               str(dapan) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
