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


def bt_dang14_p4_b2_c10_hh9(self):
    k = random.choice([2, 3])
    r = randint(2, 4)
    R = k * r
    S_tong = 4 * (R**2 + r**2)
    V_hieu = Rational(4, 3) * (R**3 - r**3)

    noidungcauhoi = ('''Cho hai hình cầu có bán kính lần lượt là $R$ và $r$ ($R > r > 0$). Biết bán kính của hình cầu lớn gấp $%s$ lần bán kính của hình cầu nhỏ và tổng diện tích của hai mặt cầu bằng $%s\\pi\\text{ cm}^2$.\\\na) Tính bán kính của mỗi hình cầu.\\\nb) Tính hiệu thể tích của hai hình cầu đó.\\\nc) Nếu đúc cả hai hình cầu này thành một hình cầu mới duy nhất thì bán kính của hình cầu mới bằng bao nhiêu (làm tròn đến hàng phần trăm của $\\text{cm}$)?'''
                     % (k, S_tong))

    R_moi = Decimal(str((R**3 + r**3)**(1/3))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    R_moi_str = str(R_moi).replace('.', ',')

    loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Theo đề bài, ta có $R = %sr$ và tổng diện tích hai mặt cầu là:
$$4\\pi R^2 + 4\\pi r^2 = %s\\pi \\Leftrightarrow R^2 + r^2 = %s.$$
Thay $R = %sr$ vào phương trình trên, ta được:
$$(%sr)^2 + r^2 = %s \\Leftrightarrow %sr^2 = %s \\Leftrightarrow r^2 = %s \\Rightarrow r = %s\\text{ (cm)} \\text{ (do } r > 0\\text{)}.$$
Suy ra bán kính của hình cầu lớn là $R = %s \\cdot %s = %s\\text{ (cm)}$.
\\item Hiệu thể tích của hai hình cầu là:
$$V_{\\text{hiệu}} = \\dfrac{4}{3}\\pi R^3 - \\dfrac{4}{3}\\pi r^3 = \\dfrac{4}{3}\\pi (%s^3 - %s^3) = %s\\pi\\text{ (cm}^3\\text{)}.$$
\\item Gọi $R_{\\text{mới}}$ là bán kính của hình cầu đúc mới, ta có:
$$\\dfrac{4}{3}\\pi R_{\\text{mới}}^3 = \\dfrac{4}{3}\\pi (R^3 + r^3) \\Rightarrow R_{\\text{mới}} = \\sqrt[3]{%s^3 + %s^3} = \\sqrt[3]{%s} \\approx %s\\text{ (cm)}.$$
\\end{enumEX}'''
               % (k, S_tong, S_tong // 4, k, k, S_tong // 4, k**2 + 1, S_tong // 4, r**2, r, k, r, R, R, r, latex(V_hieu), R, r, R**3 + r**3, R_moi_str))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
