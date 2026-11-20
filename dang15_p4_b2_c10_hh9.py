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


def bt_dang15_p4_b2_c10_hh9(self):
    R = 3
    h_non = 4
    l_non = 5
    V_nuacau = Rational(2, 3) * R**3
    V_non = Rational(1, 3) * R**2 * h_non
    V_tong = V_nuacau + V_non
    S_tp = 2 * R**2 + R * l_non

    noidungcauhoi = ('''Cho hình phẳng $(M)$ gồm một nửa hình tròn tâm $O$ bán kính $R = %s\\text{ cm}$ đường kính $AB$ và tam giác $SAB$ cân tại $S$ có đường cao $SO = %s\\text{ cm}$ nằm về hai phía khác nhau đối với đường thẳng $AB$. Quay hình phẳng $(M)$ một vòng quanh đường thẳng $SO$ cố định ta được một con quay tròn xoay.\\\na) Tính tổng chiều cao của con quay tròn xoay tạo thành.\\\nb) Tính diện tích bề mặt của con quay đó.\\\nc) Tính thể tích của con quay đó.'''
                     % (R, h_non))

    loigiai = ('''\\begin{enumEX}[a)]{1}
\\item Khi quay hình phẳng $(M)$ quanh trục $SO$, nửa hình tròn tạo thành một nửa hình cầu tâm $O$ bán kính $R = %s\\text{ cm}$ và tam giác cân $SAB$ tạo thành một hình nón đỉnh $S$, bán kính đáy $R = %s\\text{ cm}$, chiều cao $h = SO = %s\\text{ cm}$.\\\nTổng chiều cao của con quay bằng: $H = R + SO = %s + %s = %s\\text{ (cm)}$.
\\item Độ dài đường sinh của phần hình nón là: $l = SB = \\sqrt{OB^2 + SO^2} = \\sqrt{%s^2 + %s^2} = %s\\text{ (cm)}$.\\\nDiện tích bề mặt của con quay gồm diện tích nửa mặt cầu và diện tích xung quanh hình nón:
$$S = 2\\pi R^2 + \\pi R l = 2\\pi \\cdot %s^2 + \\pi \\cdot %s \\cdot %s = %s\\pi\\text{ (cm}^2\\text{)}.$$
\\item Thể tích của con quay là:
$$V = V_{\\text{nửa cầu}} + V_{\\text{nón}} = \\dfrac{2}{3}\\pi R^3 + \\dfrac{1}{3}\\pi R^2 h = \\dfrac{2}{3}\\pi \\cdot %s^3 + \\dfrac{1}{3}\\pi \\cdot %s^2 \\cdot %s = %s\\pi\\text{ (cm}^3\\text{)}.$$
\\end{enumEX}'''
               % (R, R, h_non, R, h_non, R + h_non, R, h_non, l_non, R, R, l_non, S_tp, R, R, h_non, latex(V_tong)))

    # Xuất câu hỏi tự luận
    content = ('\\begin{minipage}{\\textwidth} \n' +
               '\\begin{ex}\n' +
               str(noidungcauhoi) +
               '\\loigiai{ \n' +
               str(loigiai) + '}\n' +
               '\\end{ex}\n \\end{minipage} \n\n')
    return content
