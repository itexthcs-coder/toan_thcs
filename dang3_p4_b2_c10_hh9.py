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


def bt_dang3_p4_b2_c10_hh9(self):
    k = random.choice([1, 2, 3])
    R = 5 * k
    r_day = 3 * k
    half_h = 4 * k
    h_tru = 2 * half_h
    S_xq = 2 * r_day * h_tru
    S_tp = S_xq + 2 * r_day**2
    V_tru = r_day**2 * h_tru

    noidungcauhoi = ('''Cho hình cầu tâm $O$ bán kính $R = %s\\text{ cm}$. Một hình trụ có bán kính đáy $r = %s\\text{ cm}$ và hai đường tròn đáy cùng nằm trên mặt cầu $(O)$.\\\na) Tính chiều cao của hình trụ đó.\\\nb) Tính diện tích xung quanh và diện tích toàn phần của hình trụ.\\\nc) Tính thể tích của hình trụ và so sánh với thể tích của khối cầu $(O)$.'''
                     % (R, r_day))

    V_cau = Rational(4, 3) * R**3
    ti_so = Rational(V_tru, V_cau)

    loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Gọi $O_1, O_2$ là tâm hai đáy của hình trụ và $A$ là một điểm thuộc đường tròn đáy tâm $O_1$.\\\nTam giác $OO_1A$ vuông tại $O_1$ có $OA = R = %s\\text{ cm}$ và $O_1A = r = %s\\text{ cm}$, suy ra:
$$OO_1 = \\sqrt{OA^2 - O_1A^2} = \\sqrt{%s^2 - %s^2} = %s\\text{ (cm)}.$$
Do tính đối xứng, $O$ là trung điểm của $O_1O_2$ nên chiều cao của hình trụ là:
$$h = O_1O_2 = 2 \\cdot OO_1 = 2 \\cdot %s = %s\\text{ (cm)}.$$
\\item Diện tích xung quanh của hình trụ là: $S_{\\text{xq}} = 2\\pi r h = 2\\pi \\cdot %s \\cdot %s = %s\\pi\\text{ (cm}^2\\text{)}$.\\\nDiện tích toàn phần của hình trụ là: $S_{\\text{tp}} = S_{\\text{xq}} + 2\\pi r^2 = %s\\pi + 2\\pi \\cdot %s^2 = %s\\pi\\text{ (cm}^2\\text{)}$.
\\item Thể tích của hình trụ là: $V_{\\text{trụ}} = \\pi r^2 h = \\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}$.\\\nThể tích của khối cầu $(O)$ là: $V_{\\text{cầu}} = \\dfrac{4}{3}\\pi R^3 = \\dfrac{4}{3}\\pi \\cdot %s^3 = %s\\pi\\text{ (cm}^3\\text{)}$.\\\nVậy tỉ số $\\dfrac{V_{\\text{trụ}}}{V_{\\text{cầu}}} = \\dfrac{%s\\pi}{%s\\pi} = %s$.
\\end{enumEX}'''
               % (R, r_day, R, r_day, half_h, half_h, h_tru, r_day, h_tru, S_xq, S_xq, r_day, S_tp, r_day, h_tru, V_tru, R, latex(V_cau), V_tru, latex(V_cau), latex(ti_so)))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
