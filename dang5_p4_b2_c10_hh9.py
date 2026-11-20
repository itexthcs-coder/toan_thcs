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


def bt_dang5_p4_b2_c10_hh9(self):
    # Hình gồm HCN kích thước 2R x h và 2 nửa hình tròn bán kính R ở hai đầu => quay quanh trục đối xứng dọc tạo thành hình trụ + 2 nửa hình cầu!
    R = random.choice([3, 6])
    h = randint(5, 10)
    S_hinh = 2 * R * h + R**2
    V_khoi = R**2 * h + Rational(4, 3) * R**3
    S_mat = 2 * R * h + 4 * R**2

    noidungcauhoi = ('''Cho hình phẳng $(H)$ gồm một hình chữ nhật kích thước $%s\\text{ cm} \\times %s\\text{ cm}$ và hai nửa hình tròn đường kính $%s\\text{ cm}$ gắn khít vào hai cạnh đối diện có độ dài $%s\\text{ cm}$ của hình chữ nhật đó. Quay hình phẳng $(H)$ một vòng quanh trục đối xứng đi qua tâm của hai nửa hình tròn ta được một vật thể tròn xoay $(T)$.\\\na) Tính diện tích của hình phẳng $(H)$ ban đầu.\\\nb) Tính diện tích bề mặt của vật thể tròn xoay $(T)$.\\\nc) Tính thể tích của vật thể tròn xoay $(T)$.'''
                     % (2 * R, h, 2 * R, 2 * R))

    loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Bán kính của mỗi nửa hình tròn là $R = \\dfrac{%s}{2} = %s\\text{ (cm)}$.\\\nHai nửa hình tròn ghép lại tạo thành một hình tròn có diện tích $S_{\\text{tròn}} = \\pi R^2 = %s\\pi\\text{ (cm}^2\\text{)}$.\\\nDiện tích hình chữ nhật là $S_{\\text{hcn}} = %s \\cdot %s = %s\\text{ (cm}^2\\text{)}$.\\\nVậy diện tích hình phẳng $(H)$ là: $S_{(H)} = %s + %s\\pi\\text{ (cm}^2\\text{)}$.
\\item Khi quay quanh trục đối xứng đi qua tâm hai nửa hình tròn, hình chữ nhật tạo thành hình trụ bán kính đáy $R = %s\\text{ cm}$, chiều cao $h = %s\\text{ cm}$; hai nửa hình tròn tạo thành hai nửa hình cầu bán kính $R = %s\\text{ cm}$ (ghép lại thành một mặt cầu bán kính $R = %s\\text{ cm}$).\\\nDiện tích bề mặt của $(T)$ là:
$$S_{(T)} = S_{\\text{xq trụ}} + S_{\\text{mặt cầu}} = 2\\pi R h + 4\\pi R^2 = 2\\pi \\cdot %s \\cdot %s + 4\\pi \\cdot %s^2 = %s\\pi\\text{ (cm}^2\\text{)}.$$
\\item Thể tích của vật thể tròn xoay $(T)$ là:
$$V_{(T)} = V_{\\text{trụ}} + V_{\\text{cầu}} = \\pi R^2 h + \\dfrac{4}{3}\\pi R^3 = \\pi \\cdot %s^2 \\cdot %s + \\dfrac{4}{3}\\pi \\cdot %s^3 = %s\\pi\\text{ (cm}^3\\text{)}.$$
\\end{enumEX}'''
               % (2 * R, R, R**2, 2 * R, h, 2 * R * h, 2 * R * h, R**2, R, h, R, R, R, h, R, S_mat, R, h, R, latex(V_khoi)))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
